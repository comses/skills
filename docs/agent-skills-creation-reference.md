# Agent Skills: Unified Reference (Condensed)

## 0. Core model

* A **skill = folder + SKILL.md + optional resources** ([Agent Skills][1])
* Purpose: inject **domain-specific procedures + context** into an agent
* Loading uses **progressive disclosure**:

  1. name + description (discovery)
  2. full instructions (activation)
  3. referenced files (on demand) ([Agent Skills][1])

---

## 1. Skill design principles

### 1.1 Start from real expertise

* Derive from **actual tasks, failures, fixes, and workflows**
* Prefer:

  * runbooks, code reviews, incident logs
  * real I/O formats and constraints
* Avoid generic “best practices” summaries ([Agent Skills][2])

### 1.2 Extract reusable patterns

Capture:

* successful step sequences
* corrections you applied
* edge cases encountered
* concrete inputs/outputs ([Agent Skills][2])

---

## 2. Scope and structure

### 2.1 Coherent unit of work

* Like a function: **one composable responsibility**
* Too small → fragmentation
* Too large → bloated context

### 2.2 Progressive disclosure design

* Keep `SKILL.md` focused (< ~500 lines recommended) ([Agent Skills][3])
* Move detail into:

  * `references/` (docs)
  * `scripts/` (execution)
* Explicitly instruct when to load them

Example:

```
If API returns non-200 → read references/api-errors.md
```

---

## 3. SKILL.md structure (canonical)

### 3.1 Frontmatter (required + optional)

```yaml
name: short-identifier
description: when to use this skill (≤1024 chars)
compatibility: optional environment requirements
allowed-tools: optional allowlist
metadata:
  key: value
```

([Agent Skills][3])

### 3.2 Body (no strict schema, but recommended)

Include:

* step-by-step instructions
* input/output examples
* edge cases and failure handling ([Agent Skills][3])

---

## 4. Writing effective instructions

### 4.1 Add only what the agent lacks

* Include:

  * domain conventions
  * specific tools/APIs
  * non-obvious pitfalls
* Exclude:

  * general knowledge (HTTP, PDFs, etc.) ([Agent Skills][2])

### 4.2 Be concrete and opinionated

* Prefer:

  * “Use library X”
  * “Check condition Y”
* Avoid:

  * vague guidance
  * multiple equivalent options without default

### 4.3 Optimize for execution traces

If the agent:

* hesitates → instructions too vague
* tries many paths → missing defaults
* wastes steps → irrelevant instructions

Refine accordingly ([Agent Skills][2])

---

## 5. Description (activation-critical)

* Format: **imperative trigger**

  * “Use this skill when…”
* Focus on **user intent**, not implementation
* Include implicit cases (not just explicit keywords)
* Keep concise but specific ([Agent Skills][4])

---

## 6. Context efficiency

* Every token competes with:

  * conversation
  * system prompt
  * other skills
* Rule:

  > If the agent would succeed without it, remove it ([Agent Skills][2])

---

## 7. Scripts (optional)

Use `scripts/` when:

* commands are complex or error-prone

Guidelines:

* self-contained or declare dependencies
* deterministic outputs
* clear stdout/stderr for agent decisions
* prefer version-pinned tools ([Agent Skills][5])

---

## 8. References (optional)

Use `references/` for:

* large documentation
* schemas, formats, domain rules

Guidelines:

* small, focused files
* shallow linking (avoid deep chains)
* load only when needed ([Agent Skills][3])

---

## 9. Evaluation loop (required for quality)

### 9.1 Test structure

Each test:

* prompt (realistic)
* expected outcome
* optional files ([Agent Skills][6])

### 9.2 Method

Run:

* with skill
* without skill

Compare:

* correctness
* efficiency
* failure modes

### 9.3 Iterate

Refine based on:

* false positives
* missed cases
* unnecessary steps ([Agent Skills][2])

---

## 10. Trigger evaluation (description testing)

* Build ~20 queries:

  * should trigger
  * should not trigger
* Include:

  * vague phrasing
  * realistic context
  * near-miss negatives ([Agent Skills][4])

---

## 11. Directory layout (reference)

```
my-skill/
├── SKILL.md
├── scripts/        # executable logic
├── references/     # optional docs
├── assets/         # templates/data
└── evals/          # tests
```

([Agent Skills][1])

---

## 12. Heuristics checklist

**Good skill:**

* grounded in real workflows
* scoped to one task
* minimal but specific
* has clear trigger conditions
* tested against realistic prompts

**Bad skill:**

* generic advice
* redundant with base model ability
* overly verbose
* ambiguous activation
* untested

---

## 13. Design mantra

Encode *how experts actually do the task*, not how documentation describes it.

## References

[1]: https://agentskills.io/home "Agent Skills Overview - Agent Skills"
[2]: https://agentskills.io/skill-creation/best-practices "Best practices for skill creators - Agent Skills"
[3]: https://agentskills.io/specification "Specification - Agent Skills"
[4]: https://agentskills.io/skill-creation/optimizing-descriptions "Optimizing skill descriptions - Agent Skills"
[5]: https://agentskills.io/skill-creation/using-scripts "Using scripts in skills - Agent Skills"
[6]: https://agentskills.io/skill-creation/evaluating-skills "Evaluating skill output quality - Agent Skills"
