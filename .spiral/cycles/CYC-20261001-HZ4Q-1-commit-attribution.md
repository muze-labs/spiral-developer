---
id: CYC-20261001-HZ4Q-1
---

# Cycle: Give every agent the same commit attribution

Repository branch: `spiral/CYC-20261001-HZ4Q-1-commit-attribution`
Branch verified: verified at cycle open against actual Git branch state; re-check before each semantic causal commit and during evaluation.

## Analyze

Project state / prior evaluation that makes this cycle relevant:

Spiral Developer tells agents to perform routine Git operations, including creating semantic causal commits (`docs/git-workflow.md`, "AI as Git operator"). It did not previously say who such a commit is attributed to.

A repository-wide search found no `Co-Authored-By` usage anywhere. The only trailers the process described were the optional `Spiral-*` navigation trailers, and the only guidance on them was that they are human/navigation summaries whose authoritative form lives in the companion Turtle. `AGENTS.md` "Git ownership" and `CONTRIBUTING.md` were both silent on authorship.

The premise that a commit stays signed and attributable to a verified account is not hypothetical: `AGENTS.md` requires signed merges to preserve verified authorship, and this repository's own history is GPG-signed.

Important risk / uncertainty / desired movement:

Without a stated rule, an agent operating Git has no normative basis for choosing author/committer fields or for crediting the model that wrote the code. That is an unstated-authority problem rather than a bug: the trust model depends on commits being attributable and human-owned, and the process did not say how to keep them so.

Relevant human direction / feedback:

`SRC-20261001-HZ4Q-2`. The human supplied the rule and its reasoning directly, marked the substantive points settled, and asked that the `:variant` question not be decided — only its analysis recorded. On being asked directly, the human confirmed collapsing the variant and landing the work as a proper cycle.

Governing higher-level plan / direction:

None. No durable multi-cycle roadmap exists for this repository; each cycle so far was opened from its own direction.

Current position in that plan:

Not applicable.

## Plan

### Cycle goal

Give Spiral Developer a standing commit-attribution rule that every agent working under it follows, without contradicting the existing invariants about Git history, navigation trailers, or the single authoritative causal graph.

### Commitment boundary

The human directed the rule and its content directly, stating the substantive points were settled and not to be relitigated. The one held-open element was explicitly deferred with a request to record its analysis rather than decide it. The human subsequently confirmed both the variant treatment and the choice to land the work as a proper cycle. That confirmation is the commitment boundary for this cycle.

### Why now / why this cycle boundary

The gap is cheap to falsify and was falsified immediately: the rule is absent everywhere. It is also upstream of every future governed commit in this repository, so establishing it before more causal history accumulates avoids retrofitting attribution later. The boundary is one coherent documentation change with its own review surface; splitting it further would separate the rule from the rationale that makes it safe to apply.

### Plan continuity decision

No governing plan. The cycle proceeds from direct human direction rather than from a roadmap position.

### Current starting evidence

- Repository-wide search: no `Co-Authored-By` present in any file.
- `docs/git-workflow.md` describes only optional `Spiral-*` navigation trailers.
- `AGENTS.md` "Git ownership" and `CONTRIBUTING.md`: no authorship guidance.
- Existing commits in this repository are GPG-signed, so attribution is observable rather than theoretical.

### Evaluation basis

The rule is stated once canonically in `docs/git-workflow.md` and pointed to from the agent-facing and human-facing entry points; every settled element of the human's direction is present; the `:variant` analysis is recorded with the confirmed treatment rather than left open; and no existing invariant is contradicted.

### Likely work

State the rule and its rationale in `docs/git-workflow.md`; add a concise operator instruction in `AGENTS.md`; add the human-facing consequence in `CONTRIBUTING.md`.

### Explicit non-goals

- No tooling, hook, or CI enforcement of the trailer.
- No retroactive attribution of existing commits. Existing history stays as it is.
- No change to the Turtle ontology or the `Spiral-*` navigation trailers.
- No culture or warning-profile change. This is a trust invariant of the process, not a preference.

### Pause / re-plan conditions

Evidence that the rule contradicts an existing invariant; or that attribution cannot be applied to a real commit without a decision the human has withheld.

## Act

Important artifacts / semantic commits produced:

- `SRC-20261001-HZ4Q-2` — the human direction, including the recorded `:variant` analysis.
- `docs/git-workflow.md` — the canonical rule, rationale, and variant treatment.
- `AGENTS.md`, `CONTRIBUTING.md` — entry-point consequences.

Material implementation decisions or deviations from the initial likely work:

