---
id: UND-DIST-002
---

# Understanding: Distributed creation is optimistic; integration is the serialization boundary

## Current interpretation

Spiral Developer should allow independent branches/checkouts/forks to make progress without locking one another, while treating integration into the authoritative history as the point where their independently valid causal claims must be reconciled.

A branch being valid against the history it started from does **not** prove that it is still valid to merge after the target branch changes. Spiral therefore needs two related but distinct notions:

1. **branch/local validity** — the branch's artifacts and historical references are internally valid against its own reachable history; and
2. **integration validity** — the exact candidate result remains causally coherent when combined with the current authoritative target.

The integration check must inspect the actual current target/prospective merge result. Opening a pull/merge request or passing CI against an earlier target tip cannot permanently certify mergeability.

If one accepted integration changes or supersedes an upstream cause that another independent branch still relies on, the branch integrated later bears the responsibility for reconciling that newly exposed staleness. It may update the downstream artifact, explicitly justify why the older upstream version still applies, or withdraw/supersede the affected work. Spiral does not need distributed locking to prevent the divergence in advance.

This yields the working principle:

> **Distributed work is optimistic; integration is serialized and revalidated.**

and the integration invariant:

> **A clean Git merge is necessary but not sufficient. A Spiral merge must also produce a causally coherent resulting repository.**

## Intake and integration consequence

The project/cycle intake needs enough integration context to make this enforceable rather than aspirational:

- identify the authoritative target branch or other integration boundary;
- identify how the repository can run required pre-merge checks (for example CI/required checks, merge-result pipelines/queues, server-side hooks, or explicit maintainer validation);
- make local acceptance mean "ready to propose for integration," not "permanently safe to merge regardless of later target changes."

Hosting-specific configuration should remain an adapter around common Spiral semantics. GitHub, GitLab, or plain Git should not each invent a different definition of causal integration validity.

## CLI consequence

The repeated need for distributed-safe artifact creation, repository validation, active-cycle/target inspection, and prospective-integration checks is now concrete enough to justify a repository-local `spiral` command.

The command should become the executable reference implementation of **mechanically checkable Spiral invariants**. The initial scope should be only what `CYC-005` needs, with a likely surface around:

- creating a new governed artifact with an independently allocatable identity;
- validating the checked-out repository;
- validating a prospective integration against a current target and candidate branch/commit;
- reporting enough repository/cycle/integration context to make those operations understandable and safe.

The exact subcommand names and implementation technology remain design questions. The CLI is not authorization to mechanize discourse, evidence quality, materiality judgments, human acceptance, or other semantics that require human/AI reasoning.

## Sources considered

- `SRC-DIST-001` established the accepted distributed-development goal and the distinction between accidental Spiral bookkeeping conflicts and meaningful Git conflicts.
- `UND-DIST-001` established that distributed-safe identity must be independently allocatable and that identity should not depend on globally serialized human-friendly numbering.
- `SRC-DIST-002` at commit `55f3eaa2864cff11253f01bc3f0b43b62bd5a1dc` records the later human agreement on causal integration revalidation, pre-merge enforcement, intake integration context, and inclusion of a minimal `spiral` CLI in this cycle.

## Clarifications / reframing

| Question / assumption | Alternative or clarification | Resolution |
|---|---|---|
| If two branches merge cleanly, distributed integration is safe. | Git detects textual/tree conflicts, not whether independently produced causal claims are still current after another branch changes their upstream context. | Integration must add causal validation of the prospective combined state. |
| Prevent stale causal branches by coordinating writers before they diverge. | Divergence is normal distributed development and may be legitimate. | Let branches progress independently; make the later integration reconcile against the actual target. |
| Cycle acceptance means the branch is mergeable. | Target history can change after acceptance. | Acceptance means ready to propose; integration validity is rechecked at merge time. |
| GitHub/GitLab need separate Spiral logic. | Different hosts provide different enforcement surfaces but should share the same invariant. | Host integrations should invoke the common validator. |
| The growing list of proposed helper commands is still premature tooling. | Distributed identity and integration correctness now require repeatable mechanical enforcement. | Introduce the smallest `spiral` CLI substrate needed by this cycle. |
| Once a CLI exists, more of Spiral should be automated. | Mechanical enforceability and collaborative judgment are different categories. | Keep the CLI limited to mechanically checkable invariants unless later dogfooding demonstrates another concrete need. |

## Current effective behavior / evidenced gap

The current repository documents strict backward Git-ancestry rules for versioned historical references and recommends staged/range validation where tooling exists. It also treats the cycle branch as the integration boundary and permits merging the authoritative branch into an active cycle branch.

However, it does not currently provide:

- an executable reference validator in this repository;
- a required prospective-integration check against the latest target state;
- a rule for detecting or resolving causal staleness introduced only when independent histories are combined;
- intake guidance that records the intended target and available integration gate;
- distributed-safe creation tooling for new governed artifact identities.

The gap is therefore broader than identifier allocation: Spiral lacks an executable distributed integration boundary.

## Provenance confidence

`explicit` for the desired behavior and CLI scope because the human directly agreed to them; `evidenced` for the current repository gap based on repository inspection.

## Remaining uncertainty

- the collision-resistant identity format and whether it needs global uniqueness or only practical merge-domain uniqueness;
- whether a human-facing display sequence should exist separately from durable identity;
- the precise rule by which a prospective merge determines that downstream causal claims became stale rather than merely historical;
- whether integration validation should construct a temporary merge commit/tree, use Git's merge-tree facilities, or use another non-history-rewriting mechanism;
- the minimum implementation/runtime dependency acceptable for the first `spiral` CLI;
- exact CLI command names and stable interface;
- which GitHub/GitLab examples should be normative versus illustrative;
- how to represent an explicit exception where an older upstream artifact remains intentionally applicable after a newer sibling/successor exists.

These uncertainties are now the design/inquiry work of `CYC-005` rather than reasons to reopen the accepted cycle goal.

## Commitment / disposition

Accepted as the current interaction/design frame for `CYC-005`. The human explicitly agreed to make the later merge responsible for causal reconciliation, to add pre-merge/integration checks and integration context to intake, and to include the minimum `spiral` CLI in this cycle.

## Consequence

Proceed with repository inquiry and small falsification probes before selecting the identity format or integration algorithm. The resulting design should keep decentralized creation independent, make integration validity re-evaluable against the actual target, and centralize mechanical semantics in the `spiral` CLI rather than in host-specific adapters.
