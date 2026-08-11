---
id: SRC-INTENT-002
---

# Source: Dogfooding feedback on confirmed understanding and evidenced gap

## Source kind

Connected human dogfooding feedback after applying the intent/repository-preflight guardrail on a brownfield project.

## What was actually observed

The agent reported that it had made a code change and was then adding a Spiral request/design/evidence trail. In the attempted task:

- the agent found an earlier branch containing related work; this was environmental noise and not the core failure;
- it performed a brownfield check for related or already-fixed work, but did not identify that the desired CSS behavior was already provided by a more generic existing rule/class;
- it did not present its Understanding of the assignment to the human and stop for confirmation before changing product code;
- it misunderstood the assignment;
- the code it added was unnecessary because the exact effective styles were already applied through existing generic CSS.

## Clarified desired guardrail

For consequential direct human work, the earlier guidance is not strong enough when it is treated as advice rather than an execution gate.

Before consequential product implementation is allowed:

1. the agent must investigate enough to formulate a concrete Understanding of the desired outcome and material assumptions;
2. that Understanding must be presented to the human and explicitly confirmed or corrected;
3. the agent must establish evidence of the relevant **observable gap** between current system behavior and the confirmed intended outcome, rather than merely searching for a similarly named implementation;
4. for brownfield work, the gap check must account for effective behavior that may arise indirectly through generic abstractions, inheritance, shared rules, configuration, callers, defaults, or other composition;
5. if later investigation falsifies either the confirmed Understanding or the evidenced gap, the implementation gate closes again and the agent returns to inquiry/human clarification.

The form of the gap evidence should fit the work. Examples include reproducing a bug, inspecting rendered/computed behavior, exercising an API, running a focused probe, reading effective configuration, or otherwise demonstrating that the requested outcome is actually unmet.

## Integrity / version

Captured prospectively after the second dogfooding attempt of the direct-intent preflight.

## Provenance confidence

Explicit.

## Limitations / uncertainty

This source does not require a new artifact type, a fixed technical probe, or human confirmation for genuinely trivial/local/reversible edits. It establishes the stronger gate for consequential work and the distinction between searching for related code and evidencing an unmet outcome.