The rule is stated canonically in one place rather than duplicated in full. `AGENTS.md` carries the operator instruction and `CONTRIBUTING.md` the human-facing consequence, both pointing at `docs/git-workflow.md`.

A case was found where the rule's assumption does not hold universally, and it is recorded in the cycle evaluation rather than resolved inside the rule.

Out-of-scope discoveries retained for later:

- No mechanical check verifies the trailer's presence or form. CI enforcement was not requested and is deliberately out of scope.
- `git-workflow.md:109` ("Trailers are human/navigation summaries") reads as a blanket statement four lines above a non-navigation trailer. The new subsection carves out the exception explicitly instead of editing the older sentence.

## Evaluate

Integrated result against cycle goal:

The rule now exists canonically in `docs/git-workflow.md` and is pointed to from both entry points. Every settled element of the human's direction is stated: the trailer form, the human holding author and committer, the display-name rule, the slug derivation with the namespace dropped, the rejection of vendor no-reply addresses, the subaddressed address, and identification from the agent's own tooling. The `:variant` treatment is settled as confirmed rather than left open.

Evidence / acceptance result:

- Repository-wide search before the change: no `Co-Authored-By` anywhere; the gap was real, not merely unlocated.
- `spiral validate` reports `ok` across 98 Turtle files and 1232 triples.
- The rule was applied to this cycle's own commits. Each carries `Co-Authored-By: Space Bunny Alpha <ai+space-bunny-alpha@muze.nl>`, the human holds both author and committer, and `git log --format=%G?` returns `G` for each, confirming a good signature.

Metric or risk movement:

The risk named at cycle open — an agent having no normative basis for choosing author/committer fields — is closed for agents that read the process. No measurable proxy exists for it, and none was claimed.

What changed in our understanding:

Two corrections to earlier working conclusions in this cycle.

The model that actually served a step is recoverable from the agent's own tooling, even when the configured session route does not name a model. A router may present a route rather than a resolved model, so a rule that says "identify yourself from your tooling" is only as good as the tooling's ability to report the acting model, and the acting model may not be the model the session was configured with.

Relatedly, a session is not guaranteed to use one model throughout. A session may be served by more than one model across its steps, so the model that should be credited is the one that served the work immediately being committed, not an average or a session-level assumption.

Neither correction changes the rule as written; both bear on how reliably an agent can follow it.

Surprises / model mismatches:

None material.

Known compromises:

The rule is documentation only. Nothing mechanically verifies that a commit carries the trailer, in the correct form, or with the correct identity. An agent could ignore it and history would show it.

`git-workflow.md:109` ("Trailers are human/navigation summaries") still reads as a blanket statement immediately above a trailer that is not a navigation summary. The new `#### Relationship to the navigation trailers` subsection carves out the exception rather than editing the older sentence, to avoid churn against a stable line. A future reader skimming only that sentence could still be misled.

Unresolved issues within current goal:

None blocking. The rule is applied and consistent.

Candidate next-cycle inputs (surface high-leverage assumptions only when material):

- The rule says to identify the model from "what the agent's own tooling reports" without saying which report to trust when several disagree, or when the configured route and the resolved model differ. Stating the preference explicitly would remove the ambiguity rather than leaving each agent to infer it.
- Consider a mechanical check for trailer presence and form. This would make the rule enforceable rather than advisory, and the repository already runs a required Spiral check.

Human evaluation / feedback:

The human confirmed the `:variant` treatment (collapse, credit the base model), chose a proper cycle over a direct commit, and directed use of the catalogue identity for this cycle's own trailers.

Cycle accepted, still open, or deliberately re-planned:

Pending human evaluation. The cycle is `Active` on `spiral/CYC-20261001-HZ4Q-1-commit-attribution`; `main` is untouched.

## Process learning

What context/constraint/evaluation helped:

Asking directly instead of reasoning in circles about the variant question and the model identity. Both were held open by the human on purpose, and each resolved immediately once put as a clean either/or.

Recording the `:variant` analysis in the source artifact rather than only in prose is what made the follow-up question answerable: the confirmation had a rationale already attached, so it was a confirmation rather than a fresh design decision.

What bookkeeping was useless:

None notable. Allocating a workspace code before knowing whether a cycle would be opened was slightly premature, since the human subsequently chose to land the work as a proper cycle.

What should the environment learn from this cycle:

A rule that depends on identifying the acting agent should say how to identify it, at least to the level of "read the record of what actually served the work, not the configured route." Leaving that to "your own tooling" invites a confidently wrong answer when several records exist and disagree.
