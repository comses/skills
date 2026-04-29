---
description: "Scaffold a new COMSES skill folder from the SKILL-TEMPLATE. Provide the skill name and a brief description of what it does."
argument-hint: "skill name + what it does (e.g. 'reproduce — verify a model run produces identical outputs')"
agent: agent
---

Scaffold a new COMSES skill using the template at [docs/SKILL-TEMPLATE.md](../../docs/SKILL-TEMPLATE.md).

The user's request: {{input}}

## Instructions

1. Parse the user's request to extract:
   - **Skill name** — must be `kebab-case`, ≤48 characters. Ask if unclear.
   - **One-sentence purpose** — what concrete task the skill performs.

2. Create the folder `skills/<skill-name>/` and write `skills/<skill-name>/SKILL.md` by:
   - Copying the full content of `docs/SKILL-TEMPLATE.md` verbatim as the starting point.
   - Replacing every `<placeholder>` with a value derived from the user's request. Use sensible defaults for optional metadata fields; leave them commented out if you cannot infer a good value.
   - Removing all HTML `<!-- ... -->` authoring-instruction comments (keep the pre-submission checklist comment at the bottom until the user is ready to submit).
   - Do **not** invent skill instructions — fill structural placeholders only. Leave step bodies as clear `<TODO>` stubs so the author knows what to write.

3. Create a minimal `skills/<skill-name>/evals.json`:
   ```json
   {
     "skill_name": "<skill-name>",
     "evals": [
       {
         "id": 1,
         "prompt": "<realistic should-trigger prompt>",
         "should_trigger": true,
         "expected_output": "<description of expected behavior>",
         "success_criteria": ["<criterion 1>", "<criterion 2>"]
       },
       {
         "id": 2,
         "prompt": "<second should-trigger prompt>",
         "should_trigger": true,
         "expected_output": "<description>",
         "success_criteria": ["<criterion>"]
       },
       {
         "id": 3,
         "prompt": "<third should-trigger prompt>",
         "should_trigger": true,
         "expected_output": "<description>",
         "success_criteria": ["<criterion>"]
       },
       {
         "id": 4,
         "prompt": "<tangentially related prompt that should NOT activate this skill>",
         "should_trigger": false,
         "expected_output": "Skill does not activate"
       },
       {
         "id": 5,
         "prompt": "<second should-not-trigger prompt>",
         "should_trigger": false,
         "expected_output": "Skill does not activate"
       },
       {
         "id": 6,
         "prompt": "<third should-not-trigger prompt>",
         "should_trigger": false,
         "expected_output": "Skill does not activate"
       }
     ]
   }
   ```
   Fill the `<placeholders>` with realistic prompts for the skill's domain.

4. Print a short summary:
   - Files created
   - What the author should fill in next (step bodies, gotchas, any references/ or assets/ to add)
   - Reminder to run the skill against the evals before submitting a PR

## Constraints

- Do not create `references/`, `assets/`, or `scripts/` subdirectories — the author adds those as needed.
- Do not write actual skill instructions. Scaffold structure only.
- `name:` in frontmatter must exactly match the folder name.
- See [AGENTS.md](../../AGENTS.md) for naming rules and authoring constraints.
