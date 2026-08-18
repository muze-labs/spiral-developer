---
id: REQ-20260818-DGB8Z-14
---

# Request: Distributed cycle and convergence guards

## Operationalized intent

Extend Spiral's distributed-development safety so cycle branches cannot silently leak unfinished work into accepted history, parallel revisions of the same governed artifact cannot silently collapse at convergence, and a stale worktree-local allocator cannot reuse a slot that is already visible in its own namespace.

The controls must preserve the distributed model: independent writers still allocate and work optimistically without a central coordinator; accepted upstream work may still flow into an open cycle; integration remains the serialization/revalidation boundary.

## Upstream understanding

`UND-20260818-DGB8Z-13` establishes the accepted interpretation: cycle activity is branch-scoped, unfinished cycle work does not flow outward, stable-artifact divergence needs explicit predecessor-preserving convergence, and local allocator state may defensively fast-forward against already-visible allocations in its own namespace.

## Intended audience

Humans and AI agents using Spiral Developer concurrently across Git branches, worktrees, clones, and forks, plus repository-host integration gates that must mechanically enforce the distributed invariants.

## Observable desired outcomes

### local-allocation-never-reuses-visible-own-slot

Before allocating `TYPE-YYYYMMDD-WORKSPACE-N`, the allocator compares the local counter with already-visible distributed IDs using that same workspace namespace and starts above whichever is higher. It does not consult or serialize against other workspace namespaces.

### open-cycle-cannot-integrate-authoritatively

Prospective integration of a candidate that introduces or changes its cycle record fails while that candidate cycle remains `sd:Active`. The cycle must be `sd:Accepted` before authoritative integration can pass.

### candidate-cycle-branch-matches-cycle-id

When integration context supplies the candidate branch name, a candidate that changes one cycle record must come from `spiral/<cycle-id>` or `spiral/<cycle-id>-...`. A differently named branch fails with an actionable diagnostic.

### open-cycle-is-not-a-target-for-another-cycle

When integration context identifies the target as a different cycle branch whose corresponding cycle is still active, Spiral rejects integration of another cycle into it. This does not prohibit bringing the authoritative branch into an open cycle for reconciliation.

### parallel-artifact-revisions-require-explicit-convergence

When a merge commit introduced by a candidate combines two parent histories that both materially changed the same existing governed artifact since their merge-base, that merge commit must represent the convergence as a new artifact version retaining exact predecessor references to the latest version from each parent lineage.

A clean Git auto-merge is not sufficient evidence of reconciliation.

### predecessor-relation-applies-to-governed-artifacts

`sd:transforms` can express exact predecessor versions for any governed `sd:Artifact`. Implementation-specific transition cause/change-kind semantics remain implementation-specific.

### historical-premature-merge-remains-visible

Do not rewrite CYC-005 history to conceal that it was previously merged to `main` while still Active. Correct the process prospectively and close/reintegrate the continued cycle normally after human evaluation.

## Assumptions / ambiguity

| Claim | Provenance | Evidence / question |
|---|---|---|
| Two-parent merge commits cover the normal convergence case worth enforcing first. | evidenced | Current Git workflow uses ordinary merge commits; octopus/rename generalization can follow only if dogfooding exposes it. |
| Companion artifact paths are a sufficient first detector of the same stable artifact changing on both parent histories. | evidenced | Governed artifacts use stable Markdown/Turtle pairs and repository paths; identity-based rename handling is deferred explicitly. |
| Integration branch names are host/context metadata, not RDF truth. | explicit | Branch identity is an execution/integration boundary and may disappear after merge; stable artifact identity remains in RDF. |

## Non-goals

- coordinate disconnected copies that accidentally share a workspace namespace before their histories meet;
- prevent ordinary source-code conflicts;
- implement distributed consensus or a central cycle allocator;
- infer semantic reconciliation when the artifact itself does not record surviving predecessor versions;
- support octopus merges or arbitrary artifact renames in the first convergence detector;
- prohibit merging completed authoritative work into an open cycle branch.

## Constraints already known

| Constraint | Source | Effect |
|---|---|---|
| Git causal history is immutable. | Spiral trust model | Preserve the premature CYC-005 merge and record correction prospectively. |
| Existing legacy and distributed IDs remain valid. | CYC-005 | Allocator recovery may skip numbers but must not rename historical artifacts. |
| Host adapters must share repository-local semantics. | `UND-DIST-002` | Branch metadata may be supplied by adapters, but enforcement remains in `spiral`. |

## Important uncertainty / assumption

The highest-risk assumption is that same-path divergence captures the practically important first class of stable-artifact convergence. The cheapest falsification is to construct real temporary Git histories with clean non-conflicting edits to one governed artifact and verify that an unannotated merge is rejected while a merge version containing both exact predecessor references passes.

## Acceptance shape

Automated disposable-repository tests must establish at least:

1. stale local counter + visible same-workspace artifact advances allocation instead of reusing the slot;
2. an Active candidate cycle is rejected at prospective integration;
3. an Accepted candidate cycle on the matching cycle branch passes the branch/closure gate;
4. an open target cycle rejects another cycle candidate when branch context is supplied;
5. a clean merge commit combining independent revisions of the same governed artifact fails without both predecessor references;
6. the same convergence passes when the merge commit records both exact parent-lineage predecessors;
7. ordinary independent artifact changes remain unaffected.
