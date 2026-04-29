# Contributing Skills to COMSES

Thank you for contributing to this skills repository! This guide walks you through the process of creating, testing, and submitting skills for computational modelers.

## Table of Contents

1. [Before You Start](#before-you-start)
2. [Skill Creation Workflow](#skill-creation-workflow)
3. [Naming Conventions](#naming-conventions)
4. [Writing Guidelines](#writing-guidelines)
5. [Frontmatter Specification](#frontmatter-specification)
6. [Testing Your Skill](#testing-your-skill)
7. [Submission Checklist](#submission-checklist)

## Before You Start

- Familiarize yourself with the [Agent Skills specification](https://agentskills.io)
- Review existing skills in `skills/` to understand the pattern
- Copy [docs/SKILL-TEMPLATE.md](docs/SKILL-TEMPLATE.md) as your starting point
- Ensure your skill addresses a concrete pain point for computational modelers
- Confirm your skill does NOT substantially overlap with existing skills

## Skill Creation Workflow

### 1. Plan Your Skill

Answer these questions before writing:

- **What problem does it solve?** (e.g., "Modelers struggle to document ODD+2 protocols manually")
- **When should the coding agent use it?** (e.g., "When user has model code and needs narrative documentation")
- **What does it take as input?** (e.g., Python/R model files, docstrings, parameter descriptions)
- **What does it produce?** (e.g., Markdown ODD narrative, validation checklist, completed sections)
- **Are there dependencies?** (e.g., Python 3.10+, git, Docker)

### 2. Create Your Skill Folder

Run `/create-skill <name> — <one-sentence description>` in your coding agent. This scaffolds `skills/<name>/SKILL.md` from [docs/SKILL-TEMPLATE.md](docs/SKILL-TEMPLATE.md) with placeholders filled in, and generates a starter `evals.json`.

Alternatively, copy manually:
```bash
mkdir -p skills/your-skill-name
cp docs/SKILL-TEMPLATE.md skills/your-skill-name/SKILL.md
```

### 3. Write SKILL.md

See [Frontmatter Specification](#frontmatter-specification) and [Writing Guidelines](#writing-guidelines) below.

### 4. Add Optional Resources

As your skill grows, add supporting files:

```
your-skill-name/
├── SKILL.md                     ← always required
├── scripts/
│   ├── setup.py
│   ├── validate.py
│   └── requirements.txt
├── references/
│   ├── METHODOLOGY.md
│   ├── CHECKLIST.md
│   └── EXAMPLES.md
└── assets/
    ├── template.md
    ├── default-config.yaml
    └── example-output.md
```

### 5. Test Your Skill

See [Testing Your Skill](#testing-your-skill).

### 6. Submit a Pull Request

Include:
- Your skill folder with SKILL.md and any bundled resources
- A description of what the skill does and when it triggers
- Results of your test runs (include prompts you tested against)
- Link to any relevant documentation or examples

## Naming Conventions

### Skill Folders & Names

- **Format:** `kebab-case`, lowercase, hyphens only
- **Length:** ≤ 48 characters (allows room for versioning)
- **Requirements:** Folder name MUST match the `name:` field in frontmatter
- **Examples:** ✅ `document`, `ospool`
- **Anti-patterns:** ❌ `ODD_Protocol_Narrative`, `document-v2`, `my_skill`

### Script Names in Bundled Resources

- **Format:** `snake_case.py` for Python, `kebab.sh` or `word.sh` for shell scripts
- **Examples:** `extract_metadata.py`, `validate-checklist.sh`, `generate-template.py`

### Reference & Asset File Names

- **Format:** `UPPERCASE_TOPIC.md` for detailed references, `topic-guide.md` for guides
- **Examples:** `ODD-CHECKLIST.md`, `FAIR4RS-HANDBOOK.md`, `hpc-quickstart.md`

## Writing Guidelines

### Principles

1. **Imperative tone:** Use direct commands ("Generate the ODD narrative", not "The ODD narrative is generated")
2. **Progressive disclosure:** Start with brief overview; reference bundled docs for deep dives
3. **Progressive repetition:** If a step recurs, briefly repeat instructions rather than forcing the user to scroll back
4. **Concrete examples:** Include at least one realistic input/output (even if brief)
5. **Gotchas section:** Always include ⚠️ Gotchas with common failure modes

### Structure

A typical SKILL.md body includes:

```markdown
# Skill Name

## When to Use This Skill

- You have model code and need...
- When preparing for publication...
- If OSPool execution is required...

## Key Inputs

- Model source files (Python/R/C++)
- Parameter descriptions or config files
- Optional: docstrings with metadata

## Step-by-Step Instructions

1. Read the model code
2. Extract metadata using scripts/extract.py
3. Generate narrative following references/TEMPLATE.md
4. Validate against references/CHECKLIST.md

## ⚠️ Gotchas

- **Stochastic models:** If your model uses randomness, document any fixed random seeds
- **Large codebases:** Summarize into entity/subsystem abstractions first
- **Missing documentation:** Skill will ask clarifying questions rather than guess

## Templates & Resources

- See `references/ODD-CHECKLIST.md` for the 23-point validation list
- See `assets/odd_template.md` for narrative structure
- Use `scripts/validate_odd.py` to check for completeness

## Example

**Input:** A Python ABM with classes for Agent, Environment, and Scheduler
**Output:** An ODD narrative section covering entities/state variables for all three
```

### Dos and Don'ts

| Do | Don't |
|---|---|
| Include specific CLI examples | Use vague instructions like "use the tool" |
| Reference scripts/resources as `scripts/name.py` (one level deep) | Create nested utility folders that bury important files |
| Use YAML for config templates | Use INI or custom formats without strong justification |
| Link to authoritative specs (arXiv, OSG docs, FAIR4RS) | Reproduce entire external specs verbatim |
| Point out when a step might take time (e.g., "Docker build ~5 min") | Leave latency expectations to chance |
| Ask clarifying questions before guessing | Make unsupported assumptions (e.g., "all models use Python") |

## Frontmatter Specification

### Required Fields

```yaml
---
name: your-skill-name
description: |
  A complete description of what this skill does.
  
  Use when: you have model code and need...
  When to trigger: mention [keywords like ODD, documentation, publication]
  Expected output: [specific deliverables]
---
```

### Optional Fields

```yaml
---
name: your-skill-name
description: ...
license: MIT (default) | Apache-2.0 | Proprietary
compatibility: Python 3.10+, git, Docker (optional)
metadata:
  domain: computational-modeling | documentation | publication | execution
  maturity: alpha | beta | stable
  audience: modelers | researchers | data scientists
---
```

### Guidancefor `description`

The description is your **primary triggering mechanism**. Make it:

- **Task-specific:** "ODD+2 narrative for agent-based models" not just "model documentation"
- **Keyword-rich:** Include trigger phrases users would naturally type
- **Outcome-focused:** Mention specific deliverables (e.g., "checklist", "narrative sections", "validation report")
- **Slightly pushy:** Coding agents tend to under-trigger skills. Emphasize when to use: "Use whenever you mention ODD, ABM documentation, or model publication preparation"

## Testing Your Skill

### Manual Testing

1. **Should-trigger cases** (5–10 prompts that SHOULD activate your skill):
   ```
   - "I need to document my ABM following ODD+2"
   - "Generate an ODD narrative for my model"
   - "Create publication-ready documentation for my code"
   ```

2. **Should-NOT-trigger cases** (3–5 negative prompts):
   ```
   - "Write a timeline for my project"
   - "Document my API endpoints"
   - "Generate a README file"
   ```

3. **Test each case** by mentioning the skill in a real coding agent session (Claude Code, Claude.ai, Cursor, Cline, or other AI coding agents)

### Creating an Evaluation Strategy

For each skill, document 3–5 concrete test cases in a file `evals/evals.json`:

```json
{
  "skill_name": "document",
  "evals": [
    {
      "id": 1,
      "prompt": "I have a Python ABM with Agent and Environment classes. Generate an ODD narrative.",
      "should_trigger": true,
      "expected_output": "ODD sections covering entities, state variables, and processes",
      "files": ["evals/files/minimal_abm.py"]
    }
  ]
}
```

## Submission Checklist

Before submitting, verify:

- [ ] Skill folder name matches `name:` field in frontmatter
- [ ] Frontmatter includes `name` and `description` (and optionally `license`, `compatibility`, `metadata`)
- [ ] Description includes triggers ("Use when you...") and expected outputs
- [ ] All script references use relative paths: `scripts/name.py` (not `./scripts/name.py`)
- [ ] README/CONTRIBUTING sections are consistent with repository guidelines
- [ ] Tested skill against ≥5 should-trigger and ≥3 should-not-trigger prompts
- [ ] No hardcoded paths or user-specific settings
- [ ] Scripts have clear usage documentation (docstrings, help text, or references/SCRIPT.md)
- [ ] No credentials, API keys, or personal data in examples
- [ ] License field in frontmatter (defaults to MIT if omitted)

## Questions?

Open an issue or start a discussion in the repository. We're here to help!

---

**Thanks for contributing to computational modeling skills!** 🎉
