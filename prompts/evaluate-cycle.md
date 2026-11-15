# Evaluate Cycle Prompt

Use this when execution has reached a point where the agreed cycle goal can be judged. Evaluation returns the collaboration to **discourse**: interpret what the evidence and human feedback mean before turning anything into another instruction. **Evaluate first; do not immediately plan new work.** Recent discoveries are deliberately retained here without being promoted into priority yet; next-cycle selection happens only after `plan-cycle` re-reads any governing plan/roadmap.

Read the current `CYC-*` goal/non-goals, relevant causal artifacts, actual repository/runtime evidence, and human/user feedback. For a repository-changing cycle, mechanically inspect the current Git branch and verify that it still matches the active `CYC-*` identity before presenting evaluation; surface/correct a stale cycle branch rather than normalizing it.

## Check whether simplification is warranted

Briefly review accumulated complexity in the affected area using [the cycle guidance](../docs/cycles.md#review-accumulated-complexity-during-evaluate). Ask what became harder to understand/change/verify, which earlier constraints still justify it, and whether removing or restructuring something would reduce that burden enough to justify the cost.

Repeated defects or exceptions at the same boundary, duplicated ownership/state, growing verification effort, or a substantial milestone may warrant a bounded deeper review. Keep the current design as a valid option. Use state modelling only when it helps resolve a concrete uncertainty; retain the same properties across alternatives and distinguish model results from implementation evidence.

Record a concise conclusion and supporting reason, including a revisit condition for a material deferred candidate. Do not turn the review into an automatic refactor, mandatory model, metric quota, or whole-history audit. Apply normal cycle scope and human acceptance boundaries.

## Present the cycle evaluation

Summarize:

**Cycle goal:** …
**Integrated result:** …
**Evidence / acceptance:** …
**Metric/risk movement:** …
**What changed in our understanding:** …
**Surprises / model mismatches:** …
**Known compromises:** …
**Simplification review:** … (brief conclusion/reason; candidate and revisit condition when material)
**Unresolved issues within the agreed goal:** …
**Out-of-scope discoveries retained for later:** …
**Implications for governing plan/roadmap:** … (evidence that may support continuing, revising, or deviating; do not choose the next cycle here)
**Possible reusable lesson:** …

Explicitly distinguish:

- work/evidence showing the current goal is still incomplete;
- genuinely new direction that belongs in a later cycle.

Do not hide failed verification, missing measurements, weak evidence, or newly exposed risks merely because implementation is complete. If the cycle exposed a materially uncertain assumption with large downstream consequences, include it among candidate next-cycle inputs together with why late discovery matters and any cheap falsification. Do not invent a risk list merely to fill the evaluation, and do not choose its priority here.

## Ask the human to evaluate

Ask whether the human considers the agreed cycle goal sufficiently achieved and whether the evaluation reflects reality. Treat suggestions, reactions, and tentative alternatives here as discourse/feedback unless the human clearly commits to correcting the same goal or explicitly re-plans the cycle.

If feedback shows the **same agreed goal is not yet satisfied**, keep the current cycle open. Correct the work on the same cycle branch, preserve causal history, and evaluate again.

If feedback introduces **new direction outside the agreed goal**, record it as feedback/risk/candidate next-cycle input. Do not silently expand scope. The human may explicitly re-scope the current cycle, but treat that as deliberate re-planning.

For repository-changing work, this evaluation may be presented through the pull request/review surface itself; do not require duplicate human approval. When the cycle is accepted, complete the normal merge boundary. Only then return to `prompts/plan-cycle.md` for the next Analyze/Plan interview.

At the boundary also ask whether the cycle produced a reusable `LES-*` lesson whose scope is justified by evidence.
