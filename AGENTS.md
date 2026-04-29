# AGENTS.md — COMSES Skills Repository

Agent instructions for working in this repository. Every AI agent should read this file before creating, editing, or reviewing skills.

---

## What this repo is

A curated collection of [Agent Skills](https://agentskills.io) targeting computational modelers: provides agentic support for model documentation, publication, execution on HPC / HTC / cloud compute, and peer review.

Published skills live in `skills/`. A local, maintainer-only skill for updating / refreshing skill content and references lives in `.github/skills/update-skill/` and is **not** part of the published catalog.

---

## Required authoring reference (load when editing skills)

When you are:
- creating a new skill
- modifying an existing skill
- reviewing or debugging a skill

**You must read:**
```

docs/agent-skills-creation-reference.md

```

Use it as the canonical guide for:
- SKILL.md structure and constraints
- description (trigger) optimization
- scoping and decomposition
- progressive disclosure
- evaluation and testing

Do not rely on memory of best practices. Load the file when needed.

---

## Skill anatomy

```

skills/<kebab-case-name>/
├── SKILL.md          ← required: YAML frontmatter + agent instructions
├── assets/           ← output templates and starter files (copy/fill)
├── references/       ← normative checklists, standards, compressed artifacts
└── scripts/          ← deterministic automation helpers

````

Rules:
- Folder name **must** match the `name:` frontmatter field exactly.
- `SKILL.md` should stay under **500 lines / 5 000 tokens**.
- Move deep detail to `references/` and explicitly instruct when to load each file.
- All paths must be relative.
- No secrets, absolute paths, or personal configuration.

---

## Required frontmatter

```yaml
---
name: kebab-case-name
description: |
  Use this skill when...
  Triggers: "phrase 1", "phrase 2"
  Expected output: ...
license: MIT
---
````

Optional: `compatibility`, `metadata.domain`, `metadata.maturity`, `metadata.audience`.

---

## Skill loading model (critical)

Agents load skills in stages:

1. Discovery → name + description
2. Activation → full `SKILL.md`
3. On-demand → `references/` and `scripts/`

Implications:

* If the description is weak, the skill will never activate
* `SKILL.md` must work without references unless explicitly invoked
* References must include **clear load conditions**

---

## Local best practices (summary)

This section is intentionally compressed. Full guidance lives in the authoring reference.

### Start from real workflows

Use actual runs, fixes, and artifacts. Avoid generic advice.

### Add only missing knowledge

Include only what the base model would get wrong.

### One skill = one unit

Ensure clear, composable scope.

### Progressive disclosure

Keep `SKILL.md` minimal. Push bulk to `references/` with explicit triggers.

### Defaults over options

Always choose a primary approach.

### Gotchas are required

Document real failure patterns the agent will hit.

### Use templates and validation

* Templates for outputs
* Validation loops for correctness

### Prefer scripts for repeated logic

Move complex or repeated steps into `scripts/`.

### Refine using execution traces

Fix:

* indecision → unclear instructions
* branching → too many options
* inefficiency → irrelevant content

---

## COMSES-specific conventions

| Convention       | Rule                                           |
| ---------------- | ---------------------------------------------- |
| Naming           | `kebab-case`; folder name = `name:`; ≤48 chars |
| Scripts          | `snake_case.py`, `kebab.sh`                    |
| References       | `UPPERCASE-TOPIC.md`                           |
| Config/templates | YAML or JSON only                              |
| Maturity         | `alpha`, `beta`, `stable`                      |
| Evals            | ≥3 trigger + ≥3 non-trigger cases              |
| License          | MIT default                                    |

---

## Skill semantic roles

* `SKILL.md` → orchestration, decisions, constraints
* `assets/` → templates to fill
* `references/` → standards and rules (load on demand)
* `scripts/` → deterministic execution

Do not duplicate logic across layers.

---

## Evaluation strategy

Each skill must include:

```json
{
  "skill_name": "example",
  "evals": [
    {
      "id": 1,
      "prompt": "realistic request",
      "should_trigger": true
    },
    {
      "id": 2,
      "prompt": "non-trigger case",
      "should_trigger": false
    }
  ]
}
```

### Required evaluation behavior

Test:

* with the skill
* without the skill

Compare:

* correctness
* efficiency
* failure modes

---

## Key documentation

| File                                    | Purpose                                      |
| --------------------------------------- | -------------------------------------------- |
| docs/agent-skills-creation-reference.md | Canonical skill design + specification guide |
| CONTRIBUTING.md                         | Contribution workflow                        |
| docs/SKILL-TEMPLATE.md                  | New skill template                           |
| docs/VALIDATION.md                      | Validation rules                             |
| docs/roadmap.md                         | Planned skills                               |

---

## Gotchas

* No `template/` directory exists. Copy an existing skill.
* `name:` must exactly match folder name.
* Weak descriptions prevent triggering.
* Do not publish `.github/skills/update-skill/`.
* Do not duplicate large guidance into `SKILL.md`; use references instead.