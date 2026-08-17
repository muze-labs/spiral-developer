---
id: UND-PROCESS-003
---

# Understanding: Plan continuity must survive local discovery

## Interpreted intent

The dogfooding problem is not that Spiral should follow plans rigidly. It is that the agent currently has a stronger mechanism for preserving **cycle-local scope** than for preserving **multi-cycle direction**.

After a cycle exposes a compelling new fact, that fact is highly salient. The next Analyze/Plan step can therefore treat the latest discovery as the obvious next priority even when an existing implementation plan, roadmap, or human-confirmed direction already describes a broader sequence and unresolved dependencies.

This is a recency/plan-continuity failure:

1. the active cycle correctly retains new discoveries for later rather than absorbing them;
2. Evaluate correctly lists them as candidate next-cycle inputs;
3. but the subsequent planning step does not explicitly re-read and reconcile the governing plan before selecting among those inputs;
4. the newest finding can therefore become the de facto roadmap without an explicit decision to revise the old one.

The SimplyStore example makes the failure concrete: adversarial OD-JSONTag work exposed the boundary where integrity hashes will eventually matter, and the agent began jumping to full integrity work until the human reminded it to consult the original durability/extensibility plan again.

## Current effective behavior / evidenced gap

Repository inspection before implementation established that:

- `docs/cycles.md` and `prompts/evaluate-cycle.md` preserve out-of-scope discoveries for the next Analyze/Plan interview;
- `prompts/plan-cycle.md` says not to assume the newest request is automatically highest priority, but does not require identifying or re-reading an existing governing plan/roadmap;
- `.spiral/project-context.md` can record current direction, future direction, and later possibilities, but the template has no explicit place for a durable governing plan/reference and current position;
- the cycle template records candidate next-cycle inputs but not whether the next proposed cycle continues, revises, or deliberately deviates from a governing plan.

This leaves a real gap between **preserving discoveries** and **prioritizing them in context**.

## Desired outcome

Harden Spiral so that when a durable multi-cycle plan, roadmap, or equivalent human-confirmed direction exists:

- the next Analyze/Plan step re-reads it rather than relying on remembered summary;
- the agent identifies the current position in that plan;
- recent evidence is compared against planned dependencies/priorities;
- the next-cycle proposal explicitly says whether it continues the plan, revises it, or deliberately deviates from it;
- a revision/deviation records why the new evidence justifies changing direction.

If no governing plan exists, say so and continue proportionately. Spiral must not require speculative long-range planning merely to satisfy the process.

Plans remain defeasible. New evidence can and should change them; the process change is that **cycle-local discoveries may inform the plan but may not silently replace it**.

## Confidence and uncertainty

High confidence in the failure mode because it was observed directly after the previous process improvements and is supported by an identifiable omission in the current planning/evaluation guidance. Moderate confidence in the exact amount of durable plan metadata needed; the first change should remain Markdown/process-level and be dogfooded before introducing any plan ontology or automation.
