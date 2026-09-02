#!/usr/bin/env python3

import json
import sys
from pathlib import Path

OUTPUT_FILE = "results_cross.json"


# ---- deterministic routing smoke test (not an agent-behavior evaluator) ----
def mock_agent_run(prompt):
    invoked = []

    p = prompt.lower()

    if "conceptual model" in p or "model card" in p or "scientific specification" in p:
        invoked.append("omfa")
    if "odd" in p or "documentation" in p or ("complete" in p and "publishable" in p):
        invoked.append("document")
    if (
        "fair" in p
        or "publication" in p
        or "publishable" in p
        or "citable" in p
        or "metadata" in p
        or "archive" in p
        or "archiv" in p
        or "citation" in p
        or "reproduc" in p
        or "portable" in p
        or "doi" in p
        or "package" in p
        or "provenance" in p
    ) and "general terms" not in p:
        invoked.append("fair")
    if "large parameter sweeps" in p:
        invoked.append("hpc")
        invoked.append("ospool")
    if "scalable" in p:
        invoked.append("hpc")
        invoked.append("ospool")
    if "at scale" in p:
        invoked.append("ospool")
    if "slurm" in p or "hpc" in p:
        invoked.append("hpc")
    if "ospool" in p or "htcondor" in p or "osg" in p:
        invoked.append("ospool")
    if (
        "review" in p
        or "ready" in p
        or "submission" in p
        or "readiness" in p
        or "assessment" in p
        or "reviewed" in p
    ):
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

        if (
            e.get("sequence_required", False)
            and set(expected) == set(invoked)
            and expected != invoked
        ):
            failures.append("wrong_order")

    else:
        # should not trigger any skills
        if invoked:
            failures.append("over_trigger")

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
