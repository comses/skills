---
name: fair4rs
description: |
  Create FAIR4RS-compliant metadata, publication checklists, and citation files
  for computational models of social-ecological systems to prepare them for publication, sharing, and reuse.
  
  Use this skill when preparing models for Zenodo, arXiv, discipline-specific repositories, 
  or journal supplementary materials. Triggers: "prepare for publication", "create FAIR metadata", 
  "generate publication checklist", "archive my model", "submit to Zenodo", "make my code citable".
  
  Expected output: codemeta.json (canonical metadata source), CITATION.cff generated from codemeta.json,
  data management plan (DMP), software management plan (SMP), publication checklist, and metadata JSON-LD
  suitable for Zenodo, arXiv, or disciplinary repositories.
license: MIT
compatibility: Works with any model type
metadata:
  domain: computational-modeling
  maturity: beta
  audience: modelers, researchers who code, research software engineers
  category: publication
---

# FAIR4RS Publication Readiness Skill

## When to Use This Skill

Use this skill when:

- You are planning a research project with research software and/or data needs and need software and data management plans to help organize and share your digital research objects effectively.
- You are preparing a computational model for publication or archival (Zenodo, GitHub, institutional repository)
- You need to generate and maintain codemeta.json metadata, and derive CITATION.cff for citation workflows
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

Software and data management plans should be created as early as possible in a research project in the planning phases. If they do not exist, create them based on the following criteria.

### 0. Co-evolving, Evergreen Data and Software Management Plans (DMP + SMP)

Do not treat DMP and SMP as sequential deliverables. Start with a joint sketch, formalize the DMP if required, and iteratively refine both as a coupled system.

Establish explicit cross-links between DMP and SMP sections (data formats ↔ code, metadata ↔ APIs, storage ↔ deployment).

---

### Data Management Plan (DMP) — FAIR-aligned, publication-ready

A FAIR4RS-aligned DMP should define data in a way that is actionable for software design and reproducibility:

- **Data sources and generation**
  - Inputs, outputs, intermediate data
  - Synthetic vs external data, acquisition workflows

- **Formats, structure, and scale**
  - File formats, schemas, expected volumes
  - Constraints that impact software design (streaming, chunking, HPC)

- **Storage, backup, and access**
  - Active storage vs archival storage
  - Access control, authentication, and sharing boundaries

- **Metadata and provenance**
  - Standards (e.g., schema.org, domain standards)
  - Provenance capture strategy (automated vs manual)

- **Licensing and reuse**
  - Data licenses, restrictions, derivative permissions
  - Alignment with software licensing

- **Archival and publication**
  - Target repositories (e.g., Zenodo, InvenioRDM, institutional)
  - DOI strategy and version linkage to software releases

---

### Software Management Plan (SMP) — FAIR4RS-aligned, actionable

Maintain the SMP as a living document aligned with EVERSE RSQKit guidance and best practices for maintainable research software engineering.

- **Project context and scope**
  - Software type (analysis, library, infrastructure)
  - Stakeholders, roles, responsibilities

- **Architecture and design**
  - System boundaries, interfaces to data
  - Interoperability and standards compliance

- **Development practices**
  - Version control, branching model
  - Coding standards, documentation strategy

- **Testing and quality assurance**
  - Test levels (unit, integration, system)
  - CI/CD, reproducibility checks, quality gates

- **Packaging and environments**
  - Dependency management, containers, workflows
  - Execution environments (local, HPC, cloud)

- **Release and versioning**
  - Semantic versioning, release cadence
  - Changelog, deprecation and compatibility policy

- **Licensing and governance**
  - License selection aligned with data
  - Contribution model, code of conduct, attribution

- **Maintenance and sustainability**
  - Resourcing, ownership, succession planning
  - Risk and contingency planning

- **Discoverability and preservation**
  - Repository practices (GitHub/GitLab)
  - Archival (Zenodo DOI, Software Heritage)
  - Metadata for software citation (CITATION.cff, codemeta.json)

---

### Coupling Rules (DMP ↔ SMP)

Make dependencies explicit and testable:

- Data formats and schemas in DMP should be enforced or validated by software
- Metadata and provenance requirements should be automated in pipelines where possible
- Storage and access constraints should map to deployment and execution environments
- Licensing choices for data and software must be compatible and documented
- Archival strategy must link data DOIs and software releases

### Coupling Assertions (machine-checkable where possible)

- Every data format referenced in DMP has a corresponding reader/writer in the codebase
- Every external dataset in DMP has a DOI or persistent URL in codemeta.json `isBasedOn`
- Storage constraints in DMP are reflected in deployment specs in SMP
- Data license in DMP is compatible with software license in SMP (use SPDX compatibility rules)

