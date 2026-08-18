---
id: UND-20260818-DGB8Z-2
---

# Understanding: Workspace-scoped artifact identity with one local sequence

## Current interpretation

Spiral does not need globally unique, internet-scale artifact identifiers. It needs identifiers that independently concurrent development work can allocate without coordination and that remain unambiguous when those histories are later integrated.

The accepted identity model is:

```text
<TYPE>-<YYYYMMDD>-<WORKSPACE>-<N>
```

where:

- `TYPE` preserves the existing human-recognizable artifact kind (`SRC`, `UND`, `REQ`, `DES`, `IMP`, `EVD`, `CYC`, and so on);
- `YYYYMMDD` is the local creation date, included primarily for human readability and coarse chronological grouping;
- `WORKSPACE` is a stable namespace for one independently concurrent Git checkout/worktree, generated randomly by default or chosen explicitly when appropriate;
- `N` is one monotonically increasing, unpadded sequence shared by every Spiral artifact created in that workspace, across artifact types and dates.

The workspace namespace is allocation metadata only. It must not be interpreted as the identity of a human, AI agent, organization, or causal author. Actor provenance remains a separate concern.

The local sequence is useful to humans because it exposes creation order within one workspace without requiring globally serialized numbering. Git remains the authoritative history and chronology.

Historical sequential identifiers remain valid and must not be renamed merely for consistency.

## Sources considered

- `SRC-DIST-001` and `UND-DIST-001` established that new artifact identity must be independently allocatable without a central sequence allocator.
- `SRC-20260818-DGB8Z-1` at commit `4e1eaddb745ccef099a58d9d3d2eb299281eb1c5` records the human-confirmed workspace/date/sequence direction.

## Clarifications / reframing

| Question / assumption | Alternative or clarification | Evidence / resolution |
|---|---|---|
| Every artifact needs a UUID/ULID-strength random component. | The actual collision domain is the relatively small set of independently concurrent workspaces that may later merge. | Move randomness to the stable workspace namespace and use a local sequence for artifacts. |
| A counter must remain globally ordered. | Global creation ordering is neither required nor reliably meaningful in distributed Git. | The counter is only ordered within its workspace; Git records authoritative history. |
| Counters should reset per type or date. | Resetting adds state dimensions and weakens the simple human ordering signal. | Use one monotonic counter across all artifact types and dates. |
| Counters should be zero-padded for lexical sorting. | The visible date already provides coarse sorting, and Git provides exact chronology. | Do not zero-pad `N`. |
| A readable workspace code identifies who made the artifact. | Workspaces and actors have different lifecycle and provenance semantics. | Treat the workspace code only as a collision-avoidance namespace. |

## Current effective behavior / evidenced gap

The repository still requires writers to invent human-readable artifact IDs manually. Sequential or category-scoped conventions can collide when two independent histories create the same next identifier. No repository-local tool currently owns a stable per-workspace namespace or shared sequence.

## Provenance confidence

Explicit for the desired identity structure; evidenced for the current repository gap.

## Remaining uncertainty

- default workspace identifier length and alphabet;
- how a chosen workspace identifier is validated;
- where worktree-local state is stored so linked Git worktrees do not accidentally share a namespace/counter;
- how allocation is made safe against two concurrent `spiral` processes in one workspace;
- how much of artifact skeleton creation belongs in the first CLI slice;
- how integration validation detects the exceptional workspace/identity collision.

## Commitment / disposition

Accepted. The human explicitly agreed to try this identity model in `CYC-005`.

## Consequence

Implement the smallest allocator/CLI slice that can dogfood this model in independent workspaces, preserve legacy IDs, and provide evidence about whether the human-facing scheme remains practical in actual repository use.
