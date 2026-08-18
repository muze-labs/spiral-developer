# Distributed Development

Spiral Developer assumes ordinary distributed Git development: multiple humans and agents may work concurrently in independent clones, checkouts, worktrees, branches, or forks.

The process must not introduce coordination conflicts merely to allocate its own bookkeeping identities, and locally valid branches must not be assumed to remain causally coherent after other work has integrated.

> **Distributed work is optimistic; integration is serialized and revalidated.**

## Distributed artifact identity

New governed artifacts use an independently allocatable identity:

```text
<TYPE>-<YYYYMMDD>-<WORKSPACE>-<N>
```

For example:

```text
SRC-20260818-K7M4-12
UND-20260818-K7M4-13
DES-20260819-K7M4-18
```

The parts mean:

- `TYPE` — the existing human-recognizable artifact kind;
- `YYYYMMDD` — the local creation date for human readability and coarse chronological grouping;
- `WORKSPACE` — a stable allocation namespace for one independently concurrent Git worktree/checkout;
- `N` — one monotonically increasing, unpadded local sequence shared by all artifact types and dates in that workspace.

The workspace code is **not** an actor identity, author identity, machine identity, or causal claim. It exists only to prevent unrelated concurrent writers from allocating the same local sequence into the same artifact namespace.

Git remains the authoritative history and ordering mechanism. The date and sequence are human navigation aids, not an independent version system.

Historical IDs such as `REQ-017`, `UND-DIST-002`, and `CYC-005` remain valid. Do not rename old artifacts merely to adopt the distributed form.

## Worktree-local allocation state

The reference CLI stores the workspace namespace and local sequence below the current worktree's private Git directory, resolved with:

```text
git rev-parse --path-format=absolute --git-dir
```

The state is therefore outside the committed tree and is not inherited as shared project content. Linked Git worktrees receive distinct private Git directories and therefore distinct allocation state.

Initialize a chosen workspace namespace before the first allocation when useful:

```text
spiral workspace init AUKE
```

Or let the first allocation generate a short random namespace:

```text
spiral allocate source
```

Inspect the state with:

```text
spiral status
```

Before consuming the next number, the allocator also scans the checked-out Turtle for already-visible distributed IDs in **its own workspace namespace**. If the visible maximum is higher than the private sequence file, it fast-forwards the local floor and allocates above it. This prevents stale/restored local state from reusing a slot the checkout can already see. It does not inspect other workspace namespaces and does not coordinate disconnected copies that accidentally share one workspace ID; the integration collision check remains the backstop for that exceptional case.

The allocator returns only the new ID. Artifact scaffolding remains separate until Spiral has enough evidence to generate type-specific Markdown/Turtle without encouraging invalid placeholder provenance.

## Normal Git conflicts remain normal

Distributed-safe Spiral identity does not attempt to make ordinary source development conflict-free.

If two branches change the same source region, Git may report a normal merge conflict. Resolve source text with normal Git review and conflict-resolution practice.

For a **governed artifact**, however, textual conflict resolution is not the whole trust problem. If both parent histories materially revised the same stable artifact, the merge version must explicitly preserve both predecessor lineages; a clean Git auto-merge is not evidence that the meanings were deliberately reconciled. See **Explicit convergence of parallel artifact revisions** below.

The defect Spiral must avoid is an **accidental bookkeeping conflict** where two unrelated new artifacts receive the same identity merely because both writers consulted the same old sequence.

## Local validation

Run:

```text
spiral validate
```

before proposing integration and whenever local changes may have affected Spiral graph coherence.

The current validator checks the present Turtle snapshot for:

- Turtle parse failures;
- duplicate governed artifact definitions/identifiers;
- duplicate distributed allocation slots (`WORKSPACE` + local sequence);
- live (`Active`/`Accepted`) artifacts that still depend through current/effective causal relations on exact versions now explicitly superseded;
- live artifacts that depend on artifacts currently marked `Suspect`, `Superseded`, or `Rejected`.

This is a **snapshot/coherence** check. It does not replace the historical/range validation described in `causal-validation.md`, and it does not decide whether evidence or a superseding decision is semantically correct.

## Prospective integration validation

A branch can be valid in isolation and become invalid when combined with a newer target branch. A clean textual merge is therefore necessary but not sufficient.

Immediately before integration, validate the state Git would actually combine:

```text
spiral validate integration --base <current-target> --head <candidate> \
  --base-branch <target-name> --head-branch <candidate-name>
```

The reference implementation resolves both arguments to commits and asks Git to construct the prospective merge tree without checking it out or rewriting either history. If Git cannot construct a clean merge, resolve the ordinary Git conflict first. If it can, Spiral validates the combined Turtle graph plus candidate merge history. `--base-branch` / `--head-branch` are optional for local use but should be supplied by hosting adapters when known so branch/cycle correspondence can be enforced mechanically.

The important invariant is:

> **A cycle may be accepted as ready to integrate, but integration is allowed only if that exact candidate remains causally coherent against the current integration target.**

If another branch has meanwhile superseded an exact upstream version that the candidate still treats as effective causality, the later integration is responsible for reconciliation. Typical responses are to update/revalidate the affected downstream artifact, move it out of effective status, or abandon the affected work. Do not solve this by distributed locking merely to prevent legitimate branches from diverging.

`sd:supersedes` is itself transition/current-state information, not a dependency that must remain current; otherwise every supersession would invalidate itself. Historical transition relations such as `sd:transforms` and implementation transition provenance such as `sd:changeCausedBy` remain outside current/effective causal-dependency checking.

