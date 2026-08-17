# Model Card (Guidance Template)

The Model Card provides a concise, high-level summary of the computational model, its purpose, evaluation, intended use, and limitations.

---

## Model Overview

- **Name:** <Model Name>
- **Version:** <Version>
- **Status:** <Conceptual | Prototype | Under Evaluation | Validated for Intended Purpose | Archived>
- **Authors:** <Authors or Organization>
- **License:** <License>
- **Repository / DOI:** <Repository, archive, or publication>
- **Model Type:** <Agent-Based, System Dynamics, Statistical, Hybrid, etc.>

---

## Scientific Purpose

### Scientific Question

<What scientific or decision-support question is this model intended to answer?>

### Purpose

<One-sentence description of why the model exists.>

### Intended Users

<Researchers, policymakers, educators, operational analysts, etc.>

Reference:
- `artifacts/problem-statement.md`
- `artifacts/research-questions.md`

---

## Conceptual Summary

### Core Mechanisms

<Brief description of the principal entities, processes, and interactions represented by the model.>

### System Scope

<Spatial, temporal, organizational, or conceptual boundaries.>

### Key Assumptions

<Summary only. Reference the full assumptions document.>

Reference:
- `artifacts/conceptual-model.md`
- `artifacts/assumptions.md`

---

## Evaluation Summary

### Evaluation Approach

<How the model was evaluated (verification, calibration, validation, expert review, etc.)>

### Credibility

<Summary of the evidence supporting model credibility>

### Uncertainty

<Brief summary of the principal uncertainties affecting interpretation>

Reference:
- `artifacts/evaluation-report.md`
- `artifacts/uncertainty-register.md`

---

## Supported Claims and Intended Use:

### Supported Claims

This model is intended to support:

- <Scientific conclusions or decision-support uses supported by the available evidence.>

This model should **not** be used to support:

- <Unsupported extrapolations, inappropriate policy claims, forecasting contexts, etc.>

### Appropriate contexts

- <Where the model is scientifically appropriate.>

### Inappropriate contexts

- <Known situations where the model should not be applied.>

---

## Known Limitations

Summarize important limitations, including:

- abstraction boundaries;
- omitted processes;
- unresolved uncertainty;
- known failure modes;
- computational or data limitations.

Reference:
- `artifacts/limitations.md`

---

## Implementation

Implementation details are maintained separately.

Reference:

- `artifacts/implementation/plan.md`
- `artifacts/implementation/architecture.md`
- `artifacts/fair/provenance-manifest.json`
- `fair` skill guidance for reproducibility assessment, packaging, archival, and stewardship

---

## Version Summary

Describe major changes since the previous release, including:

- scientific changes
- implementation changes
- evaluation changes
- known compatibility impacts
