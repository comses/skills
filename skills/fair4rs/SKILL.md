---
name: fair4rs
description: |
  Create FAIR4RS-compliant metadata, publication checklists, and citation files to ensure 
  your computational artifacts are ready for archival and academic publication.
  
  Use this skill when preparing models for Zenodo, arXiv, discipline-specific repositories, 
  or journal supplementary materials. Triggers: "prepare for publication", "create FAIR metadata", 
  "generate publication checklist", "archive my model", "submit to Zenodo", "make my code citable".
  
  Expected output: codemeta.json (canonical metadata source), CITATION.cff generated from codemeta.json,
  data management plan, software management plan (SMP), publication checklist, and metadata JSON-LD
  suitable for Zenodo, arXiv, or disciplinary repositories.
license: MIT
compatibility: Works with any model type; requires Git repository
metadata:
  domain: computational-modeling
  maturity: beta
  audience: modelers, researchers
  category: publication
---

# FAIR4RS Publication Readiness Skill

## When to Use This Skill

Use this skill when:

- You are preparing a computational model for publication or archival (Zenodo, GitHub, institutional repository)
- You need to generate and maintain codemeta.json metadata, and derive CITATION.cff for citation workflows
- You need a data management plan (DMP) aligned with FAIR4RS principles
- You need a software management plan (SMP) aligned with EVERSE guidance for software lifecycle, quality, and sustainability
- You want to ensure your code meets journal supplementary material requirements
- You are creating a registered report or pre-registration of a model study

## Key Inputs

This skill works best with:

- **Model repository information** (GitHub URL, license, primary language)
- **Authors and affiliations** (names, ORCID if available, institutions)
- **Model purpose and scope** (1-2 sentence description, research questions, field)
- **Dependencies** (Python packages, external tools, data requirements)
- **DOI or permanent identifier** (if already published)
- **Ethical considerations** (if any; e.g., privacy, sensitive data)
- **Software lifecycle scope** (exploratory code, reusable research software, or long-lived infrastructure)
- **Team roles and governance** (maintainers, reviewers, release managers, user support roles)

## Step-by-Step Instructions

### 1. Gather Publication Metadata

Prepare information about your model:

