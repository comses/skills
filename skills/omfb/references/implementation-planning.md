# Implementation Planning Guidance

Use this reference when OMFB is asked to plan the implementation of a conceptual model as research software.

## Input

The authoritative inputs are OMFA artifacts:

- `omf-artifacts/conceptual-model.md` — entities, processes, and system boundaries.
- `omf-artifacts/assumptions.md` — scientific assumptions that implementation must preserve.
- `omf-artifacts/implementation/plan.md` — any existing plan, when resuming work.
- `omf-artifacts/abm-spec.md` — for agent-based model implementation/planning; treat as authoritative and do not infer missing ABM details.

If the task is ABM implementation/planning and `omf-artifacts/abm-spec.md` is missing, pause and route to OMFA instead of synthesizing the specification.

## Output

OMFB creates or updates `omf-artifacts/implementation/plan.md`.

## Planning Steps

1. **Identify the implementation surface.** Map conceptual entities and processes to candidate code artifacts (modules, classes, functions, configuration files).
   - For ABMs, derive agent, environment, interaction, and scheduling structures from `omf-artifacts/abm-spec.md`.
2. **Choose the default architecture.** Prefer a clear separation between:
   - scientific logic (what the model means);
   - execution infrastructure (how it runs);
   - input/output and configuration.
3. **Externalize parameters.** Decide which quantities are configuration versus hard-coded constants. Document why each is configurable.
4. **Schedule verification checkpoints.** Define what must be true before implementation is considered complete (tests, reviews, comparisons).
5. **Flag risks.** Record approximation choices, performance constraints, or tool limitations that could alter scientific meaning.

## Must / Must-Not

- MUST preserve traceability from each implementation decision back to a conceptual-model element or documented assumption.
- MUST treat `omf-artifacts/abm-spec.md` as authoritative for ABM implementation/planning.
- MUST pause and route to OMFA if ABM implementation/planning is requested but `omf-artifacts/abm-spec.md` is absent.
- MUST NOT silently change the conceptual model to fit implementation convenience.
- MUST recommend revisiting OMFA artifacts when implementation constraints force a scientific change.
