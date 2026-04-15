# FAIR4RS to SMP Crosswalk

This crosswalk helps teams avoid duplicate effort when producing publication-readiness outputs and a Software Management Plan (SMP).

## How to use this crosswalk

1. Draft FAIR4RS deliverables (codemeta.json, CITATION.cff, DMP, publication checklist, metadata).
2. Draft SMP sections using `assets/SMP-TEMPLATE.md`.
3. Use this mapping to ensure consistency across both artifacts.
4. Resolve any conflicts in one place and propagate updates.

## Crosswalk Table

| FAIR4RS / Publication Deliverable | SMP Section(s) | Consistency Checks |
|---|---|---|
| codemeta.json (canonical machine-readable source) | Project Overview; Collaboration and Licensing; Versioning and Releases | codemeta.json is the authoritative source for software metadata; other metadata artifacts are synchronized from it. |
| Repository metadata (title, version, license, URL, keywords) | Project Overview; Collaboration and Licensing; Versioning and Releases | Title/version/license are identical in metadata, CITATION.cff, and SMP. |
| CITATION.cff + ORCID attribution | Collaboration, Governance, and Licensing | Contributor roles and credit policy in SMP match citation authorship and attribution rules. |
| Data Management Plan (DMP) | Deployment/Delivery; Discoverability/Preservation; Sustainability | DMP storage/access/archival commitments match SMP preservation and maintenance plans. |
| Publication checklist | Testing and QA; Versioning/Releases; Deployment/Delivery | Checklist pass criteria map to explicit SMP quality gates and release steps. |
| Dependency and environment documentation | Analysis/Design/Implementation; Testing and QA; Deployment/Delivery | Dependency strategy and compatibility policies are consistent across docs and release artifacts. |
| Archival target (Zenodo, institutional repository, Software Heritage) | Versioning/Releases; Discoverability/Preservation | DOI and archival strategy in SMP align with publication deposit workflow. |
| Governance and onboarding statements | Stakeholders/Roles; Governance; Sustainability | Maintainer responsibilities and succession plan are explicit and actionable. |
| Reproducibility claims | Testing and QA; Software-Type-Aware Priorities | Reproducibility methods (tests, CI, provenance) are concrete and software-type appropriate. |

## Minimal Coherence Checklist

Before finalizing outputs, verify:

- Names, versions, and license identifiers are identical across all outputs.
- codemeta.json is treated as the canonical metadata source and CITATION.cff remains synchronized with it.
- Author and contributor lists are consistent between CITATION.cff and SMP governance sections.
- Archival route and preservation commitments are not contradictory.
- Release cadence and quality gates are documented both in checklist and SMP.
- Maintenance responsibilities and contingency plan are explicitly assigned.

## Typical Workflow Order

1. Generate codemeta.json as canonical software metadata.
2. Generate or update CITATION.cff from codemeta.json.
3. Draft DMP.
4. Draft SMP from template.
5. Run crosswalk checks and reconcile discrepancies.
6. Finalize publication checklist and submission package.

## Refresh Note

Revalidate this crosswalk during scheduled refreshes defined in `EVERSE-SMP-REFRESH-POLICY.md`.
