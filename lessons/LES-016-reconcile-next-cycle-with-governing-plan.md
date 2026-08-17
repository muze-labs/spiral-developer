---
id: LES-016
---

# Lesson: Reconcile the next cycle with the governing plan

## Observation / evidence

Interpreted evidence: `UND-PROCESS-003` (from `SRC-PROCESS-003`).

SimplyStore dogfooding showed that Spiral can preserve scope inside a cycle yet still drift between cycles. A newly exposed integrity concern became salient enough that the agent began treating full integrity work as the obvious next step, despite an existing broader implementation plan. The human had to explicitly ask the agent to re-read that plan.

## Lesson

Recent discoveries are inputs to planning, not an automatic replacement for prior direction.

When a durable multi-cycle plan, roadmap, or equivalent human-confirmed direction exists, the next Analyze/Plan step should re-read it, identify the current position, and reconcile new evidence against it before proposing a cycle. The proposal should state whether it:

- **continues** the governing plan;
- **revises** the governing plan because new evidence changes assumptions, dependencies, or priority; or
- **deliberately deviates** from it for an explicit reason.

A cycle-local discovery may justify changing the roadmap, but it must not silently become the roadmap.

If no governing plan exists, say so and proceed proportionately. Do not create speculative long-range plans solely to satisfy this lesson.

## Scope

Projects where more than one cycle is expected and a durable plan/roadmap/higher-level direction already exists. The same reasoning may apply to shorter work when explicit sequencing or dependencies matter, but no new ceremony is required for trivial/local changes.

## Confidence / limits

High confidence in the recency-drift failure mode from direct dogfooding. Moderate confidence that explicit plan reconciliation is sufficient; repeated use may show that stronger plan-version provenance or tooling is worthwhile, but that should be earned by evidence.

## Proposed consequence

Add plan continuity to normative cycle/process guidance, prompts, agent preflight, project context, and the cycle template. Keep plans defeasible and avoid a new plan ontology or priority-scoring system.
