# OMFA Reference Library

This directory contains the methodological references, guidance documents, and supporting materials used by the Open Modeling Foundation Assistant (OMFA).

The reference library separates scientific literature, expert methodological guidance, and reusable templates so each can evolve independently.

## Structure

### `REFERENCES.md`

Canonical annotated bibliography for computational modeling methodology, including:

- good modeling practice
- conceptual modeling
- agent-based modeling
- uncertainty and sensitivity analysis
- evaluation and validation
- participatory modeling
- deep uncertainty
- ethics and governance
- FAIR principles relevant to computational modeling

### `guidance/`

Expert methodological guidance that helps the agent:

- recognize when a methodology applies
- make consequential analytical choices
- select appropriate methods
- generate reviewable intermediate artifacts
- identify common methodological failure patterns

Each guidance document addresses a distinct methodological question and is loaded only when relevant.

Current guidance includes:

- `lifecycle.md`
- `project-bootstrap.md`
- `conceptual-modeling.md`
- `project-planning.md`
- `implementation-planning.md`
- `analysis-planning.md`
- `abm.md`
- `uncertainty.md`
- `deep-uncertainty.md`
- `evaluation.md`
- `participatory.md`
- `ethics.md`

### `assets/`

Reusable templates, schemas, and example artifacts instantiated during the modeling lifecycle.

## Design Principles

The reference library intentionally separates:

- **scientific literature** (`REFERENCES.md`)
- **methodological reasoning** (`guidance/`)
- **reusable project artifacts** (`assets/`)

This separation allows references, guidance, and templates to evolve independently while remaining internally consistent.

## Maintenance

Treat this library as a living resource.

When updating the library:

- add new literature to `REFERENCES.md`
- update guidance documents when methodological recommendations evolve or as foundation models improve and make them obsolete
- update templates when project artifacts or documentation standards change
- preserve consistency between the bibliography, guidance, and generated artifacts
