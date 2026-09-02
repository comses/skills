# OMF Artifact Contracts

This registry defines authority and collaboration boundaries for shared files under `omf-artifacts/`. Ownership identifies the skill that controls an artifact's contract and resolves conflicts; it does not prohibit declared contributors from making scoped changes.

## Shared rules

- Preserve the artifact's structure, provenance, and existing scientific commitments unless the contract permits changing them.
- Record the evidence and reason for a cross-skill contribution.
- Flag contradictions and stale dependencies rather than silently reconciling them.
- Route structural changes, conflicting evidence, and edits outside a declared contribution scope to the owner.
- Follow explicit user direction when it overrides a contract, and report the exception.

## Contract registry

| Artifact or namespace | Owner | Permitted contributions | Protected decisions and route conditions |
| --- | --- | --- | --- |
| `omf-artifacts/README.md` | `omfa` | Namespace owners may maintain entries and status for their own subtree. | Route changes to namespace conventions, lifecycle status semantics, or cross-namespace dependencies to `omfa`. |
| Scientific artifacts directly under `omf-artifacts/` | `omfa` | Method specialists may add traceable evidence to the relevant report or register. `fair` may update persistent identifiers and provenance links in `model-card.md`. | Do not reinterpret purpose, scope, conceptual structure, assumptions, research questions, or scientific conclusions. Route contradictions, schema changes, and substantive scientific revisions to `omfa`. |
| `omf-artifacts/implementation/` | `omfb` | Verification, platform, and execution work may update evidence, status, and measured constraints in the applicable implementation artifact. | Do not change scientific intent inherited from OMFA artifacts. Route implementation architecture or contract changes to `omfb`; route required scientific changes to `omfa`. |
| `omf-artifacts/fair/` | `fair` | Other skills may add factual inventory entries, identifiers, repository locations, and provenance evidence. | Do not change FAIR assessments, stewardship commitments, preservation decisions, or management-plan structure. Route those changes and conflicting metadata to `fair`. |
| `omf-artifacts/document/` and document-authored narratives | `document` | OMFA artifacts provide authoritative scientific content; reviewers may provide traceable corrections and comments. | Do not silently change scientific claims to reconcile source conflicts. Route scientific changes to `omfa` and narrative structure or framework changes to `document`. |

Scientific artifacts directly under `omf-artifacts/` include the model card, problem statement, research questions, conceptual model, assumptions, decision log, uncertainty register, analysis and evaluation reports, stakeholder and ethics records, limitations, ABM specification, and other OMFA lifecycle artifacts.

## Applying a contract

Before modifying an existing artifact:

1. Identify its owner and the active skill's role as owner, contributor, or consumer.
2. Compare the proposed edit with the permitted contribution scope.
3. Make the smallest traceable change when it is permitted.
4. Otherwise, preserve the file, describe the proposed change and evidence, and route it to the owner.
