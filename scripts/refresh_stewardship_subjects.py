#!/usr/bin/env python3

"""Refresh deterministic subject manifests in existing stewardship records."""

from __future__ import annotations

import hashlib
from pathlib import Path

import yaml

from validate_stewardship import Problems, file_digest, validate_paths


ROOT = Path("skills")


def main() -> None:
    for skill_dir in sorted(path for path in ROOT.iterdir() if path.is_dir()):
        record_path = skill_dir / "stewardship.yaml"
        if not record_path.exists():
            continue
        record = yaml.safe_load(record_path.read_text(encoding="utf-8"))
        problems = Problems()
        paths = validate_paths(skill_dir, record, problems)
        if problems.items:
            for problem in problems.items:
                print(f"error: {problem}")
            raise SystemExit(1)
        manifest = [{"path": path, "digest": file_digest(skill_dir / path)} for path in paths]
        stream = bytearray()
        for entry in manifest:
            stream.extend(entry["path"].encode("utf-8"))
            stream.extend(b"\0")
            stream.extend(entry["digest"].encode("ascii"))
            stream.extend(b"\n")
        record["subject-revision"]["manifest"] = manifest
        record["subject-revision"]["digest"] = "sha256:" + hashlib.sha256(stream).hexdigest()
        record_path.write_text(
            yaml.safe_dump(record, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
        print(f"Refreshed stewardship subject for {skill_dir.name}")


if __name__ == "__main__":
    main()