---

### Software-type-aware prioritization

Adjust SMP emphasis based on software role:

- **Exploratory analysis**
  - Prioritize reproducibility, provenance capture, environment capture

- **Reusable research software**
  - Prioritize documentation, API stability, interoperability

- **Long-lived infrastructure**
  - Prioritize robustness, scalability, security, operational sustainability

---

### Evergreen maintenance

Treat both plans as versioned artifacts:

- Update alongside major software releases
- Track changes via version control
- Use `references/EVERSE-SMP-REFRESH-POLICY.md` to check refresh cadence and update process
- Use `references/FAIR4RS-SMP-CROSSWALK.md` to keep publication artifacts and SMP content consistent

ALWAYS verify consistency between plans and published artifacts at release time

### 1. Gather Publication Metadata (SES-aware, FAIR-aligned)

Collect structured metadata for the computational model:

- **Title** (concise, ≤200 characters)
- **Description** (2–3 sentences: system modeled, processes, scale)
- **Model type** (e.g., agent-based, system dynamics, network, hybrid)
- **Scope and scale** (spatial, temporal, organizational levels)
- **Authors** (names, ORCIDs, affiliations)
- **Version** (semantic versioning, e.g., 1.0.0)
- **License** (SPDX identifier)
- **Repository URL**
- **Publication date**
- **Keywords** (include domain + method, e.g., “SES”, “ABM”, “land use”)
- **Related works** (DOIs of papers, datasets, prior model versions)
- **Funding sources**

SES-specific additions:
- **System components** (actors, institutions, ecological units)
- **Core processes** (feedbacks, adaptation, learning, disturbance)
- **Data dependencies** (empirical inputs, calibration datasets)

FAIR4RS intent:
- **Findable:** rich, domain-relevant descriptors
- **Accessible:** clear repository and access conditions
- **Interoperable:** standard identifiers (ORCID, DOI, SPDX)
- **Reusable:** explicit system assumptions and scope

---

### 2. Create Canonical Metadata (codemeta.json)

Generate `codemeta.json` as the **single machine-readable source of truth**.

Minimum fields:
- `@context`, `@type` = SoftwareSourceCode
- `name`, `description`, `codeRepository`
- `version`, `license`
- `author`, `keywords`

Recommended SES extensions:
- `applicationCategory`: "ComputationalModel"
- `additionalType`: "AgentBasedModel" (or other type)
- `temporalCoverage`, `spatialCoverage`
- `isBasedOn` (input datasets, prior models)
- `citation` (linked publications)
- `softwareRequirements` (simulation frameworks, runtimes)

Guidance:
- Align dataset references with DMP (DOIs, formats)
- Reflect execution environment from SMP (containers, workflows)
- Prefer resolvable identifiers for all linked resources

---

### 3. Derive Citation Metadata (CITATION.cff)

Generate `CITATION.cff` **from `codemeta.json`**.

Ensure:
- Full author list with affiliations
- Versioned citation (matches release)
- Repository and license included

SES considerations:
- If a canonical paper exists, include it alongside software citation
- Ensure consistency between model name, paper title, and repository

Rules:
- Treat `codemeta.json` as authoritative
- Regenerate on metadata changes
- Preserve author order and attribution

---

### 4. Validate Model Publication Readiness

Review against publication checklist (`references/PUBLICATION-CHECKLIST.md`):

Core checks:
- [ ] Version-controlled repository with history
- [ ] README with installation, execution, and purpose
- [ ] LICENSE file (SPDX-aligned) - if missing: prompt user for license preference, suggest based on existing dependencies and SMP and DMP
- [ ] CITATION.cff present
- [ ] Dependencies and environments specified
- [ ] Tests, workflows, or scripts enable reproducibility - if missing: flag as publication risk, suggest minimum viable test strategy
- [ ] Metadata complete (authors, version, identifiers)

SES-specific checks:
- [ ] Model description (ODD, ODD+D, or equivalent) included
- [ ] State variables, entities, and scales documented
- [ ] Process overview (scheduling, feedbacks) described
- [ ] Calibration and validation approach documented
- [ ] Example scenarios or runs provided
- [ ] Input datasets referenced with persistent identifiers

FAIR4RS signals:
- Reproducibility → executable workflows, environments
- Reusability → documented assumptions and processes
- Interoperability → standard formats and schemas
- Findability → rich, structured metadata

---

### 5. Prepare for Deposit and Archival

Prepare SES model artifacts for deposition:

Required:
- Versioned source code
- Model documentation (ODD or equivalent)
- Parameter sets and configuration files
- Example inputs and outputs

