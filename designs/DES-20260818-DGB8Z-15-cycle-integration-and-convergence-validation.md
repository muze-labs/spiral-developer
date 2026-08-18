---
id: DES-20260818-DGB8Z-15
---

# Design: Cycle integration and explicit convergence validation

## Role

Extend the existing CYC-005 allocator/integration substrate with three narrow controls: local counter recovery, cycle branch/closure integration guards, and merge-history validation for parallel revisions of the same governed artifact.

## Why this exists

`REQ-20260818-DGB8Z-14` requires Spiral to keep unfinished cycle work out of authoritative history and preserve both causal lineages when independently revised stable artifacts converge. The uploaded repository also demonstrated that worktree-local allocator state can lag already-visible allocations in its own namespace.

## Cultural influence / constraints

Keep the mechanism high in the stack and Git-native: use existing artifact status, branch identity, Git merge history, and historical references rather than introducing a lock service, central cycle registry, or collaborative-editing protocol. Fail on mechanically provable missing reconciliation; do not pretend to infer semantic correctness.

## Behavior / responsibilities

### 1. Defensive local allocator fast-forward

Inside the existing allocation lock:

1. initialize/read the stable worktree workspace ID;
2. read the local sequence file;
3. scan visible non-`.git` Turtle text for distributed-format IDs in the same workspace namespace;
4. take `floor = max(local sequence, highest visible same-workspace sequence)`;
5. persist/return `floor + 1` as the next allocation.

The scan is intentionally conservative and local. It may skip numbers if it sees a same-workspace distributed ID in a reference or example; gaps are harmless and reuse is forbidden. It must not choose the highest sequence across other workspaces.

This protects against stale copied/restored local state once conflicting allocations are already visible. Two disconnected copies with the same workspace can still allocate the same next slot concurrently; the existing integration collision validator remains the backstop.

### 2. Candidate cycle identification

For `spiral validate integration --base <target> --head <candidate>`:

- resolve base/head commits as today;
- compute the candidate delta relative to the base using the merge-base-to-head diff;
- identify changed `.spiral/cycles/*.ttl` records in that candidate delta;
- parse cycle identities/status from the candidate/prospective RDF graph.

The first enforceable rule expects at most one candidate cycle record to be introduced/changed by one cycle branch. More than one changed cycle record is reported as ambiguous cycle integration rather than guessed.

Historical Active cycle records already present unchanged on the base do not make a new candidate fail. This is important because earlier Spiral history predates the prospective branch-closure rule.

### 3. Closure gate

If the candidate delta contains one cycle record, that cycle must be `sd:Accepted` in the prospective combined state. `sd:Active` means the cycle is still open and integration fails.

This separates:

- **working branch state** — cycle may be Active;
- **integration candidate state** — cycle must already be Accepted.

The rule is prospective. It does not rewrite or relabel earlier merges that happened before the invariant existed.

### 4. Branch/cycle correspondence

Integration accepts optional branch metadata:

```text
--base-branch <name>
--head-branch <name>
```

When `--head-branch` is supplied and the candidate changes one cycle record, the branch must equal `spiral/<cycle-id>` or begin `spiral/<cycle-id>-`.

If `--base-branch` identifies a different cycle branch and that target cycle is Active at the base commit, integration fails: an open cycle is not an integration target for another cycle.

Branch metadata is integration context, not persistent artifact identity. Hosted adapters should pass it; local validation without branch metadata still enforces the closure gate but cannot prove branch naming.

Bringing authoritative `main` into an open cycle is not modeled as "candidate integration" and remains allowed. After such a merge the cycle runs ordinary snapshot/history validation and any convergence checks on its introduced merge commit.

### 5. Detecting parallel stable-artifact revision at merge commits

Integration validation examines merge commits introduced by the candidate (`base..head`). For each ordinary two-parent merge commit `M`:

1. let parents be `P1` and `P2` and compute their merge-base `A`;
2. list governed companion artifact paths (`*.md` / `*.ttl` outside templates/examples) changed on `A..P1` and `A..P2`;
3. map changed companion paths to governed Turtle artifact definitions;
4. when the same stable artifact identity exists on both parent lineages and its companion path changed on both sides, treat it as a divergent stable-artifact revision;
5. find the latest commit on each parent lineage that changed that artifact companion path after `A` (`L1`, `L2`);
6. inspect the artifact version in merge commit `M` and require `sd:transforms` references to exact predecessor versions `(artifact, L1)` and `(artifact, L2)`.

The merge commit is therefore the explicit convergence version. For a clean Git auto-merge, the agent should use `git merge --no-commit <upstream>` (or amend the uncommitted merge result before creating the merge commit), add both predecessor references, reconcile effective provenance deliberately, and then commit the merge. Once the merge commit exists, it is immutable causal history.

