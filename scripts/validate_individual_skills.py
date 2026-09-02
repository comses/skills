#!/usr/bin/env python3

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path("skills")


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, skill, rule, msg, hint=None):
        self.errors.append((skill, rule, msg, hint))

    def warn(self, skill, rule, msg, hint=None):
        self.warnings.append((skill, rule, msg, hint))

    def print(self):
        if not self.errors and not self.warnings:
            print("🎉 All skills validated successfully")
            return

        def fmt(entries, label):
            if not entries:
                return
            print(f"\n{label}:")
            current = None
            for skill, rule, msg, hint in entries:
                if skill != current:
                    print(f"\n  [{skill}]")
                    current = skill
                print(f"    - ({rule}) {msg}")
                if hint:
                    print(f"      → fix: {hint}")

        fmt(self.errors, "❌ Errors")
        fmt(self.warnings, "⚠️ Warnings")

        print("\nSummary:")
        print(f"  Errors: {len(self.errors)}")
        print(f"  Warnings: {len(self.warnings)}")

        if self.errors:
            sys.exit(1)


def load_frontmatter(text, report, skill):
    if not text.startswith("---"):
        report.error(
            skill,
            "frontmatter",
            "Missing YAML frontmatter",
            "Add --- at top with name, description, license",
        )
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        report.error(
            skill,
            "frontmatter",
            "Malformed frontmatter block",
            "Ensure closing --- exists",
        )
        return None
    return parts[1]


def parse_field(pattern, text):
    m = re.search(pattern, text, re.MULTILINE)
    return m.group(1).strip() if m else None


def parse_description(frontmatter):
    m = re.search(r"description:\s*\|\s*\n([\s\S]+?)(\n\w+:|\Z)", frontmatter)
    return m.group(1).strip() if m else None


def parse_metadata(frontmatter):
    """Parse scalar keys directly nested under metadata without accepting misplaced fields."""
    lines = frontmatter.splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line == "metadata:") + 1
    except StopIteration:
        return None
    metadata = {}
    for line in lines[start:]:
        if line and not line.startswith((" ", "\t")):
            break
        match = re.match(r"^  ([a-z][a-z0-9-]*):\s*(.*?)\s*$", line)
        if match and match.group(2):
            metadata[match.group(1)] = match.group(2)
    return metadata


