# Contributing with Spiral Developer

This document is the human collaborator's operational guide.

Spiral Developer changes who performs much of the implementation work, but it does not remove human authority over meaning, risk, and acceptance. It is deliberately a **trust-but-verify** process: the agent is given broad freedom for contained work because the process is designed to make consequential claims independently inspectable before they become authoritative.

## The short version

For a normal cycle:

1. Start from the current project state, need, prior evaluation, and known risks; agree one coherent cycle goal and how you will judge it.
2. Let Spiral Developer create and operate one cycle branch when repository changes are involved.
3. Let the AI crystallize the source/understanding/request/design/evidence artifacts that are actually needed inside that cycle; do not review every internal task as a separate unit.
4. Give feedback about intent, behavior, constraints, trade-offs, and observed problems rather than micromanaging code generation.
5. When the goal can be judged, review the integrated cycle evaluation (often in the PR). If the same goal is incomplete, keep the cycle open; if feedback creates new direction, normally save it for next-cycle planning.
6. Let the AI maintain the causal artifacts, Turtle graph, tests/evidence, and Git commits.
7. Merge accepted cycle history with a normal merge commit. Never squash or rebase causal history, then plan the next cycle.

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

## Starting a brownfield project

When Spiral is first introduced to an existing project, the AI should begin with a short guided intake rather than expecting you to study the whole process or immediately provide a perfectly framed feature. Intake has an explicit `Incomplete/Complete/Stale` status: every required topic must be considered, although `Unknown`, `Not relevant`, and deliberate deferral are valid answers. While intake is incomplete, the AI should keep telling you which topics remain rather than silently moving on. The intake asks about project goals, important outcomes/metrics, consequential decisions already taken, constraints/commitments, known tolerated problems, feedback sources, future direction, and which risk/metric lenses seem relevant. It should explain why each question matters and offer common choices while always allowing custom, uncertain, or not-relevant answers.

After you confirm the project summary, the AI inspects current reality and brings back candidate risks, metric gaps, missing measurements, and uncertainties. **You set priority.** You can reject a supposed risk, accept or defer it, ask for more evidence, change the framing, or add something the AI missed. That produces the starting risk picture for the next Spiral cycle. See `docs/brownfield-intake.md`.

## Starting work

Before consequential execution, agree one coherent **cycle goal** with the AI. For ordinary repository-changing work, the AI then creates one cycle branch, for example:

```text
spiral/CYC-017-account-deactivation
```

The AI should mechanically verify that the actual Git branch matches the active cycle when the cycle opens, before each semantic causal commit, and during evaluation; this is intended to catch accidental continued work on an older cycle branch.

The AI may carry out several tasks and create several semantic commits on that branch. You should not need to review a separate branch/PR for each internal task. Early/unfamiliar cycles may be small, but once governing assumptions are stable, the AI should prefer a larger coherent cycle rather than creating tiny cycles by habit. The first crystallized commits should establish the cycle and whatever upstream causal artifacts are needed to ground its work.

If an adjacent problem appears during execution, the default is to retain it for the next planning interview. It belongs in the active cycle only when it is necessary to achieve/evaluate the agreed goal or repair a regression caused by the cycle.

## Engineering culture

Not every implementation choice is dictated by a requirement. A project may explicitly adopt organization, team, client, or local `CUL-*` culture profiles. These express defeasible preferences about how to choose among several trustworthy options.

When reviewing a consequential choice, it is legitimate to ask both “what required this?” and “why did we choose this particular approach?” The second answer may be culture. Culture can change prospectively without rewriting why older software was built under an earlier profile. See `docs/culture.md`.

## Warning profiles

Projects may explicitly adopt `WPF-*` warning profiles independently of engineering culture. They identify patterns worth inspecting, not universal rules or automatic blockers. A useful warning is concise, materially relevant, and connected to a concrete decision.

Humans should feel free to reject, defer, or scope a warning when the evidence does not justify the concern. Conversely, a warning that exposes a consequential accessibility, authority, evidence, composition, optionality, or model-assumption issue can become an ordinary `RSK-*` artifact for durable review. See `docs/warning-profiles.md`.

## Development cycles

The main human-visible rhythm is not “approve every AI task.” It is:

> **agree the cycle goal → let the AI execute inside that boundary → evaluate the integrated result → choose the next goal**

A cycle may contain several tasks and commits. New adjacent work is normally saved for the next cycle rather than added mid-cycle; work required to achieve/evaluate the current goal or repair a regression caused by it can remain inside the cycle.

At evaluation, feedback such as “this still does not satisfy the agreed goal” keeps the cycle open for correction. Feedback such as “this makes me want a different capability too” is normally next-cycle input. This keeps human review focused on the outcome you agreed to, not the AI's internal task decomposition.

See [`docs/cycles.md`](docs/cycles.md).

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
11. **Warnings** — did an explicitly adopted warning profile surface a materially relevant concern, and was it dispositioned rather than automatically obeyed or ignored?
12. **Code** — inspect directly wherever semantic, security, maintainability, or operational risk makes that valuable.

Do not approve a PR merely because CI is green. CI establishes mechanical and executable claims; the human review establishes that the claims themselves are sensible.

See [`docs/review.md`](docs/review.md).

## Merge means acceptance of history

Use a normal merge commit.

Do not:

- squash the cycle branch;
- rebase it onto the authoritative branch after causal commits exist;
- amend published causal commits;
- force-push causal history.

If the branch needs newer authoritative work, merge the authoritative branch **into** the cycle branch.

The merge commit means:

> **This cycle outcome, including the causal history that produced it, was reviewed and admitted into authoritative project history.**

## Existing projects

Do not reconstruct the whole project's past.

When new work touches legacy behavior, reconstruct only enough context to change that behavior safely. Mark historical claims as explicit, evidenced, inferred, or unknown. Leave the touched capability better traced than before.

See [`docs/brownfield.md`](docs/brownfield.md).

## When the process gets in the way

Say so.

Spiral Developer is experimental. An artifact or relation that repeatedly creates bookkeeping without improving reasoning, context, verification, impact analysis, or auditability should be challenged and potentially removed.

Humans preserve meaning; AI should carry as much of the mechanical bookkeeping as possible.
