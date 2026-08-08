# Causal Artifact Model

## Purpose

Spiral Developer preserves enough causality for humans, agents, and ordinary tools to answer:

- Why does this exist?
- Which exact upstream understanding caused it?
- What evidence justified it?
- What becomes suspect when something upstream changes?
- Where should a defect be corrected?

It does not model every line of code, prompt, or intermediate attempt.

## Stable identity; Git version

Each durable artifact gets a stable ID, for example:

- `CUL-001` — culture/principle set;
- `CTX-001` — project context;
- `REQ-001` — request/intent unit;
- `FBK-001` — feedback/observation;
- `DES-001` — design element/decision;
- `IMP-001` — implementation unit/vertical slice;
- `LEG-001` — reconstructed legacy context/constraint;
- `EVD-001` — verification evidence;
- `ACC-001` — acceptance evidence;
- `DEF-001` — defect/root-cause analysis;
- `CYC-001` — development cycle;
- `EXT-001` — external constraint when it needs explicit identity;
- `RSK-001` — durable risk when it needs explicit identity.

**There is no independent numeric revision system.**

The Git commit is the artifact version.

Human shorthand may use:

```text
REQ-001@a12f9e1
```

The machine-readable graph stores the full commit hash.

A Git commit cannot contain its own hash. Therefore an artifact does not declare “my version is X” inside the commit that creates it. Downstream artifacts record the upstream hash after that commit exists.

## Human artifacts and machine graph

Human-facing artifacts are normally Markdown and should contain the meaning that humans need to inspect, discuss, and approve.

The canonical machine-readable causal relationships live in companion Turtle resources under `.spiral/`, normally beside the human-facing artifact they describe. Their RDF union is the project causal graph. See `rdf-graph.md`.

Do not maintain parallel causal fields in Markdown and Turtle unless a migration explicitly requires it. Duplicated graphs drift.

If prose and graph disagree, treat that as a defect to resolve, not as an invitation to silently choose whichever source is convenient.

## Artifact states

Useful states include:

- draft;
- active;
- accepted;
- suspect;
- superseded;
- rejected.

When an upstream artifact version is superseded, downstream artifacts are candidates for `suspect`. They are not automatically wrong.

Artifact status is about the artifact's semantic lifecycle. Do not duplicate branch/merge state in the graph; Git already tells us whether a commit is part of authoritative history.

## Core relation semantics

Use typed relations rather than generic “related to”.

### `derivedFrom`

The downstream artifact was created using the upstream artifact as a source of meaning or evidence.

### `satisfies`

A design element claims to satisfy a request outcome or fragment.

### `supports`

The artifact is technically/enablingly necessary for another artifact but is not direct client intent.

### `constrainedBy`

A culture rule, external standard, platform limitation, legal requirement, legacy constraint, or explicit project constraint narrows the valid solution space.

### `implements`

An implementation unit realizes a design element.

### `verifies`

Evidence establishes a property of implementation or design.

### `accepts`

Acceptance evidence establishes that observable behavior satisfies a request outcome.

### `observes`

Feedback or runtime evidence records something learned by interacting with or operating the system.

### `supersedes`

A new artifact/version prospectively replaces an earlier one without rewriting its historical role.

Do not create a relation unless it will plausibly help reasoning, impact analysis, audit, or verification.

## Versioned references

A causal relation to an upstream artifact should point to the exact Git commit containing the upstream version that informed the decision.

In Turtle this is represented as an `sd:ArtifactReference` containing:

- the stable artifact IRI;
- the full Git commit hash;
- optionally a stable fragment/key within the artifact.

See `rdf-graph.md`.

## Fragment references

When only part of an artifact matters, use a stable semantic key such as:

```text
outcome-1
reset-expiry
permission-boundary
```

Avoid line numbers as durable semantic references.

## Provenance confidence

For reconstructed legacy claims use:

- `explicit` — currently authoritative statement;
- `evidenced` — strongly supported by surviving artifacts;
- `inferred` — plausible but not established;
- `unknown` — behavior exists but its reason is not known.

These describe the provenance of a claim, not whether observable behavior exists.

## Implementation references

Code remains in the normal repository. A meaningful implementation unit may be represented in the graph with a stable `IMP-*` identity and paths/symbols that locate the implementation.

Do not scatter requirement IDs through generated source merely to satisfy traceability.

The useful unit is normally a meaningful behavior, design decision, boundary, or vertical slice.

## Change propagation

When an upstream artifact changes:

1. preserve the old artifact and commit;
2. create the new upstream version in a new commit;
3. query/find direct dependents of the old version;
4. mark materially affected downstream artifacts as suspect;
5. re-evaluate each dependent;
6. preserve whether it remains valid, is revised, or is replaced.

Git history tells us what happened. The graph tells us what depended on what.

## What not to preserve by default

Do not preserve every prompt, token, intermediate code draft, or conversational branch.

Crystallize durable meaning:

- intent;
- assumptions;
- consequential decisions;
- constraints;
- evidence;
- acceptance;
- root-cause findings;
- causal provenance.

Record model/tool configuration only when it was materially causal to a result, defect, or reproducibility question.
