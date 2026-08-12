---
id: LES-012
---

# Lesson: Make the outer cycle the visible unit of progress

## Observation / evidence

Spiral Developer already contains a cycle concept and Analyze/Plan/Act/Evaluate language, but normal instructions still organize work around one feature/meaningful change and one feature branch. In use, the human therefore experiences the process mainly as “give the AI a task and let it execute,” while the outer feedback loop remains implicit.

Treating every internal task as its own branch/PR would make a broader cycle visible only by multiplying human review burden. Conversely, allowing arbitrary new tasks to enter an active cycle would erode its value as an evaluation boundary.

## Lesson

Use a **cycle** as the outer learning and integration boundary: agree one coherent goal, let the agent execute the work needed to pursue it through multiple causal commits/artifacts, then explicitly evaluate the integrated outcome before planning new direction.

Keep scope stable during execution. Newly discovered work belongs in the current cycle only when it is necessary to achieve the agreed goal, establish the required evidence, or repair a regression caused by the cycle. Other discoveries should normally be retained for the next planning round.

For ordinary repository-changing cycles, one cycle branch and one integrated human review boundary are preferable to one branch/PR per subtask. The causal history can remain fine-grained inside that branch.

## Scope

Normal Spiral development cycles, especially AI-driven work where one coherent project outcome requires several implementation/investigation tasks.

## Confidence / limits

High confidence that the current repository under-exposes its existing outer-cycle model and that branch-per-subtask would create unnecessary review overhead. Moderate confidence that one cycle branch is the right default across project types; dogfooding should test very large, cross-repository, operational, and non-code cycles before stronger rules are added.

## Proposed consequence

Promote `CYC-*` into the normal human-visible cadence; add an interview-style cycle planning prompt; strengthen cycle evaluation; change Git/review guidance so repository-changing cycles normally use one cycle branch with multiple semantic commits; and explicitly defer newly discovered out-of-scope work to the next planning cycle unless the human deliberately re-scopes the current one.
