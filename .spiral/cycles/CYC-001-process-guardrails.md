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

Pending.

Material implementation decisions or deviations from the initial likely work:

None yet.

Out-of-scope discoveries retained for later:

None yet.

## Evaluate

Integrated result against cycle goal:

Pending.

Evidence / acceptance result:

Pending.

Metric or risk movement:

Pending.

What changed in our understanding:

Pending.

Surprises / model mismatches:

Pending.

Known compromises:

Pending.

Unresolved issues within current goal:

Pending.

Candidate next-cycle inputs:

Pending.

Human evaluation / feedback:

Pending.

Cycle accepted, still open, or deliberately re-planned:

Still open.

## Process learning

What context/constraint/evaluation helped:

Pending.

What bookkeeping was useless:

Pending.

What should the environment learn from this cycle:

Pending.