## Cycle branches are isolation boundaries

For ordinary repository-changing work, one open cycle lives on one branch named for that cycle. The branch is the scope of unfinished work; there is no project-global "current cycle" pointer.

The integration rules are directional:

- **open cycle → authoritative branch:** forbidden; the candidate cycle must already be `sd:Accepted`;
- **open cycle → another open cycle:** forbidden; unfinished cycles do not become causal foundations for each other by merging branches;
- **authoritative branch → open cycle:** allowed, and often necessary so a long-running cycle can reconcile against newly accepted upstream work;
- **accepted cycle → authoritative branch:** allowed only after normal review and prospective integration validation.

When branch metadata is available, the integration validator requires a candidate that changes one cycle record to come from `spiral/<cycle-id>` or `spiral/<cycle-id>-...`. Existing historical Active cycle records that are unchanged on the target do not retroactively invalidate new candidates; the rule is prospective.

This gives the authoritative branch a clear intended meaning: **completed cycle outcomes only**. If older history violated that rule, preserve the evidence and correct the process prospectively rather than rewriting Git history.

## Explicit convergence of parallel artifact revisions

When an open cycle incorporates accepted upstream history, inspect the merge as a semantic convergence point. If both merge parents materially revised the same stable governed artifact since their common ancestor, the merge commit is a new version of that artifact and must record both surviving immediate predecessor versions with `sd:transforms`.

Conceptually:

```text
artifact@A ──> artifact@left ──┐
                              ├──> artifact@merge
artifact@A ──> artifact@right ─┘
```

The merge version's companion Turtle records exact references to both `artifact@left` and `artifact@right`. It must also reconcile current/effective provenance to what actually survives. Verification is then repeated where the reconciliation makes claims that matter.

For a clean upstream merge, prefer:

```text
git merge --no-commit <authoritative-branch>
# inspect/reconcile any governed artifact changed on both histories
# add both sd:transforms predecessors to the merge version
git commit
```

If Git reports a conflict, resolving the text is still necessary, but the same lineage rule applies before the merge commit is created. Do not create an unannotated semantic merge commit and plan to amend it later; published causal commits remain immutable.

`sd:transforms` is therefore a general historical predecessor-version relation for governed `sd:Artifact` versions. Implementation lineage continues to use it, while `sd:implementationChangeKind` and `sd:changeCausedBy` remain implementation-specific transition metadata.

The first reference detector covers ordinary two-parent merges and stable companion paths. Rename/move and octopus-merge generalization should be added only when concrete use demonstrates the need; do not claim that the current detector solves arbitrary distributed collaborative editing.

## Integration context belongs in intake

A project adopting Spiral should establish, in durable project context:

- the authoritative integration branch/ref;
- how candidate work reaches it (pull/merge request, direct protected integration, or another explicit boundary);
- which mechanism runs `spiral validate integration` or equivalently validates an already-created prospective merged result;
- whether the hosting platform provides a merge queue/train or another serialization mechanism when several accepted changes may integrate concurrently.

This is an intake concern because an agent should know from the start that local validity is provisional until integration validation succeeds. `Unknown`, `Not relevant`, and a deliberate manual gate remain valid dispositions where appropriate.

## Hosting adapters stay thin

GitHub, GitLab, and plain Git should not each implement their own interpretation of Spiral causality. Their job is to arrange the correct Git state and invoke the repository-local validator.

### Plain Git / other CI

Before updating the authoritative ref, fetch/resolve its actual current tip and run:

```text
spiral validate integration --base <authoritative-tip> --head <candidate-tip> \
  --base-branch <authoritative-name> --head-branch <cycle-branch-name>
```

Only update the authoritative ref when the command succeeds and the repository's normal human/CI gates pass. If the target moves before the actual update, re-run against the new target.

### GitHub

For a pull-request check, run the prospective integration validator against the pull request's current base and head commits. If GitHub Merge Queue is used, the required Spiral workflow must also run for the `merge_group` event so the check applies to the merge-group commit GitHub is actually considering.

A minimal adapter example is in `examples/ci/github-spiral-integration.yml`. Spiral Developer itself dogfoods the same adapter at `.github/workflows/spiral-integration.yml`; repository-host settings must still make that check required if it is to block merges.

References:

- https://docs.github.com/actions/using-workflows/events-that-trigger-workflows#pull_request
- https://docs.github.com/actions/using-workflows/events-that-trigger-workflows#merge_group

### GitLab

A normal merge-request pipeline runs on source-branch content, so a portable adapter can fetch the current target and invoke `spiral validate integration` explicitly. When GitLab merged-results pipelines are enabled, GitLab instead tests a temporary commit containing source + target; merge trains extend this by testing queued merge requests with earlier queued changes.

A minimal adapter example is in `examples/ci/gitlab-spiral-integration.yml`.

References:

- https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/
- https://docs.gitlab.com/ci/pipelines/merged_results_pipelines/
- https://docs.gitlab.com/ci/pipelines/merge_trains/

## Current implementation boundary

The first reference validator deliberately remains small:

- Node provides the `spiral` command and Git orchestration;
- a narrow Python helper uses `rdflib` for standards-conforming Turtle/RDF parsing;
- `requirements.txt` declares that parser dependency;
- host adapters invoke the same local semantics rather than duplicating them.

This two-runtime packaging is a dogfooding compromise, not a process invariant. Consolidate or package it differently only when real use makes that worthwhile.
