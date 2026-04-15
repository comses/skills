# Skills Roadmap

This document outlines planned expansions to the COMSES skills repository, organized by domain and priority tier.

## Tier 1: Core Literacy & Documentation (Current Release)

**Status:** Actively developed; starter skills available

### Current Skills
- **document** (beta): ODD+2 documentation for ABMs
- **fair4rs** (beta): Publication metadata and archival readiness
- **ospool** (beta): OSPool batch and parameter sweep scaffolding
- **hpc** (beta): HPC cluster job submission and arrays

### Outcomes
- Researchers can document models following ODD+2 protocol
- Models are publication-ready with FAIR4RS metadata
- Parameter sweeps can be executed on OSPool or HPC infrastructure at scale

---

## Tier 2: Reproducibility & Containerization (Q2-Q3 2026)

**Status:** In planning

### Planned Skills

#### **reproducibility-capsule** (alpha)
Capture model environment (Python/R dependencies, system libraries, git commit hash) and verify rerun reproducibility via containerized snapshots.

**Value:** Ensures that future runs of the model produce identical outputs (or identified stochasticity) even after years or environment changes.

**Key features:**
- `scripts/capture_env.sh`: Extract dependency tree and git metadata
- `scripts/build_dockerfile.py`: Generate minimal Dockerfile from environment specs
- `scripts/verify_rerun.py`: Compare outputs via checksum matrix and diff report
- Integration with Zenodo for automated container archival

**Audience:** Modelers requiring long-term reproducibility guarantees; journals/funders requiring reproducibility verification

#### **model-data-lineage** (alpha)
Track input→process→output lineage with DVC (Data Version Control) configuration, materialization specs, and dependency DAGs.

**Value:** Audit trail showing how each output was generated, enables reproduction of specific analyses, supports downstream reuse.

**Key features:**
- `scripts/dvc_init_model.sh`: Setup DVC for S3, local, or Google Cloud storage
- `scripts/lineage_to_mermaid.py`: Generate DAG visualization for documentation
- Support for DVC.yaml pipeline definitions and Airflow integration
- W3C PROV-compatible metadata export

**Audience:** Data-intensive modelers; researchers requiring audit trails for regulatory or publication compliance

---

## Tier 3: Analysis & Validation (Q3-Q4 2026)

**Status:** In planning

### Planned Skills

#### **parameter-sweep-analysis** (alpha)
Design parameter sweeps using One-At-a-Time (OAT), 2-level factorial, or Latin Hypercube sampling; compute sensitivity indices (Sobol, Morris); generate interactive dashboards.

**Value:** Automate sensitivity analysis workflow from design to visualization.

**Key features:**
- `scripts/design_sweep.py`: Generate sweep configurations for multiple DOE strategies
- `scripts/analyze_sensitivity.py`: Compute Sobol, Morris, and variance-based indices
- `scripts/plot_heatmap.R`: Interactive Plotly HTML dashboards from results
- Standardized JSON output format for downstream analysis

**Audience:** Modelers exploring parameter sensitivity; researchers developing emulators or calibration pipelines

#### **model-validation-harness** (alpha)
Generate unit test templates, regression test scaffolding, and parameter bounds checking for model logic validation.

**Value:** Reduce validation burden by auto-generating test boilerplate; catch regressions early in development.

**Key features:**
- `scripts/generate_tests.py`: Stub test file from model functions/classes
- `scripts/check_bounds.py`: Validate parameter ranges and state variable invariants
- `scripts/regression_suite.py`: Snapshot-based output regression tests
- CI/CD integration (GitHub Actions, GitLab CI templates)

**Audience:** Model developers; teams requiring continuous regression checking

#### **notebooks-to-reproducible-workflow** (alpha)
Convert Jupyter/Quarto notebooks into containerized, version-controlled, reproducible pipelines.

**Value:** Bridge exploratory analysis (notebooks) and reproducible production workflows.

**Key features:**
- `scripts/nb_to_script.py`: Jupytext conversion to .py with markdown cells
- `scripts/exec_script.sh`: Ordered cell execution with error capture and logging
- `scripts/validate_rerun.py`: Determinism check against output snapshots
- Integration with reproducibility-capsule for containerization

**Audience:** Researchers transitioning from exploratory analysis to reproducible workflows; computational journalism

---

## Tier 4: Advanced Integration & Domain Extensions (Q4 2026+)

**Status:** Conceptual

### Planned Skills

#### **agentpy-scaffolder** (alpha)
Automated scaffolding for models built with AgentPy framework; template generation, API documentation, ODD extraction from code decorators.

**Value:** Reduce boilerplate for AgentPy users; auto-generate ODD from within-code metadata.

**Audience:** AgentPy modelers

#### **netlogo-to-python** (alpha)
Semi-automated translation from NetLogo to Python using AST analysis and pattern matching.

**Value:** Enable Python modelers to leverage NetLogo benchmark models.

**Audience:** NetLogo users interested in Python; multi-language model comparison research

#### **bayesian-inference-wrapper** (alpha)
Setup Bayesian calibration (PyMC, STAN) for parameter estimation from observed data; generate inference diagnostics and posterior predictive plots.

**Value:** Automate Bayesian workflow for model calibration.

**Audience:** Quantitative modelers; researchers with observational or experimental data

#### **model-ensemble-framework** (alpha)
Orchestrate ensembles of models (different implementations, parameters, or structures) for comparative analysis and voting/stacking.

**Value:** Support multi-model comparison and ensemble decision-making.

**Audience:** Modelers comparing competing paradigms or theories

---

## Sustainability & Governance

### Community Contributions
All skills are open to community contributions. See [CONTRIBUTING.md](../CONTRIBUTING.md) and [spec/README.md](../spec/README.md) for guidelines.

### Review & Acceptance
- Skills undergo community review before merge (GitHub PR workflow)
- Merged skills are tracked on skills.sh leaderboard
- Feedback and issues are tracked on the repository

### Version & Support
- Skills follow semantic versioning (v1.0.0, v1.1.0, v2.0.0)
- Critical bugfixes are backported to stable versions
- Deprecated skills remain available but marked as such

---

## Feedback & Roadmap Updates

We welcome feedback on the roadmap! Please:

1. Open an issue to discuss a planned skill or propose a new skill
2. Share use cases or pain points your research encounters
3. Contribute implementations (see CONTRIBUTING.md)

This roadmap is a living document and will be updated quarterly. Last updated: April 14, 2026.
