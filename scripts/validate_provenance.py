#!/usr/bin/env python3

import argparse
import copy
import json
import sys
from pathlib import Path

import jsonschema


SCHEMA_PATH = Path("skills/fair/assets/provenance-manifest-schema.json")
TEMPLATE_PATH = Path("skills/fair/assets/provenance-manifest-template.json")
AUTHORITY_PATH = Path("docs/artifact-contracts.json")
AUTHORITY_CONTRACTS = json.loads(AUTHORITY_PATH.read_text())["contracts"]


def contract_authority(path):
    for contract in AUTHORITY_CONTRACTS:
        base = contract["path"]
        if contract["match"] == "exact" and path == base:
            return contract["authority"]
        if contract["match"] == "prefix" and path.startswith(base):
            return contract["authority"]
        if contract["match"] == "direct-child" and path.startswith(base) and "/" not in path[len(base):]:
            return contract["authority"]
    return None


def semantic_errors(document):
    manifest = document["provenance_manifest"]
    collections = {
        "entity": manifest["entities"],
        "agent": manifest["agents"],
        "activity": manifest["activities"],
        "dependency": manifest["dependency_assertions"],
        "review": manifest["reviews"],
    }
    errors = []
    ids = {}
    for kind, records in collections.items():
        for record in records:
            record_id = record["id"]
            if record_id in ids:
                errors.append(f"identifier '{record_id}' is reused by {kind} and {ids[record_id]}")
            ids[record_id] = kind

    entities = {item["id"]: item for item in manifest["entities"]}
    agents = {item["id"]: item for item in manifest["agents"]}
    activities = {item["id"]: item for item in manifest["activities"]}
    relations = {
        (item["subject"], item["predicate"], item["object"])
        for item in manifest["relations"]
    }

    for entity in manifest["entities"]:
        if entity["type"] == "artifact":
            if "@" not in entity["id"] or entity["id"] == entity["logical_id"]:
                errors.append(f"artifact revision '{entity['id']}' must have an immutable revision identifier")
            expected = contract_authority(entity["path_or_uri"])
            if expected and entity["contract_authority"] != expected:
                errors.append(f"artifact '{entity['id']}' authority must be '{expected}'")

    for activity in manifest["activities"]:
        activity_id = activity["id"]
        for entity_id in activity["used"] + activity["generated"]:
            if entity_id not in entities:
                errors.append(f"activity '{activity_id}' references unknown entity '{entity_id}'")
        for association in activity["associated_agents"]:
            if association["agent"] not in agents:
                errors.append(f"activity '{activity_id}' references unknown agent '{association['agent']}'")
        for generated_id in activity["generated"]:
            entity = entities.get(generated_id)
            if not entity:
                continue
            if (generated_id, "wasGeneratedBy", activity_id) not in relations:
                errors.append(f"generated entity '{generated_id}' lacks its wasGeneratedBy relation")
            if entity["type"] == "artifact" and activity["authorization"]["contract_authority"] != entity["contract_authority"]:
                errors.append(f"activity '{activity_id}' authorization does not match '{generated_id}' authority")
        for used_id in activity["used"]:
            if (activity_id, "used", used_id) not in relations:
                errors.append(f"activity '{activity_id}' used entity '{used_id}' without a matching relation")
        if activity["type"] == "revise":
            for generated_id in activity["generated"]:
                generated = entities.get(generated_id)
                if not generated or generated["type"] != "artifact":
                    continue
                predecessors = [
                    used_id for used_id in activity["used"]
                    if used_id in entities and entities[used_id]["logical_id"] == generated["logical_id"]
                ]
                if not predecessors:
                    errors.append(f"revision '{activity_id}' does not use a prior revision of '{generated['logical_id']}'")
                elif not any((generated_id, "wasRevisionOf", prior) in relations for prior in predecessors):
                    errors.append(f"revision entity '{generated_id}' lacks wasRevisionOf")
        for decision in activity["decisions"]:
            for evidence_id in decision["evidence"]:
                if evidence_id not in entities:
                    errors.append(f"activity '{activity_id}' decision references unknown evidence '{evidence_id}'")

    relation_shapes = {
        "wasGeneratedBy": ("entity", "activity"),
        "used": ("activity", "entity"),
        "wasDerivedFrom": ("entity", "entity"),
        "wasAttributedTo": (None, "agent"),
        "wasRevisionOf": ("entity", "entity"),
    }
    for relation in manifest["relations"]:
        subject, predicate, obj = relation["subject"], relation["predicate"], relation["object"]
        if subject not in ids:
            errors.append(f"relation references unknown subject '{subject}'")
            continue
        if obj not in ids:
            errors.append(f"relation references unknown object '{obj}'")
            continue
        expected_subject, expected_object = relation_shapes[predicate]
        if expected_subject and ids[subject] != expected_subject:
            errors.append(f"relation '{predicate}' has invalid subject type '{ids[subject]}'")
        if ids[obj] != expected_object:
            errors.append(f"relation '{predicate}' has invalid object type '{ids[obj]}'")

    for assertion in manifest["dependency_assertions"]:
        for field in ("upstream_entity", "downstream_entity"):
            if assertion[field] not in entities:
                errors.append(f"dependency '{assertion['id']}' references unknown {field}")
        if assertion["caused_by_activity"] not in activities:
            errors.append(f"dependency '{assertion['id']}' has an unknown cause activity")
        resolved_by = assertion["resolved_by_activity"]
        if assertion["status"] == "resolved":
            if not resolved_by or resolved_by not in activities:
                errors.append(f"resolved dependency '{assertion['id']}' needs a resolution activity")
        elif resolved_by is not None:
            errors.append(f"unresolved dependency '{assertion['id']}' cannot name a resolution activity")
        downstream = entities.get(assertion["downstream_entity"])
        if downstream and assertion["status"] in {"potentially-stale", "invalidated"} and downstream["status"] != assertion["status"]:
            errors.append(f"dependency '{assertion['id']}' and downstream entity status disagree")

    reviewed_entities = set()
    for review in manifest["reviews"]:
        entity_id = review["entity"]
        if entity_id not in entities:
            errors.append(f"review '{review['id']}' references unknown entity '{entity_id}'")
        reviewed_entities.add(entity_id)
        if review["reviewer"] != "unknown" and review["reviewer"] not in agents:
            errors.append(f"review '{review['id']}' references unknown reviewer")
        if review["status"] in {"reviewed", "approved", "changes-requested"}:
            if review["reviewer"] == "unknown" or review["reviewed_at"] is None or review["activity"] not in activities:
                errors.append(f"completed review '{review['id']}' lacks reviewer, time, or review activity")
        for evidence_id in review["evidence"]:
            if evidence_id not in entities:
                errors.append(f"review '{review['id']}' references unknown evidence '{evidence_id}'")

    generated_artifacts = {
        entity_id
        for activity in manifest["activities"]
        for entity_id in activity["generated"]
        if entity_id in entities and entities[entity_id]["type"] == "artifact"
    }
    for entity_id in generated_artifacts - reviewed_entities:
        errors.append(f"generated artifact '{entity_id}' lacks a review assertion")

    if manifest["privacy"]["raw_prompt_recorded"] is not False:
        errors.append("raw_prompt_recorded must remain false")
    return errors