- **Title** (concise, ≤200 characters)
- **Description** (2-3 sentences on what the model does)
- **Authors** (names, ORCIDs, affiliations)
- **License** (Apache-2.0, MIT, GPL, etc.; see https://choosearlicense.com)
- **Publication date** (when model was first public or will be published)
- **Repository URL** (GitHub, GitLab, or institutional repository)
- **Version** (semantic versioning: v1.0.0)
- **Keywords** (5-10 relevant terms: "agent-based model", "climate", etc.)
- **Related publications** (DOI of papers describing or using the model)
- **Funding agencies** (grant IDs if applicable)

### 2. Generate CITATION.cff File

First, generate a `codemeta.json` metadata artifact and treat it as the single machine-readable source of truth.

The skill will create a `codemeta.json` file that includes at minimum:

- `@context` (CodeMeta context URI)
- `@type` (SoftwareSourceCode)
- `name`, `description`, `codeRepository`, `version`, `license`
- `author` (with ORCID where available), `keywords`
- optional but recommended: `issueTracker`, `continuousIntegration`, `programmingLanguage`, `developmentStatus`

Then generate `CITATION.cff` from `codemeta.json` so citation metadata stays synchronized.

The skill will create a `CITATION.cff` file that:

- Enables GitHub to display a "Cite this repository" button
- Provides BibTeX and plain-text citations
- Includes all authors and affiliations
- Specifies license and repository information

When fields conflict, `codemeta.json` is authoritative and `CITATION.cff` should be regenerated.

### 3. Create Data Management Plan

A FAIR4RS-aligned DMP addressing:

- **Data sources** (what input data does the model require? where is it stored?)
- **Storage & backup** (where will code and data live long-term? cloud? institutional archive?)
- **Access & reuse** (who can access? are there restrictions? are derivatives allowed?)
- **Metadata standards** (how is provenance documented? what schemas apply?)
- **Long-term archival** (Zenodo? InvenioRDM? Institutional repository?)

### 4. Generate Publication Checklist

Review the checklist (see `references/PUBLICATION-CHECKLIST.md`):

- [ ] Code is in a version control system with commit history
- [ ] README.md exists with clear installation and usage instructions
- [ ] LICENSE file is present and matches declared license
- [ ] CITATION.cff or CITATION.bib exists for citation tracking
- [ ] Dependencies are pinned (requirements.txt, pyproject.toml, environment.yml)
- [ ] Tests or examples demonstrate reproducibility
- [ ] Code follows a standard license (not closed-source for published work)
- [ ] Repository is public (or embargo period specified)
- [ ] Metadata includes authors, version, and publication date
- [ ] Model documentation (ODD, equivalent, or domain-specific) exists

### 5. Create Software Management Plan (SMP)

Create an SMP aligned with EVERSE RSQKit guidance as a living document. The plan should include:

- **General information** (project scope, software type/tier, stakeholders, responsibilities)
- **Collaboration and licensing** (contribution workflow, code of conduct, licensing strategy, attribution)
- **Analysis, design, and implementation** (architecture approach, coding standards, documentation strategy)
- **Testing and quality assurance** (test strategy, CI, code review, release quality gates)
- **Deployment and delivery** (distribution channels, packaging, execution environments, registries)
- **Versioning and releases** (release cadence, semantic versioning, changelog, deprecation policy)
- **Maintenance and sustainability** (resourcing, succession plans, contingency planning)
- **Discoverability and preservation** (GitHub/GitLab integration, Zenodo/Software Heritage archival)

SMP priorities should be explicit and software-type aware:

- **Exploratory analysis code:** emphasize reproducibility, transparency, provenance
- **Reusable research software:** emphasize documentation quality, interoperability, onboarding
- **Long-lived infrastructure:** emphasize robustness, scalability, security, long-term maintenance

Treat SMP guidance as evergreen:

- Use `references/EVERSE-SMP-REFRESH-POLICY.md` to check refresh cadence and update process
- Use `references/FAIR4RS-SMP-CROSSWALK.md` to keep publication artifacts and SMP content consistent

### 6. Prepare for Deposit

The skill will provide:

- Metadata JSON template for Zenodo/arXiv submission
- Dublin Core metadata for institutional repositories
- Suggested directory structure for supplementary materials
- Checklist of additional materials (ODD, parameters, example outputs)

## ⚠️ Gotchas

- **Author attribution:** Ensure all contributors are listed. ORCIDs are optional but strongly recommended for career tracking.
- **License selection:** Permissive licenses (MIT, Apache-2.0) are strongly preferred for research code. GPL is acceptable but may limit reuse. Closed licenses are not recommended for published research.
- **Version strings:** Use semantic versioning (v1.0.0, v1.1.2). Zenodo and GitHub use these for releases.
- **Ephemeral URLs:** GitHub URLs may change if repositories are renamed or deleted. Consider archival options (Zenodo GitHub integration, institutional repository) for long-term stability.
- **Citation gaps:** If your model was published in a paper, ensure the paper DOI is included in metadata; tools like Zenodo will link them automatically.

## Templates & Resources

- **FAIR4RS Handbook:** See `references/FAIR4RS-HANDBOOK.md` for principles and best practices
- **Publication Checklist:** See `references/PUBLICATION-CHECKLIST.md` for the 10-item verification list
- **CodeMeta Template:** See `assets/codemeta.json` for a starter CodeMeta artifact (JSON-LD)
- **CITATION.cff Template:** See `assets/CITATION-TEMPLATE.cff` for the RFC 8949 format
- **DMP Template:** See `assets/DMP-TEMPLATE.md` for a 1-2 page data management plan
- **SMP Template:** See `assets/SMP-TEMPLATE.md` for a software management plan aligned with EVERSE guidance
- **SMP Refresh Policy:** See `references/EVERSE-SMP-REFRESH-POLICY.md` for periodic refresh and governance of local guidance
- **FAIR4RS ↔ SMP Crosswalk:** See `references/FAIR4RS-SMP-CROSSWALK.md` to avoid duplication and keep outputs coherent
- **EVERSE SMP Guidance:** See https://everse.software/RSQKit/software_management_planning for lifecycle and sustainability criteria
- **CodeMeta User Guide:** See https://codemeta.github.io/user-guide for codemeta.json structure and validation
- **Zenodo Guide:** See `references/ZENODO-GUIDE.md` for deposit workflow and metadata requirements

## Example

**Input:** Python ABM repository with git history, authors, and institutional affiliation

**Output:**

1. **codemeta.json** (canonical metadata source):
  ```json
  {
    "@context": "https://w3id.org/codemeta/3.1",
    "@type": "SoftwareSourceCode",
    "name": "forest-fire-abm",
    "description": "An agent-based model of forest fire dynamics.",
    "codeRepository": "https://github.com/example/forest-fire-abm",
    "version": "1.0.0",
    "license": "https://spdx.org/licenses/MIT",
    "keywords": ["agent-based model", "ecology", "wildfire"]
  }
  ```

2. **CITATION.cff** file generated from codemeta metadata (GitHub will display cite button):
   ```yaml
   cff-version: 1.2.0
   title: "An Agent-Based Model of Forest Fire Dynamics"
   authors:
     - family-names: Smith
       given-names: Alice
       orcid: "https://orcid.org/0000-0001-2345-6789"
       affiliation: "University of Example"
   version: 1.0.0
   license: MIT
   repository-code: "https://github.com/example/forest-fire-abm"
   ```

3. **Publication checklist** with passing marks:
   - ✅ Code is in Git with commit history
   - ✅ README with installation instructions
   - ✅ MIT LICENSE
   - ✅ CITATION.cff file
   - ✅ Pinned dependencies (requirements.txt)

4. **DMP summary:**
   ```markdown
   ## Data Management Plan
   - Input: Land use raster (GeoTIFF), forest inventory (CSV)
   - Storage: GitHub (code), Zenodo (releases)
   - Access: Public, MIT licensed
   - Archival: Zenodo GitHub integration (automatic on release)
   ```

5. **SMP summary (EVERSE-aligned):**
  ```markdown
  ## Software Management Plan
  - Scope: Reusable research software for ecological ABM studies
  - Roles: PI (owner), maintainer, reviewer, release manager
  - QA: CI on pull requests, unit tests, code review required before merge
  - Releases: Semantic versioning with changelog and DOI-minted releases on Zenodo
  - Sustainability: Successor maintainer policy and deprecation plan documented
  - Preservation: Archived in Software Heritage and Zenodo
  ```

---

## Quick Reference

| Task | Reference |
|------|-----------|
| Create codemeta.json | See `assets/codemeta.json` and CodeMeta User Guide |
| Create CITATION.cff | See `assets/CITATION-TEMPLATE.cff` |
| Know FAIR4RS principles | See `references/FAIR4RS-HANDBOOK.md` |
| Create Software Management Plan | See `assets/SMP-TEMPLATE.md` and EVERSE SMP guidance |
| Refresh SMP references | See `references/EVERSE-SMP-REFRESH-POLICY.md` |
| Reconcile FAIR4RS and SMP outputs | See `references/FAIR4RS-SMP-CROSSWALK.md` |
| Prepare for Zenodo | See `references/ZENODO-GUIDE.md` |
| Check publication readiness | See `references/PUBLICATION-CHECKLIST.md` |

---

For community feedback or issues, see the [COMSES Skills](https://github.com/comses-network/skills) repository.
