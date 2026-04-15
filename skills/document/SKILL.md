---
name: document
description: |
  Generate and validate ODD+2 (Overview, Design Concepts, Details) documentation for agent-based models.
  
  Use this skill whenever you have model code and need to create publication-ready ODD+2 narrative 
  documentation, validate existing ODD against the 23-point checklist, or guide iterative improvement 
  of model documentation. Triggers: "document my ABM", "generate ODD", "write model narrative", 
  "publish my model", "create ODD for my code".
  
  Expected output: Markdown ODD+2 sections covering entities, state variables, processes, 
  validation checklist feedback, and completion report.
license: MIT
compatibility: Python 3.8+, can work with Python/R/C++ models
metadata:
  domain: computational-modeling
  maturity: beta
  audience: modelers, researchers
  category: documentation
---

# ODD Protocol Narrative Skill

## When to Use This Skill

Use this skill when:

- You have an agent-based model (or complex computational model) and need to create publication-ready narrative documentation
- You are preparing a paper and need to follow the Grimm et al. ODD+2 (Overview, Design Concepts, Details) protocol
- You want to validate your existing ODD documentation against the 23-point ODD+2 checklist
- You need to ensure all critical model components (entities, state variables, processes, parameters) are documented

## Key Inputs

This skill works best with:

- **Model source code** (Python, R, C++, Java, or pseudocode)
- **Model docstrings** or parameter descriptions
- **High-level model overview** (what the model represents, research questions it addresses)
- **Optional:** Existing ODD draft or README file to improve iteratively

## Step-by-Step Instructions

### 1. Gather Model Information

Before generating ODD, extract or prepare:

- List of **entities** (Agent types, Environment components, Observer/Scheduler)
- State variables for each entity (attribute names, types, initialization ranges)
- **Processes** and their order (update rules, initialization, random draws)
- **Parameters** (variable inputs and fixed constants)
- **Stochasticity** (random number generators, seeds, distributions)
- **Input data** (external files, specifications)
- **Observations** (what outputs/statistics the model tracks)

### 2. Generate ODD Sections

1. **Overview:** Model purpose, entities, state variables, and main processes (auto-generated from code analysis)
2. **Design Concepts:** Model philosophy and assumptions (requires your input on key hypotheses)
3. **Details section (Entities):** Structured table of entities and their state variables
4. **Details section (Processes):** Pseudocode or flow description for each update rule
5. **Input/Output:** Data files and observation outputs
6. **Initialization & Parameterization:** Default and variable parameters

### 3. Validate Against Checklist

Use the ODD+2 validation checklist (see `references/ODD-CHECKLIST.md`):

- Does the Overview include purpose, entities, variables, processes?
- Are all entities described with all state variables?
- Is stochasticity explicitly documented?
- Are all parameters listed (variable and fixed)?
- Is the time step defined?
- Is initialization logic clear?

### 4. Iterate on Feedback

The skill will provide:

- Completeness score (how many of 23 checklist items are covered)
- Missing sections or state variables that should be added
- Suggestions for clarity or additional detail

Revise model documentation or code comments as needed, then re-run validation.

## ⚠️ Gotchas

- **Stochastic models:** Always document random seed initialization and distributions used. If your model is inherently random, note which outputs should be averaged over replicate runs.
- **Implicit initialization:** If parameters are hardcoded in the model, extract them explicitly. This skill works best when parameters are clearly separated from logic.
- **State variable naming:** Use descriptive names (e.g., `energy`, `x_position`) not cryptic abbreviations. This makes ODD much clearer.
- **Missing docstrings:** If your model code lacks docstrings, provide a README or brief description of entities and processes in plain text first.
- **Large models:** For complex models with many entities/processes, summarize into subsystems or agent hierarchies first. Don't expect the skill to invent abstractions.

## Templates & Resources

- **ODD+2 Checklist:** See `references/ODD-CHECKLIST.md` for the 23 items that must be covered
- **ODD Template:** See `assets/ODD-TEMPLATE.md` for narrative structure and example sections
- **Example ODD:** See `examples/minimal-abm-odd.md` for a complete minimal example
- **Validation script:** Use `scripts/validate_odd.py` to check your ODD against the checklist
- **ODD assistant:** See `https://github.com/comses/odder` for a set of agent skills that can guide you through ODD generation interactively

## Example

**Input:** Python ABM with Agent and Environment classes:
```python
class Agent:
    def __init__(self, energy):
        self.energy = energy
        self.x = random.randint(0, 100)
    def step(self):
        self.energy -= 1
        if self.energy > 10:
            self.reproduce()

class Environment:
    def __init__(self, n_agents=10):
        self.agents = [Agent(energy=50) for _ in range(n_agents)]
    def step(self):
        for agent in self.agents:
            agent.step()
```

**Output:** ODD narrative sections:
```markdown
## Entities
- **Agent:** Individual organisms in the simulation
  - energy (integer, 0-100): Current energy reserve
  - x (integer, 0-100): Position in environment
  - age (integer, ≥0): Time steps alive

- **Environment:** The spatial grid and resource pool
  - grid_size (integer): 100 × 100 positions
  - resources (float): Replenishment rate per step

## Processes
1. **Agent move (every step):** Random walk with energy cost
   - If energy > 10, move with 50% probability in random direction
   - Energy cost: 1 unit per step
2. **Agent reproduction (every step):** If energy > threshold
   - Probability: energy / 100
   - Offspring initialized at parent location with half parent energy
3. **Environment step (every step):** Resource regeneration
```

---

## Quick Reference

| Task | Command/Reference |
|------|---|
| View full ODD checklist | See `references/ODD-CHECKLIST.md` |
| Validate your draft | `python scripts/validate_odd.py my_odd.md` |
| See a minimal example | See `examples/minimal-abm-odd.md` |
| Read methodology | See `references/ODD-METHODOLOGY.md` |

---

For community feedback or issues, see the [COMSES Skills](https://github.com/comses-network/skills) repository.
