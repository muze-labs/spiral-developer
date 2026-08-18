---
id: SRC-20260818-DGB8Z-1
---

# Source: Human direction for distributed artifact identity

## Source kind

Connected human/AI design discourse during `CYC-005`.

## What was actually expressed or observed

The human rejected the need for internet-scale random identifiers for Spiral artifacts. A Git project normally has a modest number of concurrent writers, and integration validation can detect the exceptional collision.

The human then proposed moving randomness from every artifact into a stable identifier for the independently concurrent development workspace that produces artifacts. The agreed direction is:

- each independently concurrent checkout/worktree has a stable random or deliberately chosen workspace identifier;
- all governed Spiral artifacts created from that workspace share one monotonically increasing local sequence, regardless of artifact type;
- artifact IDs include the artifact type, a human-readable creation date, the workspace identifier, and the local sequence;
- the local sequence does not reset by artifact type or by date;
- sequence values are not zero-padded; the date already provides useful coarse chronology and preserving lexical numeric order is not a requirement;
- the workspace identifier is an allocation namespace, not an actor identity or provenance claim.

The intended shape is:

```text
<TYPE>-<YYYYMMDD>-<WORKSPACE>-<N>
```

For example:

```text
CYC-20260818-K7M4-1
SRC-20260818-K7M4-2
UND-20260818-K7M4-3
DES-20260819-K7M4-4
```

The human explicitly agreed to try this approach in the active distributed-development cycle.

## Origin / locator

Human/AI conversation on 2026-08-18 during `CYC-005`.

## Primary evidence availability

Retained in the conversation context and represented here as a source record.

## Integrity / version

This artifact is the first deliberate dogfood use of the proposed distributed identifier shape. Its workspace namespace was bootstrapped locally before the allocator CLI exists.

## Provenance confidence

Explicit.

## Limitations / uncertainty

The exact default workspace-ID alphabet/length, local state location, allocation locking mechanism, and CLI interface remain implementation/design choices. The human direction establishes the identity structure and semantics, not those lower-level details.
