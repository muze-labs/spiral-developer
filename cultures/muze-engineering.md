# CUL-MUZE-001 — Muze Engineering Culture

**Status:** active first extraction  
**Scope:** Muze software projects unless a project explicitly adopts different or more specific preferences

This profile captures engineering preferences that influenced Spiral Developer while it was created at Muze but are not required for justified trust in every Spiral project.

These preferences are **defeasible**. A project-specific constraint, better evidence, or a more specific culture profile may justify another choice. When the difference is consequential, record why.

Canonical organization source:

- https://github.com/muze-nl/.github/blob/main/maturity-policy.md

## Principles

### `meaningful-feedback-early` — Prefer early reality-based feedback

Prefer short feedback loops in which intended users interact with something behaviorally meaningful before large downstream commitments accumulate.

Do not confuse early feedback with premature visual polish or infrastructure completeness.

### `frontend-first` — Prefer frontend-first probes for interactive web work

For ordinary Muze web products, an interactive frontend is often the cheapest artifact capable of eliciting high-quality user feedback. Prefer building enough working interaction for intended users to spend meaningful time with the feature before investing heavily in production architecture.

This is a cultural strategy for obtaining evidence, not a Spiral invariant. Use another probe when it produces better evidence for the current uncertainty.

### `vertical-slices` — Prefer thin end-to-end implementation slices

When replacing a validated interaction hypothesis with production behavior, prefer small vertical slices that connect enough of the real system to produce an observable outcome. Avoid large horizontal infrastructure layers that cannot yet be evaluated against user value or a current risk.

### `simplicity-over-completeness` — Prefer the simplest adequate system

Prefer fewer concepts and less speculative completeness when several approaches satisfy the current need. AI makes complexity cheap to generate, not cheap to own.

### `small-decoupled-components` — Prefer small components with clear conceptual boundaries

Keep responsibilities narrow enough that future change and verification can stay local. Avoid abstractions whose main benefit is making the architecture look more general.

### `web-native-standards` — Prefer browser/web-native standards where they fit

Prefer established browser and web mechanisms over custom machinery when they satisfy the requirement and preserve useful interoperability.

### `replaceable-dependencies` — Prefer replaceable dependencies and thin application coupling

Avoid unnecessary lock-in. Keep external dependencies behind boundaries that make their role, capability, and replacement cost understandable.

### `stable-interfaces` — Prefer stable, explicit interfaces

When a boundary is likely to be reused, prefer clear and stable interfaces over implicit coupling or framework magic.

## Tensions

These principles can conflict. For example, the simplest local solution may increase dependency lock-in; frontend-first may be the wrong probe for a backend reliability risk; a stable abstraction may introduce more concepts than a one-off implementation.

Do not resolve those tensions by hidden priority order. Use the evidence and constraints of the current project and record consequential deviations or trade-offs.
