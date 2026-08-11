---
id: SRC-BROWNFIELD-001
---

# Source: Build affinity before confidence in brownfield projects

## Human direction

Dogfooding showed that the confirmed-Understanding gate can work while the evidenced-gap check can still be shallow when an agent does not yet understand the project's structure well enough to know where relevant behavior may originate.

In the observed case, the agent understood the requested outcome and produced apparently reasonable evidence for its proposed CSS change, but inspected only component-specific CSS. The effective behavior also came from a more generic existing rule, so the evidence supported a false conclusion because the investigation scope was too narrow.

The human interpretation is that this is a normal brownfield condition rather than something to solve immediately with more architecture. Every established project is unique, and an agent entering it will initially have limited project-specific understanding. Early human handholding is therefore acceptable and useful.

The requested process principle is intentionally light:

> **Build affinity before confidence.** In an unfamiliar existing project, assume understanding is partial. Spend time learning how the project actually works before making strong claims about what is missing, duplicated, broken, or safe to change. Humans should expect to provide more guidance early; agents should expose uncertainty rather than project familiarity they have not earned.

Do not introduce project-affinity scores, stages, confidence machinery, or another artifact merely for this concern. Let human-AI collaboration discover what gaining affinity means in each project, and add more structure later only if dogfooding earns it.
