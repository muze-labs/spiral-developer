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

- `051932459267d6c522e9ab6cc00d10a3d2c56485` — `SRC-RISK-001` plus cycle record.
- `6f2bfe697f738b1972d6fec15255743cecf4f20e` — `UND-RISK-001`.
- `89d0a778e2f8b33b63d5b141f6e1d82bfd5cbf69` — `LES-017`.
- `4bfbb0692f5d0237ae2a825ba134a64e32fdc5f9` — prospective process/prompt/template changes.
- `EVD-RISK-001` — verification evidence recorded at cycle evaluation.

Material implementation decisions or deviations from the initial likely work:

The four risk positions remain a reasoning aid only. Existing horizon labels remain available for durable risk disposition but are no longer mandatory planning fields. The newest plan-continuity guardrail is preserved: high-leverage risks are surfaced during Evaluate, then reconciled with the governing roadmap during the next Analyze/Plan step rather than automatically promoted.

Out-of-scope discoveries retained for later:

None.

## Evaluate

Integrated result against cycle goal:

Spiral now prioritizes risk by uncertainty, downstream leverage, late-discovery cost, and cheap falsifiability. Strategy/business → domain/architecture → workflow/interface → implementation is used as a rough causal ordering, while local reversible implementation choices receive proportionately less de-risking attention.

Evidence / acceptance result:

`EVD-RISK-001` records structural, Turtle, Git-reference, repository-integrity, and branch consistency checks. Automated verification passes; human evaluation of this process change remains pending.

Metric or risk movement:

The old horizon-first selection rule no longer dominates live guidance. The process now gives explicit preference to cheap tests of uncertain assumptions whose failure would invalidate substantial downstream work, while preserving lightweight horizon metadata when it is genuinely useful.

What changed in our understanding:

Risk assessment does not need a separate ceremony to become more useful. The missing operation was prioritization by causal leverage: ask what later work depends on the assumption and how expensive late discovery would be.

Surprises / model mismatches:

The newly merged plan-continuity work made an important interaction explicit: even a high-leverage risk must not silently replace the roadmap. It becomes a strong candidate input whose priority is decided during deliberate next-cycle planning.

Known compromises:

The four causal positions are intentionally qualitative and not machine-readable taxonomy. No numeric probability/impact scoring or automatic prioritization is attempted.

Unresolved issues within current goal:

No structural issue remains in the proposed change. Human acceptance and dogfooding are still needed to establish whether the heuristic improves actual cycle choices.

Candidate next-cycle inputs:

If dogfooding shows repeated ambiguity in applying the four positions or comparing risks, refine the heuristic only as much as observed failures justify. Do not add a matrix or formal risk state pre-emptively.

Human evaluation / feedback:

Pending review of this branch/update.

Cycle accepted, still open, or deliberately re-planned:

Still open pending human evaluation.

## Process learning

What context/constraint/evaluation helped:

Grounding the discussion in the downstream consequences of early versus late decisions produced a clearer prioritization rule than the previous horizon labels. Reviewing it against the newest plan-continuity guardrail prevented risk salience from becoming a new form of recency drift.

What bookkeeping was useless:

A new risk phase, between-cycle state, numeric score, matrix, or mandatory risk artifact was unnecessary.

What should the environment learn from this cycle:

Prefer cycles that cheaply test uncertain assumptions with large downstream consequences. Use risk leverage to inform next-cycle selection, then reconcile it with governing direction rather than letting either recent discoveries or generic risk labels choose automatically.
