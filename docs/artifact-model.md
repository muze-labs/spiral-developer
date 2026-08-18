# Causal Artifact Model

## Purpose

Spiral Developer preserves enough causality for humans, agents, and ordinary tools to answer:

- Why does this exist?
- What source evidence ultimately caused it?
- How was that evidence interpreted before it became a request?
- Which exact upstream understanding caused it?
- Which historical implementation versions accumulated into the current one?
- Which causes still justify current implementation semantics, and which are only historical?
- What evidence justified it?
- What becomes suspect when something upstream changes?
- Where should a defect be corrected?

It does not model every line of code, prompt, or intermediate attempt.

## Requirements are derived artifacts

A request is not treated as infallible ground truth about human intent. It is a durable statement of what the project currently intends to achieve.

Where the formation of that intent matters, preserve the upstream chain explicitly:

> **source evidence → understanding → request → design → implementation → verification → acceptance**

A **Source** identifies or captures what was actually expressed, observed, received, or mandated. Examples include a connected conversation, email, issue, meeting, contract, regulation, research result, observed behavior, stakeholder statement, or historical report.

An **Understanding** is a claim about what one or more sources mean for the system. It is the right place to crystallize causally important clarification, reframing, interpretation, remaining uncertainty, and repository/reality findings that materially affect what change is actually needed.

The source and understanding layers are deliberately not chat-specific. A connected AI conversation is simply a source that can often be captured with unusually good fidelity. Direct human wording need not be crystallized immediately. For consequential direct work, the agent should investigate enough to formulate a concrete Understanding and establish an evidenced gap against current effective behavior, present both to the human, and stop for confirmation before product implementation. If no gap exists or later evidence changes the apparent task, clarification continues before durable intent drives implementation.

Do not create `SRC-*` and `UND-*` artifacts ceremonially for every request. Create them when origin, interpretation, disagreement, reframing, repository overlap, or provenance strength could plausibly matter later. For simple direct requests, the request may remain the first durable artifact **after any proportionate clarification needed to establish what the human actually wants**. Preserve raw initial wording only when that source history is causally useful.

If the original source is unavailable, do not invent one. A `SRC-*` artifact may record an attributed report or historical claim with `sd:sourceAvailability sd:Unavailable` and an appropriate provenance confidence. An explicit gap is valid causal information.

## Stable identity; Git version

Each durable artifact gets a stable ID. Existing accepted repositories may contain legacy sequential identities such as `REQ-017` or `CYC-005`; these remain valid and must not be renamed merely to adopt a newer convention.

New independently created artifacts use the distributed form:

```text
<TYPE>-<YYYYMMDD>-<WORKSPACE>-<N>
```

Examples:

```text
SRC-20260818-K7M4-12
UND-20260818-K7M4-13
REQ-20260818-K7M4-14
DES-20260819-K7M4-18
```

The type prefix keeps the existing artifact vocabulary (`CUL`, `CTX`, `SRC`, `UND`, `REQ`, `FBK`, `DES`, `IMP`, `LEG`, `EVD`, `ACC`, `DEF`, `CYC`, `EXT`, `RSK`, `LES`, and so on). The date is a human-readable creation hint. `WORKSPACE` is a stable allocation namespace for one independently concurrent Git worktree/checkout. `N` is one monotonically increasing, unpadded sequence shared by all Spiral artifact types and dates in that workspace.

Do not infer authorship or actor identity from the workspace namespace. Do not use the date/local sequence as an independent version or authoritative global chronology. Git supplies authoritative history.

Use the repository `spiral allocate <TYPE>` command for new IDs where available; do not scan the repository and choose a globally “next” sequence number. See `distributed-development.md`.

**There is no independent numeric revision system.**

The Git commit is the artifact version.

Human shorthand may use:

```text
REQ-20260818-K7M4-14@a12f9e1
```

The machine-readable graph stores the full commit hash.

A Git commit cannot contain its own hash. Therefore an artifact does not declare “my version is X” inside the commit that creates it. Downstream artifacts record the upstream hash after that commit exists.

## Human artifacts and machine graph

Human-facing artifacts are normally Markdown and should contain the meaning that humans need to inspect, discuss, and approve.

The canonical machine-readable causal relationships live in companion Turtle resources under `.spiral/`, normally beside the human-facing artifact they describe. Their RDF union is the project causal graph. See `rdf-graph.md`.

Do not maintain parallel causal fields in Markdown and Turtle unless a migration explicitly requires it. Duplicated graphs drift.

