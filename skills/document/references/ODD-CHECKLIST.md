# ODD Checklist

This repository uses a compact 23-point review checklist synthesized from Grimm et al. (2020), "The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism".

This is practical guidance, not a verbatim reproduction of the article's supplementary materials. Use it to review whether an ODD is complete enough for replication and critical reading.

## How To Use This Checklist

- Mark each item as `Yes`, `Partial`, `No`, or `Not applicable`.
- Treat `Partial` as a revision target, not as a pass.
- If a design concept is not used by the model, explicitly say so instead of leaving the section blank.
- Prefer checking the written ODD against the code to confirm naming, process order, and parameter use.

## 23 Review Items

### 1. Purpose and patterns

1. The ODD states the model's specific purpose, question, or hypothesis clearly enough that a reader can judge whether the model is fit for that purpose.
2. The ODD identifies the empirical or theoretical patterns used to evaluate whether the model is realistic or useful enough for its stated purpose.
3. The ODD makes the model purpose operational by clarifying what the model is intended to explain, predict, demonstrate, compare, or explore.

### 2. Entities, state variables, and scales

4. All entity types are identified, including agents, environmental entities, spatial units, schedulers, and any global containers that matter to model behavior.
5. Each entity type has its state variables described with meaning, units or categories where relevant, and enough detail to distinguish state variables from fixed parameters.
6. Spatial and temporal scales are specified, including resolution, extent, time step, and any important boundary or coordination assumptions.

### 3. Process overview and scheduling

7. The ODD gives a readable overview of the main processes before diving into submodel detail.
8. The schedule explains who acts, when they act, in what order, and whether updating is synchronous, asynchronous, staged, or event-driven.
9. The ODD specifies when observations, stopping conditions, and major outputs are produced.

### 4. Design concepts

10. Basic principles: the conceptual basis, theory, or domain logic behind the model is stated.
11. Emergence: the ODD explains which system-level patterns or outcomes emerge from lower-level processes.
12. Adaptation: the ODD explains whether agents adapt or adjust behavior in response to circumstances, and how.
13. Objectives: the ODD states whether agents pursue explicit objectives, utilities, heuristics, or no explicit objective at all.
14. Learning: the ODD explains whether agents change internal rules, parameters, or expectations over time.
15. Prediction: the ODD explains whether agents anticipate future states, consequences, or payoffs when acting.
16. Sensing: the ODD states what information agents can detect, access, or infer from their environment or other agents.
17. Interaction: the ODD explains direct and indirect interactions among agents and between agents and environment.
18. Stochasticity: the ODD identifies where randomness enters the model, including random draws, distributions, and any seed or replication policy.
19. Collectives: the ODD explains whether groups, institutions, herds, households, or other collectives exist and how they behave.
20. Observation: the ODD explains what outputs, indicators, or diagnostics are recorded and how they relate to the model purpose and patterns.

### 5. Details

21. Initialization describes the starting state completely enough to recreate initial agents, environment, parameter values, random seeds, and any scenario-specific setup.
22. Input data describes all external drivers or datasets, including what they are, when they enter the model, and how they affect state or process execution.
23. Submodels describe the algorithms, equations, thresholds, parameter use, stochastic components, and key implementation details needed to reproduce each process.

## Strong-Practice Additions

The 23 items above are the minimum review backbone. Grimm et al. (2020) also recommends the following practices whenever they improve clarity or reuse:

- Add an optional `Rationale` subsection under each ODD element to explain why a design choice was made.
- Describe what the program does, not just the modeler's verbal story about the system.
- Use the same names in the ODD and in code where possible.
- Add code pointers for important submodels, equations, or algorithms when ambiguity remains.
- Report important target patterns the model failed to reproduce, not only the ones it matched.
- For large models, write a full ODD first and then create a shorter summary ODD for publication text.
- For very complex models, use nested ODDs for large submodels.
- For reused or modified models, consider a delta-ODD only when the original ODD is easily accessible; otherwise prepare a new complete ODD and clearly attribute reused text.

## Common Failure Modes

- Purpose is too vague, for example only saying the model is used to "explore" or "investigate".
- Patterns are missing, so there is no explicit fit-for-purpose criterion.
- Parameters are mixed up with state variables.
- The overview section includes detail that belongs in submodels, but the process schedule remains unclear.
- Design concepts are left implicit instead of being addressed directly.
- Initialization omits randomization, scenario setup, or boundary conditions.
- Stochasticity appears in code but is not documented in the ODD.
- The ODD narrates intended mechanisms while the code implements different logic.

## Source

- Grimm, V. et al. (2020). The ODD Protocol for Describing Agent-Based and Other Simulation Models: A Second Update to Improve Clarity, Replication, and Structural Realism. JASSS 23(2):7. https://jasss.soc.surrey.ac.uk/23/2/7.html