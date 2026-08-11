# CUL-MUZE-LIB-001 — Muze Library Stewardship Culture

**Status:** active first extraction
**Scope:** Muze-owned reusable libraries, packages, public developer tooling, and related artifacts where Muze controls the stewardship model and intended developer audience. Do not apply this profile automatically to client projects.

This profile supplements `CUL-MUZE-001`. It captures preferences from Muze's own library/product stewardship that would be misleading if treated as universal Muze client-work rules.

The profile is **defeasible and explicitly adopted**. A Muze-owned project may adopt only the parts that actually fit its audience and operational context.

## Provenance

This split is derived from explicit human scope clarification in `SRC-CUL-MUZE-002`, which refers to the Muze design-principles / maturity-policy summary and explains that the library audience, package namespace policy, and some performance/distribution preferences are not general client-project requirements.

Canonical organization source:

- https://github.com/muze-nl/.github/blob/main/maturity-policy.md

## Principles

### `curious-developer-audience` — Build own libraries for curious developers without excluding professionals

For Muze-owned libraries and developer-facing tools, prefer interfaces and documentation that work for technically curious non-professional programmers while remaining attractive and useful to professional developers.

This is an intended audience for Muze-owned reusable software, not a claim about the end users of client applications.

### `view-source` — Invite people to look under the hood

Prefer libraries whose implementation, examples, and abstractions reward inspection. Make it reasonable for developers to learn by looking at how the thing works rather than treating internals as deliberately opaque magic.

This complements the broader `collaborative-inspectability` principle in `CUL-MUZE-001`, but is stronger and specifically developer-facing.

### `lightweight-distribution` — Keep reusable software economical to load and run where practical

For Muze-owned libraries, prefer software small enough to remain useful on slower devices and connections when doing so does not conflict with the library's actual purpose.

Do not turn this into a universal performance threshold. The relevant constraint depends on the product, audience, and deployment context.

### `package-maturity-signal` — Treat Muze package namespaces as stewardship signals

The `@muze-nl` npm namespace is intended as a trust signal for libraries that are close to production-ready: the public API is expected to be stable, a fresh project should be able to install and use the package, and supported usage should be documented clearly.

Experimental libraries should normally remain under `@muze-labs` until they are mature enough to carry the main Muze production-readiness signal.

Moving from `@muze-labs` to `@muze-nl` is a release-readiness and stewardship decision, not merely a naming cleanup.

This principle concerns Muze-owned packages/GitHub organizations. It must not leak into client project naming or release policy unless that project explicitly adopts it.

## Relationship to general Muze culture

A Muze-owned reusable library will normally adopt both:

- `CUL-MUZE-001` for broad engineering preferences; and
- `CUL-MUZE-LIB-001` for library-specific audience/stewardship preferences.

A client project should not inherit `CUL-MUZE-LIB-001` merely because Muze is developing it.

## Tensions / trade-offs

Library stewardship goals can conflict with project realities. For example, minimizing size may be less important than standards compliance for a particular library; a professional-only internal tool may not need the same onboarding posture; a client-owned package may have a different release taxonomy.

Use the profile only where its scope matches the work, and record consequential deviations rather than silently treating it as organization-wide law.
