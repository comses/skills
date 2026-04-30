#!/usr/bin/env python3

import json
from collections import Counter, defaultdict
from pathlib import Path
import argparse


def load_all_evals():
    eval_files = list(Path("skills").rglob("evals.json"))
    data = []

    for f in eval_files:
        try:
            content = json.loads(f.read_text())
            skill = content.get("skill_name", f.parent.name)
            for e in content.get("evals", []):
                e["_skill"] = skill
                data.append(e)
        except Exception as e:
            print(f"⚠️ Failed to load {f}: {e}")

    return data


def aggregate_expected_failures(evals):
    """Counts declared failure_modes (design-time coverage)"""
    global_counts = Counter()
    per_skill = defaultdict(Counter)

    for e in evals:
        if e.get("type") in ["adversarial", "cross-adversarial"]:
            for fm in e.get("failure_modes", []):
                global_counts[fm] += 1
                per_skill[e["_skill"]][fm] += 1

    return global_counts, per_skill


def load_results(path):
    """
    Expected format:
    [
      {
        "id": 101,
        "skill": "document",
        "passed": false,
        "failure_modes": ["over_trigger"]
      }
    ]
    """
    return json.loads(Path(path).read_text())


def aggregate_actual_failures(results):
    """Counts observed failures from CI run"""
    counts = Counter()
    per_skill = defaultdict(Counter)

    for r in results:
        if not r.get("passed", True):
            for fm in r.get("failure_modes", []):
                counts[fm] += 1
                per_skill[r["skill"]][fm] += 1

    return counts, per_skill


def print_table(title, counts, per_skill):
    total = sum(counts.values())

    print(f"\n=== {title} ===\n")

    if total == 0:
        print("No data.\n")
        return

    print("Global:")
    for k, v in counts.most_common():
        pct = (v / total) * 100
        print(f"  {k:22} {v:4} ({pct:5.1f}%)")

    print("\nPer skill:")
    for skill, counter in per_skill.items():
        print(f"\n  [{skill}]")
        s_total = sum(counter.values())
        for k, v in counter.most_common():
            pct = (v / s_total) * 100 if s_total else 0
            print(f"    {k:20} {v:4} ({pct:5.1f}%)")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", help="Path to CI results JSON")
    args = parser.parse_args()

    evals = load_all_evals()

    # design-time coverage
    expected_counts, expected_per_skill = aggregate_expected_failures(evals)
    print_table("Expected Failure Coverage (from eval definitions)",
                expected_counts, expected_per_skill)

    # runtime failures (optional)
    if args.results:
        results = load_results(args.results)
        actual_counts, actual_per_skill = aggregate_actual_failures(results)

        print_table("Observed Failures (from CI run)",
                    actual_counts, actual_per_skill)


if __name__ == "__main__":
    main()
