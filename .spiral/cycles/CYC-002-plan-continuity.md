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

- `4b4e225c1e3ff1f601dd7c4aa1613bdf33cd304a` — `SRC-PROCESS-003` plus cycle record.
- `0c31e1e98fe7e3f4f25bf4bf3e2d991bf54298da` — `UND-PROCESS-003`.
- `547438c498ce20e603aebe7090a94c1d6a4fb433` — `LES-016`.
- `db7464c7a1a008e23b00bc34bf45d086b119a91d` — prospective process/prompt/template changes.
- `EVD-PROCESS-003` — verification evidence recorded at cycle evaluation.

Material implementation decisions or deviations from the initial likely work:

No new Plan artifact/ontology was introduced. Existing durable project context gained an optional governing-plan/reference table, while the normative behavior lives at the Evaluate → Analyze/Plan boundary: Evaluate retains discoveries without ranking them; Plan re-reads any governing plan and explicitly chooses continue/revise/deliberate deviation/no governing plan.

Out-of-scope discoveries retained for later:

None yet.

## Evaluate

Integrated result against cycle goal:

Spiral now requires next-cycle planning to reconcile recent discoveries with any durable governing multi-cycle plan/roadmap. The plan is explicitly re-read, the current position is stated, and the proposal is classified as continue/revise/deliberate deviation. Projects without such a plan are not forced to invent one.

Evidence / acceptance result:

`EVD-PROCESS-003` records structural, scenario, Turtle, Git-ancestry, and branch/cycle consistency checks. Automated verification passes; human evaluation of this process change remains pending.

Metric or risk movement:

The observed between-cycle recency-drift failure now has an explicit check at both ends of the boundary: Evaluate may surface implications but not choose priority, and the next Plan step must re-read/reconcile the governing direction before selecting work.

What changed in our understanding:

Scope stability inside a cycle is insufficient to preserve strategic continuity across cycles. A process can correctly defer discoveries yet still let the newest one dominate the next planning step unless higher-level direction is reintroduced explicitly.

Surprises / model mismatches:

The existing process already warned that the newest request is not automatically highest priority, but that negative instruction did not provide a positive source of continuity. The missing operation was concrete: re-read the governing plan and state the relationship of the proposed cycle to it.

Known compromises:

Plan continuity is currently Markdown/process-level. Spiral does not version plans as a new ontology class, automatically compute current plan position, or score priority. This is intentional until dogfooding demonstrates a need.

Unresolved issues within current goal:

No structural issue remains in the proposed change. Human acceptance and subsequent dogfooding are still needed to establish whether the explicit reconciliation step is sufficient in practice.

Candidate next-cycle inputs:

If agents still exhibit recency drift despite explicit plan reconciliation, consider whether plan references/position need stronger machine-readable/versioned support. Do not add it pre-emptively.

Human evaluation / feedback:

Pending review of this branch/update.

Cycle accepted, still open, or deliberately re-planned:

Still open pending human evaluation.

## Process learning

What context/constraint/evaluation helped:

The concrete SimplyStore sequence made the distinction between useful evidence-driven replanning and accidental recency drift visible. Comparing that behavior with the existing Evaluate and Plan prompts exposed the exact missing handoff.

What bookkeeping was useless:

A new planning ontology, priority score, or mandatory long-range roadmap was unnecessary. Existing project context and cycle records can carry enough durable references for the first version.

What should the environment learn from this cycle:

A recent discovery can be both important and still not be the right next step. Preserve the discovery, then deliberately reconcile it with governing direction before changing the roadmap.
