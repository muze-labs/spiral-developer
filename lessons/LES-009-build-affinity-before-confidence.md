---
id: LES-009
---

# Lesson: Build affinity before confidence in brownfield projects

## Observation / evidence

A dogfood task passed the strengthened human-Understanding gate but still produced shallow gap evidence. The agent inspected the obvious component-local styling surface and concluded a visual affordance was absent, while the same effective CSS was already supplied through a more generic project rule.

The failure was not fabricated evidence. The evidence was plausible inside an incomplete model of where behavior could originate in that project.

## Lesson

An agent entering an established project should assume that its project-specific understanding is partial. Before making strong claims about what is absent, duplicated, broken, or safe to change, it should build enough affinity with the relevant project area to understand where the behavior could actually come from.

Humans should expect to provide more guidance early in brownfield collaboration. That handholding is useful transfer of local knowledge, not a process failure. Agents should expose uncertainty rather than project familiarity they have not earned.

This is deliberately a principle rather than an architecture. Do not introduce affinity scores, formal stages, or new artifact types unless later dogfooding demonstrates a need.

## Scope

Brownfield work, especially when making negative or absence claims about an unfamiliar project or subsystem.

## Confidence / limits

High confidence that project-local knowledge affects the adequacy of evidence scope. What sufficient affinity means is project-specific and should initially be inferred through human-AI collaboration rather than standardized.

## Proposed consequence

Add a concise **build affinity before confidence** instruction to the agent and human-facing brownfield guidance. Use it to temper the evidenced-gap rule: when the agent cannot justify that it understands the relevant behavior surface well enough, it should learn more or ask the human rather than making a strong gap claim.
