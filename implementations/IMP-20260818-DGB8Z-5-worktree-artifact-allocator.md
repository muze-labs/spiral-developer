---
id: IMP-20260818-DGB8Z-5
---

# Implementation: Worktree-local artifact identity allocator

## Scope

First executable Spiral CLI slice for distributed-safe artifact ID allocation.

## Observable behavior

- `spiral workspace init [ID]` creates or reports a stable worktree-local allocation namespace.
- `spiral allocate <TYPE>` atomically allocates one shared local sequence and prints `<TYPE>-<YYYYMMDD>-<WORKSPACE>-<N>`.
- `spiral status` reports the current worktree namespace, last sequence, next sequence, and private state path.
- Common artifact type names map to existing Spiral type codes; short codes remain accepted.
- Default namespaces are five characters drawn from an unambiguous Base32 alphabet; explicit chosen namespaces are uppercase ASCII alphanumeric values of 2–12 characters.
- allocator state lives below the worktree-specific Git directory and therefore remains outside committed project state.
- a local lock serializes concurrent allocator processes in one worktree.

## Repository locations

| Path / symbol | Role |
|---|---|
| `bin/spiral.mjs` | Repository CLI entry point and allocator implementation. |
| `package.json` | Declares the `spiral` executable and test command. |
| `test/spiral-allocator.test.mjs` | Independent clone/worktree/concurrency probes. |
| `docs/distributed-development.md` | Human-facing distributed identity and integration model. |
| `AGENTS.md`, `docs/artifact-model.md`, `docs/git-workflow.md` | Normative agent/process guidance for new identities. |
| `templates/*` | Distributed-ID placeholders for newly copied artifacts. |

## Effective provenance

Implements `DES-20260818-DGB8Z-4`, which satisfies the human-confirmed distributed artifact allocation request.

## Important implementation decisions

The allocator uses `git rev-parse --path-format=absolute --git-dir` rather than repository-root state. This is intentional: linked Git worktrees share repository objects/history but receive separate private Git directories, matching the independently concurrent allocation boundary.

The first CLI slice exposes allocation as a primitive rather than producing artifact files. Artifact types have materially different required causal metadata; generating superficially complete companion Turtle before those inputs are known would encourage invalid or invented provenance. A later `spiral new` command can build on the allocator.

## New dependencies / capabilities / permissions

Requires Node.js and Git. This slice adds no third-party package dependency and no network capability.

## Known limits

- No `spiral validate` or prospective-integration validation yet.
- No automatic collision scan at integration yet; the default namespace only makes collision unlikely, not impossible.
- No artifact skeleton generation yet.
- Workspace state can be deliberately deleted by a user; doing so after artifacts have been allocated can create a new namespace/sequence. The committed artifact identities remain intact, but operators should treat allocator state as workspace metadata worth preserving for the life of that workspace.
