# Trust Model: Autonomy Through Verification

Spiral Developer is a **trust-but-verify** development process.

That phrase does not mean the agent is assumed to be correct. It means the agent is deliberately allowed substantial freedom inside an environment designed to make consequential work inspectable, testable, attributable, and rejectable before it becomes authoritative.

A useful formulation is:

> **Autonomy is earned by verification architecture, not by confidence in the agent.**

## What is trusted

Within a contained working branch, a capable agent may normally be trusted to investigate, reframe, design, implement, test, document, maintain provenance, and operate Git without a human approving every intermediate action.

This is permission to act, not a claim that the action is correct.

The process makes that freedom practical by preserving and checking:

- the source and interpretation of consequential intent where it matters;
- explicit requests, constraints, design decisions, and cultural influences;
- exact historical provenance and implementation lineage;
- executable verification and acceptance evidence;
- immutable causal history;
- automated structural/invariant checks;
- a human governance boundary before proposed history becomes authoritative.

The verification architecture should make an incorrect agent action detectable at the earliest useful boundary and make its causal consequences diagnosable afterward.

## Verification is not always post-action

Trust-but-verify is appropriate only when verification happens before unacceptable irreversible consequences.

For contained and reversible work, the agent can often act first and be verified at the next boundary. Examples include:

- edits on an unmerged feature branch;
- local experiments;
- generated tests or documentation;
- proposed design and causal artifacts.

For difficult-to-reverse or high-impact actions, verification or explicit human authorization moves **before** the action. Examples may include:

- destructive production-data changes;
- security- or authorization-boundary changes with immediate external effect;
- financial transfers;
- irreversible migrations;
- publication or deployment where rollback is inadequate.

The governing question is not “do we trust the agent?” but:

> **Can an unacceptable consequence occur before the relevant claim has been independently checked?**

If yes, add a pre-action gate.

## Verification must be independent enough to matter

An agent claiming that its own output is correct is not sufficient verification.

Evidence should be capable of detecting plausible wrong outcomes. Depending on the claim this may mean tests, invariants, static analysis, independent fixtures, intended-user interaction, external observations, or human judgment.

Avoid verification loops where implementation, test oracle, and acceptance claim all merely restate the same agent assumption.

## Human authority is not micromanagement

Humans remain responsible for meaning, accountability, risk appetite, accepted interpretations of consequential intent, and decisions whose consequences require human ownership. Human authority over desired intent does **not** imply factual infallibility about the current software: for consequential work, the agent should confirm its interpretation with the human and then reconcile relevant premises with repository/runtime evidence before acting.

That does not imply mandatory line-by-line supervision. Excessive micromanagement can reduce the benefit of the verification architecture by replacing inspectable agent autonomy with undocumented human steering.

A human reviewer should be able to ask:

> **What did the agent do, why did it do it, what independently supports the result, and what would become suspect if an upstream belief changes?**

## The trust envelope can change

Agent autonomy is contextual rather than fixed. It can increase when:

- provenance is strong;
- verification is discriminating;
- consequences are contained/reversible;
- the implementation area is well governed;
- failure modes are observable.

It should decrease or move behind earlier gates when:

- provenance is weak or reconstructed;
- verification is shallow;
- blast radius is high;
- rollback is inadequate;
- the environment is opaque;
- a decision requires accountable human judgment.

Spiral Developer therefore aims for **high agent autonomy inside a deliberately engineered trust envelope**, not maximal autonomy as an end in itself.
