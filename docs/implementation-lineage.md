# Implementation Lineage

## Purpose

Real implementation accumulates causes over time. A current function, branch, constant, or boundary may embody several surviving decisions even though Git records only which commits touched the text.

Spiral Developer therefore distinguishes three questions:

1. **Why is this implementation this way now?** — current/effective provenance.
2. **How did this implementation get here?** — implementation lineage.
3. **Why did this particular revision happen?** — transition provenance.

These must not be collapsed into one generic history relation.

## The three layers

A tracked implementation version keeps a compact current view:

```text
current IMP version
├─ effective causal references → design / constraints / other current reasons
├─ transforms                  → immediate predecessor implementation version(s)
├─ change caused by            → defect / design / feedback / request / other transition reason
└─ change kind                 → behavior-preserving / semantic / mixed / unknown
```

The current checked-out `IMP-*` resource is the **effective provenance projection**. Older projections remain available in Git and are reached only through lineage traversal.

### Effective provenance

Effective provenance answers:

> **Which reasons still justify the current semantics?**

For an implementation, this is represented by its current-purpose causal relations such as `sd:implements`, `sd:derivedFrom`, `sd:supports`, and `sd:constrainedBy`.

Do not infer current justification merely because an old cause is reachable through history.

If requirement A originally introduced a 30-second timeout and requirement B later replaces it with 60 seconds, A remains historical provenance but is no longer a current justification for the value 60.

### Implementation lineage

`sd:transforms` points from the current implementation version to the exact predecessor implementation version or versions that it materially revised, moved, replaced, split, merged, or refactored.

It is deliberately **not** a subproperty of `sd:causalReference`. It means identity/evolution through implementation time, not current justification.

For the common case the stable artifact identity remains the same:

```text
IMP-023@current --transforms--> IMP-023@previous
```

A split, merge, or replacement may legitimately transform one or more different `IMP-*` identities.

### Transition provenance

`sd:changeCausedBy` records why this revision happened. It points to the exact version of the defect, feedback, design, request, risk, or other artifact that caused the transition.

This is separate from effective provenance because a change can be causally important without becoming a permanent justification for current behavior.

For example, a defect may cause code to be corrected so that it finally implements the same design it was always supposed to implement. The effective design reference does not change, but the defect remains the historical reason for that revision.

`sd:implementationChangeKind` records the intended semantic character of the transition:

- `sd:BehaviorPreservingChange` — structure/location changed; relevant behavior was intended to remain the same;
- `sd:SemanticChange` — observable or contract-relevant semantics intentionally changed;
- `sd:MixedChange` — the revision combines semantic and behavior-preserving structural change;
- `sd:UnknownChange` — the character of a reconstructed historical change cannot be established.

A behavior-preserving claim is a claim, not proof. Use verification evidence when preservation matters.

## Lineage invariant

For implementation that Spiral Developer already governs:

> **When a tracked implementation unit is materially revised, moved, replaced, split, merged, or refactored, the new implementation version must retain `sd:transforms` reference(s) to the exact predecessor implementation version(s). For prospective governed changes it must also record the transition cause and change kind. Reconstructed history may use `sd:UnknownChange` and leave the cause absent rather than inventing one.**

Additionally:

> **The current implementation version must preserve the effective causal references that still justify its current semantics and remove or supersede those that no longer do.**

These rules are intentionally prospective. Brownfield adoption must not invent lineage that cannot be established.

Do not create lineage events for formatting-only, generated-noise, or other changes that do not materially revise a tracked implementation unit.

## Semantic changes do not necessarily change design

A semantic implementation change may repair an implementation against an unchanged design:

```text
DES-014 ───────────────→ IMP-014@1
                            │
                            │ transforms
                            ↓
DES-014 ───────────────→ IMP-014@2
DEF-031 ─ changeCausedBy ───┘
```

The current effective reason can remain `DES-014`; `DEF-031` explains why version 2 replaced version 1.

If the defect instead reveals that the request or design was incomplete, correct that earlier artifact first and let the new implementation point to the corrected effective cause.

## Behavior-preserving refactors remain in lineage

Do not omit lineage merely because behavior was intended to remain unchanged. A refactor can otherwise sever the path between current code and the reasons embedded in its predecessor.

```text
IMP@1
  ↓ transforms
IMP@2  (BehaviorPreservingChange; caused by DES-refactor)
  ↓ transforms
IMP@3  (SemanticChange; caused by DEF-031)
```