Metadata outputs:
- Zenodo / InvenioRDM JSON
- Dublin Core (institutional repositories)

Ensure:
- DOI minted for software release
- Input datasets linked via DOIs (DMP alignment)
- Model version ↔ DOI ↔ publication cross-referenced

SES-specific guidance:
- Archive representative simulation outputs where feasible
- Include scenario definitions used in publications
- Document stochastic elements and random seeds

---

## Activation Logic

Determine user's project stage and respond accordingly:

### Planning stage
Triggers: "start a new SES modeling project", "plan my research data", "create a software management plan"
→ Begin with joint DMP + SMP sketch
→ Establish data–model coupling assertions early
→ Recommend ODD protocol structure

### Active development
Triggers: "set up my model metadata", "create codemeta"
→ Generate codemeta.json with SES extensions
→ Check for DMP/SMP; flag if missing, offer to create

### Pre-publication
Triggers: "prepare for publication", "submit to Zenodo", "make my code citable", "prepare for CoMSES", "generate publication checklist", "archive my model"
→ Full pipeline: metadata → CITATION.cff → checklist → deposit preparation
→ Validate DMP/SMP consistency with artifacts

### Single artifact request
Triggers: "create CITATION.cff", "generate codemeta", "make citable"
→ Produce requested artifact directly
→ Validate against existing metadata if available

## ⚠️ Gotchas (SES Models)

- **Hidden assumptions:** SES models embed normative, behavioral, and institutional assumptions. Document them explicitly.

- **Data–model mismatch:** Ensure input data formats, units, and scales align with model expectations (spatial, temporal, organizational).

- **Non-reproducible runs:** Stochastic models require fixed random seeds, documented RNG strategy, and repeatable workflows.

- **Underspecified processes:** Missing scheduling, feedbacks, or adaptation rules reduces interpretability and reuse.

- **Sensitivity analysis gaps:** 
  - Failing to explore parameter space (local or global sensitivity) limits confidence in results
  - Report which parameters drive outcomes and which are negligible
  - Document methods used (e.g., one-at-a-time, Sobol, Morris) and parameter ranges

- **Uncertainty quantification missing or unclear:**
  - Distinguish sources: parameter uncertainty, structural uncertainty, stochastic variability, input data uncertainty
  - Provide uncertainty propagation (ensembles, Monte Carlo, bootstrapping)
  - Report distributions or confidence intervals, not just point estimates

- **Scenario ambiguity:**
  - Scenarios must be explicitly defined, parameterized, and versioned
  - Avoid informal or implicit scenario descriptions

- **License conflicts:** Ensure compatibility between data and software licenses.

- **Incomplete linkage:** Publications, datasets, and software must be cross-referenced via persistent identifiers (DOIs).

- **Archival gaps:** Failure to preserve parameter sets, seeds, and configurations prevents reproduction of published results.

---

## Templates & Resources

- FAIR4RS Handbook → `references/FAIR4RS-HANDBOOK.md`
- Publication Checklist → `references/PUBLICATION-CHECKLIST.md`
- CodeMeta Template → `assets/codemeta.json`
- CITATION Template → `assets/CITATION-TEMPLATE.cff`
- DMP Template → `assets/DMP-TEMPLATE.md`
- SMP Template → `assets/SMP-TEMPLATE.md`
- ODD Protocol → (standard for ABMs and SES models)
- FAIR4RS ↔ SMP Crosswalk → `references/FAIR4RS-SMP-CROSSWALK.md`
- EVERSE SMP Guidance → https://everse.software/RSQKit/software_management_planning
- CodeMeta Guide → https://codemeta.github.io/user-guide
- Zenodo Guide → `references/ZENODO-GUIDE.md`

---

## Example (SES Model)

Input: Agent-based model of land-use change with farmer decision-making

Output artifacts:

1. `codemeta.json`
   - includes spatialCoverage, temporalCoverage, dataset DOIs

2. `CITATION.cff`
   - software citation + linked paper DOI

3. Publication checklist
   - validated with SES-specific criteria

4. Documentation bundle
   - ODD protocol
   - parameter sets
   - scenario definitions

5. Archival package
   - versioned release with DOI
   - linked datasets and reproducible workflows

---

## Quick Reference

| Task | Resource |
|------|----------|
| Create codemeta.json | `assets/codemeta.json` |
| Generate CITATION.cff | `assets/CITATION-TEMPLATE.cff` |
| Document model (ODD) | domain standard |
| Create SMP | `assets/SMP-TEMPLATE.md` |
| Crosswalk FAIR4RS | `references/FAIR4RS-SMP-CROSSWALK.md` |
| Prepare Zenodo deposit | `references/ZENODO-GUIDE.md` |

---
