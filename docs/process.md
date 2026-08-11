# Development Process

This is the normative Spiral Developer lifecycle for feature work.

The process is iterative, not a waterfall. Upstream artifacts may be revised when reality teaches us something new. The purpose of traceability is to make those revisions and their consequences explicit.

## 1. Create a working branch

Start each feature or meaningful change on a dedicated branch from the current authoritative branch.

Prefer:

```text
spiral/<request-id>-<short-name>
```

The branch is an evolving proposed reality. The authoritative branch remains accepted project reality.

See `git-workflow.md`.

## 2. Establish current intent and its provenance

Create or identify the current request artifact, but do not automatically treat the request as the root of truth. Ask what caused the project to believe this is the needed outcome.

When origin or interpretation is materially useful, preserve the upstream chain:

> **source evidence → understanding → request**

A `SRC-*` source artifact identifies or captures what was actually expressed, observed, received, or mandated. Sources can include connected conversations, emails, tickets, meetings, contracts, regulations, observations, human reports, legacy material, or external artifacts. Chat is one source type, not a privileged root.

A `UND-*` understanding artifact records what the project currently believes one or more sources mean. Use it when clarification, interpretation, disagreement, reframing, or uncertainty could plausibly matter later. Link it to exact upstream source versions with `sd:interprets`.

If primary origin evidence is unavailable, preserve that fact explicitly. A source may record an attributed or inherited claim with `sd:sourceAvailability sd:Unavailable`; do not invent historical intent to complete the graph.

Then capture a request that describes:

- who needs something;
- what meaningful outcome they need;
- observable behavior that would indicate success;
- assumptions and ambiguities;
- known constraints;
- non-goals.

When a material understanding artifact exists, link the request to its exact version with `sd:derivedFrom`. For simple direct requests, do not create source/understanding artifacts merely for ceremony.

Commit each artifact when it has crystallized enough to guide the next step. Its commit hash becomes the version referenced by downstream artifacts.

## 3. Check consequential framing

Before committing to a solution space, ask whether the request or proposed next step contains an assumption that would materially constrain downstream work.

Do this selectively. A framing check is useful for product direction, core abstractions, architecture, schemas, trust boundaries, irreversible changes, or other choices where a different framing would plausibly change what should be built or how success should be judged. It is usually noise for local, reversible implementation details.

When the premise is still open, state it briefly and reformulate the question at the level the evidence can actually support. For example:

> **Framing check:** “How should we add caching?” assumes caching is the right response. What latency/load problem are we trying to solve, and what evidence distinguishes caching from other responses?

A coherent design is not evidence that the framing was right. **Capability is not endorsement.** If a consequential direction looks unusually elegant, test at least one materially different framing before hardening it.

Record only assumptions or reframings that are causally useful later; do not create ceremony for routine decisions.

See `ai-collaboration.md`.

## 4. Find the nearest important uncertainty

Ask:

> **What unresolved issue is most likely to prevent useful progress in the next development cycle?**

Classify risks by horizon:

- blocker;
- near-term;
- deferred;
- existential.

Resolve the blocker or nearest risk. Record later risks. Pull a deferred risk forward only if it can invalidate the current direction.

## 5. Seek meaningful interaction

Where product intent or interaction is uncertain, build the cheapest artifact that can elicit high-quality reality-based feedback from the intended audience.

For ordinary Muze web work, use frontend-first development: create enough functioning UI for intended users to spend real time with the feature.

Optimize for behavioral fidelity and learning, not visual polish, generic usability work, production infrastructure, or speculative completeness unless those are required for meaningful interaction.

Record observations separately from interpretation. If feedback changes what the project believes the source or user need means, create or revise the relevant `UND-*` artifact and then revise the request when the operationalized outcome changes. Do not rewrite the older understanding or request.

## 6. Create a traceable design

Design the smallest system needed for the current validated understanding.

Each significant design element should be able to explain why it exists:

- which request outcome it satisfies;
- which feedback changed it;
- which culture/external/legacy constraint restricts it;
- which risk it addresses;
- which other design it technically supports.

Supporting plumbing does not need invented client ancestry. Preserve the truthful chain upward.

Commit design decisions at meaningful causal boundaries. Record their links to exact upstream Git versions in the design companion Turtle resource.

## 7. Implement reality in vertical slices

Once the interaction model is credible enough, replace simulation with reality through the smallest useful vertical slice.

A slice should connect enough of the actual system to produce observable behavior, for example:

> **interface → domain behavior → state → integration → observable result**