Verification can establish that `IMP@2` preserved the relevant behavior. Git blame alone cannot.

## Overlapping implementation units are valid

Implementation artifacts represent meaningful behaviors, boundaries, capabilities, or design realizations. They do not partition source code.

The same code location may therefore be located by several `IMP-*` artifacts, for example authorization, audit logging, retry behavior, and privacy constraints. `sd:implementationLocation` is repeatable and overlap is allowed.

This matters for interrogation:

- “Why does this function look like this?” may return several effective causal branches.
- “Why is this authorization check here?” should narrow to the relevant implementation concern.

Do not force every line or symbol to have exactly one causal owner.

## Interrogation modes

### Why is this here now?

Start from the relevant current implementation unit(s) and traverse **current effective provenance** upward. Do not traverse older `sd:transforms` links unless current provenance is insufficient or the user asks for history.

A good answer may have several surviving branches:

> This authorization check realizes DES-014. The privacy guard is additionally constrained by EXT-003. The 60-second timeout comes from the current session-policy design.

### How did this get here?

Follow `sd:transforms` backward on demand. At each historical version, inspect `sd:changeCausedBy`, `sd:implementationChangeKind`, and differences in effective causal references.

A good answer distinguishes introduction, later semantic modifications, behavior-preserving refactors, and superseded reasons.

### Never confuse reachability with justification

A historical cause being reachable proves that it participated in the implementation's history. It does **not** prove that it remains an effective cause of current semantics.

This is a core trust invariant:

> **Historical reachability must never be presented as current justification without evidence that the cause survives in the current effective provenance projection.**

## Bounded agent context

Implementation lineage must not force an agent to replay the full history on every change.

For normal continued development, the default working set is:

```text
current code
+ current IMP effective provenance
+ relevant current design/tests/evidence
+ the new reason for change
+ immediate predecessor reference
```

Older lineage is queryable on demand.

When creating the next version, the agent normally:

1. identifies the current tracked implementation unit(s);
2. preserves effective causal references that remain valid;
3. updates only the effective causes that the new semantics supersede or add;
4. records `sd:transforms` to the immediate predecessor version(s);
5. records `sd:changeCausedBy` and `sd:implementationChangeKind`;
6. verifies any important behavior-preservation claim;
7. leaves older history in Git rather than copying it into the current resource.

The bookkeeping cost should therefore track the semantic complexity of the current change, not the age of the codebase.

## Progressive-development hypothesis

Ordinary codebases often become harder for AI agents to modify as hidden intent, compatibility behavior, and unexplained historical decisions accumulate. The agent spends more effort on archaeology and still risks removing a reason it cannot see.

Spiral Developer is designed to trade that growing archaeology cost for a small provenance-maintenance cost on each governed change.

The hypothesis is:

> **As governed development accumulates, the current causal projection can make later AI changes require less rediscovery and less human intervention, even while the historical record grows.**

This is a design hypothesis, not a guarantee. Dogfooding should measure it. Useful signals include:

- how much historical material the agent had to load for a normal change;
- how many archaeology steps were needed before acting;
- how often a human had to recover an old reason manually;
- whether current effective provenance stayed compact as lineage grew;
- whether a previously governed area was cheaper/safer to change than an equally complex opaque area;
- whether stale effective causes were detected when semantics changed.

The desired asymmetry is:

- **storage/history:** grows with development;
- **ordinary development context:** remains bounded by current semantic complexity;
- **deep historical interrogation:** pays history cost only when requested;
- **archaeology:** should decrease as provenance coverage accumulates.

## Git and versioning

The existing stable-ID/Git-version model is sufficient.

An implementation resource does not contain its own current commit hash. Before creating a new implementation commit, the predecessor hash already exists, so the new resource can safely point backward:

```turtle
project:IMP-023
    a sd:Implementation ;
    sd:transforms [
        a sd:ArtifactReference ;
        sd:artifact project:IMP-023 ;
        sd:gitCommit "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ] ;
    sd:changeCausedBy [
        a sd:ArtifactReference ;
        sd:artifact project:DEF-031 ;
        sd:gitCommit "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    ] ;
    sd:implementationChangeKind sd:SemanticChange .
```

A later evidence or downstream artifact can then refer to this new implementation version by the commit that contains it.
