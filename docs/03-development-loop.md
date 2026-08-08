# Development Loop

Spiral Developer keeps the useful structure of spiral development while changing what each cycle produces.

The familiar loop remains:

> **Analyze → Plan → Act → Evaluate**

But its purpose is not to maintain status documents. It is to create a short evidence-producing loop in which the causal model becomes more accurate.

## Analyze

Establish:

- the current request revision;
- what meaningful outcome the intended audience needs;
- the nearest important uncertainty;
- current relevant feedback/observations;
- relevant legacy constraints;
- blockers, near-term, deferred, and existential risks;
- culture, external constraints, and dependencies that materially restrict design.

For brownfield work, characterize existing behavior before trying to explain its original purpose.

## Plan

Choose the smallest artifact or change capable of answering the main question.

For interactive web work, this will often be a frontend-first behavioral probe.

Define before implementation:

- which request fragments are being addressed;
- explicit non-goals;
- which future risks are deliberately deferred;
- expected evidence;
- pause/change conditions;
- human authority boundaries for consequential choices.

Avoid designing later cycles in detail.

## Act

Build the smallest useful thing.

Early validation should optimize for meaningful interaction and working behavior, not finish.

Once the interaction model is credible, prefer vertical slices through real architecture.

During implementation:

- preserve design links;
- keep components small and boundaries explicit;
- avoid unrelated cleanup;
- add tests/evals that verify design properties rather than merely mirror implementation;
- record important supporting/intrinsic technical work honestly.

## Evaluate

Collect evidence at the correct level.

### Interaction feedback

Did intended users behave as expected? What did their interaction reveal about the request or design?

### Verification

Does the implementation realize the design?

### Acceptance

Does the resulting behavior satisfy the request?

### Process learning

Did the environment give the agent enough context and constraints? Did a failure expose a missing invariant or bad causal link?

The outcome may be:

- accept and continue;
- revise the request;
- revise the design;
- improve verification;
- repair context/culture/constraints;
- simplify or split;
- pause for evidence;
- abandon the direction.

## Feedback quality

Do not confuse fast iteration with useful feedback.

The preferred early artifact is the cheapest artifact that causes the intended audience to interact meaningfully enough to reveal mistaken assumptions.

For frontend-first work, visual polish and general usability are secondary until their absence prevents meaningful interaction.

## Risk horizon

A risk should have both severity and horizon. Horizon determines when it deserves engineering attention.

| Horizon | Meaning | Default action |
|---|---|---|
| Blocker | Prevents next meaningful step | Resolve now |
| Near-term | Likely to impede next cycles | Investigate/mitigate soon |
| Deferred | Real but not relevant yet | Record, do not solve |
| Existential | Could invalidate direction | Pull forward and test |

## Simplicity as an economic property

A simple system is cheaper for both humans and AI to extend.

Evaluate changes by asking:

- Did the conceptual vocabulary grow unnecessarily?
- Did dependency count or coupling increase?
- Did the change radius grow?
- Did new abstractions simplify dependent code?
- Did tests become easier or harder to write?
- Does a future agent need more context to change this safely?
- Can the system still be explained through its causal production model?
