# FAIR Management Plan

> Living stewardship plan for the project's digital research objects.
>
> This document is the sole canonical stewardship source for datasets, software, computational models, workflows, documentation, and other research outputs.
>
> It describes how those objects will be managed throughout their lifecycle in accordance with the FAIR Principles.
>
> This plan should be created early, reviewed regularly, and updated whenever significant research objects, repositories, metadata, or preservation strategies change.

---

## Project Information

| Field | Value |
|-------|-------|
| Project | |
| Acronym | |
| Version | |
| Date | |
| Principal Investigator | |
| FAIR Steward(s) | |
| Repository | |
| License | |

---

# Executive Summary

Briefly summarize:

- project objectives
- major research outputs
- FAIR strategy
- long-term stewardship goals

---

# Research Object Inventory

Describe each significant research object managed by the project.

| Research Object | Type | Description | Repository | Identifier | Status |
|----------------|------|-------------|------------|------------|--------|
| | Dataset | | | | |
| | Software | | | | |
| | Computational model | | | | |
| | Workflow | | | | |
| | Documentation | | | | |

Additional object types may be added as needed.

---

# Findability

## Persistent Identifiers

Describe identifier strategy.

Examples:

- DOI
- ORCID
- ROR
- SWHID
- UUID
- accession numbers

---

## Metadata

Describe metadata standards used for each research object.

Examples include:

- CodeMeta
- DataCite
- RO-Crate
- OMF metadata
- Dublin Core

Document any project-specific metadata.

For computational models, FAIR records stewardship metadata and references the OMFA-owned model card at `artifacts/model-card.md`; it does not replace or canonicalize that content.

---

## Discovery

Describe how research objects will be discoverable.

Include:

- repositories
- indexing
- keywords
- searchable metadata

---

# Accessibility

## Repository Strategy

Identify repositories used for each research object.

Examples:

- GitHub
- Zenodo
- CoMSES Net
- WorkflowHub
- institutional repository

---

## Access Conditions

Describe:

- open access
- embargoes
- controlled access
- authentication
- sensitive data restrictions

Explain any limitations.

---

## Preservation

Describe:

- archival repositories
- retention period
- preservation responsibilities
- expected availability

---

# Interoperability

Describe how research objects support interoperability.

Include where applicable:

- open formats
- community standards
- controlled vocabularies
- ontologies
- qualified references
- machine-readable metadata

Document justified deviations from community standards.

---

# Reusability

Describe how research objects support reuse.

Include:

- documentation
- provenance
- quality assurance
- versioning
- licensing
- citation

Describe any known limitations on reuse.

---

# Provenance

Describe how provenance will be captured.

Include:

- source datasets
- derived products
- workflow provenance
- software versions
- parameterization
- execution environments

Reference:

- `artifacts/fair/provenance-manifest.json`

where applicable.

---

# Computational Environment

Describe:

- programming languages
- dependencies
- containers
- package managers
- workflow systems
- operating systems

Document reproducibility strategy.

---

# Licensing

Summarize licensing strategy.

Maintain detailed licensing information separately in:

`artifacts/fair/license-inventory.md`

Document:

- licensing rationale
- copyright ownership
- SPDX identifiers
- known restrictions
- unresolved licensing questions

---

# Roles and Responsibilities

Identify responsibility for:

- metadata
- repositories
- software
- datasets
- preservation
- FAIR review

Typical boundary: FAIR owns stewardship metadata, reproducibility assessment, object/workflow provenance, packaging, and pointers to scientific artifacts; OMFA owns `artifacts/model-card.md` and other scientific specifications; `document` owns ODD narratives.

---

# Resources

Describe anticipated resources for:

- storage
- archival
- repository costs
- persistent identifiers
- curation
- long-term preservation

---

# Security and Ethics

Describe:

- security measures
- backup strategy
- sensitive data handling
- ethical considerations
- legal or contractual constraints

Reference ethics documentation where applicable.

---

# FAIR Assessment

Summarize current FAIR maturity per research object and workflow.

Store the backing assessment narrative at `artifacts/fair/fair-assessment-report.md`.

| Principle | Status | Notes |
|-----------|--------|-------|
| Findable | | |
| Accessible | | |
| Interoperable | | |
| Reusable | | |

Document planned improvements.

---

# Review History

| Version | Date | Summary |
|----------|------|---------|
| 0.1 | | Initial draft |

---

# Derived management plans

The FAIR Management Plan may be disseminated as one or more specialized management plans, including:

- Data Management Plan (DMP)
- Software Management Plan (SMP)
- future Model Management Plan (MMP)
- future Workflow Management Plan (WMP)

These documents are derived dissemination extracts of stewardship decisions already captured here. If a new requirement appears in a DMP, SMP, or future derived plan, add it to the FAIR Management Plan first and then regenerate the downstream extract.

## Related Artifacts

This plan references or summarizes information maintained elsewhere.

Examples include:

- `README.md`
- `codemeta.json`
- `CITATION.cff`
- `artifacts/fair/provenance-manifest.json`
- `artifacts/fair/license-inventory.md`
- `artifacts/fair/fair-assessment-report.md`
- `artifacts/model-card.md`
- `artifacts/conceptual-model.md`
- `artifacts/fair/metadata/`

FAIR may inventory or reference `artifacts/model-card.md` and related scientific artifacts, but it does not author or replace them.
