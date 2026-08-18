# Distributed Development

Spiral Developer assumes ordinary distributed Git development: multiple humans and agents may work concurrently in independent clones, checkouts, worktrees, branches, or forks.

The process must not introduce coordination conflicts merely to allocate its own bookkeeping identities.

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

The current allocator command intentionally returns only the new ID. Artifact scaffolding remains separate until Spiral has enough evidence to generate type-specific Markdown/Turtle without encouraging invalid placeholder provenance.

## Normal Git conflicts remain normal

Distributed-safe Spiral identity does not attempt to make ordinary source development conflict-free.

If two branches change the same source region or the same existing governed artifact, Git may report a normal merge conflict. Resolve it with normal Git review and conflict-resolution practice.

The defect Spiral must avoid is an **accidental bookkeeping conflict** where two unrelated new artifacts receive the same identity merely because both writers consulted the same old sequence.

## Integration revalidation

Independent branches may each be locally valid and still become causally inconsistent when combined. A clean textual merge is therefore necessary but not sufficient for Spiral integration.

The distributed model is:

> **Distributed work is optimistic; integration is serialized and revalidated.**

The later integration must validate the candidate against the actual current target/prospective merged state. If another accepted branch has superseded or changed an upstream cause, downstream work on the later branch may need to be revalidated, revised, explicitly justified, or withdrawn before merge.

The full prospective-integration validator and hosting adapters are being developed separately from the allocator primitive. They should share one `spiral` implementation rather than duplicate causal semantics in GitHub, GitLab, or other hosting configuration.
