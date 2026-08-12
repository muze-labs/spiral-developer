---
id: EVD-CYCLE-001
---

# Verification Evidence: Explicit outer cycle cadence

## What is being verified

Adoption of `LES-012`: Spiral's existing outer cycle should become the normal human-visible learning/integration boundary, with one coherent goal, stable scope during execution, one cycle branch/review boundary for ordinary repository-changing work, explicit evaluation before new direction, and interview-style planning for the next cycle.

Implementation commit under verification: `b1e35d4f653492fdc7ce3fe68ead9dfaf2c96d80`.

## Structural / consistency checks

- `docs/cycles.md` now defines the outer `Analyze → Plan → Act → Evaluate → Analyze` cadence and explicitly distinguishes a coherent cycle goal from an arbitrary task bucket.
- `prompts/plan-cycle.md` provides an interview-style planning flow that uses current project state, prior evaluation, risks/metrics, and human direction to propose one goal with why-now, evaluation basis, likely work, non-goals, and pause/re-plan conditions.
- `templates/CYCLE.md` records the agreed goal, evaluation basis, likely work, non-goals, execution discoveries, and human evaluation without introducing a task ontology or formal state machine. `templates/CYCLE.ttl` supplies only the existing `sd:Cycle` artifact identity.
- `docs/process.md`, `AGENTS.md`, `docs/quickstart.md`, `CONTRIBUTING.md`, and the start/brownfield/bootstrap prompts route normal work through an active human-confirmed cycle before consequential execution.
- `docs/git-workflow.md` now makes one cycle branch the default repository integration/review boundary and explicitly says internal tasks do not normally receive their own branches/PRs.
- Scope-stability guidance consistently keeps adjacent discoveries out of the active cycle unless they are necessary to achieve/evaluate the agreed goal or repair a regression introduced by the cycle.
- `prompts/evaluate-cycle.md`, `docs/process.md`, `docs/review.md`, and `docs/cycles.md` distinguish feedback showing the current goal is incomplete from feedback that introduces new direction.
- Repository-changing evaluation may be presented through the PR itself, avoiding a duplicate human approval ceremony.
- The existing per-change confirmed-Understanding/evidenced-gap gate remains intact inside the cycle; cycle planning may satisfy the same checkpoint when it already contains all required premises, avoiding duplicate confirmation.
- Live process documentation no longer instructs agents to create a branch per feature/subtask; historical material was intentionally not rewritten.
- All 50 Turtle resources present before this evidence commit parsed successfully with RDFLib.
- All 31 then-current durable exact Git references resolved to strict ancestors of the artifact versions containing them.
- Explicit `docs/`, `prompts/`, and `templates/` paths referenced from current guidance resolved to existing repository files.
- `git diff --check` reported no whitespace errors; `git fsck --no-reflogs --unreachable` reported only ordinary unreachable blobs and no structural corruption.

## Scenario consistency checks

The current rules give an unambiguous answer to the main dogfood scenarios:

1. **One goal needs several implementation tasks** — keep one cycle/branch and use several semantic commits/artifacts; no branch per task.
2. **An adjacent problem is discovered during Act** — record it for next-cycle planning unless it is required to achieve/evaluate the agreed goal or repair a cycle-caused regression.
3. **Evaluation shows the agreed goal is still incomplete** — keep the same cycle open, correct on the same branch, and evaluate again.
4. **Evaluation reveals a desirable new capability** — retain it as next-cycle input rather than silently expanding the current cycle.
5. **Human review burden** — for repository changes, the PR can be the cycle evaluation surface, so evaluation does not create an extra mandatory approval before PR review.

## What this verification does not establish

Static consistency does not establish that real agents will reliably recognize cycle boundaries, that humans will find the planning interview lightweight, that cycle goals will be scoped well, or that one-cycle-branch remains practical for very large/cross-repository/operational work.

It also does not establish that the existing `CYC-*` Markdown record is sufficient for later interrogation or automation. The first version deliberately avoids a `partOfCycle` relation, task model, or machine-enforced cycle state. Dogfooding should determine whether any of those eventually earn their complexity.

## Result

The repository now expresses a coherent and comparatively lightweight outer Spiral cadence without replacing the existing causal evidence model: human and AI agree a cycle goal, the AI executes multiple tasks/commits inside one stable boundary, the integrated result is evaluated, and only then is new direction planned.
