---
id: CYC-001
---

# Cycle: Harden branch, cycle-sizing, and intake guardrails

Repository branch: `spiral/CYC-001-process-guardrails`
Branch verified: verified at cycle open against Git branch state; re-check before each semantic causal commit and during evaluation.

## Analyze

Project state / prior evaluation that makes this cycle relevant:

SimplyStore dogfooding exposed three process weaknesses in Spiral Developer itself: cycle work could continue on an older cycle branch without detection, very small cycles could become a default even after uncertainty fell, and guided brownfield intake could remain silently incomplete.

Nearest important risk / uncertainty / desired movement:

Move those three concerns from remembered advice into explicit workflow invariants without adding a heavy branch-management or intake subsystem.

Relevant human direction / feedback:

Captured in `SRC-PROCESS-002`.

## Plan

### Cycle goal

Make branch identity, cycle sizing, and intake completeness explicit enough that an AI following Spiral cannot silently miss them, while preserving Spiral's lightweight and conversational character.

### Why now / why this cycle boundary

The three changes came from the same dogfooding evaluation and all concern process-boundary visibility. They can be reviewed coherently together. Splitting them into three tiny cycles would add ceremony without isolating meaningful uncertainty; combining them with unrelated process work would weaken evaluation.

### Current starting evidence

- Branch-per-cycle is documented, but the workflow does not require repeated comparison of the active cycle ID with actual Git branch state.
- Cycle guidance emphasizes small evidence-producing steps but does not explicitly counter accidental tiny outer cycles once assumptions stabilize.
- Brownfield intake is guided and conversational, but does not persist an explicit completeness state or require every topic to receive a disposition.

### Evaluation basis

Repository guidance, prompts, and templates consistently express the new invariants; new causal artifacts carry valid historical references; all Turtle resources parse; links/paths resolve; Git branch state matches this cycle during causal commits and evaluation.

### Likely work

- retain the dogfooding feedback as source evidence;
- crystallize one understanding of the three process gaps;
- record separate lessons for branch validation, adaptive cycle sizing, and visible incomplete intake;
- update normative guidance, prompts, and templates;
- verify graph/reference and documentation consistency.

### Explicit non-goals

- no branch-management helper program;
- no formal intake ontology/state-machine implementation;
- no automated cycle-size scoring;
- no rewriting of previous process history.

### Pause / re-plan conditions

Pause if the existing process model already provides an equivalent enforceable mechanism, if the changes require incompatible artifact semantics, or if preserving the guardrails requires materially more machinery than explicit state/checks.

## Act

Important artifacts / semantic commits produced:

- `1c1c60364025fa1b280df9d35ebfbc15257d7057` — `SRC-PROCESS-002` plus cycle record.
- `1e75fd993c4555658dddca88a21f660086ca8ddf` — `UND-PROCESS-002`.
- `b09e4c9324c82a9fb5b3e0fc50eaa9958d513fff` — `LES-013`, `LES-014`, `LES-015`.
- `216c9c6a24a22619b7fcdaf6a8100299256104e8` — prospective process/prompt/template changes.
- `EVD-PROCESS-002` — verification evidence recorded at cycle evaluation.

Material implementation decisions or deviations from the initial likely work:

The previously uncommitted process edits were not committed as-is. Because the full repository exposed real Git history, the changes were re-sequenced prospectively into source → understanding → lessons → implementation → evidence so historical references could use actual ancestor hashes.

Out-of-scope discoveries retained for later:

None yet.

## Evaluate

Integrated result against cycle goal:

The process now makes all three dogfooding gaps explicit: branch/cycle identity is re-checked at causal boundaries, outer cycle size follows uncertainty/evaluation coherence rather than habitual smallness, and brownfield intake has durable completeness state plus visible unfinished topics.

Evidence / acceptance result:

`EVD-PROCESS-002` records structural, causal-reference, and scenario consistency checks. Automated verification evidence passes; human evaluation of the proposed branch remains pending.

Metric or risk movement:

The three observed silent-failure modes now have explicit detection/visibility points without adding a new runtime subsystem.

What changed in our understanding:

The full Git repository made clear that the earlier archive-only edit lacked the normal interpretation layer and exact historical references. Because nothing had been committed, that provenance could be repaired cleanly without rewriting evidence.

Surprises / model mismatches:

The repository already contained an established source → understanding → lesson → process-change → evidence pattern. The archive-only update had created lessons directly from a source summary and therefore needed alignment with that pattern.

Known compromises:

Branch checks and intake completion are explicit workflow obligations rather than dedicated enforcement programs. Cycle sizing remains a judgment supported by rationale rather than a computed rule.

Unresolved issues within current goal:

No structural issue remains in the proposed change. Human acceptance and later dogfooding are still needed to determine whether explicit checks are sufficient.

Candidate next-cycle inputs:

If agents still skip branch/intake checks in practice, consider lightweight repository-local validation tooling. Do not add it pre-emptively.

Human evaluation / feedback:

Pending review of this branch/update.

Cycle accepted, still open, or deliberately re-planned:

Still open pending human evaluation.

## Process learning

What context/constraint/evaluation helped:

Dogfooding against a real repository exposed process failures that were invisible in abstract process design; the full Git history then allowed exact provenance repair.

What bookkeeping was useless:

No additional branch manager, intake ontology, or task-level cycle model was needed to express the fixes.

What should the environment learn from this cycle:

When a process convention protects provenance or prevents silent omission, make its state/check visible at the point of failure rather than relying on an agent to remember prose guidance.
