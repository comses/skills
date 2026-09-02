# Evaluation Report (Guidance Template)

This report synthesizes the evidence supporting evaluation of the model. It documents how well the model is supported for its intended purpose.

This report is a **living artifact**. Create it early and update it as verification, calibration, validation, uncertainty analyses, or model revisions produce new evidence. Summarize evaluation results and trace them to supporting artifacts here; do not duplicate detailed methods, tables, or logs that belong in dedicated result artifacts such as `verification-report.md`, `calibration-report.md`, or `validation-report.md`, and do not duplicate planning details that belong in artifacts such as `uncertainty-register.md` or `sensitivity-analysis-plan.md`, or detailed sensitivity results that belong in `sensitivity-analysis-report.md`. For evaluation methodology guidance, see `references/guidance/evaluation.md`.

---

## Evaluation Context

**Goal:** Define the purpose and claims against which the model is evaluated. You cannot assess credibility without a defined purpose.

**Questions to Consider:**
1. What is the model's intended purpose and the specific claims it is meant to support?
2. What does "adequate" or "credible enough" look like for this purpose? (Success criteria or metrics.)
3. Which evaluation activities were conducted, and why were they appropriate for this purpose?
4. Where are the detailed evaluation plans, criteria, and methods documented?

**Example:**
- **Claim:** "The model can predict the spatial extent of the fire within 10% error."
- **Metric:** Intersection-over-Union (IoU) > 0.8 compared to historical satellite imagery.
- **Activities:** Mass-balance verification, calibration against 2010–2014 events, hold-out validation against the 2015 wildfire event.

---

## Scope of Evaluation

**Goal:** Make explicit what has and has not been evaluated. Evaluation establishes credibility only within the evaluated scope.

**Questions to Consider:**
1. Which behaviors, outputs, or conditions were directly evaluated?
2. Which behaviors, outputs, or conditions were not evaluated, and why?
3. Which conclusions are supported by the evaluated evidence?
4. Which conclusions, extrapolations, or use cases remain unsupported?
5. What boundaries limit the credibility this evaluation can establish?

**Example:**
- **Evaluated:** Fire extent and direction under moderate wind conditions for historical events.
- **Unevaluated:** Fire rate of spread in extreme-wind scenarios and real-time evacuation routing.
- **Supported:** The model is useful for comparing suppression strategies under historical weather regimes.
- **Unsupported:** Operational emergency evacuation decisions.

---

## Evaluation Evidence

**Goal:** Summarize the evidence produced by each major evaluation activity and trace it to supporting artifacts.

For each activity below, answer:
- **What was evaluated?**
- **Why was this evaluation appropriate for the intended purpose?**
- **Which research questions or model claims does this evidence support?**
- **Where are the supporting analyses documented?**
- **Which evaluation criteria in `evaluation-plan.md` does this evidence address?**

### Verification
- What was checked to ensure the implementation matches the conceptual model or specification?
- Example: total agent count remains constant across all time-steps (mass balance).

### Calibration
- What data or patterns were used to fit parameters?
- How was overfitting or equifinality addressed?

### Validation
- Which independent observations or patterns were used to assess predictive or explanatory adequacy?
- How do validation results relate to the stated success criteria?

### Robustness or Uncertainty Evidence
- Which sensitivity, scenario, or robustness analyses were considered?
- How do they influence the supported claims and their limitations?

**Example:**
- **Verification:** Confirmed constant agent count across all time-steps.
- **Validation:** Tested against the 2015 wildfire event (hold-out); achieved IoU of 0.82.
- **Documentation:** `omf-artifacts/verification-report.md`, `omf-artifacts/validation-report.md`.

---

## Credibility & Evidence Synthesis

**Goal:** Integrate the evidence into an assessment of model credibility, without relying on predefined maturity tiers.

**Questions to Consider:**
1. What are the main strengths of the evaluation evidence?
2. What are the key weaknesses, blind spots, or limitations?
3. Which evidence is empirical, which rests on theoretical expectations, and which rests on expert judgment?
4. How does the available evidence support (or fail to support) the model's intended claims?
5. What additional evidence would most improve confidence for the intended purpose?

**Example:**
- **Strengths:** The model consistently reproduces historical fire direction and extent under moderate winds.
- **Weaknesses:** Performance degrades in high-wind scenarios; fuel moisture is poorly constrained by observations.
- **Evidence mix:** IoU scores are empirical; the representation of fuel moisture effects relies on expert judgment and limited field data.
- **Conclusion:** The model supports comparative analysis of suppression strategies but not high-wind forecasting.

---

## How Uncertainty Informed the Evaluation

**Goal:** Summarize the role of uncertainty in shaping the evaluation and its conclusions.

**Questions to Consider:**
1. Which uncertainty analyses informed this evaluation? (e.g., sensitivity analysis, scenario exploration, calibration ambiguity assessment.)
2. Which uncertainty sources are most relevant to the model's credibility?
3. How were uncertainty and robustness findings integrated into the evaluation conclusions?
4. Where are the supporting uncertainty artifacts and reports documented? (e.g., `omf-artifacts/uncertainty-register.md`, `omf-artifacts/sensitivity-analysis-report.md`.)

**Example:**
- **Uncertainty source:** Fuel moisture strongly affects fire area.
- **Informing analysis:** Sensitivity analysis showed that a 10% increase in `fuel_moisture` reduces predicted fire area by 40%.
- **Implication:** Moisture data quality is a critical credibility constraint; conclusions should be accompanied by explicit moisture assumptions.
- **Documentation:** `omf-artifacts/uncertainty-register.md`, `omf-artifacts/sensitivity-analysis-report.md`.

---

## Fitness for Purpose

**Goal:** Communicate the conditions under which the model can be relied upon, without making a binary pass/fail recommendation.

**Questions to Consider:**
1. Which intended uses are supported by the available evidence?
2. Under what assumptions, constraints, or conditions?
3. Which intended uses remain unsupported?
4. What limitations should users consider before relying on model results?
5. What changes would trigger a re-evaluation?

**Example:**
"The model supports comparing long-term suppression strategies under historical weather regimes, provided users acknowledge its sensitivity to fuel moisture and do not use it for real-time forecasts or extreme-wind scenarios. A re-evaluation is needed if fuel-moisture data sources or the fire-weather scenario set change substantially."

---

**Reference:**
- `references/guidance/evaluation.md`
