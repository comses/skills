# ODD Companion References

This directory contains companion references for generating and validating ODD+2-ready model documentation.

## Files

- `ODD-CHECKLIST.md`:
  Compact 23-point checklist for assessing ODD completeness, replication-readiness, and common failure modes.

- `ODD-METHODOLOGY.md`:
  Practical methodology guidance for drafting ODD sections from implemented model behavior, including workflow and review heuristics.

- `../assets/ODD-TEMPLATE.md`:
  Drafting scaffold for complete ODD narratives, including sections, tables, and submodel structure prompts.

## Why this exists

ODD guidance and modeling documentation expectations evolve over time. These references provide local, versioned guidance so contributors can produce consistent, high-quality model documentation while preserving a clear refresh path against authoritative sources.

## Maintenance expectation

Treat these references as a living resource:

- Review after substantive ODD guidance updates
- Record changes in pull requests with date and rationale

Use the repository-local maintainer meta skill for coordinated updates:

- `.github/skills/update-skill/SKILL.md`

When upstream changes affect semantics, update related files in the same PR:

- `../SKILL.md`
- `ODD-CHECKLIST.md`
- `ODD-METHODOLOGY.md`
- `../assets/ODD-TEMPLATE.md`
- `../evals.json` (if output or trigger expectations change)
