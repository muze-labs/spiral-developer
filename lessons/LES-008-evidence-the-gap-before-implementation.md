---
id: LES-008
---

# Lesson: Evidence the gap before consequential brownfield implementation

## Observation / evidence

A strengthened intent/repository preflight was dogfooded. The agent did some brownfield reconnaissance but still misunderstood the assignment, never stopped to present its Understanding for human confirmation, and added unnecessary CSS even though the desired effective styles were already supplied by a generic existing rule.

The process had encouraged semantic overlap search, but this did not force the agent to prove that the requested outcome was actually missing.

## Lesson

For consequential direct human work, implementation should be gated by two premises: the human has confirmed the agent's Understanding, and the agent has evidence that current effective behavior does not already satisfy that Understanding.

Brownfield reconnaissance should therefore seek evidence of the **gap**, not merely evidence about code that looks related. Effective behavior may be supplied indirectly through shared abstractions, inheritance, configuration, defaults, callers, composition, or runtime behavior.

If the gap cannot be established, do not create work to match the ticket. Return to inquiry. If later evidence falsifies the Understanding or gap, close the implementation gate again.

## Scope

Spiral-process candidate for consequential direct human changes, especially brownfield work. The exact probe depends on the claim being made.

## Confidence / limits

High confidence in the failure mode from repeated dogfooding. The threshold for consequential work and sufficient gap evidence remains empirical and should avoid ceremony for trivial/local/reversible edits.

## Proposed consequence

Turn the earlier intent/reality preflight from advisory guidance into an explicit no-implementation gate: **confirmed Understanding + evidenced gap**.

## Outcome after adoption

Dogfood whether agents now stop before product modification, surface a concrete Understanding, and verify effective existing behavior strongly enough to avoid duplicate/no-op implementation.
