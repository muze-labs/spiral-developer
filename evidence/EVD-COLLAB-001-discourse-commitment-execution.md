---
id: EVD-COLLAB-001
---

# Verification Evidence: Discourse, commitment, and execution semantics

## What is being verified

Adoption of `LES-018`: Spiral should not treat consequential human input as automatic execution authority while meaning or direction is still open. The process should distinguish **discourse → commitment → execution**, require proportionate challenge of material assumptions before commitment, and return to discourse when new evidence materially undermines the committed frame.

Implementation commit under verification: `cac4a3e4abc6e9bd4d66901aad6d963129ec5d5c`.

## Structural / consistency checks

- `AGENTS.md` now states directly that a human utterance is not automatically an instruction, defines discourse → commitment → execution, gives the agent a positive significance-gated challenge duty, and requires return to discourse on materially falsifying evidence.
- `docs/ai-collaboration.md` defines the full interaction contract, distinguishes discourse from the older narrower inquiry terminology, defines examples of valid commitment boundaries, and explicitly prevents tentative conversational suggestions from silently becoming architecture.
- `docs/process.md` makes collaboration semantics orthogonal to Analyze → Plan → Act → Evaluate and identifies human confirmation of a sufficiently explicit cycle goal as a commitment boundary.
- `docs/cycles.md` maps Analyze/Plan and Evaluate to discourse-heavy work, human goal confirmation to commitment, and Act to execution while retaining re-entry to discourse when evidence invalidates the frame.
- `docs/trust-model.md` now distinguishes human authority from human factual/interpretive infallibility and makes challenge before commitment part of trustworthy collaboration rather than disobedience.
- `prompts/start-change.md`, `prompts/plan-cycle.md`, `prompts/evaluate-cycle.md`, and `prompts/brownfield-change.md` now actively instruct agents to remain in discourse before commitment and not operationalize tentative human input.
- `templates/UNDERSTANDING.md` exposes whether an interpretation is still a discourse hypothesis or has been accepted for downstream use; `templates/CYCLE.md` exposes the commitment boundary for the cycle.
- `docs/artifact-model.md` clarifies that an accepted Understanding/Request/Design can be a scoped commitment signal, while draft/active material is not execution authority merely because it is recent or human-authored.
- `README.md`, `docs/vision.md`, `docs/quickstart.md`, `docs/brownfield.md`, and `docs/review.md` use the same return-to-discourse semantics consistently.
- No new InteractionMode/DiscourseMode/CommitmentMode/ExecutionMode ontology class or mandatory per-message artifact was introduced. Existing accepted artifact status plus explicit human-confirmed boundaries remain the first implementation.

## Repository checks

- All Turtle resources parse successfully with RDFLib.
- All non-template/example exact `sd:gitCommit` references resolve to commits and are ancestors of the current branch.
- Targeted assertions confirm the normative agent instructions and active prompts contain the expected discourse/commitment/execution rules and positive challenge duty.
- A negative assertion confirms that no formal interaction-state ontology was introduced accidentally.
- `git diff --check HEAD` reports no whitespace errors.
- `git fsck --no-reflogs --unreachable` reports no repository corruption.
- Active branch was mechanically verified as `spiral/CYC-004-discourse-commitment` during the cycle.

## What this verification does not establish

Static process consistency does not establish that every AI agent will correctly infer when a human is thinking aloud, that agents will challenge often enough without becoming performatively contrarian, or that existing accepted-artifact/human-confirmation signals are sufficiently machine-enforceable across real projects.

Those are dogfooding questions. In particular, future tests should include conversational cases where a human proposes a solution as a tentative thought, states a premise contradicted by project evidence, gives a genuinely settled execution instruction, and revises a decision during evaluation. Formal interaction-state tooling should be added only if observed failures justify it.

## Result

Spiral now encodes discourse-oriented collaboration as a core process behavior rather than an optional conversational style. Human input remains authoritative at the point of commitment, but before commitment the agent is expected to refine, test, and when materially useful challenge that input instead of automatically treating it as a task. Once commitment is explicit enough, the agent is expected to execute decisively until evidence gives a reason to reopen discourse.
