---
id: EVD-PROCESS-003
---

# Verification Evidence: Plan continuity across cycles

## What is being verified

Adoption of `LES-016`: when a durable multi-cycle plan/roadmap or equivalent human-confirmed direction exists, Spiral should re-read and reconcile it before selecting the next cycle, so that recent discoveries inform but do not silently replace broader direction.

Implementation commit under verification: `db7464c7a1a008e23b00bc34bf45d086b119a91d`.

## Structural / consistency checks

- `docs/cycles.md` now has an explicit plan-continuity section requiring re-reading the governing plan/reference, locating the current position, comparing recent evidence, and classifying the next proposal as continue/revise/deliberate deviation.
- `docs/process.md` makes the same reconciliation part of normative Analyze/Plan and states that Evaluate may retain candidate inputs but does not itself choose their priority.
- `AGENTS.md` contains both a preflight question and working-style rule against choosing the next cycle from recency alone.
- `prompts/plan-cycle.md` requires the actual durable plan/reference to be re-read when one exists and exposes `Governing plan / current position`, `Plan continuity decision`, and `New evidence affecting the plan` in the proposed cycle summary.
- `prompts/evaluate-cycle.md` retains implications for a governing plan without promoting them into next-cycle priority.
- `templates/CYCLE.md` records governing direction/current position plus a plan-continuity decision.
- `templates/PROJECT_CONTEXT.md` provides an optional durable `Governing plans / roadmaps` table with plan/reference, authority/status, current position, and review trigger.
- `docs/brownfield-intake.md` explicitly treats existing multi-cycle plans/roadmaps as part of relevant future direction so their reference/current position can enter durable project context during intake.
- `README.md` and `CONTRIBUTING.md` expose the behavior to new AI/human collaborators.
- No Plan artifact class, plan ontology vocabulary, priority score, automated plan-position inference, or mandatory long-range roadmap was introduced.
- `git diff --check` reported no whitespace errors for the implementation change.
- Actual branch state at evaluation is `spiral/CYC-002-plan-continuity`, matching active cycle `CYC-002`.

## Scenario checks

The guidance now distinguishes these cases explicitly:

1. **Plan exists; recent discovery fits it** — continue the governing plan and explain why the proposed cycle is the next planned boundary.
2. **Plan exists; new evidence invalidates an assumption/dependency** — revise the plan explicitly and retain the reason/evidence.
3. **Plan exists; another concern must temporarily outrank it** — deliberately deviate and state why, rather than presenting the detour as if it had always been planned.
4. **No governing multi-cycle plan exists** — say so proportionately and choose the next cycle from context/risk/evidence without inventing a roadmap for ceremony.
5. **Evaluate surfaces an attractive new possibility** — retain its implications, but defer prioritization until the next Plan step has re-read the governing direction.

The SimplyStore dogfooding failure maps to case 5: the integrity discovery remains valuable evidence, but it can no longer become the next cycle solely because it is the most recent salient finding.

## Causal-reference checks

- `UND-PROCESS-003` interprets the exact committed version of `SRC-PROCESS-003` at `4b4e225c1e3ff1f601dd7c4aa1613bdf33cd304a`.
- `LES-016` derives from the exact committed version of `UND-PROCESS-003` at `0c31e1e98fe7e3f4f25bf4bf3e2d991bf54298da`.
- The implementation commit records `LES-016@547438c498ce20e603aebe7090a94c1d6a4fb433` in its Git message.
- All exact Git references that resolve to real commits in repository Turtle are strict/current ancestors of the implementation/evaluation head; illustrative unresolved hash placeholders remain confined to examples/templates.

## Turtle / repository checks

- All Turtle resources, including this evidence resource, parse successfully with RDFLib.
- All real 40-character commit references found in Turtle resolve and satisfy Git ancestry relative to the evaluation head.
- `git fsck --no-reflogs` reports no Git object/database errors relevant to this cycle.

## Limits

This verifies that the process representation and prompts now make plan reconciliation explicit. It does not prove that every future AI will obey the instruction under all contexts. Continued dogfooding should test whether the behavior survives several cycles and whether plan references/current position remain fresh enough to be useful.
