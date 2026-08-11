# CUL-MUZE-001 — Muze Engineering Culture

**Status:** active, prospectively expanded from Programming for Wizards synthesis
**Scope:** Muze software work where Muze influences engineering choices, unless project/client context adopts different or more specific preferences. This profile does **not** automatically activate Muze-owned library stewardship concerns.

This profile captures broadly applicable engineering preferences that influenced Spiral Developer while it was created at Muze but are not required for justified trust in every Spiral project.

These preferences are **defeasible**. A project-specific constraint, client/platform context, better evidence, or a more specific culture profile may justify another choice. When the difference is consequential, record why.

## Human validation and scope provenance

The substantive principles in the earlier profile were explicitly reviewed by a human familiar with Muze engineering culture on 2026-08-11 and confirmed to be in line with it. That reviewed version is pinned to Git commit `7de257778193d819178ae8cc1e9d06cf5ef4df64`; see `evidence/EVD-CUL-MUZE-001-human-validation.md`.

The immediately preceding active version is `CUL-MUZE-001@7273048d88a416bb409fdab364e1d15dfa89c76c`.

The scope correction remains in force: Muze-owned library audience, package-maturity, and similar stewardship concerns live in `CUL-MUZE-LIB-001` rather than silently applying to client projects.

This revision additionally derives from `UND-CUL-MUZE-001`, which interprets the *Programming for Wizards* repository together with explicit human clarification in `SRC-CUL-MUZE-005`. The human source confirms the deeper cultural synthesis and the listed trade-offs; the exact wording of this revised profile remains prospectively reviewable rather than being treated as already line-by-line human-validated.

The culture remains versioned and changeable. Several principles were formed before efficient AI materially changed implementation economics, so their historical rationale is preserved explicitly rather than assuming every old heuristic remains optimal.

Canonical organization source:

- https://github.com/muze-nl/.github/blob/main/maturity-policy.md

That source contains principles with different applicability. Do not assume every statement in it is organization-wide merely because it appears in one document.

## Underlying engineering logic

The principles below are not intended as an unrelated checklist. Their current shared logic is:

> **Problems are shaped by representations and assumptions. Make those visible, move boundaries rather than pile on machinery, put choices where they can still change, expect to be wrong, and preserve the ability to replace the answer.**

This is a preference for systems that can learn and be corrected, not for permanent minimalism or architectural purity. When changed evidence, client constraints, or new production economics make another approach better, revise the answer prospectively.

## Principles

### `meaningful-feedback-early` — Prefer early reality-based feedback

Prefer short feedback loops in which intended users interact with something behaviorally meaningful before large downstream commitments accumulate.

Do not confuse early feedback with premature visual polish or infrastructure completeness.

### `frontend-first` — Prefer frontend-first probes for interactive web work

For ordinary Muze web products, an interactive frontend is often the cheapest artifact capable of eliciting high-quality user feedback. Prefer building enough working interaction for intended users to spend meaningful time with the feature before investing heavily in production architecture.

This is a cultural strategy for obtaining evidence, not a Spiral invariant. Use another probe when it produces better evidence for the current uncertainty.

### `vertical-slices` — Prefer thin end-to-end implementation slices

When replacing a validated interaction hypothesis with production behavior, prefer small vertical slices that connect enough of the real system to produce an observable outcome. Avoid large horizontal infrastructure layers that cannot yet be evaluated against user value or a current risk.

### `design-for-correction` — Design so being wrong stays affordable

Do not optimize primarily for predicting the final architecture correctly. Put consequential choices behind boundaries where later evidence can replace or revise them without dragging unrelated assumptions through the system.

A design that is easy to correct can be preferable to one that appears more complete but makes its assumptions expensive to unwind.

### `bounded-assumptions` — Make assumptions visible and give them boundaries

Treat hidden or widely shared assumptions as a major source of coupling. Prefer components and interfaces that make important assumptions local, explicit, and challengeable.

When two parts change for different reasons, look for the assumption that unnecessarily ties them together before adding coordination machinery.

### `reshape-before-enlarge` — Try changing the problem before enlarging the solution

Before adding machinery, ask whether a different representation, vocabulary, boundary, rule, or decomposition makes the problem smaller. Prefer removing accidental complexity over managing it more elaborately.

This is not a requirement to invent novel abstractions. The change should make the actual problem easier to understand or change.

### `keep-ideas-high` — Keep specific ideas high in the stack until they earn a lower layer

Prefer implementing specific or still-changing ideas in local/replaceable layers rather than promoting them prematurely into shared foundations. Move an idea downward only when its generality, durability, and shared value have become credible.

Use this as a practical defense against architecture astronautics: foundational abstraction is a consequence of demonstrated commonality, not a goal by itself.

### `progressive-enhancement` — Prefer useful lower layers that survive higher-layer absence

Where the domain permits it, layer capabilities so a simpler/lower layer remains independently useful when a richer layer is unavailable, fails, or is replaced.

This is broader than Web progressive enhancement. Do not force the pattern where the higher layer is inherently necessary for the behavior.

### `simplicity-over-completeness` — Prefer the simplest adequate system

Prefer fewer concepts and less speculative completeness when several approaches satisfy the current need. AI makes complexity cheap to generate, not cheap to own.

Prefer lightweight abstractions when they make the code that developers actually use or change simpler. Do not add abstraction merely to make the architecture appear more complete or general.

