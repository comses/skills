# Software Management Plan (SMP)

> This document combines two kinds of content:
>
> - **Derived content** (Software Summary, FAIR Software, Provenance, Licensing) is disseminated from the project's FAIR Management Plan. It is **not** authored independently here — changes that affect these sections MUST first be incorporated into the FAIR Management Plan and then re-derived.
> - The remaining sections are formatting, compliance-mapping, or implementation placeholders for funder-, repository-, or project-specific requirements. They must not establish an independent stewardship authority; if a new stewardship requirement appears, capture it in the FAIR Management Plan first and then propagate it here.
>
> Aligned with FAIR principles, research software engineering best practices, and EVERSE RSQKit guidance (https://everse.software/RSQKit/software_management_planning).
>
> Derived from:
>
> - FAIR Management Plan version:
> - FAIR Management Plan date:
> - Generated on:

---

# Project Information

| Field | Value |
|-------|-------|
| Project | |
| Acronym | |
| Grant / Award | |
| Principal Investigator | |
| Institution | |
| Repository | |
| License | |
| Software type | Exploratory analysis code / Reusable research software / Long-lived infrastructure |
| Planned project duration | |
| Planned maintenance horizon | |
| Version | |
| Date | |

---

# Purpose

Summarize the scope of this SMP.

Describe:

- project objectives
- software components covered
- what this SMP does not cover (e.g. dataset stewardship — see the companion DMP)

---

# Software Summary *(derived)*

Summarize the software components managed by this project.

For each component describe:

- purpose
- primary language(s)
- origin (new development, fork, derived work)
- relationship to project objectives
- intended users and reuse context

Reference the corresponding entries in the FAIR Management Plan Research Object Inventory.

---

# Stakeholders, Roles, and Responsibilities

Reference the corresponding entries in the FAIR Management Plan Roles and Responsibilities section for project-level roles. Use this section only to map or repeat roles already captured there, plus any funder-specific labels that must appear in this SMP:

- Maintainer(s):
- Release manager:
- Reviewer / QA role:
- User support / community manager:
- Succession plan for key roles:

---

# Governance and Collaboration

- Contribution workflow (issues, pull requests, reviews):
- Governance model (single maintainer, core team, steering group):
- Decision-making process:
- Code of conduct:

---

# FAIR Software *(derived)*

## Findability

Describe:

- persistent identifiers (e.g. SWHID, DOI via archival deposit)
- canonical metadata (codemeta.json, CITATION.cff)
- keywords
- discovery mechanisms
- repositories and registries

Reference metadata maintained elsewhere where appropriate.

## Accessibility

Describe:

- repository and hosting platform
- access conditions
- authentication requirements
- long-term availability

Explain any restrictions.

## Interoperability

Describe:

- community standards followed (e.g. FAIR4RS, codemeta, SPDX)
- APIs, data formats, and exchange formats supported
- interoperability with other project software or datasets

Document justified deviations.

## Reusability

Describe:

- documentation (README, API docs, usage examples)
- citation and contributor crediting strategy (e.g. ORCID, CITATION.cff)
- intended reuse and extension points

Document known limitations.

---

# Design and Implementation

- Software architecture and rationale:
- Core dependencies and compatibility policy:
- Coding standards and style guidance:
- Documentation strategy (user docs, developer docs, API docs):

---

# Dependencies and Environment

Describe:

- programming language(s) and required versions
- dependency management approach (e.g. pinned versions, lockfiles)
- containers or virtual environments
- operating system and platform requirements
- external services or APIs the software depends on

Document the reproducibility strategy for the build and runtime environment.

---

# Testing and Quality Assurance

- Testing strategy (unit, integration, regression, acceptance):
- Continuous integration setup:
- Code review requirements:
- Quality gates before merge/release:
- Reproducibility checks:
- Quality metrics and monitoring:

---

# Packaging, Distribution, and Deployment

- Packaging format(s) and distribution channels:
- Execution environments (local, HPC, cloud, containers):
- Installation and onboarding path for users:
- Registry/repository integration (GitHub/GitLab, package indexes):
- User support channels:

---

# Provenance *(derived)*

Summarize provenance strategy for the software itself and for any artifacts it generates.

Reference:

- provenance manifests
- version control history and tagging conventions
- build and release automation

---

# Versioning, Releases, and Archival

- Versioning scheme (e.g. SemVer, CalVer):
- Release cadence:
- Changelog policy:
- Release automation:
- DOI minting strategy (e.g. Zenodo):
- Archival and preservation strategy (e.g. Software Heritage):

---

# Licensing *(derived)*

Summarize licensing strategy.

Document:

- current license and SPDX identifier
- copyright ownership
- any license transitions in progress or under consideration
- known compatibility concerns with dependencies
- unresolved licensing questions

Reference `artifacts/fair/license-inventory.md` for detail.

---

# Security

- Vulnerability management and disclosure process:
- Dependency update policy:
- Access control for the repository and release process:
- Handling of secrets or credentials:

---

# Ethics and Legal Considerations

Describe:

- export control considerations, if any
- third-party code or data embedded in the software
- legal constraints on distribution

Reference additional ethics documentation where appropriate.

---

# Sustainability and Maintenance

- Long-term maintenance plan:
- Funding and resource assumptions:
- Bus-factor mitigation:
- Deprecation and end-of-life policy:
- Risks and contingency plans:

---

# Software-Type-Aware Priorities

Document explicit quality priorities based on the software type declared in Project Information.

- Exploratory analysis code priorities:
- Reusable research software priorities:
- Long-lived infrastructure priorities:

---

# Review and Update Cadence

- SMP owner:
- Review frequency (e.g. annual, on each release):
- Trigger events for updates (major architectural change, new funder requirements, role changes):
- Last updated:

---

# Relationship to FAIR Management Plan

The authoritative stewardship record remains:

`artifacts/fair/fair-management-plan.md`

Additional project artifacts may include:

- `artifacts/fair/provenance-manifest.json`
- `artifacts/fair/license-inventory.md`
- `codemeta.json`
- `CITATION.cff`

---

# Appendix A: Compliance Mapping (Optional)

- FAIR / RSE alignment notes:
- Funder-specific requirements:
- Institutional requirements:

---

# Appendix B: Machine-Actionable Hooks (Optional)

- Metadata files generated from this SMP:
- CI checks linked to SMP sections:
- Automation scripts and reporting outputs:

---

# Revision History

| Version | Date | Summary |
|----------|------|---------|
| | | |
