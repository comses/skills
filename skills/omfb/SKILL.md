---
name: omfb
description: |
  Use this skill when planning or reviewing the implementation of a computational
  model as research software. Helps translate scientific models into maintainable
  implementations, preserve traceability to the conceptual model, identify
  implementation risks, and delegate platform-specific practices to specialized
  guidance.

  Expected output: implementation guidance, implementation review, implementation
  planning, and routing to platform-specific implementation guidance.
license: MIT
compatibility: Works with agent-based, system dynamics, statistical, simulation,
  optimization, and hybrid computational models.
metadata:
  domain: computational-modeling
  maturity: alpha
  audience: model developers
  category: implementation
---

# Model Implementation Guidance

## When to Use This Skill

Use this skill to:

- plan the implementation of a conceptual model into research software.
- review implementation decisions to ensure they preserve scientific intent.
- organize model architecture for maintainability and traceability.
- identify implementation risks or prepare a model for coding agents.

Do **not** use this skill when: performing conceptual modeling, uncertainty analysis, evaluation methodology, or seeking language-specific coding advice.

## OMFA Handoff Contract

OMFB consumes the reviewable scientific artifacts produced by OMFA. These artifacts are the authoritative implementation specification. These artifacts are the authoritative description of scientific intent and SHOULD be treated as the implementation specification. Implementation artifacts supplement, but never supersede, these scientific artifacts.

For agent-based models (ABMs), `artifacts/abm-spec.md` is the authoritative implementation/planning artifact. If the work is ABM implementation or ABM implementation planning and that artifact is absent, pause and route to OMFA instead of inferring or reconstructing the ABM specification.

## Required Inputs

OMFB uses reviewable artifacts as the authoritative implementation specification.

Before substantial implementation begins, the following artifacts MUST exist unless the work is explicitly exploratory or the omission is justified.

| Artifact | Status | Purpose |
|----------|--------|---------|
| `artifacts/conceptual-model.md` | REQUIRED | Authoritative conceptual specification. |
| `artifacts/assumptions.md` | REQUIRED | Scientific assumptions that implementation must preserve. |
| `artifacts/implementation/plan.md` | OPTIONAL | Existing implementation planning, if resuming work. |

### Conditional Inputs

Load these artifacts only when they materially affect implementation decisions.

| Artifact | When Required |
|----------|---------------|
| `artifacts/research-questions.md` | When implementation choices affect the questions the model is intended to answer. |
| `artifacts/problem-statement.md` | When project scope or intended use influences implementation priorities. |
| `artifacts/uncertainty-register.md` | When stochasticity, calibration, numerical methods, or experimental design influence implementation. |
| `artifacts/analysis-plan.md` | When implementation must support planned experiments, outputs, or evaluation. |
| `artifacts/stakeholder-register.md` | When implementation decisions have governance, transparency, privacy, or participation implications. |
| `artifacts/abm-spec.md` | When the work is ABM implementation or ABM implementation planning. Treat as authoritative; if absent, pause and route to OMFA rather than inferring it. |

## Guidance Library

Load only the implementation guidance required from `references/`.

| Context | Guidance |
|----------|----------|
| General implementation planning | `references/implementation-planning.md` |
| Architecture and modularization | `references/architecture.md` |
| Verification planning           | `references/verification.md` |
| Stochastic simulation           | `references/stochastic.md` |
| Performance optimization        | `references/performance.md` |
| Parallel execution              | `references/parallel.md` |
| Language and framework idioms   | `references/platform-guidance.md` |

Use `references/platform-guidance.md` to choose the platform; detailed language or framework idioms belong in the project's tooling or another applicable specialist.

## Deliverables

OMFB creates or maintains:

| Artifact | Purpose |
|----------|---------|
| `artifacts/implementation/plan.md` | Implementation plan |
| `artifacts/implementation/architecture.md` | Implementation architecture |
| `artifacts/implementation/module-mapping.md` | Mapping from conceptual model to implementation |
| `artifacts/implementation/parameter-schema.md` | Externalized parameters and configuration |
| `artifacts/implementation/verification-plan.md` | Implementation verification plan |

## Implementation Contract

OMFB MUST:

- preserve traceability between conceptual models and implementation;
- preserve separation between scientific logic and implementation infrastructure;
- document consequential implementation decisions and implementation-introduced assumptions;
- produce reviewable implementation artifacts;
- delegate language- and platform-specific guidance when appropriate;
- return implementation findings that require revision of upstream conceptual artifacts.

OMFB MUST NOT:

- silently modify the conceptual model;
- reinterpret scientific assumptions for implementation convenience;
- introduce implementation-driven behavior without documenting and justifying it.

If implementation constraints require changes to scientific assumptions or conceptual structure, pause planning and recommend revising affected upstream artifact(s).

## Gotchas

- **Implementation can silently redefine the conceptual model.** Watch for data structures, scheduling logic, or approximation choices that change the scientific meaning of entities or relationships. Surface these explicitly rather than letting them become implicit behavior.
- **OMFB is not a coding tutor.** It provides architecture and traceability guidance; use `references/platform-guidance.md` for platform selection, and keep detailed language/framework idioms in the project's tooling or another applicable specialist.
- **Traceability without reviewability is insufficient.** A mapping from conceptual model to code is useful only if it is kept current and reviewed when either side changes.
- **Do not duplicate OMFA's work.** Conceptual modeling, uncertainty analysis, and evaluation methodology remain OMFA responsibilities; OMFB consumes their outputs, not replace them.
