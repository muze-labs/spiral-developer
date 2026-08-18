# Development Cycles

Spiral Developer uses an explicit outer feedback cadence:

> **Analyze → Plan → Act → Evaluate → Analyze …**

This is OODA-like in spirit, but Spiral keeps its own terms. The important property is not the label; it is that execution is bounded by a human-visible goal before work starts and a human-visible evaluation before new direction is chosen.

The collaboration semantics inside that cadence are:

> **discourse → commitment → execution**

They are not another outer phase sequence. Analyze/Plan is normally discourse-oriented while the goal and framing are still open; human confirmation of the cycle goal is a commitment boundary; Act is normally execution-oriented; Evaluate returns to discourse about whether evidence supports the current commitment. If new evidence materially invalidates a settled frame, execution stops and the collaboration returns to discourse/re-planning.

A human utterance during discourse is not automatically a task. The agent should challenge a material assumption or alternative framing when resolving it differently could change the cycle goal, acceptance model, architecture, trust boundary, or substantial downstream work. Once the frame is genuinely committed, avoid performative re-litigation.

## The cycle is the outer unit of progress

A cycle is a bounded attempt to achieve **one coherent project outcome, reduce one important risk, or resolve one important uncertainty**.

A cycle is not merely a bag of tasks. Tasks are provisional work decomposition inside the cycle and may change as implementation teaches us more.

A useful cycle can contain:

- several requests/design decisions;
- several implementation units;
- several semantic commits;
- probes or investigations that produce no code;
- corrective work discovered during evaluation.

The cycle remains coherent because all included work is causally relevant to the same agreed goal.


## Size cycles by uncertainty, not by minimum task size

A cycle should be **as small as necessary to isolate important uncertainty, risk, or a human evaluation boundary — not as small as possible by default**.

Early in an unfamiliar area, small cycles are often appropriate because one observation can invalidate the next planned step. As the project model, invariants, and evidence become stable, prefer larger coherent cycles that can carry several related implementation/evidence steps without forcing repeated planning/review ceremony.

Split work into another cycle when, for example:

- one part can materially invalidate the assumptions required by another;
- the parts need meaningfully different human evaluation or acceptance decisions;
- combining them would obscure whether the agreed outcome was achieved;
- risk or irreversibility warrants a separate integration boundary.

Do **not** split merely because the work contains several files, requests, implementation units, tests, or semantic commits. A small evidence-producing probe inside a cycle does not imply that the whole cycle must be tiny.

During planning, make the boundary explicit enough to answer: **what uncertainty or evaluation need justifies ending the cycle here?** If there is no good answer, consider a larger coherent cycle.

## Keep cycle choices connected to governing direction

A cycle is local, but many projects are not. When a durable multi-cycle implementation plan, roadmap, migration sequence, or equivalent human-confirmed direction already exists, treat it as an input to **every next-cycle selection**.

Before proposing the next cycle:

1. **re-read the governing plan/reference** rather than relying only on memory or the most recent cycle;
2. identify the **current position** in that plan and which planned dependencies or boundaries remain unresolved;
3. compare the latest evidence and retained discoveries with that plan;
4. state whether the proposal **continues**, **revises**, or **deliberately deviates from** the governing plan.

New evidence is allowed to change the plan. The requirement is not obedience to an outdated roadmap; it is an explicit reconciliation step so that a locally salient discovery does not silently become the new roadmap.

If the evidence justifies revision or deviation, record the reason and update the durable project context/plan as appropriate. If no governing multi-cycle plan exists, say so proportionately and continue without inventing one.

> **Cycle-local discoveries may inform the roadmap; they may not silently replace it.**

## Analyze and plan with the human

Before normal execution, establish the current project state well enough to propose the next useful cycle goal. Inputs may include:

- the previous cycle evaluation;
- the current governing plan/roadmap and position in it, when one exists;
- prioritized risks and metric gaps;
- current project goals/context;
- new human direction or feedback;
- current runtime/repository evidence;
- adopted warning/risk-discovery/metric profiles.

When risk/uncertainty influences the choice, prefer assumptions where uncertainty, downstream leverage, and late-discovery cost are materially high and a useful falsification is cheap now. Do not calculate a score: ask what later work depends on the premise. Use strategy/business → domain/architecture → workflow/interface → implementation as a rough causal ordering, and give upstream assumptions disproportionate attention when being wrong would invalidate later work. Reconcile any such candidate with the governing plan rather than treating risk salience as automatic priority.

Use `prompts/plan-cycle.md` as an interview, not a fixed form. The result should make clear:

- **Cycle goal** — the coherent outcome/risk reduction/uncertainty to pursue;
- **Why now** — why this is the useful next boundary;
- **Plan continuity** — when a governing plan exists, whether this cycle continues, revises, or deliberately deviates from it and why;
- **Evaluation basis** — what evidence or observation will let us judge what happened;
- **Known scope / likely work** — what currently appears necessary, without pretending implementation is fully predictable;
- **Non-goals** — adjacent work that should not silently enter the cycle;
- **Pause/replan conditions** — evidence that would invalidate the goal or make continuing unsafe/wasteful.

