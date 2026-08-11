# Engineering Culture as Provenance

Requirements and trust invariants often underdetermine a design.

Several implementations may satisfy the same request, preserve the same safety properties, and pass the same tests. Which one an engineering team chooses is influenced by accumulated experience, values, habits, aesthetics, preferred standards, and ideas absorbed from previous systems.

Spiral Developer treats that **engineering culture as explicit, versioned provenance** rather than pretending every design choice follows logically from the requirement.

A useful boundary is:

> **Spiral core contains what must be true for justified trust. Culture contains what we prefer when several trustworthy choices remain available.**

This boundary is itself revisable. When uncertain, make the assumption visible rather than forcing a permanent classification.

## Culture profiles

A `CUL-*` artifact describes durable engineering preferences that may shape many requests, designs, and implementations.

Examples include preferences for:

- frontend-first interaction probes;
- small composable components;
- web-native standards;
- replaceable dependencies;
- explicitness over framework magic;
- particular API, testing, operational, or architectural styles.

A project should make its active culture explicit when those preferences materially affect agent decisions. Culture can come from:

- an organization-wide profile;
- a team profile;
- a client or platform context;
- project-specific additions.

Do not load arbitrary culture merely because it exists. A consuming project should adopt the profile(s) it actually wants the agent to use.

### Scope is part of culture provenance

A culture profile is not automatically applicable everywhere its organization name appears. Prefer multiple scoped profiles over one organization-wide bag of preferences when principles have materially different applicability.

For example, a broad engineering profile may apply to most work while a library-stewardship profile applies only to organization-owned reusable packages. A client project should not inherit the narrower profile merely because the supplier organization uses it elsewhere.

Treat profile adoption as the executable scope boundary: if the project has not adopted a profile, an agent should not silently use that profile as justification. When only some principles inside a profile are conditional, say so explicitly in the profile and prefer splitting the profile if conditionality becomes consequential or recurrent.

## Human recognition and validation

An agent may extract, compare, or propose a culture profile, but it should not silently declare that its own inference *is* an organization’s culture. When an agent-derived profile is intended to represent a team or organization, preserve a relevant human review or adoption decision as evidence against an exact profile version.

A useful pattern is a `sd:VerificationEvidence` artifact whose `sd:verifies` relation points to the exact reviewed `CUL-*` version and whose provenance leads to the human source or decision. The review establishes representational accuracy at that point in time; it does not make culture immutable or universally binding.

Human-authored culture can have more direct provenance, but consequential adoption should still remain explicit and versioned.

## Adoption

Use `sd:adoptsCulture` from project context to the exact `CUL-*` version(s) that are active for the project when this provenance matters.

For simple projects, a local `.spiral/culture.md` may contain the active profile directly. For shared profiles, copy/vendor a pinned version into the project or otherwise preserve enough source/version information to reconstruct which profile was in force. Cross-repository provenance should not be faked with a Git hash whose repository is ambiguous.

When several profiles are active, adopt each one explicitly. A general organization profile does not imply its narrower companion profiles.

## Cultural influence on decisions

Use `sd:shapedBy` when a design or implementation choice is materially influenced by an active culture preference but is not required by it.

This enables explanations such as:

> “The capability exists because request Y requires it. We implemented it with approach X because culture principle Z shaped the choice.”

This is different from `sd:constrainedBy`:

- `constrainedBy` means the referenced artifact materially narrows the acceptable solution space;
- `shapedBy` means the referenced preference influenced which acceptable solution was chosen.

Both may point to a culture artifact when truthful.

Use stable fragments inside a `CUL-*` artifact when a specific principle matters, for example `frontend-first` or `replaceable-dependencies`.

## Culture is defeasible

Culture is not invisible law.

An agent should be able to choose against a cultural preference when more specific evidence, constraints, risks, or project culture justify another approach. Record the consequential trade-off in the design rather than applying automatic precedence rules.

A good explanation may say:

> “The normal culture profile prefers X, but constraint Y made Z the better choice here.”

Do not treat a cultural preference as an acceptance criterion unless the project has explicitly promoted it into a requirement or constraint.

## Culture changes prospectively

Culture profiles are versioned. When a team changes its mind:

1. preserve the old culture version;
2. record the lesson/evidence that motivated the change where useful;
3. create a new culture version;
4. let new work use the new profile;
5. do not rewrite the provenance of older decisions.

This lets historical interrogation distinguish:

- what was required;
- what was culturally preferred at the time;
- what the team would prefer now.

## Muze engineering culture

The first explicit reusable profiles ship in `cultures/muze-engineering.md` and `cultures/muze-library-stewardship.md`. The former captures broadly applicable Muze engineering preferences; the latter is intentionally scoped to Muze-owned reusable libraries/packages and should not leak into client projects.

It is **not Spiral core**. It is the initial extraction of preferences that had accumulated inside Spiral Developer while the process was being developed at Muze. Other organizations should be able to adopt Spiral without inheriting those preferences.

The profile is deliberately a first pass. Further dogfooding should identify assumptions that still belong in culture rather than core, and lessons may move principles in either direction when evidence justifies it.
