---
id: IMP-20260818-DGB8Z-16
---

# Implementation: Distributed cycle and convergence guards

## Scope

Mechanical CYC-005 enforcement for stale local allocator recovery, cycle branch/closure integration rules, and explicit predecessor-preserving convergence when parallel histories revise the same governed artifact.

## Observable behavior

- `spiral allocate` never reuses an already-visible slot in its own workspace namespace merely because the private local counter is stale; it allocates above the larger of local state and visible same-workspace sequence.
- `spiral validate integration` rejects a candidate cycle record that remains `Active`, including when the cycle TTL already exists on the target and continued cycle work changes only its Markdown companion.
- when branch metadata is supplied, candidate branch naming is checked against the changed cycle ID and a different active cycle branch cannot be used as integration target.
- candidate-introduced two-parent merge commits are inspected for stable governed artifacts changed on both parent histories; the merge version must carry exact `sd:transforms` references to both immediate predecessor commits.
- `sd:transforms` is defined on `sd:Artifact`, while implementation-specific transition metadata remains scoped to `sd:Implementation`.

## Repository locations

| Path / symbol | Role |
|---|---|
| `bin/spiral.mjs` | local allocator visible-sequence floor; integration CLI branch-context plumbing |
| `bin/spiral-rdf.py` | candidate-cycle closure/branch validation and merge-history convergence detection |
| `ontology/spiral-developer.ttl` | generalized `sd:transforms` historical predecessor relation |
| `test/spiral-allocator.test.mjs` | stale local-state allocation probe |
| `test/spiral-integration.test.mjs` | cycle closure/branch/target and parallel-convergence probes |
| `.github/workflows/spiral-integration.yml` | dogfood hosted adapter with branch metadata |
| `examples/ci/*spiral-integration.yml` | thin GitHub/GitLab branch-context adapters |
| `docs/distributed-development.md` | normative distributed branch/convergence semantics |
| `docs/git-workflow.md` | operational upstream-merge procedure and integration gate |

## Effective provenance

Implements `DES-20260818-DGB8Z-15`, which operationalizes the accepted branch-isolation and explicit-convergence interpretation from `UND-20260818-DGB8Z-13`.

## Revision lineage (when revising an existing governed IMP)

The first version of this implementation concern was committed at `90991c8ce8f4d10a55016976240c977e52c80387`. Dogfood evidence `EVD-20260818-DGB8Z-17@98cae5e915f326d358ed9e47342c8a02c609c90f` showed that candidate-cycle discovery only noticed changed TTL files, allowing this historically pre-existing Active CYC-005 branch to evade the closure gate when its TTL was unchanged. This semantic revision transforms that predecessor and treats either cycle companion (`.md` or `.ttl`) as candidate-cycle activity.

## Important implementation decisions

### Candidate delta rather than global cycle status

The closure gate looks at cycle records changed by the candidate relative to its merge-base rather than requiring every historical cycle on the target to be Accepted. A change to either the cycle Markdown or Turtle companion resolves to the canonical Turtle record for identity/status validation. This makes the rule prospective while still catching continued work on an Active cycle whose record already exists on the target; unrelated historical Active cycle records are not retroactively rejected.

### Merge commit is the convergence version

The convergence detector checks candidate-introduced two-parent merge commits. For any stable companion artifact path changed on both parent histories since their merge-base, it finds the latest parent-lineage commits touching that artifact and requires both exact references in the merge version's `sd:transforms` set.

This intentionally favors an inspectable invariant over semantic guessing. It means agents should use `git merge --no-commit` when governed artifacts may have diverged, reconcile before the immutable merge commit is created, and then verify the result.

### Conservative allocator floor

The Node allocator scans visible Turtle text for same-workspace distributed IDs without depending on Python/RDF tooling. False-positive higher numbers only create harmless gaps; missing an already-visible same-workspace allocation would risk reuse. Cross-workspace values are ignored.

## New dependencies / capabilities / permissions

None. The implementation uses the existing Node/Git/Python/rdflib boundary and adds no network or write capability to validation.

## Known limits

- parallel-convergence detection currently covers ordinary two-parent merges and stable companion paths; artifact rename/move identity matching and octopus merges are deferred;
- branch/cycle correspondence can only be mechanically checked when integration context supplies branch names; hosted adapters now do so;
- local allocator fast-forward cannot prevent disconnected duplicate workspaces from concurrently allocating the same next slot; prospective integration still detects that collision;
- the validator proves presence of both predecessor references, not that the human/agent semantically reconciled them correctly; verification/evaluation remains necessary.
