# Causal Reference Validation

Spiral Developer treats Git history as evidence. A causal or historical reference is therefore not valid merely because its target hash exists: the referenced version must already have existed when the referring artifact version was committed.

> **Persisted version rule:** every versioned historical reference must point to a Git commit that is a strict ancestor of the commit containing the reference.

This rule is the primary mechanical basis for acyclicity of the versioned evidence graph. If every historical reference points strictly backward in Git ancestry, a versioned reference cycle cannot exist.

## Which relations are historical references

The ontology groups relations that point to exact prior artifact versions under `sd:historicalReference`.

This includes:

- current/effective causal provenance through `sd:causalReference` and its subproperties;
- implementation lineage through `sd:transforms`;
- transition provenance through `sd:changeCausedBy`.

These relations do **not** all mean the same thing. In particular, lineage and transition provenance are not current causal justification. The shared superproperty exists so tooling can apply historical-version integrity rules without collapsing their semantics.

## Three validation layers

### 1. Staged/pre-commit prevention

Before a semantic causal commit is created, validate the staged Spiral Turtle that will enter history.

At this point the new commit hash does not exist yet. If current `HEAD` will be its parent, every referenced target commit must:

- exist;
- be reachable from current `HEAD` (the target may be `HEAD` itself);
- contain the referenced artifact version where that can be checked;
- use a full commit hash;
- satisfy Turtle syntax and applicable SHACL constraints.

Allowing a target equal to current `HEAD` is correct: after the new commit is created, that `HEAD` becomes its strict ancestor.

A pre-commit validator should block the commit when a new or changed historical reference cannot satisfy these rules. This is prevention: once an invalid semantic causal commit exists, Spiral's immutable-history rule means the mistake itself must remain visible and be corrected prospectively.

Use a standards-conforming RDF/Turtle parser. Do not implement provenance integrity on top of a formatting-specific or partial Turtle parser.

### 2. Commit/range validation

For a persisted artifact version at source commit `S`, every `sd:historicalReference` target commit `T` must satisfy:

```text
T is a strict Git ancestor of S
```

CI should normally validate the commits introduced by the proposed change, for example a merge-base-to-branch-tip range. Validate the changed Spiral artifact versions as they existed in each introduced commit, not only the final tree.

This matters because an invalid reference can be introduced in one commit and removed in a later commit. Snapshot-only validation would miss that historical violation.

A bounded range check is normally preferable to re-auditing unrelated repository history on every CI run.

### 3. Snapshot and history audit

Snapshot validation remains useful diagnostically: it answers whether the checked-out graph is structurally valid now.

A deliberate history audit answers a different question: whether reachable preserved history contains any historical-reference violation.

Keep these conclusions distinct:

- **current snapshot valid** — the present graph satisfies the invariant;
- **history pristine** — no audited reachable historical artifact version violated it;
- **history contains a known corrected violation** — an invalid historical claim remains preserved, but later evidence records its detection/correction and the current graph is valid;
- **history contains unresolved violation(s)** — historical integrity problems remain unexplained or uncorrected.

A correction must never make a raw history audit silently pass. A higher-level trust assessment may explain that a violation is known and corrected, but must not relabel the original invalid reference as valid.

## Why Git ancestry rather than generic cycle detection

Generic graph cycle detection is useful defensive validation, but it is weaker than the causal invariant.

A graph can be acyclic while still containing a reference to a sibling branch or future/unrelated commit. Such a graph has no cycle but still makes a historically impossible causal claim.

Strict Git ancestry establishes both:

- temporal admissibility — referenced evidence already existed;
- DAG acyclicity — backward-only versioned edges cannot form a cycle.

Conceptual artifact identity may still appear cyclic across revisions. For example, a request can produce a design, feedback on that design can revise the request, and the revised request can produce another design. The versioned graph remains acyclic because each exact artifact version points backward in history.

## Merge histories

Merge commits can have multiple parents. A target from either merged parent history can legitimately be an ancestor of the merge commit.

Do not weaken the rule to "older timestamp" or "different commit". Use Git's ancestry relation.

## Validation is structural, not semantic

Passing these checks establishes historical integrity, not that a claim is true, sufficient, or well interpreted.

For example:

- SHACL can establish that a reference has the required fields;
- Git validation can establish that the referenced version already existed;
- tests can establish selected behavioral claims;
- humans still judge whether the evidence actually justifies the decision.

The purpose of structural validation is to prevent the evidentiary substrate itself from making impossible historical claims and to expose violations before fluent AI reasoning can hide them.