Keep implementation causally connected to the design it realizes. Avoid unrelated cleanup and speculative future architecture.

When changing an already governed `IMP-*` unit, treat the current implementation resource as a compact checkpoint. Preserve current effective causal references that remain valid, update those whose semantics are actually superseded, and add:

- `sd:transforms` to the exact immediate predecessor implementation version(s);
- `sd:changeCausedBy` to the exact artifact version(s) that caused this revision;
- `sd:implementationChangeKind` (`BehaviorPreservingChange`, `SemanticChange`, or `MixedChange` for prospective governed work; `UnknownChange` only for reconstructed history whose transition semantics cannot be established).

Do this for material revisions, moves, replacements, splits, merges, and refactors—not formatting-only churn. Behavior-preserving refactors still retain lineage; verify preservation when it matters. Code locations may overlap across several `IMP-*` concerns.

For normal continued development, do **not** replay the full lineage by default. Work from current code, current effective provenance, relevant current design/tests/evidence, the new reason for change, and the immediate predecessor. Traverse older lineage only when current provenance is insufficient or a historical question requires it.

Create semantic implementation commits when the change has crystallized enough to serve as evidence for later verification.

See `implementation-lineage.md`.

## 8. Verify implementation against design

Verification answers:

> **Does this implementation realize the relevant design property?**

Use evidence appropriate to the claim: automated tests, property/invariant checks, integration exercises, static analysis, benchmarks, fault injection, security checks, or direct observation.

Verification should be capable of detecting plausible wrong implementations rather than merely restating internal structure.

Commit verification evidence after the implementation commit it verifies exists, so the graph can point to the exact implementation version.

## 9. Accept behavior against request

Acceptance answers:

> **Does this observable result satisfy the relevant request intent?**

Acceptance may use executable acceptance tests, intended-user interaction, stakeholder confirmation, objective domain results, or operational evidence.

Acceptance is not the same as implementation verification.

Commit acceptance evidence after the relevant request, design, implementation, and verification versions exist.

## 10. Prepare the pull request

When the AI believes the request is satisfied, it prepares a pull request containing both the result and the causal case for accepting it.

The PR should expose:

- source/understanding provenance when material;
- request/version;
- significant feedback;
- design/version;
- implementation commits, current effective provenance, and lineage/transition metadata for revised governed implementation units;
- verification;
- acceptance;
- new dependencies;
- legacy assumptions/confidence;
- deferred risks;
- unresolved questions.

CI evaluates mechanical and executable claims. Human review evaluates meaning, judgment, risk, and sufficiency of evidence.

See `review.md`.

## 11. Merge without rewriting history

Accepted feature work is integrated with a normal merge commit.

The feature commits retain their original hashes. Merge means the causal history was reviewed and admitted into authoritative project history.

Never squash or rebase causal history merely to make the log look tidy.

## Defect loop

A defect is evidence that some part of the software-producing system was inadequate.

Use:

> **observe failure → trace upward → locate earliest meaningful cause → correct upstream artifact/environment → propagate downward → verify → accept**

Possible root causes include missing or weak source evidence, source misinterpretation, request ambiguity, missing context, incorrect design, weak boundaries, missing verification, wrong acceptance criteria, dependency behavior, stale/missing effective implementation provenance, broken implementation lineage, or implementation error.

Fix the earliest meaningful cause and create new commits. Never amend old causal history to make it appear that the correct understanding existed earlier.

When the defect does not fit the current request/design model cleanly, explicitly ask whether the problem is in the implementation **or in the framing that produced the implementation**. Cheap regeneration is a reason to repair upstream assumptions, not a reason to protect already-generated code.

## Process learning

At the end of a significant cycle ask:

- Did intended users provide meaningful feedback where needed?
- Where intent interpretation mattered, could we distinguish source evidence from our understanding of it?
- Did we reduce the nearest important uncertainty?
- Did traceability improve agent or human reasoning?
- On repeated work in a governed implementation area, did current effective provenance reduce archaeology rather than require full-history replay?
- Did any superseded historical cause remain incorrectly presented as current justification?
- Did we add unjustified complexity or dependencies?
- Did we accidentally solve deferred problems?
- Did a defect improve the production environment?
- Did a consequential framing assumption go unchallenged until downstream work made it expensive?
- Did the AI contribute useful independent search, or merely elaborate the first plausible direction?
- Did we enlarge scope mainly to make the architecture/model cleaner?
- Which artifacts/links were useful?
- Which bookkeeping was ceremonial?

The process itself should improve from evidence.
