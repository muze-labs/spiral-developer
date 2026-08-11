# Contributing with Spiral Developer

This document is the human collaborator's operational guide.

Spiral Developer changes who performs much of the implementation work, but it does not remove human authority over meaning, risk, and acceptance. It is deliberately a **trust-but-verify** process: the agent is given broad freedom for contained work because the process is designed to make consequential claims independently inspectable before they become authoritative.

## The short version

For a normal feature or change:

1. Start from the current need and its best available source; let the AI crystallize a request and, where interpretation matters, the understanding that produced it.
2. Let Spiral Developer create and operate a feature branch.
3. Give feedback about intent, behavior, constraints, trade-offs, and observed problems rather than micromanaging code generation. Treat exploratory proposals as hypotheses when you want independent search rather than simple execution.
4. When evidence is needed before commitment, evaluate the smallest realistic probe appropriate to the uncertainty; follow the active culture profile where it helps choose that probe.
5. Let the AI maintain the causal artifacts, Turtle graph, tests/evidence, and Git commits.
6. Review the pull request as a proposal to admit a complete causal history into the authoritative branch.
7. Merge with a normal merge commit. Never squash or rebase causal history.

## What humans remain responsible for

Humans retain authority over:

- which interpretation of client/user intent the project is willing to accept when judgment is required;
- interpretation of meaningful user feedback;
- material changes in product direction;
- significant trade-offs when evidence is insufficient;
- irreversible or high-impact decisions that require accountability;
- final acceptance where the project requires human responsibility.

This does **not** require a human to read every generated line of code.

The human role is not to approve every intermediate agent action. For reversible branch-contained work, let the agent operate and verify the resulting causal case. Move human authorization earlier only when consequences would be unacceptable before review or cannot be adequately reversed.

The human review question is broader:

> **Can we inspect and interrogate the production system well enough to understand why this result exists, what evidence supports it, and what must change if it is wrong?**

Inspect code directly whenever the risk or uncertainty warrants it.

## Starting work

A feature or meaningful change gets its own branch. Prefer a branch name that includes the request ID when one exists, for example:

```text
spiral/REQ-017-account-deactivation
```

The AI should create the branch and routine commits when its tools and permissions allow it.

The first crystallized commit should normally capture the current request or the smallest missing upstream artifact needed to make the work causally grounded. When source provenance or interpretation is consequential, that may be a `SRC-*` source or `UND-*` understanding before the request.

## Engineering culture

Not every implementation choice is dictated by a requirement. A project may explicitly adopt organization, team, client, or local `CUL-*` culture profiles. These express defeasible preferences about how to choose among several trustworthy options.

When reviewing a consequential choice, it is legitimate to ask both “what required this?” and “why did we choose this particular approach?” The second answer may be culture. Culture can change prospectively without rewriting why older software was built under an earlier profile. See `docs/culture.md`.

## During development

Do not ask the AI to preserve every exploratory attempt. Uncommitted exploration may be discarded.

Once the AI creates a semantic causal commit, treat it as evidence. If a later discovery shows the commit was wrong, add a new commit that supersedes or corrects it. Do not rewrite the old one.

Good human interventions sound like:

- “This does not represent the client's intent; they need X, not Y.”
- “This interaction does not produce meaningful feedback because users cannot complete the task.”
- “This dependency is inconsistent with our replaceability principle.”
- “This test only mirrors the implementation; it does not establish the design invariant.”
- “We are solving a problem that belongs to a later cycle.”

Avoid turning the human into an expensive prompt router who dictates line-by-line implementation unless that level of control is genuinely required.

## Continued development and implementation history

When the AI revises code that Spiral already governs, it should not ask you to re-explain every historical decision or load the entire history into context. The current `IMP-*` resource should expose the causes that still matter now; older versions remain available for historical interrogation.

For a material revision, the AI should preserve immediate implementation lineage and the reason for the transition. A behavior-preserving refactor still belongs in lineage when it materially moves or reshapes a governed implementation.

As a human reviewer, watch for two opposite failures:

- **lost history** — a refactor or rewrite severs the implementation from the reasons it inherited;
- **history overload** — every old cause is carried into current context or presented as if it still justified current behavior.

The target is a small current explanation plus deep history on demand. If this works, repeatedly governed areas should require less archaeology over time. Treat that as something to verify in practice, not as an assumption.

## Inquiry versus execution

When the product/problem framing is still open, invite the AI to challenge consequential assumptions rather than merely elaborating the first proposed solution. A useful human prompt is “treat this as a hypothesis, not a decision” or “what assumption in this question would matter most if it were wrong?”

Once the frame has survived enough evidence, let the AI execute without repeatedly reopening it. Good collaboration is not constant debate.

Remember:

> **Capability is not endorsement.**

An impressive architecture or implementation plan demonstrates that a direction is feasible to elaborate. It does not by itself establish that the direction answers the right problem.

## Reviewing a pull request

The PR is the main human governance boundary.

Review in this order when practical:

1. **Origin and understanding** — where it matters, can we tell what was actually expressed/observed, how it was interpreted, and where provenance is weak or unavailable?
2. **Intent** — does the request accurately operationalize the accepted understanding?
3. **Framing** — did a consequential assumption prematurely narrow the problem or acceptance space?
4. **Meaningful feedback** — where intent was uncertain, did intended users interact with something real enough to teach us?
5. **Design** — do the design choices answer the request and respect current constraints?
6. **Causal graph** — are the significant relationships and upstream versions truthful, including the distinction between current effective implementation causes and historical lineage?
7. **Evidence** — does verification actually establish that implementation realizes design?
8. **Acceptance** — does acceptance establish that behavior satisfies the request?
9. **Complexity** — are new concepts, dependencies, abstractions, or change radius justified?
10. **Risk** — are deferred risks still appropriately deferred, and are unresolved assumptions visible?
11. **Code** — inspect directly wherever semantic, security, maintainability, or operational risk makes that valuable.

Do not approve a PR merely because CI is green. CI establishes mechanical and executable claims; the human review establishes that the claims themselves are sensible.

See [`docs/review.md`](docs/review.md).

## Merge means acceptance of history

Use a normal merge commit.

Do not:

- squash the feature branch;
- rebase it onto the authoritative branch after causal commits exist;
- amend published causal commits;
- force-push causal history.

If the branch needs newer authoritative work, merge the authoritative branch **into** the feature branch.

The merge commit means:

> **This feature branch, including the causal history that produced it, was reviewed and admitted into authoritative project history.**

## Existing projects

Do not reconstruct the whole project's past.

When new work touches legacy behavior, reconstruct only enough context to change that behavior safely. Mark historical claims as explicit, evidenced, inferred, or unknown. Leave the touched capability better traced than before.

See [`docs/brownfield.md`](docs/brownfield.md).

## When the process gets in the way

Say so.

Spiral Developer is experimental. An artifact or relation that repeatedly creates bookkeeping without improving reasoning, context, verification, impact analysis, or auditability should be challenged and potentially removed.

Humans preserve meaning; AI should carry as much of the mechanical bookkeeping as possible.
