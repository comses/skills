# Agent Skills Creation Reference

This document defines the design standard for Agent Skills within the OMF repository.

---

## Part 1: Agent Skills Fundamentals

### The Core Model

A skill is a self-contained unit of domain-specific procedure.

- **Structure**: `folder` $\rightarrow$ `SKILL.md` (instructions) + optional `references/` (knowledge), `scripts/` (logic), and `assets/` (templates).
- **Loading**: Progressive disclosure. Discovery (name/description) $\rightarrow$ Activation (`SKILL.md`) $\rightarrow$ On-demand (resources).

### Description & Activation

Optimize for user intent, not keywords.

- **Goal-Oriented**: Describe what the user is trying to accomplish and the expected outcome.
- **Concise**: Keep activation text specific but brief.
- **Example**: Prefer _"Use when a user wants to document a computational model"_ over _"Triggers: document model, generate ODD."_

### Output Contracts

Every skill must define a predictable contract:

- **Inputs/Outputs**: Clear requirements and expected deliverables.
- **Success/Failure**: Explicit criteria for a "complete" task and conditions that trigger failure.
- **Structure**: Use structured outputs (JSON/YAML) when the result is consumed by downstream skills.

### Artifact Authority

Artifact ownership defines methodological authority, not exclusive write access. The owning skill defines an artifact's purpose, structure, invariants, and acceptance criteria and resolves conflicting changes. A contributing skill may modify only the fields or sections named in the artifact contract. A consuming skill may read and reference the artifact but does not modify it.

Every shared artifact contract should identify:

- the owning skill;
- permitted contributors and the scope of their changes;
- protected decisions contributors must not reinterpret;
- the conditions that require routing a proposed change to the owner.

Any skill may flag contradictory or stale content. It should not silently correct content outside its contribution scope. Explicit user direction may authorize an exceptional change, but the agent should preserve provenance and report the contract exception.

Use `docs/artifact-contracts.md` as the repository-wide registry. Keep the operational subset needed by an independently installed skill in that skill's `SKILL.md`.

### Evaluation

Quality is verified through comparative testing:

- **A/B Testing**: Run identical realistic prompts with and without the skill.
- **Metrics**: Compare correctness, efficiency (steps taken), and failure modes.
- **Concrete Triggers**: Test with realistic user phrasing, including "near-miss" cases that should NOT trigger the skill.

---

## Part 2: OMF Design Philosophy

### The Golden Rule: Add Only What the Agent Lacks

Do not waste context on generic knowledge.

- **Encode**: Expert workflows, community standards, non-obvious pitfalls, and methodological tradeoffs.
- **Exclude**: General software engineering or common modeling advice that foundation models already handle reliably.
- **Mantra**: If the agent would succeed without it, remove it.

### Externalize Consequential Reasoning

Transparency is a requirement, not an option. Skills must prevent "silent" scientific decisions.

- **Provenance**: Surface all consequential analytical choices (method selection, assumptions, priors).
- **Justification**: Require the agent to explain _why_ a specific path was taken based on encoded standards.
- **Intermediate Artifacts**: Emit staging artifacts (e.g., inferred assumptions list) for user review before finalization.

### Composability & Scope Discipline

Prefer many small, specialized skills over few comprehensive ones.

- **One Responsibility**: Each skill owns a single methodological step.
- **Predictability**: Minimal hidden state; clear input $\rightarrow$ clear output.
- **Routing over Expansion**: Favor routing over expanding a skill's scope. If a concern belongs to another skill, route the user to it instead of duplicating guidance.

### Architectural Rule: Favor Routing

Do not build "God-skills." When a workflow spans multiple domains:

1. Identify the specialist skill for the sub-task.
2. Instruct the current skill to delegate or route to that specialist.
3. Maintain a clean boundary between orchestration and execution.

---

## Design Mantra

**Encode how experienced practitioners make, justify, document, and communicate consequential decisions while minimizing context cost.**
