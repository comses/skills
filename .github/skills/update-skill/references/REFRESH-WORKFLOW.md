# Refresh Workflow Reference

Use this reference when updating skills that depend on evolving external standards.

## Trigger Types

- Scheduled cadence refresh
- Upstream semantic change
- New/revised indicator or rubric field
- Local drift discovered during review

## Minimal Update Loop

1. Capture current upstream source and date.
2. Compare to local compressed/reference content.
3. Update affected local artifacts.
4. Align downstream files in same PR:
   - `SKILL.md`
   - `references/*`
   - `assets/*`
   - `evals.json` if output/behavior expectations change
5. Record a changelog note in the PR.

## Quality Checks

- Terminology remains consistent across files.
- Required decision rules remain explicit.
- Templates and checklists reflect current policy.
- Evals still verify intended behavior.
