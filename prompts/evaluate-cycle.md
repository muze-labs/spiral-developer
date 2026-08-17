# Evaluate Cycle Prompt

Use this when execution has reached a point where the agreed cycle goal can be judged. **Evaluate first; do not immediately plan new work.** Recent discoveries are deliberately retained here without being promoted into priority yet; next-cycle selection happens only after `plan-cycle` re-reads any governing plan/roadmap.

Read the current `CYC-*` goal/non-goals, relevant causal artifacts, actual repository/runtime evidence, and human/user feedback. For a repository-changing cycle, mechanically inspect the current Git branch and verify that it still matches the active `CYC-*` identity before presenting evaluation; surface/correct a stale cycle branch rather than normalizing it.

## Present the cycle evaluation

Summarize:

**Cycle goal:** …
**Integrated result:** …
**Evidence / acceptance:** …
**Metric/risk movement:** …
**What changed in our understanding:** …
**Surprises / model mismatches:** …
**Known compromises:** …
**Unresolved issues within the agreed goal:** …
**Out-of-scope discoveries retained for later:** …
**Implications for governing plan/roadmap:** … (evidence that may support continuing, revising, or deviating; do not choose the next cycle here)
**Possible reusable lesson:** …

Explicitly distinguish:

- work/evidence showing the current goal is still incomplete;
- genuinely new direction that belongs in a later cycle.

Do not hide failed verification, missing measurements, weak evidence, or newly exposed risks merely because implementation is complete. If the cycle exposed a materially uncertain assumption with large downstream consequences, include it among candidate next-cycle inputs together with why late discovery matters and any cheap falsification. Do not invent a risk list merely to fill the evaluation, and do not choose its priority here.

## Ask the human to evaluate

Ask whether the human considers the agreed cycle goal sufficiently achieved and whether the evaluation reflects reality.

If feedback shows the **same agreed goal is not yet satisfied**, keep the current cycle open. Correct the work on the same cycle branch, preserve causal history, and evaluate again.

If feedback introduces **new direction outside the agreed goal**, record it as feedback/risk/candidate next-cycle input. Do not silently expand scope. The human may explicitly re-scope the current cycle, but treat that as deliberate re-planning.

For repository-changing work, this evaluation may be presented through the pull request/review surface itself; do not require duplicate human approval. When the cycle is accepted, complete the normal merge boundary. Only then return to `prompts/plan-cycle.md` for the next Analyze/Plan interview.

At the boundary also ask whether the cycle produced a reusable `LES-*` lesson whose scope is justified by evidence.
