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

Captured in `SRC-DIST-001` and the later distributed-integration/CLI commitment in `SRC-DIST-002`.

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

The sequential-ID collision is a concrete correctness problem that appears as soon as Spiral is used by multiple concurrent writers. Because identity participates in filenames, RDF subjects, references, Git branch conventions, and validation, treating it as a cosmetic rename would risk preserving other single-writer assumptions. Discourse also exposed a second correctness problem: independently valid branches can become causally inconsistent when combined even where Git has no textual conflict. One coherent cycle should identify those assumptions, make distributed creation safe, and make integration revalidate the actual prospective merged state. The recurring enforcement needs are now concrete enough to justify the minimum repository-local `spiral` CLI substrate required by this cycle.

### Plan continuity decision

`continue` — this extends Spiral's trustworthy, Git-native collaboration model to concurrent distributed development rather than changing its trust or provenance goals.

### Current starting evidence

- normative documentation and templates use examples such as `CYC-001`, `REQ-001`, `DES-001`, `IMP-001`, and `EVD-001` as stable artifact identities;
- cycle branch naming embeds the cycle identity;
- RDF subjects, `dcterms:identifier`, `sd:repositoryPath`, cross-artifact references, and commit metadata use these identities;
- no repository-local allocator/tooling was found that could make sequential allocation atomic across independent clones/forks; even such a local allocator would not coordinate disconnected writers;
- opening this cycle itself required consulting the current history and choosing the apparent next cycle number (`CYC-005`), demonstrating the bootstrap form of the single-writer assumption;
- two branches can also be textually non-conflicting yet causally stale after integration: one branch may change/supersede an upstream artifact while another creates downstream work against the earlier version;
- current guidance validates branch-local history and causal ancestry but does not yet define prospective-merge causal validation against the latest authoritative target as a required integration gate;
- the repository currently documents several mechanical checks but contains no stable `spiral` executable that can serve as one reference implementation for those invariants.

### Evaluation basis

The cycle should be judged against a concrete distributed merge scenario:

1. start two independent branches/checkouts from the same commit;
2. let each create a new cycle and several unrelated Spiral artifacts without consulting or locking the other;
3. merge the branches;
4. unrelated Spiral bookkeeping must not require identity/filename renaming or semantic reconciliation merely because both writers created artifacts concurrently;
5. all resulting artifact identities and RDF references must remain unambiguous and validator-compatible;
6. concurrent edits to the same existing source/governed artifact may still produce ordinary Git conflicts and are not a failure of the cycle;
7. if branch A changes/supersedes a causal upstream while branch B independently creates downstream work against the older state, the later integration must be checked against the current target/prospective merge and must not silently admit stale causal claims;
8. a repository-local `spiral` command must provide the shared mechanical implementation needed for distributed-safe artifact creation and integration validation, so hosting adapters invoke common semantics rather than reimplement them.

Backward compatibility with existing accepted sequential IDs must also be demonstrated or explicitly migrated without falsifying historical provenance.

### Likely work

- inventory identifier creation/use and other single-writer assumptions across docs, templates, RDF, branch conventions, validation, provenance references, and integration checks;
- distinguish artifact identity from display/order concerns;
- compare candidate distributed identity/allocation approaches without assuming the earlier ULID/UUIDv7 suggestion is correct;
- determine migration/backward-compatibility semantics for existing identifiers;
- define integration as a revalidation boundary against the actual target/prospective merged state, including causal staleness that ordinary Git conflict detection cannot see;
- add intake/integration guidance that identifies the authoritative target and available pre-merge enforcement mechanism;
- introduce the minimum repository-local `spiral` CLI needed for distributed-safe creation, local validation, and prospective-integration validation, with platform-specific GitHub/GitLab/plain-Git mechanisms kept as thin adapters;
- create two-writer merge probes that can falsify both identity safety and causal-integration safety;
- encode the accepted model in normative docs/templates/tooling/validation only after the discourse/commitment boundary is reached;
- evaluate the resulting repository using the distributed merge scenarios.

### Explicit non-goals

- eliminate meaningful Git conflicts when two branches edit the same logical source or same existing governed artifact;
- introduce a centralized ID service, lock server, or mandatory online coordinator merely to preserve sequence numbers;
- renumber historical artifacts for cosmetic consistency unless evidence shows it is necessary for correctness;
- choose an identifier technology before inquiry establishes the required properties and migration consequences;
- build a comprehensive Spiral workflow engine or automate human/discourse judgment merely because a CLI now exists;
- encode separate causal semantics in GitHub, GitLab, or other hosting adapters instead of invoking the shared validator;
- solve general distributed consensus or collaborative-editing problems outside Spiral's own bookkeeping/provenance layer.

### Pause / re-plan conditions

Pause and return to discourse if the candidate model makes historical references ambiguous, requires rewriting published causal history, requires central coordination for ordinary artifact creation, cannot distinguish accidental bookkeeping collisions from genuine semantic conflicts, cannot validate the actual integration result without rewriting branch history, or expands the `spiral` CLI into a general workflow/consensus system rather than the mechanical substrate required for Spiral's distributed-safety problem.