### `small-decoupled-components` — Prefer small components and correct conceptual boundaries

Keep responsibilities narrow enough that future change and verification can stay local. Prefer abstractions that correspond to real conceptual boundaries; avoid abstractions that cross unrelated concerns or whose main benefit is making the architecture look more general.

### `collaborative-inspectability` — Make systems understandable enough to challenge

Prefer software whose relevant behavior and structure can be inspected and discussed by the humans collaborating on it, including people who are not specialist developers.

A collaborator should be able to point at a specific behavior, component, configuration, or piece of code and say, in effect, “this is the part that must change,” without first having to master the entire system.

This is not a requirement that every client-facing product target non-programmers as end users. It is an engineering preference for keeping the produced system legible enough to support human direction and correction.

### `innovation-happens-elsewhere` — Preserve seams for ideas and actors outside the original system

Keep in mind that useful innovation often comes from outside the team, component, product, or organization that created the original system. Where the project permits it, prefer interoperable/open boundaries and small shared agreements that let other implementations or participants contribute without requiring ownership of the whole stack.

This is an observation-shaped preference, not a demand that every client system be open or extensible. Client, regulatory, commercial, or platform constraints may legitimately limit it.

### `user-data-ownership` — Prefer users retaining meaningful control of their data and future choices

Where Muze has influence, prefer architectures that avoid unnecessarily trapping user data, identity, or future options inside one application/provider. This preference is strong enough to influence project/client selection.

In client work Muze may not control these choices. Treat the preference as explicit cultural provenance and surface material conflicts rather than pretending it is always enforceable.

### `web-native-standards` — Prefer browser/web-native standards where they fit

Prefer established browser and web mechanisms over custom machinery when they satisfy the requirement and preserve useful interoperability.

### `replaceable-dependencies` — Prefer replaceable dependencies, components, and thin coupling

Avoid unnecessary lock-in. Keep external dependencies and framework-specific machinery behind boundaries that make their role, capability, adaptation cost, and replacement cost understandable.

Prefer components and frameworks that can be adapted or replaced without forcing unrelated parts of the system to change.

### `frameworks-are-a-tradeoff` — Prefer problem fit, but account for shared familiarity

Be skeptical of frameworks whose generic shape becomes the architecture regardless of the actual problem. Prefer problem-specific structure when that materially improves fit, understanding, or replaceability.

Do not turn this skepticism into a ban. A familiar framework can lower handover cost between developers with different engineering cultures, provide mature solved infrastructure, or reduce operational risk. Those benefits can outweigh poorer local fit. Record the consequential trade-off rather than applying a default ideology.

### `avoid-nih-without-damaging-fit` — Reuse mature work when it fits cleanly

Avoid NIH where possible. Prefer existing standards, libraries, tools, or well-understood ideas when they solve the real problem without importing assumptions, machinery, lock-in, or complexity that damages what is being built.

When a mature library is too costly for the needed capability, it can still be appropriate to reuse the underlying idea or standard rather than either importing the whole system or reinventing the concept blindly.

### `stable-interfaces` — Prefer stable, explicit, long-lived interfaces

When a boundary is likely to be reused, prefer clear and stable interfaces over implicit coupling or framework magic. Treat long-lived public APIs as stewardship commitments rather than incidental implementation surfaces.

### `timing-is-part-of-the-deliverable` — Prefer useful delivery at the relevant time over perfection too late

A technically better answer delivered after it can matter can be worse than a sufficiently good, replaceable answer delivered when it is useful. Treat timing as part of product/engineering quality, not as an external scheduling nuisance.

This principle is historically situated. It was formed when implementation effort made “perfect” compete strongly with “now.” Efficient AI is reducing that scarcity, so do not use the old trade-off to justify stopping refinement when additional quality is now cheap and materially useful. Optimize for useful timing under current economics.

## Trade-off tendency

When several options are otherwise acceptable, prefer **correctable boundaries, composability, replaceability, inspectability, problem fit, web-platform alignment where relevant, and long-term simplicity** over convenience, popularity, speculative completeness, premature foundational abstraction, or framework-specific cleverness.

This is a tendency, not an automatic priority rule. More specific project evidence or constraints may justify another choice.

## Historical rationale and AI-era uncertainty

Many Muze preferences were formed when implementation and exploration were expensive enough that developer time was a dominant scarcity. Efficient AI changes that environment.

Do not discard the culture merely because the tools changed: principles about ownership, inspectability, bounded assumptions, replaceability, and correction may survive independently of implementation cost. But re-evaluate heuristics whose rationale depended on scarcity, especially timing, framework familiarity, bespoke implementation cost, and how much refinement is economical.

When a changed constraint materially weakens a cultural rationale, record the lesson and revise the culture prospectively rather than silently following or silently abandoning the old rule.

## Tensions

These principles can conflict. For example, the simplest local solution may increase dependency lock-in; frontend-first may be the wrong probe for a backend reliability risk; a stable abstraction may introduce more concepts than a one-off implementation; inspectability may compete with a client-mandated platform.

Do not resolve those tensions by hidden priority order. Use the evidence and constraints of the current project and record consequential deviations or trade-offs.

## Related scoped profiles

For Muze-owned reusable libraries and packages, also consider adopting `CUL-MUZE-LIB-001 — Muze Library Stewardship Culture`. Its audience, package namespace, view-source, and lightweight-distribution preferences are intentionally **not** implied by this general profile.
