---
id: UND-20260818-DGB8Z-13
---

# Understanding: Cycle isolation and explicit convergence are distributed-safety boundaries

## Current interpretation

Spiral's distributed model should not try to maintain a single global "active cycle" state. Repository-changing work is instead scoped by Git branch:

- one open cycle works on one branch named for that cycle;
- open cycle branches do not integrate into the authoritative branch or into another open cycle branch;
- completed authoritative work may be merged into an open cycle branch so the cycle can reconcile against current accepted reality;
- only a completed/accepted cycle is eligible to integrate into the authoritative branch.

This makes cycle activity local to the branch and keeps authoritative history semantically simple: it contains accepted cycle outcomes rather than partially completed cycle state.

Distributed integration also needs to preserve independently evolved meaning. When the same stable governed artifact was materially revised on both histories before convergence, the convergence point is not an ordinary textual merge. The combined artifact version must explicitly identify the immediate predecessor version from each surviving lineage. Git may help construct the text, but Git conflict resolution or a clean auto-merge is not evidence that both causal branches were intentionally reconciled.

`sd:transforms` should therefore be treated as a general historical predecessor relation for governed artifacts, not only implementation artifacts. Implementation lineage remains one important use, with implementation-specific change-kind/cause metadata still applying only to implementations.

Finally, worktree-local allocation remains the correct decentralized model, but local state should never reuse a slot that is already visible in its own workspace namespace. Before allocating, the local counter can safely fast-forward to the highest visible `(same workspace, sequence)` value in the checked-out repository. This is only local defensive recovery; it does not coordinate disconnected duplicate workspaces, so prospective integration collision validation remains required.

## Sources considered

- `SRC-20260818-DGB8Z-12` records the human-confirmed branch/convergence rules and the current repository observations.
- Existing `UND-DIST-001` and `UND-DIST-002` establish independently allocatable identity and serialized/revalidated integration.

## Clarifications / reframing

| Question / assumption | Alternative or clarification | Evidence / resolution |
|---|---|---|
| Spiral needs one globally stored current cycle. | The active cycle is branch-scoped; the branch identifies the cycle being worked. | Human-confirmed direction in `SRC-20260818-DGB8Z-12`. |
| An accepted branch can be merged whenever Git can merge it. | An open cycle is never an integration candidate; acceptance/closure precedes authoritative integration. | Human-confirmed direction plus the observed CYC-005 premature merge. |
| Merging main into an open cycle violates cycle isolation. | Upstream accepted work may flow into the cycle; what is prohibited is unfinished cycle work flowing outward. | Explicit human clarification. |
| A clean Git merge of parallel revisions means the artifact is reconciled. | Textual compatibility can still silently combine or discard independently evolved meaning. | Human-confirmed convergence rule. |
| `sd:transforms` is inherently implementation-only. | The predecessor-version semantics are useful for any stable governed artifact; only implementation-specific transition metadata needs the narrower domain. | The agreed reconciliation requirement applies beyond `IMP-*`. |
| Worktree-local sequence must be trusted exactly as stored. | If the same namespace already has higher committed allocations visible locally, fast-forwarding the local counter is safe and prevents avoidable reuse. | Uploaded checkout had local sequence 6 while repository contained DGB8Z through sequence 11. |

## Current effective behavior / evidenced gap (when material)

The current repository already allocates distributed IDs and validates duplicate allocation slots and prospective causal staleness. It also documents one-cycle/one-branch practice.

However:

- prospective integration does not currently reject a cycle that is still `Active`;
- hosted integration adapters do not currently verify that the candidate branch is named for the cycle it changes;
- the validator does not detect a clean convergence where both parent histories materially revised the same stable governed artifact but the merge version failed to retain both predecessor versions;
- `sd:transforms` is currently declared with `sd:Implementation` as its RDF domain;
- allocation trusts the local sequence file even when higher allocations in the same workspace namespace are already visible in the current checkout.

The uploaded repository itself demonstrates the first and last gaps.

## Provenance confidence

`explicit` for the branch/convergence semantics; `evidenced` for the implementation gaps and allocator recovery need.

## Remaining uncertainty

A fully general convergence detector must eventually handle artifact renames/moves and more complex octopus merges. The first enforceable version can use governed companion paths/identities and ordinary two-parent merge commits, provided the limitation is explicit and the design fails safely rather than claiming complete distributed consensus.

## Commitment / disposition

Accepted as the current design frame for continuation of CYC-005. The human explicitly agreed to the cycle-branch isolation and explicit convergence rules. The allocator fast-forward is a narrow defensive consequence of directly observed stale local state and does not alter the accepted decentralized-allocation model.

## Consequence

Extend CYC-005 with prospective cycle-integration guards, explicit convergence validation, generalized predecessor-version semantics, and local allocator fast-forwarding, then dogfood those rules against temporary divergent histories and the current repository state.
