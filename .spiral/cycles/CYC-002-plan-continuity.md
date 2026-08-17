---
id: CYC-002
---

# Cycle: Keep local cycle choices aligned with governing plans

Repository branch: `spiral/CYC-002-plan-continuity`
Branch verified: verified at cycle open against actual Git branch state; re-check before each semantic causal commit and during evaluation.

## Analyze

Project state / prior evaluation that makes this cycle relevant:

The previous process-guardrail cycle successfully made intake completeness, branch identity, and adaptive cycle sizing visible. Continued SimplyStore dogfooding then exposed a different failure: after a locally important discovery, the AI treated the newest finding as the obvious next direction and began to lose alignment with the larger implementation plan until the human explicitly told it to re-read that plan.

Nearest important risk / uncertainty / desired movement:

Prevent recent cycle findings from silently replacing an existing multi-cycle plan or roadmap while preserving Spiral's ability to revise plans when evidence genuinely warrants it.

Relevant human direction / feedback:

Captured in `SRC-PROCESS-003`.

Governing higher-level plan / direction:

Spiral Developer's own process-evolution goal: use dogfooding evidence to make trustworthy AI development more causally legible without turning the methodology into a rigid planning system.

Current position in that plan:

This is a prospective process-hardening cycle following the merged branch/intake/cycle-sizing guardrails.

## Plan

### Cycle goal

Make plan continuity explicit at next-cycle selection: when a durable multi-cycle plan/roadmap exists, the agent must re-read it, locate the current position, reconcile new evidence with it, and state whether it is continuing, revising, or deliberately deviating before proposing the next cycle.

### Why now / why this cycle boundary

The failure has now been observed directly in dogfooding and concerns the boundary between Evaluate and the next Analyze/Plan step. It is coherent as one process change and does not require redesigning cycle execution or introducing a planning ontology.

### Current starting evidence

- Spiral already prevents adjacent discoveries from silently entering the *current* cycle.
- `plan-cycle` says not to assume the newest request is highest priority, but it does not require re-reading an existing governing plan/roadmap.
- Cycle evaluation retains candidate next-cycle inputs, but recent discoveries can therefore dominate the next planning interview by salience.
- Project context has `Current direction`, `Relevant future direction`, and `Later possibilities`, but no explicit place to name a governing multi-cycle plan and current position when one exists.

### Evaluation basis

Normative guidance, prompts, templates, and agent instructions consistently require plan reconciliation before next-cycle selection without forcing a plan artifact where none exists. New causal artifacts must carry valid historical references; Turtle resources and Git ancestry must validate.

### Likely work

- retain the dogfooding observation as source evidence;
- interpret the failure as recency-driven plan drift rather than a generic planning defect;
- record one process lesson;
- update cycle/process guidance, agent instructions, project-context/cycle templates, and planning/evaluation prompts;
- verify structural and causal consistency.

### Explicit non-goals

- no new Plan ontology/artifact class;
- no mandatory long-range roadmap for every project;
- no automated priority scoring;
- no rule that plans override new evidence;
- no attempt to predict all future cycles up front.

### Pause / re-plan conditions

Pause if the existing process already enforces equivalent plan reconciliation, or if the change requires making speculative plans authoritative rather than keeping them defeasible.

## Act

Important artifacts / semantic commits produced:

Pending.

Material implementation decisions or deviations from the initial likely work:

Pending.

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

Still open pending implementation and evaluation.

## Process learning

What context/constraint/evaluation helped:

Pending.

What bookkeeping was useless:

Pending.

What should the environment learn from this cycle:

Pending.
