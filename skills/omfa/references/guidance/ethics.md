# Ethics Guidance

## Purpose

Use this guidance when a model may influence policy, governance, public decisions, or other decisions with material consequences for populations that may disproportionately bear resulting risks, costs, exclusions, or benefits.

Also use it when normative assumptions materially shape model construction, interpretation, recommendation, or reuse.

---

## Core Principle

Ethics is a cross-cutting constraint on modeling decisions, not a separate lifecycle phase. Ethical modeling requires explicit, reviewable documentation of value judgments, intended use, limitations, responsibilities, and foreseeable consequences. Scientific validity alone is insufficient for socially consequential models.

---

## Decision Context

**Use this guidance when:**

- model outputs may influence decisions beyond scientific interpretation; [MUST]
- objectives, metrics, optimization criteria, or other analytical choices encode value judgments; [MUST]
- representational choices may affect how populations, places, behaviors, risks, benefits, or burdens are understood; [MUST]
- the model may be repurposed outside its original scope or decision context; [SHOULD]
- vulnerable or disproportionately affected populations may be affected by model use or interpretation. [MUST]

**Do not use this guidance when:**

- the primary question is whose knowledge and values are represented in the modeling process (use `participatory.md`);
- the primary question is decision-making across competing plausible futures (use `deep-uncertainty.md`);
- the primary question is epistemic uncertainty, sensitivity, or calibration ambiguity (use `uncertainty.md`);
- the primary question is scientific credibility or fit-for-purpose evidence (use `evaluation.md`);
- the primary question is metadata, licensing, packaging, reproducibility, or archival stewardship (use the `fair` skill; data or authority governance for affected populations routes back to this guidance).

This guidance addresses competing values, societal consequences, responsible interpretation, and the boundary between model-supported reasoning and value-laden decision authority.

---

## Consequential Analytical Choices <!-- [MUST] -->

(The categories below operationalize the draft code of ethics proposed by Anzola Pinzon, Barbrook-Johnson, & Gilbert (2022) without reproducing its structure.)

### Intended Use

Document whether the model is intended for scientific explanation, projection, policy support, operational decisions, public communication, deliberation, training, or exploratory learning. [MUST]

Identify decisions the model is not intended to support. [MUST]

### Value Assumptions

Document value assumptions embedded in objectives, objective functions, metrics, optimization criteria, rankings, thresholds, scenarios, welfare measures, or success definitions. [MUST]

Justify why those assumptions are appropriate for the stated decision context, or mark them as unresolved. [MUST]

### Representation

Document who and what is omitted, aggregated, simplified, anonymized, idealized, or treated as exogenous. [MUST]

Identify populations, places, behaviors, risks, benefits, or harms that may be hidden by aggregation or simplification. [MUST]

Document when proxy variables stand in for populations, behaviors, institutions, or social processes, and discuss the limitations of those proxies. [SHOULD]

Document representational asymmetries, where some actors, institutions, or processes are modeled in greater detail than others. [SHOULD]

### Decision Authority

Clarify which decisions remain human judgments and which decisions are only informed by model outputs. [MUST]

Do not present model outputs as policy recommendations unless the additional normative reasoning connecting evidence to recommendations is explicitly documented. [MUST]

### Communication Strategy

Separate model outputs, interpretation, recommendations, speculation, and policy preferences in all summaries and decision-support materials. [MUST]

State whether scenarios are exploratory, illustrative, stress tests, conditional projections, predictive scenarios, or recommendations. [MUST]

### Proportionality

Match model complexity, automation, and claimed authority to the importance of the decision and available evidence. [MUST]

Do not increase model complexity, automation, or claimed authority solely because it is technically feasible. [MUST]

### Misuse and Inappropriate Application

Identify foreseeable misuse, inappropriate transfer to new populations or contexts, and unsupported repurposing. [MUST]

Document constraints on reuse when the model depends on context-specific values, assumptions, data provenance, or decision authority. [SHOULD]

### Affected and Vulnerable Populations

Identify populations likely to bear disproportionate risks, costs, exclusions, or burdens from model use or interpretation. [MUST]

Document whether affected populations are represented directly, indirectly through proxies, aggregated into broader categories, or omitted. [MUST]

Consider data governance and authority over knowledge contributed by affected populations, including collective benefit, authority to control, responsibility, and accountability. [SHOULD]

---

## Method Selection <!-- optional -->

Select the lightest ethical review method that can make value-laden modeling decisions explicit and reviewable.

