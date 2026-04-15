---
name: template-modeling-skill
description: Replace with a clear description of what this skill does and when the coding agent should use it. Include specific triggers (mentions of keywords, file types, or tasks) and expected outputs.
---

# Template Modeling Skill

## When to Use This Skill

Describe the problem this skill solves and the conditions under which the coding agent should activate it:

- You encounter [specific scenario]
- The user needs [specific deliverable]
- When working with [specific file types or data]

## Key Inputs

What information or files does this skill need?

- Model source code or configuration files
- Parameter descriptions
- Example data or metadata

## Step-by-Step Instructions

Provide clear, imperative instructions:

1. Read and understand the input
2. [Specific step with details]
3. [Another step]
4. Validate or verify the output

## ⚠️ Gotchas

Common failure modes and how to handle them:

- **Edge case 1:** If [condition], then [workaround]
- **Edge case 2:** This tool requires [specific dependency]; if missing, [fallback]

## Templates & Resources

Point to bundled resources:

- See `references/GUIDANCE.md` for detailed methodology
- Use `scripts/validate.py` to check your output
- See `assets/template.md` for the template structure

## Example

**Input:** [Concise example of what the user provides]

**Output:** [What the skill produces]

---

## Copy This Template

To create a new skill, copy this entire `SKILL.md` to your skill folder:

```bash
mkdir -p skills/your-skill-name
cp template/SKILL.md skills/your-skill-name/SKILL.md
# Then edit the content and add resources as needed
```

For full guidance, see [CONTRIBUTING.md](../CONTRIBUTING.md).
