---
id: UND-DIST-001
---

# Understanding: Distributed development must not depend on coordinated bookkeeping identity

## Current interpretation

Spiral Developer must support multiple humans and AI agents creating new Spiral cycles and governed artifacts concurrently in independent Git checkouts, branches, and forks without consulting a shared allocator merely to obtain an unused identifier.

The goal is **not conflict-free distributed editing**. Git should continue to surface meaningful conflicts when concurrent work changes the same logical source or the same existing governed artifact. Spiral's responsibility is narrower: its own identity, filename, RDF-reference, and bookkeeping conventions must not manufacture conflicts between otherwise unrelated concurrent work.

The current sequential identifier convention conflates at least two concerns:

1. **durable identity** — the stable token by which an artifact is named and referenced; and
2. **human-friendly order/sequence** — the apparent chronological or local numbering conveyed by values such as `REQ-017` or `CYC-005`.

Distributed correctness requires durable identity to be allocatable independently. Human-friendly ordering may still be useful, but it must not be a prerequisite for correctness or require disconnected writers to coordinate.

No particular identifier technology is implied by this Understanding. ULID, UUIDv7, namespaced identifiers, content-derived identifiers, Git-derived identifiers, or another mechanism remain candidate designs until their properties and migration consequences are compared.

## Sources considered

- `SRC-DIST-001` at the cycle-opening commit records the human direction to make Spiral safe for concurrent distributed development and explicitly preserves normal Git conflict semantics.
- Repository inspection shows current cycle and governed-artifact conventions use stable human-readable identifiers in filenames, RDF subjects, `dcterms:identifier`, paths, branch names, and cross-artifact references, while no cross-clone allocator exists.
- The human subsequently confirmed the checkpoint interpretation, current behavior, evidenced gap, and material assumptions, with no current objections.

## Clarifications / reframing

| Question / assumption | Alternative or clarification | Evidence / resolution |
|---|---|---|
| The problem is that sequential filenames can collide. | The filename collision exposes a broader identity problem because the same token also appears in RDF identity and references. | Repository inspection and `SRC-DIST-001`; accepted as the cycle framing. |
| Distributed-safe means Spiral should prevent all merge conflicts. | Only accidental conflicts introduced by Spiral bookkeeping should be eliminated. Concurrent edits to the same logical source/artifact remain normal Git conflicts. | Explicit human clarification in `SRC-DIST-001`; confirmed in discourse. |
| The solution is ULID or UUIDv7. | Those are candidates, not requirements. The cycle should first establish required identity properties and compare mechanisms. | Explicit cycle commitment boundary; confirmed in discourse. |
| Sequential creation order is part of artifact identity. | Sequence/order may be useful for humans, but distributed correctness should not depend on a globally serialized sequence. | No objection at the human confirmation checkpoint; remains a design premise to test rather than an implementation choice. |
| Existing sequential artifacts should be renumbered. | Historical IDs should remain valid unless evidence shows migration is necessary for correctness; rewriting published provenance would itself be risky. | Cycle non-goals and trust/history invariants. |

## Current effective behavior / evidenced gap

Current artifacts and cycles commonly use identifiers such as `CYC-005`, `REQ-001`, `DES-001`, and `EVD-001`. Writers infer or choose the next unused value from the repository state they can see. That works while one visible history advances serially, but it cannot guarantee distinct identities for disconnected writers that start from the same commit.

Two independent writers can therefore create unrelated artifacts with the same identifier and path. On merge, Git then sees the same path while the RDF graph sees the same subject/identifier even though the artifacts are semantically unrelated. Resolving that requires renaming or re-identifying one artifact and repairing references: a conflict caused solely by Spiral's bookkeeping rather than by overlapping product intent.

The gap is evidenced structurally: no local algorithm that selects the "next" sequence value from one checkout can know which value a disconnected checkout is selecting at the same time, and no repository mechanism currently provides collision-resistant independent identity creation.

## Provenance confidence

`explicit` for the desired distributed-development behavior and normal-Git-conflict boundary; `evidenced` for the current single-writer/collision behavior.

## Remaining uncertainty

- whether identities need practical global uniqueness across all Spiral repositories/forks or only collision resistance among histories that may later merge;
- which identifier properties matter beyond collision resistance: lexicographic time ordering, compactness, recognizability, offline generation, monotonicity, privacy/leakage, implementation availability, or typo detection;
- whether human-facing sequence/display labels should remain, be assigned only after integration, or be dropped;
- how branch conventions and any tooling should use the new identity;
- the smallest backward-compatible migration rule for existing sequential IDs;
- whether any hidden single-writer assumptions exist beyond identifier allocation and should be handled in this cycle.

These uncertainties affect design, not the accepted outcome.

## Commitment / disposition

Accepted as the basis for downstream design in `CYC-005`. The human confirmed the presented Understanding, current effective behavior, evidenced gap, and material assumptions on 2026-08-18 and reported no current objections.

This acceptance authorizes inquiry and design within the distributed-development cycle; it does not select an identifier mechanism.

## Consequence

Inventory remaining single-writer assumptions and compare plausible distributed identity models against explicit criteria. Before encoding the mechanism, use a two-writer merge probe to distinguish candidate approaches and bring any material architectural tradeoff back into discourse.