If normal Git conflict resolution is needed, the same rule applies: resolving text is necessary but the merge artifact must still record both predecessor versions.

### 6. Generalize `sd:transforms`

Change the RDF domain of `sd:transforms` from `sd:Implementation` to `sd:Artifact` and define it as a historical predecessor-version relation for material revision/replacement/split/merge/reconciliation of governed artifacts.

Implementation lineage keeps using it exactly as before. `sd:changeCausedBy` and `sd:implementationChangeKind` remain implementation-specific.

No claim is made that every edit to every artifact needs a transform edge. The new mandatory case is a material parallel convergence where omission could erase one lineage. Existing implementation-lineage rules remain mandatory for governed implementation revisions.

## Boundaries

What belongs here:

- local prevention of already-visible same-workspace slot reuse;
- prospective candidate-cycle closure checks;
- optional branch-name/target-cycle integration context;
- two-parent merge convergence checks for stable governed artifacts;
- general predecessor-version vocabulary needed by that check.

What must remain outside:

- distributed locking/consensus;
- semantic judgment about whether the reconciled artifact is correct;
- branch-protection configuration itself;
- octopus merge and rename/move generalization until a concrete need appears;
- full historical/range causal validation beyond the introduced merge-convergence check.

What change should this boundary protect us from:

A future implementation should not turn Spiral into a workflow engine merely to enforce these mechanical invariants. The CLI should remain a verifier/allocator around Git and RDF facts.

## Supporting / intrinsic work

| Support | Why necessary |
|---|---|
| Extend GitHub/GitLab adapter examples with base/head branch metadata. | Hosted checks are where branch naming can be known reliably before merge. |
| Add disposable real-Git merge tests. | The convergence rule depends on actual parent histories and merge commits; mocked RDF is insufficient. |
| Update distributed/cycle/Git/lineage docs. | The branch flow and merge-commit reconciliation procedure must be operationally clear to agents/humans. |

## Alternatives considered

| Alternative | Why not now | Evidence / trade-off |
|---|---|---|
| Store a global current-cycle pointer. | Reintroduces shared mutable state and merge contention. | Branch scope already supplies the needed context. |
| Ban merging main into open cycles. | Makes parallel work unnecessarily stale and prevents deliberate reconciliation against accepted upstream changes. | Human explicitly allowed this direction. |
| Treat any clean Git merge as artifact convergence. | Can combine or discard independently evolved meaning without preserving predecessor lineages. | This is the core newly identified trust gap. |
| Introduce `sd:reconciles` as a new relation. | Existing `sd:transforms` already has exact predecessor/version semantics; broadening its domain is smaller and query-compatible. | Human explicitly identified `sd:transforms` as an appropriate representation example. |
| Scan global highest sequence before allocation. | Would conflate namespaces and recreate a project-global allocator assumption. | Only own-workspace visible reuse needs local recovery. |
| Require remote/network lookup during allocation. | Breaks offline/distributed creation and adds a coordinator. | Existing integration collision gate is sufficient for disconnected duplicate namespaces. |

## Complexity / maintainability check

- Concepts introduced: candidate cycle delta; explicit merge convergence version; local visible-sequence floor.
- Dependencies introduced: none beyond existing Git, Node, Python/rdflib.
- Expected change radius: allocator helper, integration-validator orchestration/RDF helper, ontology, tests, host adapter examples, distributed/cycle/Git/lineage docs.
- Replaceability considerations: branch metadata remains optional CLI input; RDF/Git analysis stays behind existing validator boundary.
- What would make this harder for a future agent/human to change: trying to infer all semantic merges or all rename histories automatically. Keep the first detector narrow and mechanically explainable.

## Verification plan

Use real temporary repositories to verify:

- same-workspace visible slot floors allocation above stale local state;
- Active candidate cycle fails, Accepted cycle passes;
- misnamed candidate branch fails when branch metadata is supplied;
- a different open target cycle fails as integration target;
- two parent histories independently make non-conflicting material changes to one governed artifact, Git creates a clean merge, and Spiral rejects the unannotated merge;
- recreating the merge with both exact `sd:transforms` predecessor references passes;
- unrelated artifacts changed on separate histories do not trigger convergence errors;
- existing allocator/integration tests remain green.

## Deferred decisions

- identity-based detection across artifact file renames/moves;
- octopus-merge convergence;
- a dedicated `spiral merge-upstream` helper that could create a `--no-commit` merge and scaffold predecessor references;
- making branch metadata mandatory for all local integration invocations rather than required only in hosted/known-context adapters.
