---
id: UND-WARN-001
---

# Understanding: Warning profiles are a separate decision-environment layer

## Current interpretation

Spiral Developer should distinguish three independently versioned layers:

1. **Spiral core** — invariants and practices required for justified trust in the development process.
2. **Culture profiles** — defeasible preferences that shape choices when several trustworthy options remain available.
3. **Warning profiles** — replaceable lenses that surface patterns deserving suspicion or deliberate inspection because they may indicate harm, lost agency, evidence overreach, or avoidable closure.

A warning profile is not a rulebook. Its signals should normally ask a concise operational question, not block work or require a philosophical discussion. The profile should include a significance gate so routine local choices do not generate noise.

Projects must explicitly adopt the warning profiles they want active. An agent may propose a new warning or profile, but should not silently add a normative warning system to the project environment.

When an adopted warning becomes materially relevant, the normal `RSK-*` mechanism can record it. The risk can point to the exact warning-profile version and, where useful, the specific warning fragment that prompted the inspection. This avoids inventing a separate artifact type for every warning occurrence.

## Sources considered

- Human direction captured in `SRC-WARN-001`.

## Clarifications / reframing

| Question / assumption | Alternative or clarification | Evidence / resolution |
|---|---|---|
| Are these warnings part of engineering culture? | No. They express patterns deserving scrutiny, not preferred implementation style. | Explicit human direction. |
| Are they Spiral core invariants? | No. Projects may replace, alter, or decline a warning profile while still using Spiral core. | Explicit human direction. |
| Should every detected pattern block work? | No. A warning prompts proportionate inspection; significance and disposition matter. | Explicit human direction. |
| Should every warning occurrence become a new artifact? | Not by default. Create a durable `RSK-*` only when the concern is consequential enough to matter to later reasoning/review. | Process-economy interpretation consistent with existing artifact philosophy. |

## Provenance confidence

Evidenced.

## Remaining uncertainty

The initial bundled warning profile may later split into multiple profiles or move to an independently versioned repository. The mechanism should not depend on the bundled profile remaining canonical.

## Consequence

Add a first-class, explicitly adopted `WarningProfile` mechanism to Spiral Developer, ship the agreed warning set as a replaceable starter profile, and keep warning-profile semantics distinct from culture and trust-critical core.