def check_skill(skill_dir, report):
    skill = skill_dir.name
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        report.error(
            skill,
            "structure",
            "Missing SKILL.md",
            "Create SKILL.md with required frontmatter",
        )
        return

    text = skill_md.read_text()
    frontmatter = load_frontmatter(text, report, skill)
    if not frontmatter:
        return

    # name
    name = parse_field(r"^name:\s*([^\n]+)", frontmatter)
    if not name:
        report.error(
            skill, "frontmatter", "Missing name field", "Add name: kebab-case-name"
        )
    elif name != skill:
        report.error(
            skill,
            "frontmatter",
            f"name '{name}' does not match folder '{skill}'",
            "Rename folder or update frontmatter",
        )

    # description
    desc = parse_description(frontmatter)
    if not desc:
        report.error(
            skill,
            "frontmatter",
            "Missing description block",
            "Use multiline description: |",
        )
    else:
        if len(desc) < 100:
            report.error(
                skill,
                "description",
                "Description < 100 characters",
                "Expand with triggers and expected output",
            )
        if "Use this skill when" not in desc:
            report.warn(
                skill,
                "description",
                "Missing 'Use this skill when' phrase",
                "Start description with trigger condition",
            )

    # license
    if not parse_field(r"^license:\s*([^\n]+)", frontmatter):
        report.error(
            skill,
            "frontmatter",
            "Missing license field",
            "Add license: MIT (or alternative)",
        )

    # identity and governance metadata
    governance_fields = {
        "source": "Add the canonical skill repository URL",
        "versioning": "Declare repository-release or another documented versioning policy",
        "maintainer": "Name the person or organization responsible for maintenance",
        "review-status": "Declare not-recorded, pending, or reviewed",
        "reviewed-by": "Name the reviewer or use unknown",
        "reviewed-at": "Record an ISO-8601 date or use unknown",
        "review-evidence": "Link the review record or use unknown",
        "review-cadence": "Declare a time- or event-based review cadence",
    }
    metadata = parse_metadata(frontmatter)
    if metadata is None:
        report.error(skill, "governance", "metadata must be a YAML mapping")
        metadata = {}
    governance = {}
    for field, hint in governance_fields.items():
        value = metadata.get(field)
        governance[field] = value
        if value is None or str(value).strip() == "":
            report.error(skill, "governance", f"Missing metadata field '{field}'", hint)

    if governance.get("review-status") not in {None, "not-recorded", "pending", "reviewed"}:
        report.error(
            skill,
            "governance",
            f"Invalid review-status '{governance['review-status']}'",
            "Use not-recorded, pending, or reviewed",
        )
    elif governance.get("review-status") == "not-recorded":
        report.warn(
            skill,
            "governance",
            "Methodological review has not been recorded",
            "Record domain reviewer evidence before promoting maturity or publishing a stable release",
        )
        for field in ("reviewed-by", "reviewed-at", "review-evidence"):
            if governance.get(field) != "unknown":
                report.error(
                    skill,
                    "governance",
                    f"'{field}' must be unknown when review-status is not-recorded",
                )
    elif governance.get("review-status") == "reviewed":
        for field in ("reviewed-by", "reviewed-at", "review-evidence"):
            if governance.get(field) in {None, "unknown"}:
                report.error(skill, "governance", f"Reviewed skill needs concrete '{field}'")
        reviewed_at = governance.get("reviewed-at")
        if reviewed_at not in {None, "unknown"}:
            try:
                date.fromisoformat(str(reviewed_at))
            except ValueError:
                report.error(skill, "governance", "reviewed-at must be an ISO-8601 date")

    source = str(governance.get("source", ""))
    if source and not re.match(r"^https://[^\s]+$", source):
        report.error(skill, "governance", "source must be a canonical HTTPS URL")

    required_contract_fields = (
        "Activation", "Authority", "Preconditions", "Effects", "Invariants",
        "Outputs", "Handoffs", "Completion", "Failure", "Provenance",
    )
    if "## Skill Contract" not in text:
        report.error(skill, "contract", "Missing '## Skill Contract' section")
    for field in required_contract_fields:
        if not re.search(rf"^- \*\*{field}:\*\*\s+\S", text, re.MULTILINE):
            report.error(skill, "contract", f"Missing or empty contract field '{field}'")

    # size
    lines = text.count("\n") + 1
    if lines > 500:
        report.error(
            skill,
            "size",
            f"SKILL.md has {lines} lines (>500)",
            "Move detail into references/",
        )

    # evals
    evals_path = skill_dir / "evals.json"
    if not evals_path.exists():
        report.error(
            skill,
            "evals",
            "Missing evals.json",
            "Add evals with ≥3 positive and ≥3 negative cases",
        )
    else:
        try:
            data = json.loads(evals_path.read_text())
            evals = data.get("evals", [])

            pos = sum(1 for e in evals if e.get("should_trigger") is True)
            neg = sum(1 for e in evals if e.get("should_trigger") is False)

            if pos < 3:
                report.error(
                    skill,
                    "evals",
                    f"{pos} positive evals (<3)",
                    "Add more should_trigger=true cases",
                )
            if neg < 3:
                report.error(
                    skill,
                    "evals",
                    f"{neg} negative evals (<3)",
                    "Add more should_trigger=false cases",
                )

        except Exception as e:
            report.error(skill, "evals", f"Invalid JSON: {e}", "Fix JSON formatting")

    # path hygiene
    for i, line in enumerate(text.splitlines(), start=1):
        if ("references/" in line or "assets/" in line) and line.strip().startswith(
            "/"
        ):
            report.error(
                skill,
                "paths",
                f"Absolute path on line {i}: {line.strip()}",
                "Use relative paths only",
            )

    # gotchas heuristic (optional)
    if "gotcha" not in text.lower():
        report.warn(
            skill,
            "gotchas",
            "No gotchas section detected",
            "Add non-obvious failure cases",
        )

    print(f"Checked {skill}")


def main():
    report = Report()

    if not ROOT.exists():
        print("❌ skills/ directory not found")
        sys.exit(1)

    for skill_dir in ROOT.iterdir():
        if skill_dir.is_dir():
            check_skill(skill_dir, report)

    report.print()


if __name__ == "__main__":
    main()
