# EVERSE SMP Refresh Policy

Use this policy to keep local SMP guidance aligned with evergreen recommendations from EVERSE RSQKit.

Primary source:
- https://everse.software/RSQKit/software_management_planning

## Refresh Cadence

Event-driven review when one of the following occurs:
- Material changes in EVERSE SMP guidance
- New institutional/funder SMP requirements
- Significant updates to FAIR4RS interpretation in this repository

Recommended schedule fields:
- Last reviewed:
- Next scheduled review:
- Reviewer:

## Review Procedure

1. Check the current EVERSE Software Management Planning page.
2. Compare local references (`SMP-TEMPLATE.md`, crosswalk, and skill instructions) against current guidance.
3. Update local files where guidance has diverged.
4. Record what changed and why in the pull request description.
5. Update review metadata in this file.

## What to Validate During Review

Validate that local guidance still covers:
- SMP as a living document across the software lifecycle
- Stakeholder participation and shared responsibilities
- Core lifecycle areas:
  - General information
  - Collaboration and licensing
  - Analysis/design/implementation
  - Testing and quality assurance
  - Deployment and delivery
  - Versioning and releases
  - Maintenance and sustainability
  - Discoverability and preservation
- Software-type-aware priorities (exploratory vs reusable vs long-lived infrastructure)
- Practical integration with common platforms and repositories

## Quality Gates for Accepting Refresh Changes

- Changes preserve model-agnostic language.
- Guidance remains compatible with FAIR4RS-oriented publication workflows.
- Template remains human-readable and usable in typical coding-agent interactions.
- Any removed section is explicitly justified.
- Links remain valid at review time.

## Review Metadata

- Last reviewed: 2026-04-14
- Reviewer: Repository initialization workflow
- Next scheduled review: 2026-07-14
