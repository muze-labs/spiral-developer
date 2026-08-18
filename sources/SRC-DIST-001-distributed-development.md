---
id: SRC-DIST-001
---

# Source: Make Spiral Developer safe for distributed development

## Human direction

The current Spiral Developer repository uses sequential artifact identifiers and filenames. In a development environment with multiple humans or AI agents working concurrently in independent Git checkouts, branches, or forks, two writers can independently allocate the same next identifier and create unrelated artifacts with the same filename and identity.

The cycle should address the broader distributed-development requirement rather than prematurely committing to a particular identifier format:

> Make Spiral Developer safe for concurrent use by multiple humans and AI agents working in independent Git checkouts, branches, and forks, without requiring centralized coordination for artifact creation.

The immediate trigger is the sequential `.spiral` naming/identity scheme, but the cycle should inspect other hidden single-writer assumptions as well, including cycle identity, filenames, RDF subjects/references, validation, bookkeeping, and merge behavior.

Ordinary source-code conflicts are explicitly **not** failures of this goal. If two branches modify the same logical source or the same existing governed artifact, normal Git conflict detection and resolution remain appropriate. Spiral should eliminate conflicts introduced only by its own bookkeeping or identity allocation, not attempt to make semantically conflicting edits conflict-free.

The human explicitly agreed that this should be a new Spiral cycle and that the solution should be worked out by following Spiral's own discourse/inquiry process rather than treating an earlier candidate such as ULID/UUIDv7 as already decided.

## Bootstrap limitation

This source and the cycle opened from it necessarily use the repository's current identifier convention (`SRC-DIST-001`, `CYC-005`) because the distributed identifier mechanism is precisely what this cycle has not yet designed or accepted. Their use here is legacy/bootstrap behavior, not evidence that sequential allocation is the desired solution.
