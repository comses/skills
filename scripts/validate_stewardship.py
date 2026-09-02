#!/usr/bin/env python3

"""Validate portable OMF skill stewardship records and subject identities."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from datetime import date
from pathlib import Path, PurePosixPath

import jsonschema
import yaml


ROOT = Path("skills")
SCHEMA = Path("schemas/skill-stewardship.schema.json")
IMPLICIT_FILES = {"stewardship.yaml", "evals.json"}
IMPLICIT_DIRS = ("evals/", "reviews/", "evaluation-results/")
LEGACY_METADATA = {
    "source",
    "versioning",
    "maintainer",
    "review-status",
    "reviewed-by",
    "reviewed-at",
    "review-evidence",
    "review-cadence",
    "maturity",
}
RANGE_MARKERS = ("*", "^", "~", ">", "<", "=", "|", ",")


class Problems:
    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, skill: str, message: str) -> None:
        self.items.append(f"{skill}: {message}")

    def finish(self) -> None:
        if self.items:
            print("Stewardship validation failed:")
            for item in self.items:
                print(f"  - {item}")
            raise SystemExit(1)
        print("All skill stewardship records are valid")


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md has no YAML frontmatter")
    parts = text.split("---", 2)
    data = yaml.safe_load(parts[1])
    if not isinstance(data, dict):
        raise ValueError("SKILL.md frontmatter is not a mapping")
    return data


def normalized_path(value: str, skill: str, field: str, problems: Problems) -> str | None:
    if "\\" in value or value.startswith("/") or value.endswith("//"):
        problems.add(skill, f"{field} path is not normalized: {value!r}")
        return None
    path = PurePosixPath(value.rstrip("/"))
    if not value or str(path) in {"", "."} or any(part in {".", ".."} for part in path.parts):
        problems.add(skill, f"{field} path is not root-relative: {value!r}")
        return None
    normalized = str(path) + ("/" if value.endswith("/") else "")
    if normalized != value:
        problems.add(skill, f"{field} path is not normalized: {value!r}")
        return None
    return value


def contains(rule: str, path: str) -> bool:
    return path.startswith(rule) if rule.endswith("/") else path == rule


def overlaps(left: str, right: str) -> bool:
    left_parts = PurePosixPath(left.rstrip("/")).parts
    right_parts = PurePosixPath(right.rstrip("/")).parts
    length = min(len(left_parts), len(right_parts))
    return left_parts[:length] == right_parts[:length]


def is_implicit(path: str) -> bool:
    return path in IMPLICIT_FILES or any(
        path == prefix.rstrip("/") or path.startswith(prefix) for prefix in IMPLICIT_DIRS
    )


def filesystem_entries(root: Path) -> tuple[set[str], set[str]]:
    regular: set[str] = set()
    links: set[str] = set()
    for directory, dirnames, filenames in os.walk(root, followlinks=False):
        base = Path(directory)
        for name in list(dirnames):
            entry = base / name
            if entry.is_symlink():
                links.add(entry.relative_to(root).as_posix())
                dirnames.remove(name)
        for name in filenames:
            entry = base / name
            relative = entry.relative_to(root).as_posix()
            if entry.is_symlink():
                links.add(relative)
            elif entry.is_file():
                regular.add(relative)
    return regular, links


def validate_paths(skill_dir: Path, record: dict, problems: Problems) -> list[str]:
    skill = skill_dir.name
    subject = record["subject-revision"]
    override_entries = subject["include-overrides"]
    exclusion_entries = subject["exclusions"]
    overrides: list[str] = []
    exclusions: list[str] = []

    for field, entries, target in (
        ("include-overrides", override_entries, overrides),
        ("exclusions", exclusion_entries, exclusions),
    ):
        for entry in entries:
            value = normalized_path(entry["path"], skill, field, problems)
            if value is not None:
                target.append(value)
                candidate = skill_dir / value.rstrip("/")
                if not candidate.exists() and not candidate.is_symlink():
                    problems.add(skill, f"{field} path does not exist: {value}")
                elif candidate.is_dir() and not candidate.is_symlink() and not value.endswith("/"):
                    problems.add(skill, f"directory path must end with '/': {value}")
                elif candidate.is_file() and value.endswith("/"):
                    problems.add(skill, f"file path must not end with '/': {value}")

    if len(overrides) != len(set(overrides)):
        problems.add(skill, "include-overrides contains duplicate paths")
    if len(exclusions) != len(set(exclusions)):
        problems.add(skill, "exclusions contains duplicate paths")
    for override in overrides:
        if not is_implicit(override.rstrip("/")) and not any(
            implicit.startswith(override) for implicit in IMPLICIT_DIRS
        ):
            problems.add(skill, f"include-overrides may reverse only an implicit exclusion: {override}")
        if (skill_dir / override.rstrip("/")).is_symlink():
            problems.add(skill, f"include-overrides cannot name a symbolic link: {override}")
    for exclusion in exclusions:
        if exclusion == "SKILL.md" or contains(exclusion, "SKILL.md"):
            problems.add(skill, "SKILL.md cannot be excluded")
        if is_implicit(exclusion.rstrip("/")):
            problems.add(skill, f"exclusions cannot repeat an implicit exclusion: {exclusion}")
    for override in overrides:
        for exclusion in exclusions:
            if overlaps(override, exclusion):
                problems.add(skill, f"include/exclusion paths overlap: {override} and {exclusion}")

    regular, links = filesystem_entries(skill_dir)

    def included(path: str) -> bool:
        if any(contains(rule, path) for rule in overrides):
            return True
        if is_implicit(path):
            return False
        return not any(contains(rule, path) for rule in exclusions)

    for link in sorted(links):
        if included(link):
            problems.add(skill, f"symbolic link would be subject content: {link}")
    paths = sorted((path for path in regular if included(path)), key=lambda item: item.encode("utf-8"))
    if "SKILL.md" not in paths:
        problems.add(skill, "subject manifest does not include SKILL.md")
    return paths


def file_digest(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def validate_manifest(skill_dir: Path, record: dict, paths: list[str], problems: Problems) -> None:
    skill = skill_dir.name
    declared = record["subject-revision"]["manifest"]
    declared_paths = [entry["path"] for entry in declared]
    if declared_paths != paths:
        missing = sorted(set(paths) - set(declared_paths))
        extra = sorted(set(declared_paths) - set(paths))
        problems.add(skill, f"subject manifest paths differ (missing={missing}, extra={extra})")
        return
    stream = bytearray()
    for entry in declared:
        actual = file_digest(skill_dir / entry["path"])
        if entry["digest"] != actual:
            problems.add(skill, f"digest mismatch for {entry['path']}")
        stream.extend(entry["path"].encode("utf-8"))
        stream.extend(b"\0")
        stream.extend(actual.encode("ascii"))
        stream.extend(b"\n")
    actual_manifest = "sha256:" + hashlib.sha256(stream).hexdigest()
    if record["subject-revision"]["digest"] != actual_manifest:
        problems.add(skill, "subject-revision digest does not match the manifest")


def component_key(component: dict) -> tuple[str, str, str]:
    return (component["name"], component["version"], component.get("source", ""))


def environment_key(environment: dict) -> tuple:
    return (
        component_key(environment["model"]),
        component_key(environment["runtime"]),
        tuple(sorted(component_key(item) for item in environment["tools"])),
        tuple(sorted(component_key(item) for item in environment["dependencies"])),
    )


def criteria_key(criteria: list[dict]) -> tuple:
    return tuple(sorted((item["name"], item["rule"]) for item in criteria))


def exact_version(value: str) -> bool:
    lowered = value.lower()
    return not (
        lowered in {"unknown", "latest"}
        or any(marker in value for marker in RANGE_MARKERS)
        or re.search(r"(^|[.])x($|[.])", lowered)
        or re.search(r"\s+-\s+", value)
    )


def validate_semantics(skill_dir: Path, record: dict, problems: Problems) -> None:
    skill = skill_dir.name
    guidance = record["guidance-provenance"]
    ids = [item["guidance-id"] for item in guidance]
    if len(ids) != len(set(ids)):
        problems.add(skill, "guidance-id values must be unique")
    known_ids = set(ids)
    subject_paths = {item["path"] for item in record["subject-revision"]["manifest"]}
    for item in guidance:
        for path in item["scope"]["files"]:
            if path not in subject_paths:
                problems.add(skill, f"guidance scope file is not subject content: {path}")
        for section in item["scope"]["sections"]:
            if section["file"] not in subject_paths:
                problems.add(skill, f"guidance section file is not subject content: {section['file']}")

    for kind in ("structural", "domain"):
        for claim in record["reviews"][kind]["claims"]:
            if claim.get("outcome") == "invalidated":
                continue
            scoped = claim["scope"]["guidance-ids"]
            unknown = sorted(set(scoped) - known_ids)
            if unknown:
                problems.add(skill, f"{kind} review references unknown guidance-id values: {unknown}")
            if kind == "domain" and not scoped:
                problems.add(skill, "domain review scope must contain guidance-ids")
            if kind == "structural" and not (claim["scope"]["files"] or claim["scope"]["concerns"]):
                problems.add(skill, "structural review scope needs files or concerns")

    supported: dict[tuple, dict] = {}
    environments: list[dict] = []
    for environment in record["evaluation"]["supported-environments"]:
        environments.append(environment)
        criteria = criteria_key(environment["acceptance-criteria"])
        if len(criteria) != len(set(criteria)):
            problems.add(skill, "supported environment contains duplicate acceptance criteria")
        key = (environment_key(environment), environment["required-suite-revision"], criteria)
        if key in supported:
            problems.add(skill, "duplicate supported environment")
        supported[key] = environment
    for claim in record["evaluation"]["claims"]:
        if claim.get("outcome") == "invalidated":
            continue
        environments.append(claim["environment"])
        criteria = criteria_key(claim["acceptance-criteria"])
        if len(criteria) != len(set(criteria)):
            problems.add(skill, "evaluation claim contains duplicate acceptance criteria")
        key = (environment_key(claim["environment"]), claim["suite-revision"], criteria)
        if key not in supported:
            problems.add(skill, "evaluation claim does not exactly match a supported environment")

    components = []
    for environment in environments:
        components.extend([environment["model"], environment["runtime"], *environment["tools"], *environment["dependencies"]])
        for group in (environment["tools"], environment["dependencies"]):
            keys = [component_key(item) for item in group]
            if len(keys) != len(set(keys)):
                problems.add(skill, "environment contains duplicate tool or dependency entries")
    for component in components:
        if not exact_version(component["version"]):
            problems.add(skill, f"environment version is not exact: {component['version']!r}")

    stability = record["development"]["stability"]
    if record["maintenance"]["status"] == "maintained" and not record["maintenance"]["stewards"]:
        problems.add(skill, "maintained skill needs at least one steward")
    if stability == "stable":
        if record["maintenance"]["status"] != "maintained" or record["distribution"]["status"] != "current":
            problems.add(skill, "stable skill must be maintained and current")
        if "compatibility" not in record or "migration" not in record["distribution"]:
            problems.add(skill, "stable skill needs compatibility and migration statements")
        if not record["evaluation"]["supported-environments"]:
            problems.add(skill, "stable skill needs at least one supported environment")
        subject = record["subject-revision"]["digest"]
        today = date.today().isoformat()
        review_claims = [
            claim
            for kind in ("structural", "domain")
            for claim in record["reviews"][kind]["claims"]
            if claim.get("outcome") != "invalidated"
            and claim["subject-revision"] == subject
            and claim["outcome"] == "reviewed"
            and claim.get("review-due", today) >= today
        ]
        structural = [
            claim for claim in record["reviews"]["structural"]["claims"]
            if claim in review_claims
        ]
        if not structural:
            problems.add(skill, "stable skill needs a current structural review")
        covered = {
            guidance_id
            for claim in record["reviews"]["domain"]["claims"]
            if claim in review_claims
            for guidance_id in claim["scope"]["guidance-ids"]
        }
        consequential = {item["guidance-id"] for item in guidance if item["consequential"]}
        if not consequential.issubset(covered):
            problems.add(skill, "stable skill lacks current domain-review coverage")
        accepted = {
            (
                environment_key(claim["environment"]),
                claim["suite-revision"],
                criteria_key(claim["acceptance-criteria"]),
            )
            for claim in record["evaluation"]["claims"]
            if claim.get("outcome") != "invalidated"
            and claim["subject-revision"] == subject
            and claim["result"]["outcome"] == "passed"
            and claim.get("valid-until", today) >= today
        }
        if not set(supported).issubset(accepted):
            problems.add(skill, "stable skill lacks accepted evaluation coverage")


def main() -> None:
    problems = Problems()
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    jsonschema.Draft7Validator.check_schema(schema)
    validator = jsonschema.Draft7Validator(schema, format_checker=jsonschema.FormatChecker())
    for skill_dir in sorted(path for path in ROOT.iterdir() if path.is_dir()):
        skill = skill_dir.name
        record_path = skill_dir / "stewardship.yaml"
        if not record_path.exists():
            problems.add(skill, "missing stewardship.yaml")
            continue
        try:
            metadata = frontmatter(skill_dir / "SKILL.md").get("metadata")
            if not isinstance(metadata, dict) or metadata.get("omf-stewardship") != "stewardship.yaml":
                problems.add(skill, "frontmatter must point metadata.omf-stewardship to stewardship.yaml")
            elif LEGACY_METADATA.intersection(metadata):
                problems.add(skill, "legacy governance metadata must move to stewardship.yaml")
        except (OSError, ValueError, yaml.YAMLError) as error:
            problems.add(skill, str(error))
        try:
            record = yaml.safe_load(record_path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as error:
            problems.add(skill, f"cannot load stewardship.yaml: {error}")
            continue
        errors = sorted(validator.iter_errors(record), key=lambda error: list(error.absolute_path))
        if errors:
            for error in errors:
                location = ".".join(str(part) for part in error.absolute_path) or "record"
                problems.add(skill, f"schema {location}: {error.message}")
            continue
        if record["skill"]["name"] != skill:
            problems.add(skill, "record skill.name does not match its directory")
        paths = validate_paths(skill_dir, record, problems)
        validate_manifest(skill_dir, record, paths, problems)
        validate_semantics(skill_dir, record, problems)
        print(f"Checked stewardship for {skill}")
    problems.finish()


if __name__ == "__main__":
    main()