## Act

Important artifacts / semantic commits produced:

- `a05551b12a4ba54905da2628325df6a180c9efa4` — opened the distributed-development cycle and captured `SRC-DIST-001`.
- `11f2a50` — accepted `UND-DIST-001`: durable identity must be independently allocatable; human-friendly sequence must not be required for correctness.
- `55f3eaa2864cff11253f01bc3f0b43b62bd5a1dc` — captured `SRC-DIST-002` and expanded the cycle to causal integration revalidation plus the minimum `spiral` CLI substrate.
- `ac41c524ed2cf3771bcd0c67ca9f0a37d61952a1` — accepted `UND-DIST-002`: distributed work is optimistic; integration is serialized and revalidated against the actual target.
- `4e1eaddb745ccef099a58d9d3d2eb299281eb1c5` — recorded the human-confirmed workspace/date/local-sequence identity direction as the first distributed-format Source artifact.
- `14730617e16e2a835be2717ca31726590453fdbf` — accepted the workspace-scoped identity Understanding.
- `2733d00f07052f41746f7f61602e2728dd875abc` — operationalized distributed artifact allocation as `REQ-20260818-DGB8Z-3`.
- `c62837f44c0808d5cb494c3c3a851e1c213e1e08` — accepted the worktree-local allocator design.
- `b68d89d53efad8151c1a29503fbdabe052873270` — implemented the first `spiral` CLI allocator slice and updated normative identity guidance/templates.
- `EVD-20260818-DGB8Z-6` — verifies independent clone/worktree allocation, shared local sequence behavior, and same-workspace concurrency locking.

Integration-validator design/implementation findings:

- The SHACL model currently treats `dcterms:identifier` as an opaque string; no structural validator requires sequential numbering. Changing the identifier form therefore does not inherently require rewriting the ontology or historical artifacts.
- Project namespaces already separate artifact IRIs belonging to unrelated projects. The collision domain that matters is independent histories/forks that intentionally share one project namespace and may later merge.
- Git already supplies authoritative chronology. No current trust invariant requires durable artifact IDs themselves to encode creation order, weakening the case for choosing a time-sortable identifier merely to preserve the old visual sequence.
- Existing process semantics already contain `sd:supersedes`, `sd:Suspect`, and the rule that downstream artifacts are candidates for suspect when an upstream version is superseded. The distributed-integration gap is therefore primarily enforcement/revalidation rather than inventing the concept of staleness.
- A prospective combined Git tree can be constructed without rewriting either branch using `git merge-tree --write-tree`; the reference CLI now uses that mechanism and fails cleanly when Git cannot construct a conflict-free result.
- Current/effective dependency relations are derived from the ontology's `sd:causalReference` subproperties, excluding `sd:supersedes` itself and keeping implementation-history relations outside the gate.
- Supersession only becomes integration-significant when the superseding artifact is itself live/effective (`Active` or `Accepted`); a rejected/tentative superseder does not retire an otherwise effective upstream version.
- `spiral validate` and `spiral validate integration` now share a standards-conforming RDF/Turtle parser boundary implemented for dogfooding with Python `rdflib`.

Accepted identity direction and first implementation result:

- new IDs use `<TYPE>-<YYYYMMDD>-<WORKSPACE>-<N>`;
- `WORKSPACE` is a stable worktree-local allocation namespace, random by default or deliberately chosen, and is not actor provenance;
- `N` is one unpadded monotonic sequence shared across artifact types and dates in that workspace;
- historical sequential IDs remain valid and are not rewritten;
- the first `spiral` CLI slice implements `workspace init`, `status`, and `allocate`, storing private allocator state below the worktree-specific Git directory;
- automated probes confirm independent clones/worktrees get independent namespaces and concurrent allocations inside one workspace are serialized;
- full artifact scaffolding is intentionally deferred until type-specific causal metadata can be created without placeholder/invented provenance.

Second implementation slice:

- `REQ-20260818-DGB8Z-7` operationalizes prospective integration validation and local snapshot validation.
- `DES-20260818-DGB8Z-8` defines prospective-tree construction, current/effective causal staleness, non-effective status propagation, collision detection, and the parser boundary; its current version clarifies that only live superseders retire upstream versions.
- `IMP-20260818-DGB8Z-9` implements `spiral validate` and `spiral validate integration`, shared RDF validation, distributed allocation-slot collision detection, intake integration context, and thin GitHub/GitLab/plain-Git adapter guidance/examples.
- The remaining work in this cycle is evidence/evaluation rather than another planned implementation mechanism unless the verification probes expose a flaw.

Material implementation decisions or deviations from the initial likely work:

