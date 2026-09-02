# Implementation Architecture Guidance

Use this reference when OMFB needs to structure the implementation architecture for a computational model.

## Core Principle

Architecture exists to keep scientific intent reviewable. Every module or component should have a single, identifiable responsibility.

## Recommended Modular Boundaries

| Layer | Responsibility | Examples |
| ----- | -------------- | -------- |
| **Model domain** | Scientific entities, state, rules, and dynamics. | Agent classes, equation solvers, network topology. |
| **Experiment runner** | Initialization, parameter loading, execution loop. | Main script, batch runner, CLI. |
| **Output / observability** | Logging, metrics, serialization, provenance. | Writers, reporters, checkpointing. |
| **Utilities** | Cross-cutting helpers with no scientific meaning. | Randomness wrappers, path helpers, config loaders. |

## Traceability Requirements

- Maintain a module-to-concept mapping in `omf-artifacts/implementation/module-mapping.md`.
- Each scientific entity in `omf-artifacts/conceptual-model.md` should map to one or more implementation artifacts.
- Each implementation artifact should justify its existence by serving a documented scientific or operational need.

## Coupling Rules

- Scientific modules should not depend on execution infrastructure.
- Configuration should be injected, not discovered at runtime via global state.
- Avoid passing raw data structures across module boundaries; use explicit interfaces or schemas.

## Warning Signs

- A single file contains both model logic and plotting/serialization.
- Scientific constants are embedded deep in execution code.
- Changing the execution platform would require rewriting scientific code.
