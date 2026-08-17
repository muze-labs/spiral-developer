---
id: CYC-003
---

# Cycle: Prioritize risk by downstream leverage

Repository branch: `spiral/CYC-003-risk-leverage`
Branch verified: verified at cycle open against actual Git branch state; re-check before each semantic causal commit and during evaluation.

## Analyze

Project state / prior evaluation that makes this cycle relevant:

Recent process-hardening cycles made cycle sizing, intake completeness, branch discipline, and plan continuity explicit. Discussion of the existing risk guidance then exposed a smaller but important gap: Spiral can identify many risks, but its live process still prioritizes them largely through horizon labels rather than through the cost of learning an upstream assumption is wrong after downstream work depends on it.

Important risk / uncertainty / desired movement:

Make risk-driven cycle selection sensitive to uncertainty, downstream blast radius, late-discovery cost, and cheap falsifiability without turning Spiral into a risk-register process.

Relevant human direction / feedback:

Captured in `SRC-RISK-001`.

Governing higher-level plan / direction:

Spiral Developer's process-evolution goal: use dogfooding evidence to improve trustworthy AI development while removing or avoiding ceremony that does not earn its cost.

Current position in that plan:

This follows the cycle-boundary and plan-continuity guardrails. It refines how candidate risks influence cycle selection and evaluation; it does not introduce a new process phase.

## Plan

### Cycle goal

Replace horizon-first risk prioritization with a lightweight leverage heuristic: give disproportionate attention to uncertain assumptions whose failure would invalidate substantial downstream work, especially when they can be tested cheaply now.

### Why now / why this cycle boundary

The existing process already has risk discovery, durable `RSK-*` artifacts, warning profiles, and cycle selection. The missing piece is a small prioritization rule across those mechanisms. The change can be evaluated coherently across current planning/evaluation guidance without introducing new ontology or tooling.

### Plan continuity decision

`continue` — this is a direct refinement of the existing process-hardening direction. It does not replace the governing plan with a local discovery; it addresses a weakness in the current risk-selection mechanism.

### Current starting evidence

- Risk discovery is already broad and intentionally profile-driven.
- The live process currently asks for blocker/near-term/deferred/existential classification and tends to choose the nearest risk.
- Earlier strategy/business assumptions can invalidate substantially more downstream work than local implementation choices.
- The human explicitly prefers a lightweight heuristic over matrices, scores, registers, or another formal between-cycle state.

### Evaluation basis

Normative guidance, prompts, templates, and agent instructions should consistently use downstream leverage/late-discovery reasoning for prioritization while preserving existing risk horizons only where they add useful durable disposition. No new mandatory risk artifact, score, matrix, or process phase should appear. Turtle/history validation must remain sound.

### Likely work

- retain the human direction as source evidence;
- interpret the intended lightweight model;
- record one reusable process lesson;
- update risk catalog, cycle/process guidance, prompts/templates, agent instructions, and concise public guidance;
- verify structural, causal, and repository consistency.

### Explicit non-goals

- no numeric risk scoring;
- no probability/impact matrix;
- no mandatory risk register;
- no new ontology class for the four rough levels;
- no new between-cycle state or meeting;
- no rule that upstream risk automatically outranks concrete urgent harm.

### Pause / re-plan conditions

Pause if the change would require formalizing the four positions as rigid taxonomy, if current process semantics depend on mandatory horizon classification for correctness, or if the heuristic conflicts with plan continuity by automatically overriding the governing roadmap.

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

Pending review.

Cycle accepted, still open, or deliberately re-planned:

Still open pending implementation/evaluation.

## Process learning

What context/constraint/evaluation helped:

Pending.

What bookkeeping was useless:

Pending.

What should the environment learn from this cycle:

Pending.