If prose and graph disagree, treat that as a defect to resolve, not as an invitation to silently choose whichever source is convenient.


## Warning profiles

A `WPF-*` warning-profile artifact is an explicit, versioned, replaceable inspection lens. It is distinct from culture: culture helps choose among trustworthy options, while a warning profile names patterns the project wants surfaced when they become consequential. It is also distinct from Spiral core: projects may replace or decline warning profiles without changing the trust architecture.

Project context adopts an exact warning-profile version with `sd:adoptsWarningProfile`. A warning occurrence does not automatically need a durable artifact. When it is consequential, represent the actual project concern as an ordinary `RSK-*` artifact and link it to the exact profile version (and optional warning ID in `sd:fragment`) that helped surface it.

See `warning-profiles.md`.

## Lessons and process learning

A `LES-*` artifact records an evidence-informed generalization that may change future project practice, a culture profile, or Spiral Developer itself. A lesson is not automatically a requirement or rule. Preserve the observation/evidence, the generalization, its intended scope, confidence/limits, and the consequence being proposed.

Link lessons to exact evidence versions when practical using normal causal relations. Later artifacts or process changes may derive from a lesson, but promotion to a broader scope should remain explicit and reviewable. Lessons themselves may be superseded when later evidence changes the generalization.

See `process-evolution.md`.

## Cycle semantics

`CYC-*` is the outer human-visible learning and integration record. One cycle pursues one coherent project outcome, risk reduction, or important uncertainty and may contain multiple lower-level causal artifacts and semantic commits. It is not a replacement for Request/Design/Implementation/Verification/Acceptance artifacts and is not an arbitrary task bucket.

For the first operational version, cycle membership does not require a new RDF relation. The cycle Markdown may list important artifacts/commits and evaluation findings. Preserve machine-readable cycle identity in a companion Turtle resource, but do not invent a task ontology or formal state machine until real queries/automation require them. See `cycles.md`.

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

For collaboration semantics, an `accepted` Understanding/Request/Design can serve as a **commitment signal** when that artifact is the decision boundary the current execution depends on. `draft` or merely `active` material must not be treated as execution authority simply because it is recent or human-authored. Acceptance is scoped to the artifact's meaning; it does not automatically authorize unrelated work or override a cycle goal/non-goal boundary. See `ai-collaboration.md`.

## Core relation semantics

Use typed relations rather than generic “related to”.

### `derivedFrom`

The downstream artifact was created using the upstream artifact as a source of meaning or evidence.

A request will commonly `sd:derivedFrom` an accepted understanding when interpretation was material.

### `interprets`

An understanding gives meaning to a specific upstream source, observation, feedback item, legacy claim, or other evidence.

This relation preserves the difference between **what was actually available upstream** and **what the project concluded it meant**. The interpretation may later be superseded without changing the source.

### `satisfies`

A design element claims to satisfy a request outcome or fragment.

### `supports`

The artifact is technically/enablingly necessary for another artifact but is not direct client intent.

### `constrainedBy`

A culture rule, external standard, platform limitation, legal requirement, legacy constraint, or explicit project constraint narrows the valid solution space.

### `shapedBy`

A current design or implementation choice was materially influenced by an exact culture/preference version, but the preference did not itself make alternatives invalid. Use this to explain *why this acceptable form was chosen* without pretending the requirement logically entailed it.

### `adoptsCulture`

Project context intentionally adopts an exact culture profile/version as active guidance. Culture remains defeasible unless a preference is separately promoted into a request or constraint.

### `adoptsWarningProfile`

Project context intentionally adopts an exact warning-profile version as an active inspection lens. Adoption means the agent/reviewer should apply the profile's scope and significance gates; it does not mean every signal is true, mandatory, or blocking.

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

### `transforms`

An artifact version points to one or more exact predecessor artifact versions that it materially revises, moves, replaces, splits, merges, refactors, or explicitly reconciles. This is **historical lineage**, not a current causal justification, so `sd:transforms` is deliberately not a subproperty of `sd:causalReference`.

Implementation lineage is the common case. Distributed convergence adds another mandatory case: if a merge combines independent material revisions of the same stable governed artifact, the merge version records the immediate predecessor version from each parent lineage.

### `changeCausedBy`

An implementation transition happened because of an exact upstream defect, feedback item, design, request, risk, or other causal artifact version. This is **transition provenance**. It explains why one implementation version replaced another without implying that the transition cause remains a current justification for the resulting semantics.

