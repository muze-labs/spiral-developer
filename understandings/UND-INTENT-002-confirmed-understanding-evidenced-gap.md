---
id: UND-INTENT-002
---

# Understanding: Consequential implementation requires confirmed understanding and an evidenced gap

## Current interpretation

The first intent/reality preflight improved repository reconnaissance but remained too advisory. An agent could perform some brownfield search, decide it had understood enough, modify product code, and only afterward create Spiral artifacts explaining the decision. That does not make the preflight a guardrail; it makes provenance a retrospective narrative.

For consequential direct human work, implementation permission should therefore be an explicit gate with two independently established premises:

1. **Confirmed Understanding** — the agent has stated the concrete outcome it believes the human wants, together with material assumptions, and the human has confirmed or corrected that understanding.
2. **Evidenced gap** — the agent has established, using evidence appropriate to the system, that current effective behavior does not already satisfy the confirmed outcome.

Both are required before consequential product code is changed.

Repository reconnaissance remains part of Understanding formation, but its purpose is stronger than finding similarly named code. The agent must investigate **effective behavior**. In brownfield systems that can require following generic rules, inherited styles, configuration, default behavior, shared abstractions, callers, composition, or runtime effects that make the requested outcome already true without an obvious dedicated implementation.

The gap evidence should be fitted to the claim rather than standardized into one ceremony. A reported bug may be reproduced; a visual claim may require rendered/computed behavior; an API claim may be exercised; a configuration claim may require resolving effective configuration. Static search can be useful evidence, but absence of a matching implementation is not itself evidence that the behavior is absent.

If the agent cannot establish an unmet outcome, it must not invent work merely to satisfy the wording of the task. It should report what it found and return to the human where the consequence is material.

The implementation gate is revocable. If later evidence shows that either the confirmed Understanding or the evidenced gap was wrong, consequential implementation stops and inquiry resumes. Human confirmation is not a perpetual authorization after the premises have changed.

## Sources considered

- `SRC-INTENT-002`, the second dogfooding failure and clarified desired guardrail.
- `UND-INTENT-001` / `LES-007`, the earlier confirm-intent-and-reconcile-reality rule.
- Current brownfield, agent, review, and start-change guidance.

## Repository reality / overlap audit

The current process already says to confirm consequential direct human intent and search for existing/overlapping capability. However:

- it permits the sequence to be read as guidance rather than a hard no-implementation gate;
- its brownfield check emphasizes semantic overlap but does not require evidence that the requested **observable outcome is unmet**;
- it does not explicitly distinguish effective behavior from direct/local implementation, which allowed generic CSS to be overlooked;
- it does not clearly say that writing provenance after the code change cannot retroactively satisfy the preflight;
- it does not explicitly re-close the gate when later evidence falsifies the confirmed premises.

## Clarifications / reframing

| Question / assumption | Clarification | Evidence / resolution |
|---|---|---|
| Is finding related code enough brownfield reconnaissance? | No. The relevant claim is whether current effective behavior already satisfies the intended outcome. | Dogfooding found related work but still duplicated behavior already supplied indirectly. |
| May the agent implement before presenting its Understanding if it feels confident? | No for consequential direct human work. The uncertainty being verified is the agent's own interpretation, so self-confidence cannot waive the check. | Dogfooding showed the earlier proportional wording was treated too loosely. |
| Does confirmation alone permit implementation? | No. The current system must also exhibit an evidenced gap relative to the confirmed outcome. | The human can be correct about intent and wrong about current repository behavior. |
| Must gap evidence be a dedicated artifact? | No. It is evidence used to settle Understanding and implementation permission; preserve it durably when causally useful. | Existing artifact model is sufficient. |
| Does a later request/design/evidence trail repair a missed preflight? | No. Provenance recorded after an unnecessary change explains history but does not make the earlier decision justified. | Observed agent work log. |
| What if later evidence changes the premises? | Stop consequential implementation and return to inquiry/clarification. | Trust should follow current evidence, not stale confirmation. |

## Provenance confidence

Evidenced.

## Remaining uncertainty

Dogfooding should determine which classes of changes are consequential enough to require explicit human confirmation and how much evidence is sufficient to demonstrate an unmet outcome. The gate should not turn obvious typo-level changes into ceremony.

## Consequence

Strengthen Spiral's implementation boundary so consequential product modification is forbidden until both confirmed Understanding and an evidenced observable gap exist, and make this rule explicit in the agent/start-change/brownfield/review entry points.
