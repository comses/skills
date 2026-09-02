# Implementation Verification Guidance

Use this reference when OMFB is asked to plan how the implementation will be verified against its scientific intent.

## Scope

Verification checks that the code correctly implements the conceptual model. It does not validate whether the model itself is right for the research question — that is OMFA evaluation territory.

## Planning Steps

1. **Define verification claims.** For each major process or equation, write a concrete claim such as "Agent wealth updates match the budget constraint in `assumptions.md`."
2. **Select verification methods.** Typical methods include:
   - Unit tests for isolated scientific functions.
   - Invariant checks during simulation runs.
   - Comparison with analytic or reference implementations.
   - Regression tests for fixed seeds.
3. **Assign coverage targets.** State which conceptual-model elements are covered by which tests or checks.
4. **Record expected results.** A verification test without an expected result is not a test.
5. **Define pass/fail criteria.** Decide thresholds for numerical tolerance, acceptable stochastic variation, and runtime regressions.

## Output

OMFB creates or updates `omf-artifacts/implementation/verification-plan.md`.

## Must / Must-Not

- MUST distinguish implementation bugs from model-design limitations.
- MUST NOT treat successful execution as evidence of correctness.
- MUST route questions about model validity or appropriateness back to OMFA.
