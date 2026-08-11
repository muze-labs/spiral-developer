# Warning Profiles

## Purpose

Some concerns are neither Spiral trust invariants nor engineering-culture preferences.

They are **patterns worth noticing** because they may indicate lost agency, evidence overreach, avoidable closure, exclusion, or other meaningful harm. Spiral Developer represents these as explicit, versioned **warning profiles**.

A useful boundary is:

> **Spiral core says what must be true for justified trust. Culture says what we prefer when several trustworthy choices remain. Warning profiles say what deserves suspicion or deliberate inspection.**

Warning profiles are replaceable. A project may adopt, extend, replace, or decline them without changing Spiral core or its engineering culture.

## Adoption is explicit

A warning profile is active only when project context explicitly adopts an exact profile version with `sd:adoptsWarningProfile`.

Do not silently apply every warning profile available to the agent. A narrower or organization-specific profile must not leak into a project merely because the same organization uses it elsewhere.

Profiles may live locally, be vendored, or come from independently versioned repositories. The important property is that the project can identify the exact profile/version it chose to use. Bundled profiles in this repository are starter material, not permanent canonical policy.

## Warnings are signals, not automatic prohibitions

A warning should normally have four parts:

1. **Pattern** — what condition deserves attention?
2. **Significance gate** — when is the concern material enough to surface?
3. **Question** — one concise operational question for the agent/reviewer.
4. **Default effect** — inspect and disposition; do not automatically block unless another constraint/risk requires it.

Do not turn routine work into a philosophical debate. Surface a warning only when it could materially change a decision, user outcome, authority boundary, evidence claim, reversibility, accessibility, or future ability to correct the system.

## Relationship to risks

A warning occurrence does not need its own durable artifact merely because it fired.

When a concern is consequential enough to matter to later reasoning or review, create an ordinary `RSK-*` artifact and link it to:

- the project artifact(s) that exhibit the concern; and
- the exact adopted warning-profile version that prompted the inspection.

Where useful, use the `sd:fragment` on the profile reference to identify the warning ID, for example `WPF-HUMAN-001-W7`.

The resulting risk remains a project claim that can be accepted, mitigated, deferred, rejected, or superseded. The warning profile is the lens that helped notice it, not proof that harm exists.

## Agent behavior

For consequential work:

1. identify the project's explicitly adopted warning profile(s);
2. apply only signals whose scope and significance gate fit the current change;
3. state the warning in ordinary operational language;
4. distinguish observed facts from inference about possible consequences;
5. avoid automatic vetoes unless a separate hard constraint demands one;
6. record a durable risk/disposition only when the concern is material enough to be useful later.

An agent may propose a new warning or refinement when experience exposes a recurring pattern. It must not silently add that proposal to the project's active normative environment. Adoption is an explicit project/process decision.

## Initial bundled profile

This repository currently ships a replaceable starter profile at:

- `warning-profiles/human-impact-and-epistemic.md`

It is intentionally separate from Muze engineering culture and is not active merely because a project uses Spiral Developer or the Muze culture profile.