Do not create a relation unless it will plausibly help reasoning, impact analysis, audit, or verification.

## Source availability

`sd:Source` artifacts record whether their primary origin evidence is:

- `retained` — the relevant source material is preserved in or with the project;
- `referenced` — the source remains externally identifiable/retrievable but is not retained as project content;
- `unavailable` — the project has only a report, memory, inherited claim, or other secondary trace.

Availability is not the same as correctness. A retained source can still be ambiguous or misleading, and an unavailable source can still describe an operationally important requirement. The point is to make the epistemic difference visible.

## Versioned references

Relations that point to exact prior artifact versions are grouped under `sd:historicalReference` for integrity validation. `sd:causalReference`, `sd:transforms`, and `sd:changeCausedBy` remain semantically distinct even though they share the rule that the referenced version must already exist in Git history.

A causal relation to an upstream artifact should point to the exact Git commit containing the upstream version that informed the decision. Once persisted, every historical-reference target commit must be a strict Git ancestor of the source artifact version's commit. This makes the versioned historical-reference graph acyclic by construction; see `causal-validation.md`.

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

Use provenance confidence for claims whose grounding matters, including source reports, reconstructed legacy context, and interpretations:

- `explicit` — directly and currently stated by an authoritative source;
- `evidenced` — strongly supported by available evidence;
- `inferred` — plausible but not established;
- `unknown` — the relevant reason or meaning is not known.

These describe the provenance of a claim, not whether observable behavior exists.

## Implementation references

Code remains in the normal repository. A meaningful implementation unit may be represented in the graph with a stable `IMP-*` identity. `sd:implementationLocation` may be repeated to locate relevant paths/symbols. Locations may overlap across implementation artifacts: implementation concerns do not partition source code into exclusive ownership.

Do not scatter requirement IDs through generated source merely to satisfy traceability.

The useful unit is normally a meaningful behavior, design decision, boundary, capability, or vertical slice.

## Effective provenance and implementation lineage

Real code accumulates causes across revisions. Git blame tells us what last touched text; it does not establish which earlier decisions still explain current behavior.

Spiral Developer therefore separates:

- **effective provenance** — current-purpose causal references on the current `IMP-*` version that still justify its semantics;
- **implementation lineage** — `sd:transforms` references to exact predecessor implementation version(s);
- **transition provenance** — `sd:changeCausedBy` plus `sd:implementationChangeKind`, explaining why that particular revision happened and whether behavior was intended to change.

The current checked-out implementation resource is a compact effective-provenance projection. Older projections remain in Git. Historical reachability must never be presented as current justification merely because an old cause can be reached through `sd:transforms`.

When a governed implementation unit is materially revised, moved, replaced, split, merged, or refactored, preserve lineage to its immediate predecessor version(s), record the transition cause and change kind, and carry forward only the effective causal references that remain valid. Do not create lineage noise for formatting-only or other immaterial edits.

A semantic implementation change can still implement the same design—for example a defect correction. In that case the design may remain in effective provenance while the defect is recorded as the transition cause. A behavior-preserving refactor should retain relevant effective provenance and should be verified when preservation matters.

See `implementation-lineage.md`.

## Change propagation

When an upstream artifact changes:

1. preserve the old artifact and commit;
2. create the new upstream version in a new commit;
3. query/find direct dependents of the old version;
4. mark materially affected downstream artifacts as suspect;
5. re-evaluate each dependent;
6. preserve whether it remains valid, is revised, or is replaced.

This applies above the request layer as well. A revised interpretation of an unchanged source can make a request suspect. A newly recovered primary source can make an earlier understanding suspect.

Git history tells us what happened. The causal graph tells us what depended on what. Implementation lineage tells us how those dependencies accumulated into the implementation that exists now.

## What not to preserve by default

Do not preserve every prompt, token, intermediate code draft, or conversational branch.

Crystallize durable meaning:

- source statements or observations when their identity matters;
- interpretations and accepted understandings when meaning was non-trivial;
- intent;
- assumptions and reframings;
- consequential decisions;
- constraints;
- evidence;
- acceptance;
- root-cause findings;
- causal provenance.

A long conversation may therefore produce only a few durable artifacts: the relevant source expression, a consequential reframing or clarification, the accepted understanding, and the request that operationalizes it.

Record model/tool configuration only when it was materially causal to a result, defect, or reproducibility question.
