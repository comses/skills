# Stochastic Simulation Guidance

Use this reference when implementation involves randomness, Monte Carlo methods, agents with probabilistic behavior, or any nondeterministic dynamics.

## Randomness Discipline

1. **Isolate randomness sources.** All stochastic draws should flow through a small, replaceable set of functions or a single generator. Avoid scattering `random()` calls through scientific code.
2. **Seed control.** Support seeding at the experiment level. Record the seed and the generator used in provenance output.
3. **Reproducibility notes.** Document known sources of non-reproducibility (parallel execution order, floating-point reductions across architectures, library version differences).

## Testing

- Use fixed seeds for regression tests.
- Report confidence intervals or distributional summaries, not single-run outcomes.
- Use statistical tests sparingly; prefer deterministic invariants where possible.

## Common Traps

- **Correlation by accident.** Reusing the same generator across unrelated processes can introduce hidden correlations.
- **Seed-dependent initialization.** A small initialization change can amplify into large trajectory differences.
- **Randomness in unexpected places.** Sorting ties, hash ordering, or thread scheduling can introduce nondeterminism even when the RNG is seeded.

## Output

Record stochastic design decisions in `omf-artifacts/implementation/verification-plan.md` and `omf-artifacts/implementation/plan.md`.