The human confirms or corrects the cycle goal before consequential execution. That confirmation is the cycle's commitment boundary: before it, proposed goals and implementation ideas remain discourse; after it, the agent may execute within the agreed goal without treating every subsequent comment as automatic scope change. For consequential direct human input, if this planning interview already contains the concrete Understanding, current effective behavior, evidenced gap, and material assumptions required by the normal preflight gate, do not demand a second ceremonial confirmation.

For trivial/local/reversible work, keep this proportional: the explicit goal may be one sentence and the evaluation basis obvious.

## Scope stability during Act

Once the cycle begins, treat its goal and non-goals as a stable evaluation contract.

Do **not** casually add new tasks because adjacent problems are interesting or easy to fix.

Newly discovered work belongs in the current cycle when it is necessary to:

- achieve the agreed cycle goal;
- obtain evidence required to evaluate that goal; or
- correct a regression introduced by the cycle.

Other discoveries should normally be preserved as feedback, risk, uncertainty, or candidate next-cycle work. They are considered during the next Analyze/Plan interview.

If evidence shows the cycle goal itself is wrong, unsafe, or materially incomplete, stop and return to the human for deliberate re-planning. That is not ordinary scope growth.

## One cycle branch is the normal repository review boundary

For ordinary cycles that change repository state, create one branch from the authoritative branch, normally:

```text
spiral/CYC-014-keyboard-accessibility
```

**Validate, do not merely remember, the branch/cycle correspondence.** When a repository-changing cycle opens, before consequential repository changes and before each semantic causal commit, and again during evaluation, inspect the actual current Git branch (for example with `git branch --show-current`) and verify that it matches the active `CYC-*` identity. If work is still on an older cycle branch, stop and switch/create the correct cycle branch before continuing. Record an explicit exception only when the normal one-cycle-branch rule genuinely does not apply.

The agent may make multiple immutable causal commits on that branch. Internal tasks do not normally receive separate feature branches or pull requests.

The branch is also the scope of unfinished cycle state. An **Active** cycle branch must not merge into the authoritative branch or into another Active cycle branch. Only after evaluation and human acceptance changes the cycle to `Accepted` may it become an integration candidate. Conversely, newly accepted authoritative work may be merged **into** an Active cycle branch so the cycle can reconcile against current project reality.

This directional rule avoids a global mutable "current cycle" pointer: the cycle being worked is identified by the branch, while authoritative history is intended to contain completed cycle outcomes only. If older history violated this prospective rule, preserve that history and correct the process rather than rewriting it.

This keeps human review aligned with the thing the human agreed to accomplish while preserving fine-grained causal history inside the branch.

A non-code investigation or evaluation cycle may not need a development branch. Very unusual cycles spanning repositories or irreversible operational actions may require a different integration boundary; use the trust model rather than forcing the branch rule where it does not fit.

## Evaluate before choosing new direction

When the agent believes the cycle goal has been pursued far enough to judge, stop ordinary execution and enter **Evaluate**. For repository-changing work, the pull request/review surface may be the place where this evaluation is presented; do not require a separate human review merely to satisfy the phase name.

Present the integrated result against the cycle goal, including:

- what changed;
- evidence collected;
- acceptance/verification results;
- relevant metric or risk movement;
- surprises and changed understanding;
- known compromises;
- unresolved issues;
- out-of-scope discoveries retained for later;
- any reusable lesson from the cycle.

If the cycle exposed a new high-leverage assumption, surface it as a candidate next-cycle input with the reason late discovery could be costly and any cheap way to test it. Do not manufacture a risk list when nothing material emerged, and do not choose its priority until the next Analyze/Plan step reconciles it with governing direction.

Do not immediately convert every evaluation observation into another implementation task.

Evaluation returns the collaboration to discourse. Treat observations and suggestions as evidence/feedback first, then determine whether they alter the existing commitment or require a new one; do not operationalize a tentative evaluation remark automatically.

Human feedback has two important meanings:

1. **The agreed goal is not yet satisfied.** Keep the same cycle open and correct the work on the same branch. Evaluation can repeat.
2. **A new direction/opportunity/problem has appeared.** Preserve it as input for the next Analyze/Plan interview rather than silently expanding the current cycle.

The human may deliberately re-scope an active cycle, but this should be explicit because it changes the evaluation contract.

After the cycle is accepted, prospective integration validation passes, and repository-changing work is merged, return to Analyze/Plan. Before agreeing the next cycle goal, re-read any governing multi-cycle plan/roadmap and reconcile the just-completed cycle's evidence with it. Do not choose the next direction by extrapolating from the newest discovery alone.

## Relationship to causal artifacts

The cycle does not replace Source, Understanding, Request, Design, Implementation, Verification, Acceptance, Feedback, Risk, or Lesson artifacts. Those explain **why particular claims and changes are justified** inside the cycle.

`CYC-*` is the outer human-visible learning/integration record. In the first version, its Markdown may simply list important artifacts/commits and evaluation findings. Do not invent a task ontology, formal cycle state machine, or `partOfCycle` relation until dogfooding shows that queries or automation genuinely require them.
