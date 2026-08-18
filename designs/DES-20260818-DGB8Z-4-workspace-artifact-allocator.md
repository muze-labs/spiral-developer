---
id: DES-20260818-DGB8Z-4
---

# Design: Worktree-local Spiral artifact allocator

## Role

Provide the first executable `spiral` CLI substrate for independently allocating human-readable distributed Spiral artifact identities.

## Why this exists

`REQ-20260818-DGB8Z-3` requires independently concurrent Git workspaces to allocate artifact IDs without coordinating a global sequence while retaining useful human-visible date and local creation order.

## Cultural influence / constraints

Keep the first CLI slice small and high in the stack. Do not build a general workflow engine or artifact generator before dogfooding shows which creation semantics are stable. Reuse Git's own notion of a worktree-specific Git directory instead of inventing repository coordination infrastructure.

## Behavior / responsibilities

### Identity format

Allocate new IDs as:

```text
<TYPE>-<YYYYMMDD>-<WORKSPACE>-<N>
```

- `TYPE` is an uppercase Spiral artifact type code. The CLI accepts common long names (`source`, `understanding`, `request`, `design`, `implementation`, `evidence`, `acceptance`, `feedback`, `defect`, `cycle`, `constraint`, `risk`, `lesson`, `culture`, `warning-profile`, `context`) and their existing short codes.
- `YYYYMMDD` is derived from the process-local calendar date at allocation time. It is informational and human-facing, not authoritative chronology.
- `WORKSPACE` is stable for the independently concurrent Git worktree/checkout.
- `N` is the next positive integer from one sequence shared by every artifact type and date in that workspace. It is rendered without leading zeroes.

### Workspace namespace

- Resolve the current workspace's private Git directory with `git rev-parse --path-format=absolute --git-dir`.
- Store allocator state below `<git-dir>/spiral/`, which keeps it out of committed project state and gives linked Git worktrees distinct state because each linked worktree has its own Git directory.
- Generate a random workspace identifier on first allocation when none exists.
- Default generated IDs use five characters from Crockford's unambiguous Base32 alphabet. Five characters deliberately target ordinary project-scale concurrency rather than internet-scale global uniqueness.
- Allow an explicit chosen workspace identifier before allocation. Chosen identifiers are normalized to uppercase and must contain 2–12 ASCII letters/digits with no separator characters. They are namespace labels only, not actor identities.
- Once initialized, a workspace identifier cannot silently change.

### Sequence allocation

- Keep the last allocated sequence value in `<git-dir>/spiral/sequence`.
- Serialize concurrent allocation attempts inside one workspace with a local lock below the same private Git directory.
- Persist sequence updates atomically enough that interruption cannot normally duplicate the previous allocation.
- The counter never resets merely because the date or artifact type changes.

### Initial CLI surface

```text
spiral workspace init [ID]
spiral status
spiral allocate <TYPE>
```

`spiral allocate` prints exactly one allocated identifier on stdout so it can be composed by humans, agents, and future artifact-scaffolding commands.

This first slice intentionally does **not** make `spiral new` create Markdown/Turtle artifacts yet. Current artifact types have different required causal metadata; prematurely generating superficially complete but structurally invalid provenance would be worse than exposing the safe allocation primitive first. A later `spiral new` can use this allocator once creation semantics are designed.

## Boundaries

What belongs here:

- local namespace initialization;
- one worktree-local monotonic counter;
- ID formatting and type normalization;
- minimal status/introspection;
- tests proving independent allocation behavior.

What must remain outside:

- actor identity/provenance;
- global uniqueness services;
- semantic artifact completion;
- causal integration/staleness validation;
- GitHub/GitLab adapters;
- automatic branch/cycle workflow orchestration.

What change should this boundary protect us from:

Future artifact scaffolding and integration validation should be able to change without changing the already-issued artifact identity format or allocation state semantics.

## Supporting / intrinsic work

| Support | Why necessary |
|---|---|
| Repository-local Node CLI entry point | Gives Spiral one executable surface without introducing a framework. |
| Git-dir state resolution | Makes allocator state private and worktree-specific. |
| Local allocation lock | Prevents two concurrent agent processes in one workspace from receiving the same `N`. |
| CLI tests in temporary Git repositories/worktrees | Falsifies hidden sharing/single-writer assumptions before broader adoption. |

## Alternatives considered

| Alternative | Why not now | Evidence / trade-off |
|---|---|---|
| UUIDv4 per artifact | Strong uniqueness but loses visible chronology and local ordering humans value. | More entropy/length than the practical collision domain requires. |
| UUIDv7/ULID per artifact | Time-sortable but still opaque to humans without decoding and substantially longer. | Human-readable date was explicitly preferred. |
| Date + random suffix per artifact | Works, but repeated randomness gives less useful ordering than one stable workspace namespace plus sequence. | Human chose one cross-type local sequence. |
| Globally coordinated sequence | Recreates the distributed-development defect. | Violates `UND-DIST-001`. |
| Committed workspace/counter state | Independent clones would inherit/shared-edit allocation state. | Coordination conflict merely moves into a state file. |
| Build full `spiral new` now | Artifact-specific causal requirements are not uniform. | Risks generating invalid/ceremonial graph content before we understand the right interface. |

## Complexity / maintainability check

- Concepts introduced: workspace allocation namespace; worktree-local sequence.
- Dependencies introduced: Node.js runtime only for this slice; no package dependency.
- Expected change radius: CLI allocator, docs/templates describing IDs, later integration validator and scaffold commands.
- Replaceability considerations: state format is intentionally two tiny text files; allocation logic can be reimplemented in another runtime without changing IDs.
- What would make this harder for a future agent/human to change: treating the workspace code as semantic actor identity, encoding hidden ordering claims in the date, or allowing multiple independent counters.

## Verification plan

Automated probes will create temporary Git repositories and linked worktrees and establish:

1. one workspace keeps a stable namespace and increments one sequence across different artifact types;
2. rendered sequences are not padded;
3. a linked worktree gets distinct private allocator state and therefore a distinct default namespace;
4. a separately cloned repository independently initializes a distinct default namespace;
5. a chosen namespace is accepted before allocation and remains stable;
6. attempts to silently replace an initialized workspace namespace fail;
7. allocator state is stored below the worktree Git directory and is absent from `git status`.

## Deferred decisions

- `spiral new` artifact scaffolding;
- identifier-collision checks in `spiral validate` / prospective integration validation;
- whether repository/project configuration should constrain allowed custom workspace labels more tightly;
- installation/package-distribution strategy for the CLI;
- exact pre-merge integration algorithm and causal staleness relation set.
