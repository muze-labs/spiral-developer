---
id: CYC-005
---

# Cycle: Make Spiral Developer safe for distributed development

Repository branch: `spiral/CYC-005-distributed-development`
Branch verified: verified at cycle open against actual Git branch state; re-check before each semantic causal commit and during evaluation.

## Analyze

Project state / prior evaluation that makes this cycle relevant:

Spiral's current governed artifacts use stable human-readable IDs and filenames such as `CYC-004`, `REQ-001`, `DES-001`, and `EVD-001`. The convention works in a single advancing checkout, but concurrent writers starting from the same repository state can independently choose the same next ID for unrelated artifacts. That creates filename, RDF identity, and reference collisions that are bookkeeping accidents rather than meaningful Git conflicts.

Important risk / uncertainty / desired movement:

Remove hidden single-writer assumptions from Spiral's own coordination/provenance machinery so independently created work can be merged without a central identifier allocator. Preserve normal Git semantics: concurrent edits to the same logical source or existing artifact may still conflict and should use normal conflict resolution.

Relevant human direction / feedback:

Captured in `SRC-DIST-001`.

Governing higher-level plan / direction:

Spiral Developer's trust goal requires causal records to remain unambiguous under realistic multi-agent/multi-human development. Distributed Git is a normal target environment, so Spiral's bookkeeping should not require a single writer or centralized serialization point merely to create new artifacts.

Current position in that plan:

This follows the accepted discourse/commitment/execution cycle. The cycle goal is human-confirmed, but the mechanism is deliberately still open to discourse and inquiry. Earlier discussion mentioned collision-resistant identifiers as one candidate; no identifier format or migration design is yet committed.

## Plan

### Cycle goal

Make Spiral Developer safe for concurrent use by multiple humans and AI agents working in independent Git checkouts, branches, and forks, without requiring centralized coordination for creation of new Spiral artifacts/cycles and without adding avoidable bookkeeping merge conflicts.

### Commitment boundary

The human explicitly confirmed this distributed-development goal as the next Spiral cycle and clarified that ordinary source-file conflicts remain normal Git conflicts. The human also agreed that the solution should be discovered through this cycle rather than treating a previously discussed ID mechanism as already selected.

### Why now / why this cycle boundary

The sequential-ID collision is a concrete correctness problem that appears as soon as Spiral is used by multiple concurrent writers. Because identity participates in filenames, RDF subjects, references, Git branch conventions, and validation, treating it as a cosmetic rename would risk preserving other single-writer assumptions. One coherent cycle should first identify those assumptions, then select and test the smallest distributed-safe model.

### Plan continuity decision

`continue` — this extends Spiral's trustworthy, Git-native collaboration model to concurrent distributed development rather than changing its trust or provenance goals.

### Current starting evidence

- normative documentation and templates use examples such as `CYC-001`, `REQ-001`, `DES-001`, `IMP-001`, and `EVD-001` as stable artifact identities;
- cycle branch naming embeds the cycle identity;
- RDF subjects, `dcterms:identifier`, `sd:repositoryPath`, cross-artifact references, and commit metadata use these identities;
- no repository-local allocator/tooling was found that could make sequential allocation atomic across independent clones/forks; even such a local allocator would not coordinate disconnected writers;
- opening this cycle itself required consulting the current history and choosing the apparent next cycle number (`CYC-005`), demonstrating the bootstrap form of the single-writer assumption.

### Evaluation basis

The cycle should be judged against a concrete distributed merge scenario:

1. start two independent branches/checkouts from the same commit;
2. let each create a new cycle and several unrelated Spiral artifacts without consulting or locking the other;
3. merge the branches;
4. unrelated Spiral bookkeeping must not require identity/filename renaming or semantic reconciliation merely because both writers created artifacts concurrently;
5. all resulting artifact identities and RDF references must remain unambiguous and validator-compatible;
6. concurrent edits to the same existing source/governed artifact may still produce ordinary Git conflicts and are not a failure of the cycle.

Backward compatibility with existing accepted sequential IDs must also be demonstrated or explicitly migrated without falsifying historical provenance.

### Likely work

- inventory identifier creation/use and other single-writer assumptions across docs, templates, RDF, branch conventions, validation, and provenance references;
- distinguish artifact identity from display/order concerns;
- compare candidate distributed identity/allocation approaches without assuming the earlier ULID/UUIDv7 suggestion is correct;
- determine migration/backward-compatibility semantics for existing identifiers;
- create a two-writer merge probe that can falsify the proposed model;
- encode the accepted model in normative docs/templates/tooling/validation only after the discourse/commitment boundary is reached;
- evaluate the resulting repository using the distributed merge scenario.

### Explicit non-goals

- eliminate meaningful Git conflicts when two branches edit the same logical source or same existing governed artifact;
- introduce a centralized ID service, lock server, or mandatory online coordinator merely to preserve sequence numbers;
- renumber historical artifacts for cosmetic consistency unless evidence shows it is necessary for correctness;
- choose an identifier technology before inquiry establishes the required properties and migration consequences;
- solve general distributed consensus or collaborative-editing problems outside Spiral's own bookkeeping/provenance layer.

### Pause / re-plan conditions

Pause and return to discourse if the candidate model makes historical references ambiguous, requires rewriting published causal history, requires central coordination for ordinary artifact creation, cannot distinguish accidental bookkeeping collisions from genuine semantic conflicts, or expands into a general source-merge/consensus system rather than Spiral's own distributed-safety problem.

## Act

Important artifacts / semantic commits produced:

- pending

Material implementation decisions or deviations from the initial likely work:

- pending

Out-of-scope discoveries retained for later:

- pending

## Evaluate

Integrated result against cycle goal:

- pending

Evidence / acceptance result:

- pending

Metric or risk movement:

- pending

What changed in our understanding:

- pending

Surprises / model mismatches:

- pending

Known compromises:

- pending

Unresolved issues within current goal:

- pending

Candidate next-cycle inputs:

- pending

Human evaluation / feedback:

- pending

Cycle accepted, still open, or deliberately re-planned:

Active.

## Process learning

What context/constraint/evaluation helped:

- pending

What bookkeeping was useless:

- pending

What should the environment learn from this cycle:

- pending
