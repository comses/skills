# Platform and Language Guidance

Use this reference when OMFB must choose or reason about implementation languages, frameworks, or runtime environments.

## Principle

OMFB provides architecture and traceability guidance. It is not a coding tutor. Language-specific idioms and detailed framework APIs belong in platform-specific guidance or the user's chosen tooling.

## Selection Checklist

When recommending a language or framework, consider:

1. **Ecosystem fit.** Does the platform have libraries for the model's domain (spatial, network, statistical, optimization)?
2. **Agent proficiency.** How well does the coding agent know the language and framework? Lower confidence means more tests, reviews, and manual intervention.
3. **Reproducibility.** Can dependencies be pinned? Is the runtime available to future users?
4. **Performance needs.** Does the platform meet the measured bottleneck requirements?
5. **Community longevity.** Is the platform maintained and citable?

## Responsibilities

- OMFB: decides overall architecture, module boundaries, traceability, and whether a platform can support the design.
- User / coding agent: writes and maintains the actual code.
- `fair` skill: handles packaging, dependency management, archival, and release readiness.
- `hpc` / `ospool` skills: handle job submission and resource allocation.

## Common Pitfalls

- Choosing a framework for familiarity rather than fit.
- Letting framework idioms reshape the conceptual model silently.
- Mixing framework-specific code into scientific modules.

## Output

Record platform choices and rationale in `omf-artifacts/implementation/plan.md` or `omf-artifacts/implementation/architecture.md`.
