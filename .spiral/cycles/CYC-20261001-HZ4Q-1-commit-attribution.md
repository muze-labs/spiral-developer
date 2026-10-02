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

The premise that a commit stays signed and attributable to a verified account is not hypothetical in this repository: local configuration has `commit.gpgsign=true` with a configured `user.signingkey`, and `AGENTS.md` requires signed merges to preserve verified authorship.

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
- Local Git configuration: `commit.gpgsign=true`, `user.signingkey` set.

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

Pending.

## Process learning

Pending.