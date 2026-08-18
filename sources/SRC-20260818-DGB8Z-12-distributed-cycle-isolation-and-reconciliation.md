---
id: SRC-20260818-DGB8Z-12
---

# Source: Distributed cycle isolation, convergence, and allocator recovery

## Source kind

Connected human conversation plus direct repository observation during CYC-005 dogfooding.

## What was actually expressed or observed

The human confirmed three distributed-development directions during continuation of CYC-005:

1. each repository-changing cycle should work on a branch named for that cycle;
2. an unfinished cycle branch must not be merged into the authoritative branch or another cycle branch, so authoritative history contains only completed cycles;
3. when an open cycle incorporates completed upstream work and the same stable artifact evolved independently on both histories, the divergence must be explicitly reconciled rather than allowing Git conflict resolution or a clean auto-merge to erase one causal branch. The resulting artifact version should record all surviving predecessor versions (for example with `sd:transforms`) and be re-verified.

The human also confirmed that merging completed authoritative work **into** an open cycle branch remains legitimate so the cycle can reconcile against current accepted reality.

After the current repository snapshot was uploaded, direct inspection exposed two dogfooding examples relevant to those rules:

- `main` contains merge commit `b24a5e8e301437561f2ed7e60486014cebae12c6` for CYC-005 while `.spiral/cycles/CYC-005-distributed-development.ttl` still has `sd:status sd:Active` and the Markdown cycle record says human acceptance is pending;
- this checkout's local allocator state was workspace `DGB8Z`, sequence `6`, while the committed repository already contains distributed artifacts allocated through `DGB8Z` sequence `11`. A subsequent local allocation would therefore reuse an already-visible slot unless the allocator first reconciles its own visible namespace.

## Origin / locator

- Human conversation continuing Spiral Developer CYC-005 on 2026-08-18.
- Uploaded repository snapshot `spiral-developer(8).zip`, inspected on 2026-08-18.
- Git commit `b24a5e8e301437561f2ed7e60486014cebae12c6` and checkout-local `.git/spiral/{workspace-id,sequence}` state.

## Primary evidence availability

Retained for repository observations; human direction is referenced from the connected conversation.

## Integrity / version

Repository observation was made against uploaded `main` at `b24a5e8e301437561f2ed7e60486014cebae12c6` before CYC-005 continuation work.

## Provenance confidence

`explicit` for the human-confirmed branch/convergence rules; `evidenced` for the allocator and premature-integration observations.

## Limitations / uncertainty

The stale local allocator state proves that a local namespace can encounter already-visible allocations after distributed history moves. It does not establish how that state became stale, and no claim is made that local scanning can prevent two disconnected copies with the same workspace namespace from concurrently choosing the same next slot. Integration collision validation remains necessary for that exceptional case.

> The Source artifact identifies or captures origin evidence. It does not claim that the source has already been interpreted correctly.
