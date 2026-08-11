# CUL-MUZE-001 — Muze Engineering Culture

**Status:** active, prospectively scope-corrected
**Scope:** Muze software work where Muze influences engineering choices, unless project/client context adopts different or more specific preferences. This profile does **not** automatically activate Muze-owned library stewardship concerns.

This profile captures broadly applicable engineering preferences that influenced Spiral Developer while it was created at Muze but are not required for justified trust in every Spiral project.

These preferences are **defeasible**. A project-specific constraint, client/platform context, better evidence, or a more specific culture profile may justify another choice. When the difference is consequential, record why.

## Human validation and scope provenance

The substantive principles in the earlier profile were explicitly reviewed by a human familiar with Muze engineering culture on 2026-08-11 and confirmed to be in line with it. That reviewed version is pinned to Git commit `7de257778193d819178ae8cc1e9d06cf5ef4df64`; see `evidence/EVD-CUL-MUZE-001-human-validation.md`.

The immediately preceding active version is `CUL-MUZE-001@3b7348bfc045a19b4e66ad9a48848bcec7024ab0`.

This revision prospectively corrects scope and strengthens wording using explicit human clarification recorded in `SRC-CUL-MUZE-002`. In particular, Muze-owned library audience, package-maturity, and similar stewardship concerns are split into `CUL-MUZE-LIB-001` rather than silently applying to client projects.

The scope decision is human-directed. The revised wording remains versioned and changeable; future review may refine the split further.

Canonical organization source:

- https://github.com/muze-nl/.github/blob/main/maturity-policy.md

That source contains principles with different applicability. Do not assume every statement in it is organization-wide merely because it appears in one document.

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

Prefer lightweight abstractions when they make the code that developers actually use or change simpler. Do not add abstraction merely to make the architecture appear more complete or general.

### `small-decoupled-components` — Prefer small components and correct conceptual boundaries

Keep responsibilities narrow enough that future change and verification can stay local. Prefer abstractions that correspond to real conceptual boundaries; avoid abstractions that cross unrelated concerns or whose main benefit is making the architecture look more general.

### `collaborative-inspectability` — Make systems understandable enough to challenge

Prefer software whose relevant behavior and structure can be inspected and discussed by the humans collaborating on it, including people who are not specialist developers.

A collaborator should be able to point at a specific behavior, component, configuration, or piece of code and say, in effect, “this is the part that must change,” without first having to master the entire system.

This is not a requirement that every client-facing product target non-programmers as end users. It is an engineering preference for keeping the produced system legible enough to support human direction and correction.

### `web-native-standards` — Prefer browser/web-native standards where they fit

Prefer established browser and web mechanisms over custom machinery when they satisfy the requirement and preserve useful interoperability.

### `replaceable-dependencies` — Prefer replaceable dependencies, components, and thin coupling

Avoid unnecessary lock-in. Keep external dependencies and framework-specific machinery behind boundaries that make their role, capability, adaptation cost, and replacement cost understandable.

Prefer components and frameworks that can be adapted or replaced without forcing unrelated parts of the system to change.

### `stable-interfaces` — Prefer stable, explicit, long-lived interfaces

When a boundary is likely to be reused, prefer clear and stable interfaces over implicit coupling or framework magic. Treat long-lived public APIs as stewardship commitments rather than incidental implementation surfaces.

## Trade-off tendency

When several options are otherwise acceptable, prefer **composability, replaceability, web-platform alignment, inspectability, and long-term simplicity** over convenience, popularity, speculative completeness, or framework-specific cleverness.

This is a tendency, not an automatic priority rule. More specific project evidence or constraints may justify another choice.

## Tensions

These principles can conflict. For example, the simplest local solution may increase dependency lock-in; frontend-first may be the wrong probe for a backend reliability risk; a stable abstraction may introduce more concepts than a one-off implementation; inspectability may compete with a client-mandated platform.

Do not resolve those tensions by hidden priority order. Use the evidence and constraints of the current project and record consequential deviations or trade-offs.

## Related scoped profiles

For Muze-owned reusable libraries and packages, also consider adopting `CUL-MUZE-LIB-001 — Muze Library Stewardship Culture`. Its audience, package namespace, view-source, and lightweight-distribution preferences are intentionally **not** implied by this general profile.