| Method | Best suited for | Advantages | Tradeoffs |
| --- | --- | --- | --- |
| Ethics self-assessment | Low-stakes models, early scoping, internal review | Fast, repeatable, easy to attach to a decision log | Can become superficial; weak for contested decisions or affected populations |
| Ethical impact assessment | Models intended to influence public, policy, governance, or operational decisions | Connects intended use, assumptions, affected groups, misuse, and interpretation limits | Requires more judgment and revision as the model evolves |
| Participatory ethical review | Models where affected stakeholders hold essential knowledge or contested values | Surfaces lived consequences, legitimacy concerns, and omitted values | Requires careful facilitation; does not replace modeling-team responsibility |
| Independent ethics review | High-stakes, legally sensitive, institutionally governed, or vulnerable-population contexts | Provides external scrutiny and documented accountability | May be slower; institutional review can miss modeling-specific assumptions |

Default to ethical impact assessment for models intended to influence public or policy decisions. [MUST]

Use participatory ethical review alongside `participatory.md` when affected populations or decision makers should review value-laden assumptions, consequences, or interpretation limits. [SHOULD]

Use independent ethics review when model use may materially affect vulnerable populations, allocate burdens or benefits, justify coercive action, or be treated as authoritative evidence in contested decisions. [MUST]

---

## Transparency <!-- [MUST] -->

Clearly distinguish:

- empirical evidence;
- inferred conclusions;
- normative assumptions;
- stakeholder values;
- expert judgment;
- policy preferences;
- ethical disagreements versus scientific disagreements; [MUST]
- unresolved ethical questions.

Document intended scope, ethical limitations, inappropriate uses, and responsibility boundaries. [MUST]

Flag normative recommendations that are not directly entailed by model evidence. [MUST]

Record unresolved value conflicts rather than translating them into technical disagreements. [MUST]

---

## Intermediate Artifacts

Generate or maintain, as appropriate:

- `ethics-impact-statement.md`
- `misuse-assessment.md`

Reuse shared artifacts where appropriate:

- `decision-log.md`
- `stakeholder-register.md`
- `assumptions.md`

Use predictable, semantic kebab-case filenames under `omf-artifacts/` at the project root. These artifacts should support downstream review, documentation, and responsible reuse. If `omf-artifacts/` is created during this work, also create `omf-artifacts/README.md` describing artifacts as living documents created early, revised throughout the project, and gated by explicit status/review triggers.

---

## Common Failure Patterns

Watch for:

- hidden value assumptions in objectives, thresholds, rankings, or optimization targets;
- optimizing measurable outcomes while ignoring unmeasured harms;
- policy objectives presented as scientific facts;
- unsupported normative recommendations attached to model outputs;
- affected populations omitted because they are absent from data or outside the model boundary;
- scenarios communicated as predictions;
- model outputs overstated as decision authority;
- scientific disagreement confused with value disagreement;
- model precision or sophistication treated as evidence of legitimacy;
- technical transparency treated as sufficient for ethical use;
- ethical review performed only after model results are known;
- model reuse treated as valid because the code runs in a new context.

---

## Routing

**Primary entry point**

Use this guidance whenever ethical consequences arise from modeling choices, intended use, interpretation, or reuse. Ethics is complementary to sibling guidance and may be loaded alongside them when value-laden consequences cut across multiple modeling decisions.

Combine with:

- `participatory.md` when the ethical question depends on whose knowledge, values, authority, or lived consequences are represented;
- `conceptual-modeling.md` when representational ethics affects boundaries, entities, proxy variables, or omitted processes;
- `deep-uncertainty.md` when competing futures or robust decision criteria encode contested values;
- `evaluation.md` when credibility claims may be interpreted as decision authority;
- `uncertainty.md` when uncharacterized or poorly communicated uncertainty changes ethical interpretation.

**Specialist execution skills**

Potential specialist skills include:

- ethical impact assessment;
- misuse-assessment review;
- stakeholder impact review;
- policy-interpretation review.

**Downstream consumer skills**

Outputs from this guidance should support `document`, `peer-review`, and `fair`, which should communicate ethical limitations, intended scope, reuse constraints, and responsibility boundaries.

---

## Primary References

### Foundational Concepts

- Szetey et al. (2025)
- Füchslin et al. (2023)

### Operational Guidance

- Saltelli et al. (2020a)
- Saltelli et al. (2022)
- Stilgoe et al. (2013)

### Applied Practice

- Anzola Pinzon, Barbrook-Johnson, & Gilbert (2022)
- Carroll et al. (2020)

See `references/REFERENCES.md` for complete citations.
