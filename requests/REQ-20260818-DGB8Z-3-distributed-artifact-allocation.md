---
id: REQ-20260818-DGB8Z-3
---

# Request: Distributed artifact allocation

## Operationalized intent

A Spiral workspace must be able to allocate new governed artifact identities independently of other concurrent checkouts, worktrees, branches, or forks, without consulting a central sequence allocator.

New distributed-safe identities use:

```text
<TYPE>-<YYYYMMDD>-<WORKSPACE>-<N>
```

The human-facing structure is part of the requirement, not merely an implementation detail:

- the date is visible as `YYYYMMDD`;
- a stable workspace namespace distinguishes independently concurrent producers;
- one unpadded local sequence is shared across all artifact types and dates in that workspace;
- existing historical identifiers remain valid and are not renamed.

## Upstream understanding

`UND-20260818-DGB8Z-2` establishes the accepted interpretation of the distributed identity model and distinguishes allocation namespace from actor provenance.

## Intended audience

Humans and AI agents using Spiral Developer in ordinary distributed Git development.

## Observable desired outcomes

### independent-allocation

Two independently concurrent workspaces starting from the same repository state can allocate new Spiral IDs without consulting each other and do not normally allocate the same identity.

### human-readable-order

A human can see the artifact type, creation date, workspace namespace, and local creation sequence directly in the ID and filename.

### one-local-sequence

Within one workspace, allocation sequence increases monotonically across artifact types and dates and is not zero-padded.

### stable-local-namespace

A workspace keeps the same namespace across commands and branch switches, while a distinct linked worktree/clone receives its own namespace unless explicitly configured otherwise.

### legacy-compatibility

Existing IDs such as `REQ-001`, `UND-DIST-002`, and `CYC-005` continue to be valid historical identities.

## Assumptions / ambiguity

| Claim | Provenance | Evidence / question |
|---|---|---|
| A small random workspace namespace is enough for the practical merge domain. | explicit / inferred | The project expects ordinary Git collaboration, not internet-scale allocation; integration validation will still detect exceptional collisions. |
| Local sequence state belongs to the independently concurrent workspace rather than the repository's committed state. | evidenced | Committed/shared state would recreate coordination conflicts. |
| The date is informational rather than an authoritative ordering source. | explicit | Git remains authoritative history; the date exists for human readability. |

## Non-goals

- globally unique identifiers across unrelated Spiral projects;
- deriving actor identity from the workspace namespace;
- replacing Git history with the local sequence;
- renaming accepted historical artifacts;
- solving prospective causal integration validation in this first allocator slice.

## Constraints already known

| Constraint | Source | Effect |
|---|---|---|
| Distributed work must not require a central allocator. | UND-DIST-001 | Workspace state must be local. |
| Linked Git worktrees can be independently concurrent. | CYC-005 | Their allocation state must not be accidentally shared. |
| The CLI should enforce only mechanical invariants. | UND-DIST-002 | Identity allocation is appropriate CLI behavior; semantic judgment is not. |

## Acceptance shape

A repository-local CLI probe should demonstrate that:

1. a workspace can initialize or automatically acquire a stable namespace;
2. successive allocations across different artifact types share and increment one unpadded sequence;
3. a second independent clone/worktree allocates under a different default namespace without coordination;
4. an explicit human-chosen namespace can be initialized and remains stable;
5. workspace allocation state is not committed to the repository;
6. legacy IDs remain accepted by documentation/model rather than migrated.
