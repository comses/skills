# EVERSE Research Software Indicators (Compressed)

Source: https://everse.software/indicators/website/indicators.html
Last reviewed: 2026-04-28

## Purpose

EVERSE indicators define measurable software quality signals across FAIRness, maintainability, reliability, security, sustainability, and related dimensions.

## High-Value Indicator Set for Model Peer Review

Use this subset for practical review support (non-gating unless explicitly elevated by policy):

### Metadata and FAIRness
- Descriptive metadata present and up to date
- License present
- Citation metadata present (for example CFF)
- Persistent/unique identifier support
- Releases/tags available
- Versioning conventions used
- Registry/archive presence where relevant

### Reproducibility and Execution
- Requirements/dependencies specified
- Version control used
- Documentation available
- Downloadable/reusable package form where applicable

### Quality Assurance
- Tests present
- CI workflows present
- Sufficient test coverage evidence where available
- Human code review requirements in contribution workflow
- Lint/static checks or warning tools in use

### Security and Risk
- No leaked credentials
- No known critical vulnerabilities
- Static analysis for common vulnerabilities where applicable

### Maintainability and Support
- Issue tracking available
- Repository activity/maintenance signal
- Code complexity/cohesion/coupling indicators within acceptable bounds when measured

## Practical Mapping for This Repository

- Treat indicators as evidence amplifiers for review findings.
- Do not override required CoMSES criteria with indicator-only strength.
- Tests and CI remain Major but nonblocking unless they undermine a required criterion (for example reproducible execution claims).

## Refresh Guidance

Because indicator catalogs and definitions may change:

- Review cadence: re-check source page every 3 months.
- Immediate refresh triggers:
  - Indicator names/IDs used in checklist are renamed or removed
  - Dimension changes that alter interpretation of core indicators
  - New indicators that materially affect peer-review quality judgments
- Refresh procedure:
  1. Diff the current indicator table against this compressed subset.
  2. Keep only indicators used by peer-review workflow; avoid full-table duplication.
  3. Update Last reviewed date.
  4. If a mapped indicator changes semantics, update peer-review checklist language in the same PR.
