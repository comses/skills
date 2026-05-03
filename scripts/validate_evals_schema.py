#!/usr/bin/env python3

import json
import sys
from pathlib import Path

import jsonschema

SCHEMA_PATH = Path("evals/schema/schema.json")


def load_schema():
    return json.loads(SCHEMA_PATH.read_text())


def validate_file(path, schema):
    data = json.loads(path.read_text())
    try:
        jsonschema.validate(instance=data, schema=schema)
        print(f"✅ {path} valid")
    except jsonschema.ValidationError as e:
        print(f"❌ {path} invalid")
        print(f"   → {e.message}")
        sys.exit(1)


def main():
    schema = load_schema()

    # validate all evals.json in skills/
    for path in Path("skills").rglob("evals.json"):
        validate_file(path, schema)

    # validate cross-skill evals
    for path in Path("evals").glob("*.json"):
        validate_file(path, schema)


if __name__ == "__main__":
    main()
