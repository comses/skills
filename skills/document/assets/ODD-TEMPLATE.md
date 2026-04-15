# ODD Template

Use this template to draft a full ODD aligned with the second major update described by Grimm et al. (2020). Replace all prompts with model-specific content.

Do not treat this as a rigid form. If a design concept does not apply, say so briefly. If the model is complex, keep the full ODD detailed and derive a shorter summary ODD separately.

---

# [Model title]

## 1. Purpose and patterns

### Purpose

- What specific question, hypothesis, decision, or comparison is the model for?
- Is the model intended for explanation, prediction, demonstration, scenario comparison, design support, or another purpose?
- What would count as success or failure for this model?

### Patterns

Describe the empirical or theoretical patterns used to assess whether the model is realistic or useful enough for its purpose.

| Pattern | Scale | Source | Role in model design or evaluation |
| --- | --- | --- | --- |
| [Pattern name] | [individual/system/spatial/temporal] | [citation or dataset] | [selection, calibration, evaluation, comparison] |

### Rationale (optional)

Explain why this purpose was chosen and why these patterns are the right fit-for-purpose criteria.

## 2. Entities, state variables, and scales

### Entities and state variables

List every entity type that matters to model execution.

| Entity type | Description | Key state variables | Notes |
| --- | --- | --- | --- |
| [Agent type] | [What it represents] | [variable, meaning, units/range] | [constraints or remarks] |
| [Environment or spatial unit] | [What it represents] | [variable, meaning, units/range] | [constraints or remarks] |

State variables should be variables that differ among entities of the same type or change over time. Do not confuse them with fixed parameters.

### Scales

- Time step: [e.g. 1 day]
- Simulation horizon: [e.g. 365 steps]
- Spatial resolution: [e.g. 100 m cells]
- Spatial extent: [e.g. one watershed / one city]
- Boundary conditions: [e.g. torus, fixed edge, absorbing boundary]

### Rationale (optional)

Explain why these entities, variables, and scales were selected.

## 3. Process overview and scheduling

### Process overview

Summarize the main processes at a high level before giving full submodel detail.

1. [Process name]: [brief description]
2. [Process name]: [brief description]
3. [Process name]: [brief description]

### Scheduling

| Step / phase | Acting entities | Trigger | Order / update mode | Outputs or state changes |
| --- | --- | --- | --- | --- |
| [Phase 1] | [who acts] | [every tick / event / condition] | [sync / async / random order / fixed order] | [what changes] |

Clarify when the model starts, when it stops, and when outputs are recorded.

### Rationale (optional)

Explain why the chosen schedule and update order are appropriate.

## 4. Design concepts

### Basic principles

What theories, mechanisms, or domain principles does the model rely on?

### Emergence

Which system-level outcomes are expected to emerge from lower-level processes?

### Adaptation

How do agents alter behavior in response to conditions?

### Objectives

Do agents optimize, satisfice, follow heuristics, imitate, or have no explicit objective?

### Learning

Do agents update rules, beliefs, memories, or parameters over time?

### Prediction

Do agents anticipate future conditions or consequences before acting?

### Sensing

What information can agents perceive, observe, or infer?

### Interaction

How do agents interact with one another and with the environment?

### Stochasticity

Where does randomness enter the model? Include distributions, draws, and replication or seeding policy.

### Collectives

Are there persistent groups, households, organizations, flocks, or other collectives?

### Observation

What outputs are measured, logged, aggregated, or compared with observed patterns?

### Rationale (optional)

Explain the main design choices behind the concepts above, especially where alternatives were considered.

## 5. Initialization

Describe the initial state completely enough that another modeler could recreate it.

- Initial number of entities: [value or rule]
- Initial spatial arrangement: [rule or dataset]
- Initial state variables: [values, ranges, or distributions]
- Parameter settings used in baseline runs: [table or citation]
- Random seed policy: [fixed seed, varying seeds, seed archive]
- Burn-in or warm-up: [if any]

### Rationale (optional)

Explain why these initial conditions were chosen.

## 6. Input data

Describe any external data used while the model runs.

| Input dataset or driver | When used | Variables used | Preprocessing | Effect on model |
| --- | --- | --- | --- | --- |
| [Dataset or scenario input] | [initialization / each step / event-driven] | [fields] | [cleaning, interpolation, aggregation] | [how it changes the run] |

If there is no runtime input data, say so explicitly.

### Rationale (optional)

Explain why these inputs are needed and why they are used in this way.

## 7. Submodels

Repeat the following block for each important submodel.

### 7.x [Submodel name]

#### Purpose

What this submodel does and where it sits in the schedule.

#### Logic

Describe the algorithm in clear prose, pseudocode, equations, or both.

```text
[Pseudocode or equation block]
```

#### Inputs and parameters

| Name | Type | Meaning | Units / range | Source |
| --- | --- | --- | --- | --- |
| [name] | [parameter/state/input] | [meaning] | [units/range] | [citation or code source] |

#### Stochastic elements

Describe any random draws used by this submodel.

#### Outputs or state changes

Explain what this submodel updates.

#### Code reference (recommended)

- File or module: [path]
- Procedure or function: [name]
- Notes: [line numbers, equation IDs, or comments if available]

#### Rationale (optional)

Explain why this submodel was implemented this way instead of alternatives.

---

## Completion Check

Before treating the ODD as finished, review it against:

- `references/ODD-CHECKLIST.md`
- `references/ODD-METHODOLOGY.md`

## Source

- Grimm, V. et al. (2020). The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism. JASSS 23(2):7. https://jasss.soc.surrey.ac.uk/23/2/7.html