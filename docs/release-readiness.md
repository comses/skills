# Release Readiness

This document defines the minimum quality expectations for publishing a release of the OMF Skills repository.

Release readiness is evaluated against the repository's own documented standards. These criteria define what should be true before creating a release, independent of the process used to assess them.

## Core Principle

A release should present a coherent, internally consistent repository that is usable by both contributors and coding agents.

Release quality depends on methodological correctness, documentation quality, workflow reliability, and repository consistency rather than feature completeness alone.

---

## Conformance Language

Use the same conformance language throughout this document.

- MUST: Required for release readiness. An unmet MUST criterion is a release blocker.
- SHOULD: Strongly recommended. An unmet SHOULD criterion is a Major or Minor finding depending on its impact.
- MAY: Optional improvement. Absence is informational only.

## Release Criteria

Each section below defines one or more release criteria.

Each criterion should be assessed as one of:

- Satisfied: Repository evidence demonstrates conformance.
- Not Satisfied: Repository evidence demonstrates the criterion is not met.
- Not Assessed: Insufficient repository evidence exists to determine conformance.

Assessments should be grounded in repository evidence rather than assumptions.

## Documentation

Repository documentation MUST:

clearly communicate repository purpose, scope, and intended audience;
describe installation and contribution workflows;
define repository conventions and operating practices;
document validation and release workflows;
remain internally consistent.

Repository documentation SHOULD:

avoid duplicated guidance;
avoid contradictory guidance;
maintain appropriate separation between human-facing documentation, contributor guidance, and coding-agent instructions.

---

## Repository Organization

Repository organization MUST:

- use consistent naming conventions;
- separate published skills from maintainer-only tooling;
- preserve clear architectural boundaries.

Repository organization SHOULD:

- organize documentation for discoverability;
- minimize unnecessary complexity.

---

## Skill Quality

Published skills MUST:

- follow repository conventions;
- have discoverable descriptions;
- maintain unambiguous routing boundaries;
- avoid duplicated methodological responsibility.

Published skills SHOULD:

- include appropriate references;
- produce reviewable intermediate artifacts where applicable;
- include representative evaluation coverage.

---

## Repository Workflows

Repository workflows MUST:

provide a documented validation path;
expose a stable command interface;
avoid conflicting validation workflows.

Repository workflows SHOULD:

support reproducible validation;
align local validation with continuous integration where practical.

---

## Evaluation

Repository evaluation assets MUST:

- exercise expected activation behavior;
- include representative trigger and non-trigger cases.

Repository evaluation assets SHOULD:

- include boundary-condition and adversarial cases where appropriate.

---

## Consistency

The repository MUST maintain consistency across:

- terminology
- routing
- repository conventions

The repository SHOULD maintain consistency across:

- artifact naming
- command interfaces
- documentation organization

Conflicting guidance is itself evidence that one or more consistency criteria are not satisfied.

---

## Release Engineering

Before release, the repository MUST provide:

- licensing
- repository metadata
- installation workflow
- validation workflow
- skill source, versioning policy, maintainer, review status, and review cadence metadata
- a validated schema and template for tracing material `omf-artifacts` changes to producing skills, inputs, decisions, and reviews

The repository SHOULD provide:

- release documentation
- continuous integration
- packaging or distribution guidance where applicable

---

## Severity Levels

Assessment findings should be classified as:

### Release Blocker

One or more MUST release criteria are Not Satisfied.

### Major

All MUST criteria are satisfied, but one or more important SHOULD criteria are not satisfied and materially reduce repository quality.

### Minor

The repository satisfies the release criteria but would benefit from quality or maintainability improvements.

### Observation

An informational finding requiring no action.

---

## Release Outcomes

### Ready

All MUST release criteria are Satisfied.

### Ready with Caveats

All MUST release criteria are Satisfied, but one or more Major or Minor findings remain.

### Not Ready

One or more MUST release criteria are Not Satisfied.

---

## Relationship to Release Assessment

This document defines the release standard.

The release assessment procedure evaluates these criteria, records evidence for each assessment, and produces an evidence-based release recommendation.
