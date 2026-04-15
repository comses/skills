# COMSES Skills Repository

Agent Skills for computational modelers: documentation, reproducibility, publication, and execution.

This repository hosts a curated collection of [Agent Skills](https://agentskills.io) designed to help researchers and developers create, document, validate, and execute computational models effectively. Skills are reusable procedural workflows that enhance AI agents to accomplish specialized tasks.

## Quick Start

### Install a Skill

```bash
npx skills add comses-network/skills
```

Or install from GitHub directly:

```bash
npx skills add https://github.com/comses-network/skills
```

### Use a Skill in Your Coding Agent

Once installed, mention the skill by name in your conversation:
- *"Use the document skill to generate ODD+2 documentation for my ABM"*
- *"Set up an OSPool batch scaffolder for my sensitivity analysis"*
- *"Generate a FAIR4RS publication checklist for my model outputs"*

See the Agent Skills documentation for your platform for details on skill usage.

## Starter Skills Overview

This repository includes four starter skills covering core computational modeling needs:

### 1. **document**
Generates and iteratively improves ODD+2 (Overview, Design Concepts, Details) documentation for agent-based models. Use when you have model code and need publication-ready narrative documentation that satisfies the 23-point ODD+2 checklist.

**Triggers:** "Document my ABM", "Generate ODD", "Write model narrative"

### 2. **fair4rs**
Creates FAIR4RS metadata with codemeta.json as canonical machine-readable metadata, citation files derived from codemeta.json, publication checklists, and EVERSE-aligned software management plans to ensure your computational artifacts are ready for archival and publication. Use when preparing models for Zenodo, arXiv, or disciplinary repositories.

**Triggers:** "Prepare for publication", "Generate publication checklist", "Create FAIR metadata"

### 3. **ospool**
Generates HTCondor job submission scripts and parameter sweep configurations for running models on the Open Science Grid (OSPool). Use for batch processing, large parameter sweeps, or distributed sensitivity analysis.

**Triggers:** "Run on OSPool", "Generate HTCondor batch script", "Set up parameter sweep"

### 4. **hpc**
Generates Slurm job scripts, job arrays, and resource allocation templates for running models on HPC systems. Use for multi-node simulations or large-scale experiments requiring direct HPC cluster access.

**Triggers:** "Run on HPC", "Generate Slurm script", "Set up batch array job"

## Repository Structure

```
skills/
├── README.md                    (this file)
├── CONTRIBUTING.md              (contribution guidelines)
├── LICENSE                      (MIT)
├── .gitignore
├── spec/                        (Agent Skills specification & COMSES guidance)
│   └── README.md
├── template/                    (skill template for contributors)
│   └── SKILL.md
├── docs/                        (repository-level documentation)
│   └── roadmap.md
└── skills/                      (all skill folders)
    ├── document/
    │   └── SKILL.md
    ├── fair4rs/
    │   └── SKILL.md
    ├── ospool/
    │   └── SKILL.md
    └── hpc/
        └── SKILL.md
```

## For Skill Authors

### Adding a New Skill

1. **Read** [CONTRIBUTING.md](CONTRIBUTING.md) for submission guidelines and naming conventions.
2. **Copy** the template from `template/SKILL.md` to your skill folder: `skills/your-skill-name/SKILL.md`.
3. **Fill in** the YAML frontmatter (`name`, `description`) and markdown instructions following the progressive disclosure pattern.
4. **Include optional resources** (scripts, references, assets) as your skill grows.
5. **Test** against should-trigger and should-not-trigger prompts before submitting a PR.
6. **Submit** a pull request with your skill and evaluation strategy (see CONTRIBUTING.md).

### Skill Anatomy

Each skill lives in its own folder with a required `SKILL.md` file:

```
your-skill-name/
├── SKILL.md                     (required: frontmatter + instructions)
├── scripts/                     (optional: Python/shell scripts for automation)
├── references/                  (optional: detailed docs, checklists, guides)
└── assets/                      (optional: templates, icons, example files)
```

**Frontmatter (required fields):**
```yaml
---
name: your-skill-name
description: Brief description of when and why to use this skill
---
```

**Optional fields:**
```yaml
license: MIT (default) | Apache-2.0 | Proprietary
compatibility: Tool/version requirements
metadata:
  domain: computational-modeling | documentation | publication | execution
  maturity: alpha | beta | stable
  audience: modelers | researchers | data scientists
---
```

See [template/SKILL.md](template/SKILL.md) and [CONTRIBUTING.md](CONTRIBUTING.md) for full guidance.

## Roadmap

See [docs/roadmap.md](docs/roadmap.md) for planned skills expanding into:
- **Reproducibility & containerization** (Docker, environment capture, snapshot verification)
- **Data & lineage tracking** (DVC integration, provenance metadata, parameter tracking)
- **Analysis & validation** (sensitivity analysis frameworks, unit testing templates, notebooks-to-workflows)
- **Integration & composability** (standard interchange formats, skill composition patterns)

## Links & References

- **Agent Skills specification**: [agentskills.io](https://agentskills.io)
- **Skills.sh leaderboard**: [skills.sh](https://skills.sh)
- **Agent Skills documentation**: [agentskills.io](https://agentskills.io)
- **Agent Skills CLI**: [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)
- **Example skills repository**: [github.com/anthropics/skills](https://github.com/anthropics/skills)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Contribution workflow
- Naming conventions and style guidance
- Review checklist
- Community contact

## License

All skills in this repository are licensed under the [MIT License](LICENSE) unless otherwise noted in individual `SKILL.md` files.

---

**COMSES Network** • [www.comses.net](https://www.comses.net)