def validate_document(document, schema):
    errors = [
        error.message
        for error in jsonschema.Draft7Validator(
            schema, format_checker=jsonschema.FormatChecker()
        ).iter_errors(document)
    ]
    errors.extend(semantic_errors(document) if not errors else [])
    return errors


def run_negative_self_tests(document, schema):
    mutations = []
    duplicate = copy.deepcopy(document)
    duplicate["provenance_manifest"]["agents"][0]["id"] = duplicate["provenance_manifest"]["entities"][0]["id"]
    mutations.append(("duplicate identifier", duplicate))
    dangling = copy.deepcopy(document)
    dangling["provenance_manifest"]["activities"][0]["used"].append("entity:missing")
    mutations.append(("dangling reference", dangling))
    authority = copy.deepcopy(document)
    authority["provenance_manifest"]["entities"][0]["contract_authority"] = "skill:fair"
    mutations.append(("authority violation", authority))
    privacy = copy.deepcopy(document)
    privacy["provenance_manifest"]["privacy"]["raw_prompt_recorded"] = True
    mutations.append(("raw-prompt policy violation", privacy))
    missing_review = copy.deepcopy(document)
    missing_review["provenance_manifest"]["reviews"] = []
    mutations.append(("missing review assertion", missing_review))
    for label, mutation in mutations:
        if not validate_document(mutation, schema):
            return [f"negative self-test accepted {label}"]
    return []


def main():
    parser = argparse.ArgumentParser(description="Validate OMF provenance manifests")
    parser.add_argument("manifests", nargs="*", type=Path, help="Additional project manifests")
    args = parser.parse_args()
    schema = json.loads(SCHEMA_PATH.read_text())
    jsonschema.Draft7Validator.check_schema(schema)
    template = json.loads(TEMPLATE_PATH.read_text())
    failures = []
    for path, document in [(TEMPLATE_PATH, template)] + [
        (path, json.loads(path.read_text())) for path in args.manifests
    ]:
        for error in validate_document(document, schema):
            failures.append(f"{path}: {error}")
    failures.extend(run_negative_self_tests(template, schema))
    if failures:
        for failure in failures:
            print(f"❌ provenance: {failure}")
        sys.exit(1)
    print(f"✅ provenance schema, template, semantics, and {len(args.manifests)} project manifest(s) are valid")


if __name__ == "__main__":
    main()
