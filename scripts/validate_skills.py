#!/usr/bin/env python3

import os
import json
import re
import sys
from pathlib import Path

ROOT = Path("skills")


def fail(msg):
    print(f"❌ {msg}")
    sys.exit(1)


def warn(msg):
    print(f"⚠️  {msg}")


def load_frontmatter(text):
    if not text.startswith("---"):
        fail("Missing frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail("Invalid frontmatter format")
    return parts[1]


def parse_name(frontmatter):
    m = re.search(r"^name:\s*([^\n]+)", frontmatter, re.MULTILINE)
    if not m:
        fail("Missing name field")
    return m.group(1).strip()


def parse_description(frontmatter):
    m = re.search(r"description:\s*\|\s*\n([\s\S]+?)(\n\w+:|\Z)", frontmatter)
    if not m:
        fail("Missing description block")
    return m.group(1).strip()


def count_lines(path):
    return sum(1 for _ in open(path))


def check_skill(skill_dir):
    skill_name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        fail(f"{skill_name}: missing SKILL.md")

    text = skill_md.read_text()
    frontmatter = load_frontmatter(text)

    name = parse_name(frontmatter)
    if name != skill_name:
        fail(f"{skill_name}: name mismatch (frontmatter={name})")

    desc = parse_description(frontmatter)
    if len(desc) < 100:
        fail(f"{skill_name}: description too short")

    if "Use this skill when" not in desc:
        warn(f"{skill_name}: description missing trigger phrase")

    if count_lines(skill_md) > 500:
        fail(f"{skill_name}: SKILL.md exceeds 500 lines")

    # evals
    evals_path = skill_dir / "evals.json"
    if not evals_path.exists():
        fail(f"{skill_name}: missing evals.json")

    data = json.loads(evals_path.read_text())
    evals = data.get("evals", [])

    pos = sum(1 for e in evals if e.get("should_trigger") is True)
    neg = sum(1 for e in evals if e.get("should_trigger") is False)

    if pos < 3:
        fail(f"{skill_name}: <3 positive evals")
    if neg < 3:
        fail(f"{skill_name}: <3 negative evals")

    # path hygiene
    for line in text.splitlines():
        if "references/" in line or "assets/" in line:
            if line.strip().startswith("/"):
                fail(f"{skill_name}: absolute path found")

    print(f"✅ {skill_name} OK")


def main():
    if not ROOT.exists():
        fail("skills/ directory not found")

    for skill_dir in ROOT.iterdir():
        if skill_dir.is_dir():
            check_skill(skill_dir)

    print("\n🎉 All skills validated")


if __name__ == "__main__":
    main()
