---
name: update-skill
description: "Repository-local maintainer workflow for refreshing skill assets and references when upstream standards, rubrics, or guidance change. Use when updating compressed artifacts, checklists, and linked policy text across this repository in a consistent PR."
user-invocable: false
---

# Update Skill (Repository-Local)

Use this skill for maintainer updates in this repository only.

## When to Use

- Upstream standards or rubrics changed and local compressed artifacts may be stale
- A skill reference/checklist/template needs synchronized updates
- You need a repeatable refresh process across SKILL.md, references, assets, and evals

## Scope

This skill is local to this repository workspace (`.github/skills/update-skill`) and is not part of the published skill catalog under `skills/`.

## Workflow

1. Identify affected source(s) and fetch current upstream content.
2. Diff upstream changes against local compressed/reference artifacts.
3. Update only changed concepts; keep summaries compressed and decision-oriented.
4. Update "Last reviewed" dates for refreshed artifacts.
5. Propagate semantic changes in the same PR to all impacted files:
   - skill orchestration (`skills/*/SKILL.md`)
   - normative references/checklists (`skills/*/references/*`)
   - templates/assets (`skills/*/assets/*`)
   - eval expectations (`skills/*/evals.json`) when behavior changes
6. Add a concise PR note using `assets/REFRESH-PR-NOTE-TEMPLATE.md`.

## Guardrails

- Do not copy upstream pages verbatim.
- Preserve repository-specific policy decisions unless explicitly changed.
- Prefer smallest coherent change set that keeps references, templates, and evals aligned.

## References

- Process details: `references/REFRESH-WORKFLOW.md`
- PR note template: `assets/REFRESH-PR-NOTE-TEMPLATE.md`
