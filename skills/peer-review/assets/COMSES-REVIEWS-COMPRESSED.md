# CoMSES Peer Review Rubric (Compressed)

Source: https://www.comses.net/reviews/
Last reviewed: 2026-04-28

## Purpose

CoMSES peer review checks whether a computational model is reusable and publishable with baseline software engineering and documentation quality, aligned with FAIR4RS and frictionless reuse goals.

## Core Criteria (Compressed)

1. Ease of Execution
- A third party should be able to run the model with reasonable effort.
- Dependencies, data inputs, build/compile steps, and execution commands should be clearly documented.

2. Thorough Documentation
- Narrative documentation must exist as a standalone artifact (inline comments alone are insufficient).
- ODD is preferred, but equivalent frameworks are acceptable when they provide comparable model explanation depth.
- Documentation should enable another modeler to understand and replicate the model without reverse-engineering source code.
- Flowcharts, equations, and diagrams are encouraged.

3. Code Quality
- Code should be readable, organized, and maintainable.
- Variable/function names should be meaningful.
- Comments should clarify non-obvious methods, functions, and parameters.
- Technical debt patterns (unused/duplicated code, excessive globals, tangled logic) reduce review readiness.

## Scope Boundary

This rubric is not primarily for judging scientific novelty or theoretical validity.
Those concerns may be raised privately with review editors.

## Operational Notes

- Peer review occurs while codebase is private so authors can revise files during review.
- Publishing a release locks release files; major file-level fixes may require drafting a new release.

## Refresh Guidance

Because this rubric may evolve:

- Review cadence: re-check source page at least every 6 months.
- Immediate refresh triggers:
  - Any wording change to the three core criteria
  - New required submission or review process steps
  - New scope boundaries on what reviewers must assess
- Refresh procedure:
  1. Compare this file against live page sections: process overview, criteria list, scope notes.
  2. Update changed bullets only; keep this file compressed.
  3. Record date in Last reviewed.
  4. If criteria semantics changed, update peer-review checklist and skill instructions in the same PR.
