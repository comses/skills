# ODD Methodology

This note summarizes how to apply the updated ODD guidance from Grimm et al. (2020) in a practical documentation workflow.

## What Changed In The Second Update

The 2020 update kept the core seven-element ODD structure but clarified how to use it for replication, evaluation, and reuse.

Key changes and emphases:

- The first element is now `Purpose and patterns`, not only purpose. Patterns should state how the model will be judged fit for purpose.
- Each ODD element can include an optional `Rationale` subsection to explain why a design choice was made.
- Guidance materials were expanded to reduce ambiguity around state variables, design concepts, and writing style.
- Summary ODDs are recommended for article main text, but only after a full ODD exists.
- Nested ODDs are recommended for highly complex models with large submodels.
- Reused or modified models can be documented with delta-ODDs when the original ODD is easily accessible.
- Explicit links between ODD sections and code are encouraged to reduce ambiguity.
- ODD is framed as useful beyond ABMs, including hybrid and other simulation models.

## Core Writing Principle

Describe what the program does, not only the modeler's mental story about the system.

That means:

- Document the actual implemented entities, variables, ordering, thresholds, and algorithms.
- Separate fixed parameters from state variables that vary across entities or time.
- Prefer concrete operational detail over vague narrative.
- Use equations, pseudocode, and tables whenever they improve precision.

## Recommended Workflow

### 1. Start from purpose and fit-for-purpose criteria

Write the model purpose as a concrete question, hypothesis, or decision problem. Then identify the patterns that will be used to design, calibrate, compare, or evaluate the model.

Good practice:

- Name the kind of model purpose, for example explanation, prediction, demonstration, or scenario comparison.
- State the patterns early because they influence what entities, scales, and processes belong in the model.
- Report important target patterns the model fails to reproduce when relevant.

### 2. Inventory the implemented model structure

Extract the program structure before writing prose.

Capture:

- Entity types
- State variables by entity type
- Parameters and constants
- Spatial and temporal scales
- Main processes and update order
- Outputs and observations
- Input data and external drivers
- Stochastic elements

This step prevents a common failure mode where the ODD follows the author's conceptual story instead of the actual code.

### 3. Draft the overview before the details

Write the first three ODD elements in this order:

1. Purpose and patterns
2. Entities, state variables, and scales
3. Process overview and scheduling

These sections should let a reader understand the model at a glance before reading detailed submodels.

### 4. Address all eleven design concepts explicitly

The updated ODD continues to use these design concepts:

- Basic principles
- Emergence
- Adaptation
- Objectives
- Learning
- Prediction
- Sensing
- Interaction
- Stochasticity
- Collectives
- Observation

If a concept does not apply, say so briefly. Leaving it implicit forces readers to guess.

### 5. Finish the detailed sections for reproducibility

The last three elements are where reproducibility lives:

- Initialization
- Input data
- Submodels

Submodels should contain the logic required for reimplementation: equations, pseudocode, decision rules, thresholds, parameter roles, and stochastic behavior.

### 6. Add rationale where it improves trust or reuse

Rationale is optional but strongly recommended when design choices are non-obvious.

Useful rationale includes:

- Why a particular scale was chosen
- Why an agent behavior rule was selected over alternatives
- Why a parameterization or dataset was used
- Why an omitted process was excluded

If rationale becomes long, place the core explanation in the ODD and move extended design-history material to TRACE or supplementary material.

### 7. Link the ODD to code

The update recommends reducing ambiguity by helping readers find the relevant implementation.

Practical approaches:

- Use the same names in code and ODD for entities, variables, and submodels.
- Add a code reference under important submodels.
- Identify the file, class, procedure, or function that implements the described logic.
- Record software version, important library versions, and execution environment when they affect interpretation.

### 8. Produce a summary ODD only after the full ODD exists

The summary ODD is for the main text of a paper or report. It should:

- Preserve the overall narrative of the model
- Use ODD keywords so readers can map back to the full ODD
- Move long state-variable lists and tables out of the prose where needed
- Mention only the most important design concepts and submodels in detail

The full ODD remains the authoritative reference.

## Special Cases

### Highly complex models

Use nested ODDs when one or more submodels are large enough to need their own structured description. Keep the main ODD focused on the whole model, and use reduced ODD-style documentation for major submodels.

### Reused or modified models

If the model extends an earlier model:

- Use a delta-ODD only when the earlier full ODD is publicly accessible and easy to consult.
- Otherwise produce a complete new ODD.
- If text is reused from an earlier ODD, provide attribution and ensure the license allows reuse.

### Models outside classic ABM

ODD can also describe hybrid or non-agent-based simulation models. The design concepts may need to be used more selectively, but the seven-element structure still provides a useful standard description.

## What ODD Does Not Cover By Itself

ODD describes the model as the virtual laboratory. It does not fully replace documentation for simulation experiments, calibration, validation, uncertainty analysis, or broader model-development traceability.

Use separate material for:

- Simulation experiment design
- Calibration and sensitivity analysis
- Validation and evaluation workflow
- Provenance of design choices

The 2020 update points to TRACE as the companion standard for documenting iterative model development, testing, and application.

## Review Heuristics

Use these questions when checking a draft:

- Could another modeler reimplement the core logic without asking the author clarifying questions?
- Are the patterns explicit enough to show how the model is fit for purpose?
- Can a reader tell the difference between state variables, parameters, and inputs?
- Is the schedule specific enough to reproduce update order?
- Are stochastic elements documented wherever they occur?
- Does the ODD describe the implemented model rather than an aspirational narrative?
- Could a reader find the relevant code for each important submodel?

## Recommended Companion Files In This Skill

- `assets/ODD-TEMPLATE.md`: drafting scaffold for a full ODD
- `references/ODD-CHECKLIST.md`: compact 23-point review sheet

## Source

- Grimm, V. et al. (2020). The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism. JASSS 23(2):7. https://jasss.soc.surrey.ac.uk/23/2/7.html