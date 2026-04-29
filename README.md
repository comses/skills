# COMSES Skills Repository

Agent Skills for computational modelers: documentation, reproducibility, publication, and execution.

This repository hosts a curated collection of [Agent Skills](https://agentskills.io) designed to help researchers and developers develop and share computational models in the social and ecological sciences. Skills are reusable procedural workflows that enhance AI agents to accomplish specialized tasks.

## Quick Start

### Install Node.js LTS with nvm (WSL, macOS, Linux)

`npx skills ...` requires Node.js. Use the node version manager `nvm` to install and manage Node versions without `sudo`.

Security best practices:

- Install only from the official [nvm-sh/nvm](https://github.com/nvm-sh/nvm/releases) repository.
- Pin the installer to a specific release tag instead of running an unpinned command.
- Review the installer script before executing it.
- Avoid `sudo npm -g ...`; use user-level installs with `nvm`.

1. Install prerequisites

WSL / Linux:

```bash
sudo apt update
sudo apt install -y curl ca-certificates git
```

macOS (with Homebrew):

```bash
brew install curl ca-certificates git
```

2. Install `nvm` from an official tagged release

Choose the latest release tag from: https://github.com/nvm-sh/nvm/releases

```bash
export NVM_VERSION="v0.40.3"
curl -fsSL -o /tmp/install_nvm.sh "https://raw.githubusercontent.com/nvm-sh/nvm/${NVM_VERSION}/install.sh"
less /tmp/install_nvm.sh
bash /tmp/install_nvm.sh
```

3. Load `nvm` in your current shell

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
```

If needed, restart your terminal so your shell profile changes take effect.

4. Install and use the latest Node LTS

```bash
nvm install --lts
nvm alias default 'lts/*'
nvm use --lts
```

5. Verify toolchain

```bash
node -v
npm -v
npx -v
```

6. Keep Node LTS current

```bash
nvm install --lts --reinstall-packages-from=current
nvm use --lts
```

7. Continue with skills installation

```bash
npx skills add comses/skills
```

### Install a Skill

```bash
npx skills add comses/skills
```

Or install from GitHub directly:

```bash
npx skills add https://github.com/comses/skills
```

### Use a Skill in Your Coding Agent

Once installed, mention the skill by name in your conversation:
- *"Use the document skill to generate ODD+2 documentation for my ABM"*
- *"Set up an OSPool batch scaffolder for my sensitivity analysis"*
- *"Generate a FAIR4RS publication checklist for my model outputs"*

See the Agent Skills documentation for your platform for details on skill usage.

## Skills Overview

This repository currently includes five skills covering core computational modeling needs:

### 1. **document**
Generates and iteratively improves ODD+2 (Overview, Design Concepts, Details) documentation for agent-based models. Use when you have model code and need publication-ready narrative documentation that satisfies the 23-point ODD+2 checklist.

**Triggers:** "Document my model", "Generate ODD", "Write model narrative"

### 2. **fair4rs**
Creates FAIR4RS metadata with codemeta.json as canonical machine-readable metadata, citation files derived from codemeta.json, publication checklists, and EVERSE-aligned software management plans to ensure your computational artifacts are ready for archival and publication. Use when preparing models for Zenodo, arXiv, or disciplinary repositories.

**Triggers:** "Prepare for publication", "Generate publication checklist", "Create FAIR metadata"

### 3. **ospool**
Generates HTCondor job submission scripts and parameter sweep configurations for running models on the Open Science Grid (OSPool). Use for batch processing, large parameter sweeps, or distributed sensitivity analysis.

**Triggers:** "Run on OSPool", "Generate HTCondor batch script", "Set up parameter sweep"

### 4. **hpc**
Generates Slurm job scripts, job arrays, and resource allocation templates for running models on HPC systems. Use for multi-node simulations or large-scale experiments requiring direct HPC cluster access.

**Triggers:** "Run on HPC", "Generate Slurm script", "Set up batch array job"

### 5. **peer-review**
Evaluates computational model submissions for peer review readiness using required CoMSES criteria (ease of execution, documentation thoroughness, and code quality) plus supporting research software quality indicators inspired by EVERSE.

**Triggers:** "Peer review my model", "Is this model submission ready", "Review codebase quality", "Check reproducibility"

## Repository-Local Maintainer Skill

This repository also includes a local-only maintainer skill that is not part of the published `skills/` catalog:

### **update-skill** (`.github/skills/update-skill`)
Maintainer workflow for refreshing compressed artifacts, references, and eval expectations when upstream standards evolve.

Use cases:
- Refreshing rubric/indicator snapshots after upstream changes
- Keeping `SKILL.md`, `references`, `assets`, and `evals.json` synchronized in one PR
- Standardizing refresh PR notes for traceability

## Repository Structure

```
skills/
├── .github/
│   └── skills/
│       └── update-skill/        (repository-local maintainer skill)
│           ├── SKILL.md
│           ├── references/
│           │   └── REFRESH-WORKFLOW.md
│           └── assets/
│               └── REFRESH-PR-NOTE-TEMPLATE.md
├── README.md                    (this file)
├── CONTRIBUTING.md              (contribution guidelines)
├── LICENSE                      (MIT)
├── .gitignore
├── docs/                        (repository-level documentation)
│   ├── roadmap.md
│   └── SKILL-TEMPLATE.md        (copy/fill template for new skills)
└── skills/                      (all skill folders)
    ├── document/
    │   └── SKILL.md
    ├── fair4rs/
    │   └── SKILL.md
    ├── ospool/
    │   └── SKILL.md
    ├── hpc/
    │   └── SKILL.md
    └── peer-review/
        └── SKILL.md
```

## For Skill Authors

### Adding a New Skill

1. **Read** [CONTRIBUTING.md](CONTRIBUTING.md) for submission guidelines and naming conventions.
2. **Review** [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices) before drafting.
3. **Ground from real expertise**: start from real task runs, corrections, and project artifacts (not generic advice).
4. **Scope coherently**: define one composable unit of work; avoid overly broad or ultra-narrow skills.
5. **Design for context efficiency**: keep `SKILL.md` concise, move deep details to `references/`, and load references only when needed.
6. **Prefer defaults over menus**: choose one default tool/approach and list alternatives only as fallbacks.
7. **Include reusable control patterns**: gotchas, output templates, and validation loops/checklists where relevant.
8. **Refine with real execution**: test should-trigger and should-not-trigger prompts, review execution traces, then iterate.
9. **Copy** an existing skill folder as a starting point: `cp -r skills/hpc skills/your-skill-name`.
10. **Fill in** the YAML frontmatter (`name`, `description`) and markdown instructions following the progressive disclosure pattern.
11. **Include optional resources** (scripts, references, assets) as your skill grows.
12. **Test** against should-trigger and should-not-trigger prompts before submitting a PR.
13. **Submit** a pull request with your skill and evaluation strategy (see CONTRIBUTING.md).

### Skill Anatomy

Each skill lives in its own folder with a required `SKILL.md` file:

```
your-skill-name/
├── SKILL.md                     (required: frontmatter + instructions)
├── scripts/                     (optional: Python/shell scripts for automation)
├── references/                  (optional: compressed, detailed docs, checklists, guides)
└── assets/                      (optional: templates, icons, example files)
```

Recommended semantic purpose of each component:

- `SKILL.md` -> orchestration and enforcement language (when to trigger, required workflow steps, output constraints)
- `assets/` -> reusable output artifacts (templates, starter files, structured output skeletons)
- `references/` -> normative guidance / rules / compressed artifacts (checklists, standards mappings, policy summaries)
- `scripts/` -> deterministic automation helpers (validation, generation, extraction)

Authoring guidance:

- Keep operational decision logic in `SKILL.md`; do not duplicate it across assets.
- Put reusable content the model can copy/fill into `assets/`.
- Put standards and rule-oriented material in `references/`.

**Frontmatter (required fields):**
```yaml
---
name: your-skill-name
description: Brief description of when and why to use this skill
---
```

**Optional fields:**
```yaml
license: MIT (default) | Apache-2.0 | GPL-3.0-or-later
compatibility: Tool/version requirements
metadata:
  domain: computational-modeling | documentation | publication | execution
  maturity: alpha | beta | stable
  audience: modelers | researchers | data scientists
---
```

See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) for full guidance.

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
