# Performance Optimization Guidance

Use this reference when implementation faces runtime, memory, or scaling constraints.

## Optimization Rule

Optimize only after measuring. Do not change scientific meaning for speed without documenting the tradeoff.

## Steps

1. **Profile before refactoring.** Identify the actual bottleneck. Common culprits: nested loops, unnecessary I/O, object churn, and inefficient data structures.
2. **Preserve correctness.** Any approximation introduced for performance must be recorded in `omf-artifacts/assumptions.md` or `omf-artifacts/implementation/plan.md`.
3. **Benchmark against a baseline.** Use the simplest correct implementation as the reference. Report speedup and any numerical drift.
4. **Set explicit targets.** Define acceptable runtime and memory budgets for representative problem sizes.

## Common Techniques

| Problem | Safe First Response | Risk |
| ------- | ------------------- | ---- |
| Slow inner loop | Vectorization or compiled kernel | Numerical differences, readability loss |
| Large state memory | Sparse representations or chunked storage | Indexing errors, altered dynamics |
| Excessive I/O | Batch writes, binary formats | Data provenance complexity |
| Repeated initialization | Memoization or caching | Stale state between runs |

## Warning Signs

- Optimizing before the model is verified.
- Micro-optimizing code that is not in the measured bottleneck.
- Accepting numerical differences without quantifying them.

## Routing

If performance requirements force a redesign of the conceptual model or experimental design, route back to OMFA.
