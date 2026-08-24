# Project Bootstrap and OMF Conformance Guidance

## Purpose

Use this guidance to establish the minimum repository substrate for a new or existing research software or modeling repository, and to assess or reconcile an existing repository against OMF conventions, including emerging `science.toml` conventions.

This is a lazy-loaded OMFA coordination module, not a standalone bootstrap skill. Load it only on matching intent: repository initialization, bootstrap, or scaffolding; `science.toml` adoption; OMF conformance; repository infrastructure modernization; repository readiness for OMF workflows; or filesystem profile reconciliation. It establishes only the minimum substrate, then returns the repository to the OMFA lifecycle. It does not own implementation architecture, module mapping, or verification planning (route to `omfb`) or FAIR, reproducibility, packaging, citation, archival, or environment hardening (route to `fair`).

`science.toml` is an emerging, unstable convention. Use repository-local documented schemas, registries, and profiles when available. Do not claim any remote convention is fixed, and do not invent semantics that local documentation does not support. [MUST]

This guidance answers:

> How should a repository be initialized or brought into OMF conformance with the least consequential change, so modeling work can proceed on a stable substrate?

---

## Decision Context

**Use this guidance when:**

- initializing, bootstrapping, or scaffolding a modeling or research software repository
- adopting or updating `science.toml` or an OMF filesystem profile
- assessing OMF conformance of an existing repository
- modernizing repository infrastructure or reconciling a filesystem profile
- establishing repository readiness for OMFA artifact workflows

**Do not use this guidance when:**

- implementation architecture, module mapping, parameter schema, or verification planning is requested (route to `omfb`)
- reproducibility, FAIR metadata, packaging, citation, archival, or environment hardening is requested (route to `fair`)
- sustained narrative documentation is requested (route to `document`)
- the repository is already conforming and the question is about the modeling lifecycle (use `lifecycle.md`)

---

## Workflow

Execute the steps below in this exact order: **AUDIT → RESOLVE → CLASSIFY → INTERVIEW → PLAN → APPLY → VALIDATE → RETURN TO OMFA LIFECYCLE**. [MUST]

### 1. AUDIT

Audit the existing repository before asking any question. [MUST]

Audit: existing `science.toml`, `AGENTS.md` or other agent instruction files, license, README, `Makefile`, manifests and lockfiles, source, tests, docs, data, analysis, containers, CI configuration, installed skills, OMFA/OMFB artifacts under `artifacts/`, `.gitignore`, and local conventions.

Infer repository state cheaply from evidence already present. [MUST] Do not rewrite an existing repository to match a template; the existing layout and tooling are the baseline, and templates apply only to empty or near-empty repositories.

### 2. RESOLVE

If a `science.toml` exists, resolve it before classifying:

- Validate structure (syntax, known schema) where tooling permits. [MUST]
- Separately resolve `project.kind`, `project.filesystem`, and any registry or profile reference. [MUST]
- Distinguish the schema version (file format) from the `<profile>:v<version>` filesystem contract (layout). [MUST]
- Treat schema validation and identifier resolution as different checks; a failure of one does not imply a failure of the other. [MUST]
- A syntactically valid identifier that cannot be resolved locally is **UNRESOLVED**, not malformed. [MUST]
- Resolve `project.kind` and `project.filesystem` via lookup against repository-local documented vocabulary (a semi-controlled vocabulary). Do not hard-code a global enum. [MUST]
- Honour agent and user feedback about resolution outcomes; if a local registry or profile is unreachable or missing, report it as unresolved. [MUST]

Treat `science.toml` as a small declarative coordination config. It is not a log, build state, lockfile, database, or history store. [MUST]

Profile semantics are declarative only: no executable plugins, templates, inheritance, hooks, DSLs, federation, or network resolution. [MUST]

### 3. CLASSIFY

Classify the repository, or each audited item, against the resolved target into exactly one of:

| State | Meaning |
| --- | --- |
| **CONFORMING** | Satisfies the resolved profile and version |
| **COMPATIBLE** | Does not strictly conform but works with the resolved profile; no change needed |
| **DRIFT** | Deviates from the profile in a way that is safe to normalize without changing behavior or ownership |
| **CONFLICT** | Deviates from the profile in a way that changing it would alter behavior, ownership, or user decisions |
| **UNRESOLVED** | The target profile or version could not be resolved, or the item cannot be assessed |

Report the state and its meaning to the user. [MUST]

Profiles do not authorize rewrites. Preserve compatibility over cosmetic normalization. [MUST]

