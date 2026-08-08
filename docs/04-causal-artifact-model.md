# Causal Artifact Model

## Purpose

The artifact model is intentionally small. Its job is to preserve enough causality for humans and agents to answer:

- Why does this exist?
- What version of upstream intent/design caused it?
- What evidence justified it?
- What becomes suspect when something upstream changes?
- Where should we fix a defect?

It is not intended to model every line of code or every conversation.

## Stable identity and revision

Use stable IDs such as:

- `CUL-001` — culture/long-lived engineering principle;
- `REQ-001` — request or intent unit;
- `FBK-001` — meaningful feedback/observation;
- `DES-001` — design element/decision;
- `LEG-001` — reconstructed legacy constraint/context;
- `EVD-001` — verification evidence;
- `ACC-001` — acceptance evidence;
- `DEF-001` — defect/root-cause analysis;
- `CYC-001` — development cycle.

Each mutable artifact has a revision number. Refer to a specific revision as `REQ-001@3`.

Git preserves old revisions. A later harness may provide resolution/indexing, but the semantic reference should already point to the revision actually used.

## Suggested artifact states

- `draft`
- `active`
- `accepted`
- `suspect`
- `superseded`
- `rejected`

When an upstream artifact is superseded, downstream artifacts derived from that revision become candidates for `suspect`; they are not automatically wrong.

## Core relation semantics

Use a small vocabulary rather than generic “related to” links.

### `derived_from`

The downstream artifact was created using the upstream artifact as a source of meaning or evidence.

### `satisfies`

A design element claims to satisfy a request fragment.

### `supports`

The artifact is technically/enablingly necessary for another artifact but does not represent direct client intent.

### `constrained_by`

A culture rule, external standard, platform limitation, legal requirement, legacy constraint, or explicit project constraint narrows the valid solution space.

### `implements`

Code, configuration, schema, or another executable artifact realizes a design element.

### `verifies`

Evidence establishes a property of implementation/design.

### `accepts`

Acceptance evidence establishes that observable behavior satisfies a request fragment.

### `observes`

Feedback/runtime evidence records something learned by interacting with or operating the system.

### `supersedes`

A new revision replaces an earlier revision prospectively without rewriting its historical role.

Do not create a relation unless it is useful for later reasoning.

## Provenance confidence

For brownfield/reconstructed claims, use:

- `explicit`
- `evidenced`
- `inferred`
- `unknown`

These describe confidence in the claim's provenance, not confidence in whether the current behavior exists.

## Implementation references

Code itself remains in the normal repository.

Evidence/design artifacts may reference implementation by:

- path;
- symbol/component name;
- test path;
- commit/PR when known;
- generated artifact name.

The implementation link should normally be recorded in the cycle, evidence, commit/PR metadata, or another small implementation map. Do not add requirement comments throughout generated code merely to satisfy traceability.

Do not force every line to carry a requirement ID.

The useful unit is normally a meaningful behavior, design decision, boundary, or vertical slice.

## Fragment references

When only part of an artifact is relevant, use a stable section/key if practical, for example:

`REQ-001@2#reset-expiry`

Avoid brittle line-number references as the main semantic link.

## Change propagation

When `REQ-001@2` is superseded by `REQ-001@3`:

1. preserve every artifact that historically derived from `REQ-001@2`;
2. find direct dependents;
3. mark affected downstream artifacts for re-evaluation;
4. determine whether each remains valid, needs revision, or should be replaced;
5. preserve the decision/evidence.

The same logic applies to design, external constraints, culture rules, or legacy assumptions.

## What not to preserve

Do not preserve every prompt, token, intermediate code draft, or conversational branch by default.

Crystallize durable meaning:

- intent;
- assumptions;
- consequential decisions;
- constraints;
- evidence;
- acceptance;
- root-cause findings;
- versions/provenance.

Execution traces are useful only when they are needed to reproduce or audit an important decision. Record model/tool configuration only when it was materially causal to a result, defect, or reproducibility question.
