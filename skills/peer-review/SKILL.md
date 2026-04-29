---
name: peer-review
description: |
  Evaluate computational model submissions for CoMSES-style peer review readiness using
  reproducibility, documentation, code quality, and research software engineering criteria.

  Use this skill whenever a user asks to review a computational model, codebase, model release,
  or submission package for publication, reuse, or peer review. Trigger on phrases like:
  "peer review my model", "is this model submission ready", "review codebase quality",
  "check reproducibility", "review ODD documentation", "assess FAIR/research software quality".

  Expected output: structured peer review report with binary pass/fail recommendation,
  criterion-by-criterion findings, prioritized fixes, and an evidence-based checklist mapped to CoMSES review criteria and
  key EVERSE research software quality indicators.
license: MIT
compatibility: Works with Python, R, NetLogo, Julia, C/C++, and mixed-language model repositories
metadata:
  domain: computational-modeling
  maturity: alpha
  audience: modelers, reviewers, researchers
  category: quality-assurance
---

# Computational Model Peer Review Skill

## When to Use This Skill

Use this skill when:

- A model author wants a pre-submission quality review before requesting formal peer review
- A reviewer needs a consistent rubric to assess model execution, documentation, and code quality
- A team wants to identify blockers to frictionless reuse of a model by third parties
- A repository needs a structured research software engineering quality assessment

Do not use this skill to judge scientific novelty, theoretical validity, or whether conclusions are correct.
Focus on software and documentation quality for reproducibility and reuse.

## Key Inputs

Gather as many of these as available:

- Source code and repository structure
- Run instructions and dependency specifications
- Narrative model documentation (ODD or equivalent)
- Example input data and expected outputs
- Release metadata (license, citation, version, archive links)
- Tests, CI configuration, and issue tracker information

## Review Workflow

### Required Scoring Rule

Apply these rules before synthesizing any final decision:

- The three CoMSES criteria are equally weighted and each is required:
  - Ease of Execution
  - Documentation Thoroughness
  - Code Quality
- Final decision is binary:
  - **Pass:** all three CoMSES criteria are rated Pass
  - **Fail:** any one of the three CoMSES criteria is rated Partial or Fail
- Research software quality indicators support evidence and prioritization, but do not override required-criteria failures.

### 1. Scope and Submission Triage

1. Identify target artifact:
   - Repository only
   - Repository plus release package
   - Repository plus manuscript supplement
2. Confirm review scope:
   - Baseline CoMSES peer review readiness
   - Expanded RSE quality assessment
3. Record missing essentials up front (for example missing run instructions, missing docs, private dependencies).

Decision point:
- If core inputs are missing, continue with a constrained review and label all affected checks as not assessable.

Use `references/PEER-REVIEW-CHECKLIST.md` as the default rubric and evidence tracker throughout the review.

### 2. Evaluate Ease of Execution

Assess whether a third party can run the model with reasonable effort:

- Dependencies are identified and installable
- Environment setup is documented
- Input data dependencies are explicit
- Run commands are clear and complete
- Output artifacts can be generated without undocumented steps

Rate:
- Pass: runnable with minor effort
- Partial: runnable but requires interpretation or manual fixes
- Fail: cannot run from provided materials

### 3. Evaluate Documentation Thoroughness

Assess narrative documentation quality:

- Includes a standalone narrative document (not only inline comments)
- Uses ODD protocol or an equivalent model documentation framework
- Explains model purpose, entities, processes, assumptions, and parameters
- Includes enough detail for independent replication
- Uses figures, equations, or diagrams when needed for clarity

If ODD documentation is provided or expected, use the `document` skill to assess ODD structure and completeness against its checklist. If a non-ODD framework is used, evaluate it for equivalent coverage (purpose, entities/components, processes, assumptions, parameters, initialization, inputs/outputs, and stochasticity where relevant).

Decision point:
- If no narrative document exists, mark criterion as fail and provide a minimum documentation recovery plan.

### 4. Evaluate Code Quality

Assess maintainability and readability:

- Semantically meaningful names
- Logical structure and modularity
- Comments explain non-obvious logic, not trivial statements
- Low obvious technical debt (dead code, duplication, hidden globals, tangled control flow)
- No obvious hardcoded secrets or unsafe defaults

Report concrete evidence with file-level examples when possible.

### 5. Evaluate Research Software Quality Indicators

Use a focused indicator subset inspired by EVERSE guidance. Prefer evidence over assumptions.

Core indicators:
- Software has documentation
- Software has license
- Software has citation metadata
- Software uses version control
- Software has releases or tagged versions
- Software specifies requirements/dependencies
- Software has tests
- Software has CI workflows
- Software provides issue tracking
- Metadata is sufficiently descriptive and up to date

Optional advanced indicators:
- No critical vulnerabilities known
- No leaked credentials
- Lint/static-analysis hygiene
- Functional correctness measures where appropriate

For each indicator, mark:
- Pass
- Partial
- Fail
- Not assessable

Policy note:
- Tests and CI findings are **Major** quality signals but **nonblocking** for the binary pass/fail decision, unless they directly cause one of the three CoMSES required criteria to fail (for example, inability to execute reproducibly).

### 6. Synthesize Recommendation

Produce:

- Overall recommendation: binary **Pass** or **Fail**
- Severity-ranked findings:
  - Blocker
  - Major
  - Minor
  - Advisory
- Actionable remediation plan with smallest viable next steps
- Explicit statement that scientific merit is out of scope unless reviewer chooses to add private concerns

Decision logic:
- Return **Pass** only when all three CoMSES criteria pass.
- Return **Fail** if any CoMSES criterion is partial or fail.
- Keep tests and CI as Major nonblocking findings unless they materially affect a required criterion.

## Required Output Format

Always generate review outputs using:

- `assets/PEER-REVIEW-REPORT-TEMPLATE.md`

When a user asks for an author revision plan or response checklist, convert findings using:

- `assets/AUTHOR-RESPONSE-CHECKLIST-TEMPLATE.md`

## ⚠️ Gotchas

- Executable does not mean reproducible: passing run instructions can still fail reproducibility if versions and data provenance are unclear.
- Inline comments are not a substitute for narrative model documentation.
- Reviewers often over-focus style and under-focus runnability; keep execution and replication central.
- Missing tests should not automatically fail a model if execution and documentation are excellent, but should be flagged as risk.
- Avoid judging scientific conclusions in this workflow; keep scope to software and documentation readiness.

## Templates & Resources

- Primary rubric: `references/PEER-REVIEW-CHECKLIST.md`
- References companion guide: `references/README.md`
- Standard review report template: `assets/PEER-REVIEW-REPORT-TEMPLATE.md`
- Author response checklist template: `assets/AUTHOR-RESPONSE-CHECKLIST-TEMPLATE.md`
- Compressed CoMSES rubric snapshot: `assets/COMSES-REVIEWS-COMPRESSED.md`
- Compressed EVERSE indicator snapshot: `assets/EVERSE-INDICATORS-COMPRESSED.md`
- Repository-local refresh workflow: `.github/skills/update-skill/SKILL.md`
- ODD completeness checks: `../document/references/ODD-CHECKLIST.md` via the `document` skill when ODD is in scope
- CoMSES review criteria reference: https://www.comses.net/reviews/
- EVERSE indicators reference: https://everse.software/indicators/website/indicators.html

## Example

Input:
- Public repository with Python model code, README, and sample data

Output:
- Structured report with criterion ratings
- Indicator table (pass/partial/fail/not assessable)
- Binary recommendation (Pass or Fail) with prioritized fixes