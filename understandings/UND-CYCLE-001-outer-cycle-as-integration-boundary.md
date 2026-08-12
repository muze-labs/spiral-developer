---
id: UND-CYCLE-001
---

# Understanding: The Spiral cycle is the outer learning and integration boundary

## Interpretation

The repository already contains an `sd:Cycle` concept, a `CYC-*` artifact identity, an Analyze/Plan/Act/Evaluate cycle template, and an evaluation prompt. The missing part is operational: current normative guidance still treats each feature/meaningful change and its feature branch as the primary unit of execution and review. As a result, the outer spiral is largely invisible to the human.

The requested change should therefore **promote the existing cycle concept**, not invent another workflow layer.

A cycle should mean:

- one coherent project goal, risk reduction, or important uncertainty to resolve;
- a stable human-confirmed scope and explicit non-goals;
- one normal repository integration/review boundary when code or other repository state changes;
- multiple tasks, requests/designs/implementations, and semantic commits when needed to achieve the goal;
- an explicit evaluation boundary before new direction is planned.

The cycle is not an arbitrary task bucket or sprint. Work discovered during execution belongs in the current cycle only when it is necessary to achieve the agreed goal, to establish required evidence, or to correct a regression introduced by the cycle. Other discoveries should be preserved as feedback/risk/candidate future work and considered during the next planning interview.

Evaluation should be distinct from planning the next cycle. The AI first presents what happened against the agreed cycle goal: integrated result, evidence, metric/risk movement, surprises, unresolved issues, and out-of-scope discoveries. Human feedback may either:

1. show that the current goal is not yet satisfied, in which case the same cycle remains open for corrective work; or
2. introduce a new goal/direction, which normally becomes input to reorientation and next-cycle planning after the current cycle is accepted/closed.

The existing per-change trust gates remain nested inside the cycle. Consequential direct human input still needs confirmed Understanding plus an evidenced gap before product modification. When cycle planning already establishes the same concrete outcome/current behavior/gap/assumptions, the system should not demand a duplicate confirmation merely for ceremony.

## Git/review implication

For an ordinary repository-changing cycle, use one branch such as `spiral/CYC-014-keyboard-accessibility`. The agent may make multiple immutable causal commits on that branch. Human review happens against the integrated cycle outcome rather than requiring a branch/PR for every internal task.

A non-repository investigation/evaluation cycle may not need a development branch. Very small work should scale down proportionally rather than require a large interview or artifact set.

## Deliberate limits

For this first version:

- do not add a formal task model;
- do not add machine-enforced cycle states;
- do not add a new branch hierarchy beneath cycle branches;
- do not require a new RDF relation for cycle membership;
- do not make the initial task list fixed or exhaustive;
- do not allow casual scope growth merely because the agent discovers adjacent work.

Use existing Markdown `CYC-*` artifacts and prompts to make the outer cadence visible first. Dogfood whether stronger structure is needed.
