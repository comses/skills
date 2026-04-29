# Peer-Review References Companion Guide

This directory contains normative guidance and checklists for peer-review readiness outputs.

## Files

- `PEER-REVIEW-CHECKLIST.md`:
  Primary required-criteria checklist for peer-review readiness assessment.

## Related compressed artifacts

These artifacts live in `../assets/` and should be maintained alongside this references directory:

- `../assets/COMSES-REVIEWS-COMPRESSED.md`
- `../assets/EVERSE-INDICATORS-COMPRESSED.md`

## Why this exists

External rubric and indicator sources evolve over time. This directory provides local, versioned guidance that keeps review behavior stable and auditable while preserving compressed summaries for fast reuse.

## Maintenance expectation

Treat these references and related compressed artifacts as living resources:

- Review after substantive CoMSES review criteria changes
- Review after major EVERSE indicator updates
- Record changes in pull requests with date and rationale

Use the repository-local maintainer meta skill for coordinated updates:

- `.github/skills/update-skill/SKILL.md`

When upstream changes affect semantics, update the linked peer-review files in the same PR:

- `../SKILL.md`
- `PEER-REVIEW-CHECKLIST.md`
- `../assets/COMSES-REVIEWS-COMPRESSED.md`
- `../assets/EVERSE-INDICATORS-COMPRESSED.md`
- `../evals.json` (if output or trigger expectations change)
