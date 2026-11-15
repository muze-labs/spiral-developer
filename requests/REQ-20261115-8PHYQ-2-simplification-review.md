---
id: REQ-20261115-8PHYQ-2
---

# Request: Make simplification a recurring consideration

## Operationalized intent and source

On 2026-11-15, the human identified a missing push to simplify and occasionally consider whether a refactor is warranted. After discussion of a brief Evaluate review, deeper reviews prompted by accumulated complexity, and optional state modelling, the human requested:

> Please inspect muze-labs/spiral-developer and see if we can add this to it. fetch the current github repo and give me a downloadable change set that I can commit over it.

This authorizes preparation of the proposed change set for review. It is not acceptance of the resulting process change. The earlier conversation is available here only through this imported request record, not independently verified primary evidence; there is no separately committed upstream Understanding.

On 2026-11-15, the human asked this repository session to review the imported changes, commit, and push for merge. After the agent presented the recurring-review Understanding, the missing Evaluate prompt, and the packaging/staging errors, the human confirmed: “yes, please fix my clumsy changes”. This confirms the described scope and authorizes cleanup, commit, and push for review. Final cycle acceptance remains a separate review outcome.

## Current evidence

At base `860bed8cbe077318db25c3cbedddfdf87efa9bdb`, `AGENTS.md` already requires justified complexity, and `docs/process.md` already requires lineage and behavior-preservation evidence for material refactors. `docs/cycles.md`, `prompts/evaluate-cycle.md`, and `templates/CYCLE.md` include compromises, discoveries, and lessons, but no explicit recurring simplification review or handoff of its deferred candidates to planning.

The gap is a recurring decision prompt within the existing workflow. It does not require a new artifact type, metric system, or execution engine.

## Observable desired outcomes

### outcome-1: Review at Evaluate

Evaluation briefly considers whether the affected area's accumulated complexity remains justified and whether simplification would reduce the burden of understanding, changing, or verifying it. A reasoned decision to keep the current design is valid.

### outcome-2: Escalate proportionately

Recurring boundary repairs, exceptions, duplicated state/ownership, growing verification effort, or a significant milestone can prompt focused review. A deeper review compares the current design with a plausible simplification and weighs benefit against disruption and verification cost. A material deferred candidate retains evidence, a deferral reason, and a revisit condition for planning.

### outcome-3: Preserve trust and scope

Keep relevant historical rationale, current contracts, and regression cases. Broader refactors require normal cycle planning or explicit re-planning. Optional state modelling uses unchanged properties across alternatives, records assumptions/bounds/revision, and distinguishes model results from real-code evidence. Human acceptance remains authoritative.

## Non-goals

- No automatic refactor, fixed refactoring cadence, size/complexity score, or mandatory statechart tool.
- No new runtime dependencies, ontology terms, artifact classes, or historical rewrites.
- No fix or architectural decision for Solid Workbench in this change set.
- No claim that the earlier modelling discussion proves this practice improves outcomes.

## Acceptance shape and uncertainty

Inspect the canonical cycle guidance and its agent/prompt/template entry points for consistency. Review representative scenarios: trivial change, repeated boundary repairs, justified compatibility complexity, deferred refactor, and model-only verification. Run the existing repository tests and graph validation; check patch applicability against the fetched base.

These checks establish consistency and packaging, not agent compliance or long-term benefit. Subsequent dogfooding should assess whether the review identifies useful simplifications without repeated noise, missed contracts, or unnecessary scope expansion. Revise or retire guidance that adds more burden than value.
