---
id: LES-017
---

# Lesson: Prioritize uncertain assumptions by downstream leverage

## Observation / evidence

Spiral Developer can identify many possible concerns, but dogfooding exposed a missing prioritization principle: not all wrong choices have comparable consequences.

A wrong strategy/business assumption may invalidate most downstream design and implementation. A wrong domain/architecture assumption can invalidate many features and integrations. Workflow/interface mistakes are usually more bounded. Local implementation choices are often cheaper to reverse.

Without making this distinction explicit, an agent can spend similar attention on low-level technical uncertainty and high-leverage upstream assumptions, or use broad labels such as “existential” without asking what downstream work actually depends on the premise.

## Lesson

When deciding what risk to reduce next, reason about **uncertainty plus downstream leverage and late-discovery cost**, not merely the presence or category of a possible problem.

Use the rough causal positions strategy/business → domain/architecture → workflow/interface → implementation as a thinking aid. Earlier positions usually deserve disproportionate attention because more later work can depend on them, while local reversible implementation choices normally deserve less de-risking effort.

Prefer a cycle that cheaply falsifies or reduces a high-leverage uncertain assumption when discovering the mistake later would cause substantial rework.

## Scope

Cycle selection and cycle evaluation across Spiral Developer projects. This is a prioritization heuristic, not a universal severity ordering: concrete impact, urgency, reversibility, and governing-plan context still matter.

## Confidence / limits

High confidence in the general downstream-leverage principle and in avoiding equal treatment of all uncertainties. Moderate confidence that the four rough positions are sufficient as the default vocabulary; dogfooding may reveal useful refinements.

Do not turn the heuristic into numeric scoring, a mandatory risk matrix, or a new between-cycle ceremony without evidence that doing so improves decisions.

## Proposed consequence

Strengthen the risk catalog, cycle-planning prompt, cycle-evaluation prompt, process guidance, and agent instructions so they ask which uncertain assumptions have meaningful downstream leverage, what late discovery would cost, and whether a cheap falsification is available now. Keep durable risk artifacts and existing horizons available when they add value, but do not require them for ordinary lightweight risk reasoning.
