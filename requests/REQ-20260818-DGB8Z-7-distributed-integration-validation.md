---
id: REQ-20260818-DGB8Z-7
---

# Request: Distributed integration validation

## Operationalized intent

Spiral must make the integration boundary mechanically checkable so independently valid branches cannot be merged into a causally incoherent current state merely because Git reports no textual conflict.

The same repository-local validator must be usable locally and by Git/GitHub/GitLab integration adapters. Host-specific configuration may choose when/how to invoke it, but must not redefine Spiral's causal validation semantics.

## Upstream understanding

`UND-DIST-002` establishes the accepted model: distributed work is optimistic; integration is serialized and revalidated against the actual target/prospective merged state.

## Observable desired outcomes

### prospective-combined-state

`spiral validate integration --base <target> --head <candidate>` evaluates the tree that Git would produce from the specified current target and candidate, without rewriting either branch history.

### ordinary-git-conflicts-remain-git-conflicts

If Git cannot produce a clean prospective tree because the branches have ordinary merge conflicts, Spiral reports that integration validation cannot proceed until those conflicts are resolved. It does not invent a separate source-conflict resolution mechanism.

### unresolved-causal-staleness-blocks-integration

If the prospective current graph leaves a current/effective artifact causally dependent on an exact upstream version that the combined state supersedes, validation fails and identifies the downstream artifact, relation, stale upstream identity/version, and superseding artifact.

### non-effective-state-propagates

A current/effective artifact must not silently depend on an upstream artifact whose current status explicitly says it is `Suspect`, `Superseded`, or `Rejected`. A branch may preserve such an artifact as history/current uncertainty, but effective downstream claims must be reconciled before integration can be considered causally coherent.

### distributed-allocation-collisions-are-detectable

The validator detects duplicate distributed allocation slots (`WORKSPACE` + local sequence) even when differing type/date prefixes would otherwise avoid a filename conflict. Historical legacy IDs remain valid.

### standards-based-turtle-input

Validation parses Turtle with a standards-conforming RDF parser rather than depending on repository formatting conventions or regex extraction of causal claims.

### local-snapshot-validation

`spiral validate` applies the same current-state identity and causal-coherence rules to the checked-out repository, so developers/agents can detect problems before the integration boundary.

### machine-usable-result

Validation exits successfully only when the mechanically checked invariants pass and exits non-zero with actionable diagnostics when they do not.

## Non-goals

- decide whether evidence is semantically convincing or whether a superseding artifact is substantively correct;
- prevent legitimate independent branches from diverging before integration;
- replace ordinary Git conflict resolution;
- build a host-specific GitHub/GitLab semantics layer;
- implement the complete historical/range validator described elsewhere in Spiral as part of this slice;
- automate human acceptance or discourse decisions.

## Acceptance focus

A two-writer test must demonstrate the failure mode that motivated this requirement: branch A supersedes an upstream artifact while branch B independently adds a downstream current/effective artifact against the old exact version. Each branch may be locally coherent in isolation; after A is the target, validating B's prospective integration must fail until B reconciles its causal state.
