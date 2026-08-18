---
id: EVD-20260818-DGB8Z-6
---

# Verification Evidence: Distributed artifact allocation

## Claim being verified

The first `spiral` CLI allocator slice implements the accepted workspace/date/local-sequence identity model without introducing committed allocator state or requiring coordination between independently concurrent Git workspaces.

## Why this evidence exists

`REQ-20260818-DGB8Z-3` and `DES-20260818-DGB8Z-4` make distributed artifact identity a mechanical invariant rather than a naming convention that agents must remember. This evidence checks the allocator against the concrete failure modes that motivated `CYC-005`.

## Implementation under test

| Artifact/path/symbol | Commit | Role |
|---|---|---|
| `IMP-20260818-DGB8Z-5` / `bin/spiral.mjs` | `b68d89d53efad8151c1a29503fbdabe052873270` | Worktree-local namespace and sequence allocator. |
| `test/spiral-allocator.test.mjs` | `b68d89d53efad8151c1a29503fbdabe052873270` | Temporary-repository, clone, worktree, and concurrent-process probes. |
| `docs/distributed-development.md` | `b68d89d53efad8151c1a29503fbdabe052873270` | Normative human-facing semantics. |

## Evidence method

- [x] Automated test
- [x] Property/invariant check
- [ ] Static analysis
- [ ] Benchmark
- [x] Manual observation
- [x] Integration exercise
- [ ] Other:

## Result

`npm test` passes three allocator probes:

1. **chosen namespace + one sequence** — a workspace initialized as `AUKE` allocates `SRC-...-AUKE-1` then `DES-...-AUKE-2`; the sequence is shared across artifact types and is not zero-padded; allocator state leaves `git status` clean;
2. **independent distributed state** — a primary checkout, a separate clone, and a linked Git worktree independently allocate `REQ-*` identities with three distinct five-character default workspace namespaces, each beginning at local sequence `1`, without coordination or committed state;
3. **same-workspace concurrency** — twelve concurrent allocator processes in one workspace receive each sequence value `1..12` exactly once, demonstrating that the private local lock prevents duplicate local allocation.

All 83 Turtle files in the resulting repository parse successfully with a standards-conforming Turtle parser (`rdflib` used as an independent repository check for this cycle). `git diff --check` also passes.

The active cycle itself dogfooded the proposed identity shape before and after implementation:

```text
SRC-20260818-DGB8Z-1
UND-20260818-DGB8Z-2
REQ-20260818-DGB8Z-3
DES-20260818-DGB8Z-4
IMP-20260818-DGB8Z-5
EVD-20260818-DGB8Z-6
```

The first four were deliberately bootstrapped while the allocator was being specified. `IMP-...-5` and `EVD-...-6` were allocated by the implemented CLI using the same private workspace state, demonstrating continuity across the migration boundary.

## Failure cases / limits

This evidence does **not** establish the full `CYC-005` goal yet.

- It does not implement or verify `spiral validate integration`.
- It does not yet detect the exceptional case where two independently generated workspace namespaces collide.
- It does not test causal staleness introduced only by a prospective merge.
- It does not create Markdown/Turtle artifact skeletons; `spiral allocate` currently only allocates the identity primitive.
- It does not prove that five random workspace characters are optimal; it only demonstrates that the chosen project-scale default behaves as designed.
- The date is taken from the process-local calendar. This evidence verifies its rendered shape, not timezone policy across globally distributed teams.

## Evidence quality

The key tests use separate temporary Git repositories and an actual linked worktree rather than mocking Git-directory behavior. The concurrency probe launches independent Node processes rather than calling the allocator in one process, so it can detect the race condition the lock is intended to prevent. The test also checks that allocator state is invisible to `git status`, directly distinguishing private workspace metadata from committed coordination state.
