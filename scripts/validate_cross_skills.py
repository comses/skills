#!/usr/bin/env python3

import json
import sys
from pathlib import Path

OUTPUT_FILE = "results_cross.json"


# ---- mock agent (replace later with real trace) ----
def mock_agent_run(prompt):
    invoked = []

    p = prompt.lower()

    if "odd" in p or "documentation" in p:
        invoked.append("document")
    if "publish" in p or "citable" in p or "metadata" in p:
        invoked.append("fair4rs")
    if "slurm" in p or "hpc" in p:
        invoked.append("hpc")
    if "ospool" in p or "htcondor" in p or "osg" in p:
        invoked.append("ospool")
    if "review" in p or "ready" in p or "submission" in p:
        invoked.append("peer-review")

    return invoked


# ---- evaluation logic ----
def evaluate_case(e):
    prompt = e["prompt"]
    expected = e.get("skills_expected", [])
    invoked = mock_agent_run(prompt)

    failures = []

    # ---- skill selection ----
    if expected:
        missing = set(expected) - set(invoked)
        extra = set(invoked) - set(expected)

        if missing:
            failures.append("missing_step")

        if extra:
            failures.append("boundary_violation")

    else:
        # should not trigger any skills
        if invoked:
            failures.append("over_trigger")

    # ---- ordering (simple heuristic) ----
    if expected and len(expected) > 1:
        if invoked[:len(expected)] != expected:
            failures.append("wrong_order")

    # ---- planning (multi-step prompts) ----
    if len(expected) >= 3 and len(invoked) < len(expected):
        failures.append("no_planning")

    # ---- completeness ----
    if expected and len(invoked) < len(expected):
        failures.append("incomplete_execution")

    # dedupe
    failures = list(set(failures))

    passed = len(failures) == 0

    return {
        "id": e["id"],
        "type": e["type"],
        "passed": passed,
        "expected": expected,
        "invoked": invoked,
        "failure_modes": failures,
    }


# ---- main ----
def main(path):
    data = json.loads(Path(path).read_text())

    results = []
    passed = 0

    for e in data["evals"]:
        r = evaluate_case(e)
        results.append(r)

        print(f"\nEval {e['id']}")
        print(f"Prompt: {e['prompt']}")
        print(f"Expected: {r['expected']}")
        print(f"Invoked: {r['invoked']}")
        print(f"Failures: {r['failure_modes']}")

        if r["passed"]:
            print("✅ PASS")
            passed += 1
        else:
            print("❌ FAIL")

    # write results for aggregation
    Path(OUTPUT_FILE).write_text(json.dumps(results, indent=2))

    total = len(results)
    print(f"\nSummary: {passed}/{total} passed")

    # fail CI if any fail
    if passed < total:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: validate_cross_skills.py <evals.json>")
        sys.exit(1)

    main(sys.argv[1])