### 4. INTERVIEW

Interview only after AUDIT, and only about consequential unresolved repository differences. [MUST] Ask only the smallest necessary decision; never run a generic questionnaire. [MUST] When a filesystem profile is involved, include a representative preserve-versus-migrate profile choice. [MUST]

Apply the feedback policy to every decision. The policy level determines which decision risks are handled autonomously and which are asked to the user:

| Policy | Handling |
| --- | --- |
| **ALL** | Ask the user for every meaningful alternative |
| **MOST** (default) | Handle LOW autonomously; ask on MEDIUM and above |
| **CRITICAL** | Handle LOW and MEDIUM autonomously; ask on HIGH and above |
| **SAMPLED** | Sample-check LOW and MEDIUM autonomously; ask on HIGH and above |
| **CUSTOM** | Follow the project or user policy |

Decision risks: **LOW**, **MEDIUM**, **HIGH**, **IRREVERSIBLE**. The user can override the policy at any time. [MUST]

Regardless of policy level, never autonomously perform destructive, publishing, licensing, or history-rewriting operations, or any irreversible action. [MUST]

### 5. PLAN

Before any mutation, produce a plan that categorizes every item as **preserve**, **create**, **modify**, **migrate**, **defer**, or **unresolved**. [MUST]

- No migration without explicit policy permission (user approval). [MUST]
- Minimum scaffold requirement: create only demonstrated needs and cheap extension points; list possible files only when justified. [MUST]
- No CI, SBOM, publishing configuration, docs site, release automation, or complex provenance setup by default. [MUST]
- Language tooling defaults, when repository requirements do not decide otherwise: Python → `uv`; Node.js/TypeScript → `bun`; Rust → `cargo` with `rustup`; Julia → `Pkg`; R → native R tooling with reproducibility tooling as required; C/C++ → CMake with an appropriate compiler/toolchain; Java → Gradle for greenfield work unless context favors Maven; containers → Docker and Apptainer. These are defaults, not dogma: ecosystem requirements win, and never add a second package manager. [MUST]
- `Makefile`: a thin contributor interface with only targets that actually exist; if `make check` exists, it is the canonical CI/contributor validation command; do not recreate package or build logic in it. [MUST]
- `AGENTS.md`: minimal, containing only repository-specific, non-obvious, costly-consequential information; avoid generic or duplicative instructions. [MUST]
- Skill versions: pin recommended and required skill versions/revisions explicitly; do not use `latest`; install location is a runtime concern. [MUST]

### 6. APPLY

Apply the plan preserving existing files. On conflict, preserve the user-owned file and surface the conflict; never overwrite. [MUST]

### 7. VALIDATE

Validate implemented changes with established repository tooling (existing tests, linters, `make check` if present). Do not invent new validation tooling for this step. [MUST]

### 8. RETURN TO OMFA LIFECYCLE

Summarize changes made and unresolved issues. [MUST] Then resume the OMFA lifecycle: identify the current modeling stage and the next scientific step. Route only when a boundary is reached:

- implementation architecture, module mapping, parameter schema, verification planning → `omfb`
- reproducibility, FAIR, packaging, citation, archival, environment hardening, stewardship → `fair`
- sustained narrative documentation → `document`

---

## Common Failure Patterns

- Questioning before auditing the repository.
- Rewriting a healthy repository to match a template.
- Treating a syntactically valid unresolved identifier as malformed.
- Confusing the schema version with the `<profile>:v<version>` filesystem contract.
- Conflating schema validation with identifier resolution.
- Cosmetic normalization that breaks compatibility.
- Inventing `science.toml` semantics or claiming a remote convention is fixed.
- Migrating a profile without explicit policy permission.
- Over-scaffolding: adding CI, SBOM, publishing, docs site, release automation, or provenance tooling by default.
- Adding a second package manager.
- Overwriting user-owned files on conflict.
- Validating with invented tooling rather than established repository tooling.
- Lingering in bootstrap instead of returning to the OMFA lifecycle.

---

## Routing

This module is entered only from the parent `SKILL.md` activation logic on matching bootstrap/conformance intent. It exits only by returning to the OMFA lifecycle:

- Route to `omfb` for detailed implementation architecture, module mapping, parameter schema, or verification planning.
- Route to the `fair` skill for reproducibility, FAIR metadata, packaging, citation, archival, environment hardening, or stewardship.
- Route to `document` for sustained narrative documentation.
- Otherwise resume `lifecycle.md` at the current modeling stage.