- The artifact identity direction is now committed after human discourse: workspace namespace + visible date + one unpadded local sequence replaced the earlier UUID candidate.
- The first executable CLI slice exposes allocation as a primitive (`spiral allocate`) rather than immediately creating artifact files. This avoids generating invalid or invented type-specific causal metadata while still making the distributed identity invariant executable.
- Default workspace namespaces use five unambiguous Base32 characters. This is deliberately project-scale collision resistance rather than internet-scale global uniqueness; integration validation detects the exceptional duplicate `(WORKSPACE, sequence)` allocation slot.
- Integration acceptance is deliberately split from cycle acceptance: the human can accept a branch as ready to integrate, but the exact candidate must still pass prospective combined-state validation against the current target immediately before merge.
- The first RDF implementation uses Python `rdflib` behind a narrow helper boundary. This is a dogfooding packaging compromise, not a process commitment to a two-runtime CLI.

Out-of-scope discoveries retained for later:

- A full workflow engine, conversational-state automation, package-distribution strategy, and generic collaborative-editing/consensus support remain outside this cycle unless required to establish the agreed distributed invariants.

## Evaluate

Integrated result against cycle goal:

- Distributed artifact creation no longer depends on a repository-global next sequence: new artifacts use worktree-scoped allocation namespaces with one local sequence.
- The repository now has a minimal executable `spiral` CLI for allocation, local graph validation, and prospective integration validation.
- Prospective integration validation uses Git's combined tree and blocks mechanically explicit causal staleness/identity collisions that ordinary textual merge success would miss.
- Brownfield intake/project context now records the authoritative integration target and pre-merge validation mechanism.
- GitHub/GitLab/plain-Git adapters are kept thin and invoke the same repository-local validation semantics.

Evidence / acceptance result:

- `EVD-20260818-DGB8Z-6` verifies distributed-safe artifact allocation.
- `EVD-20260818-DGB8Z-10` verifies the prospective-integration slice with real temporary Git histories, including locally valid branches that become causally stale only when combined and reconciliation by the later candidate.
- Automated suite: 9/9 tests pass. Current repository snapshot and prospective CYC-005 integration against local `main` pass.
- Human cycle acceptance is still pending.

Metric or risk movement:

- Accidental new-artifact identity conflicts no longer require a central sequence allocator and exceptional workspace collisions are mechanically detectable.
- The previously silent risk of clean Git merges combining causally stale branches now has an explicit blocking integration check.
- Integration validity is no longer assumed to be preserved merely because a cycle was accepted earlier.

What changed in our understanding:

- The core distributed model is two-part: decentralized creation plus serialized/revalidated integration. Identity allocation alone would have fixed only the visible filename problem.
- Cycle acceptance and merge validity are distinct: human acceptance makes a candidate ready to integrate; the target-dependent validity claim must be re-established at the actual integration boundary.
- Effective supersession itself has lifecycle semantics: a rejected/tentative superseder must not retire an otherwise effective upstream version.

Surprises / model mismatches:

- The need for `spiral` emerged from several independent enforcement requirements rather than from a prior desire to build a CLI. This cycle supplied the first concrete reason to create that executable substrate.
- A first naive supersession check would have treated any `sd:supersedes` edge as effective; dogfooding the validator exposed that the superseding artifact's own status matters.

Known compromises:

- The first validator uses Node for CLI/Git orchestration and Python `rdflib` for RDF parsing. The boundary is explicit, but packaging is not yet polished.
- Current/prospective snapshot coherence is not the complete historical/range validator described elsewhere in Spiral.
- Host adapter examples were checked locally and against official documentation but not executed on hosted GitHub/GitLab CI in this local cycle. Host settings are still required to make the checks mandatory.

Unresolved issues within current goal:

- No conceptual correctness gap remains known from the local distributed scenarios. Live-host CI dogfooding may still expose adapter/packaging issues and should keep this cycle open if they prove material before human acceptance.

Candidate next-cycle inputs:

- Packaging/distribution of the `spiral` CLI only if actual adoption shows the Node+Python bootstrap is burdensome.
- Unifying current snapshot validation with full historical/range validation only when a concrete enforcement path is ready.
- A higher-level `spiral new` command only after type-specific scaffolding can preserve causal validity without placeholder provenance.

Human evaluation / feedback:

- pending review of the integrated CYC-005 result.

Cycle accepted, still open, or deliberately re-planned:

Active; implementation/evidence are ready for human evaluation.

## Process learning

What context/constraint/evaluation helped:

- Treating ordinary Git conflicts as explicitly out of scope kept the distributed problem focused on conflicts/inconsistencies introduced by Spiral itself.
- Separating local validity from integration validity exposed causal staleness that would have been missed by an identity-only cycle.
- Dogfooding the allocator and validator inside their own cycle made sequence, supersession-lifecycle, and integration-boundary assumptions observable.

What bookkeeping was useless:

- Preserving a globally meaningful sequential artifact number would have added coordination cost without adding trustworthy ordering; Git history already supplies authoritative chronology.
- Host-specific causal logic would have duplicated semantics and made verification harder; thin adapters are sufficient.

What should the environment learn from this cycle:

- Allocate artifact identity locally; validate exceptional collisions centrally at integration.
- Treat accepted distributed work as provisional with respect to a moving target and revalidate the exact combined state immediately before merge.
- Mechanical validators should challenge their own lifecycle assumptions: an edge such as `supersedes` is not effective merely because it exists on a non-effective artifact.
