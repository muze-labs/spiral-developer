---
id: UND-COLLAB-001
---

# Understanding: Collaboration must distinguish discourse from committed instruction

## Interpretation

Spiral's existing inquiry/execution distinction is directionally correct but too easy to interpret as a special preflight around an otherwise task-oriented assistant. The intended model is broader: **while meaning or direction is still open, human input is participation in a discourse rather than automatically an instruction to operationalize**.

The collaboration therefore has three semantic states:

1. **Discourse** — the purpose is to establish what is meant, what is true enough to rely on, what remains uncertain, and which framing should govern. Human statements may be hypotheses, examples, proposals, intuitions, constraints, corrections, or explicit preferences. They are not automatically durable decisions.
2. **Commitment** — a sufficiently explicit shared conclusion is established: the outcome, decision, cycle goal, accepted Understanding/Request/Design, or equivalent governed statement that execution may legitimately depend on. Important assumptions and remaining uncertainty stay visible.
3. **Execution** — the agent acts decisively from the committed frame. It should not keep reopening settled choices without new evidence, but if material evidence contradicts the commitment it must stop and return to discourse rather than silently compensate downstream.

This model is **orthogonal to the outer Analyze → Plan → Act → Evaluate cycle**. Analyze/Plan is normally discourse-heavy; Act is normally execution-heavy after commitment; Evaluate returns to discourse about what the evidence means and whether the current goal is satisfied. A single cycle may cross the discourse/commitment boundary more than once if evidence invalidates a prior commitment.

## Positive challenge duty

During discourse, the agent should not merely be permitted to challenge the human; it should have a **positive duty** to surface a material ambiguity, contradiction, unsupported assumption, alternative framing, or solution presupposition when ignoring it could materially change:

- the intended outcome;
- a consequential requirement or acceptance criterion;
- architecture/schema/security/trust boundaries;
- a high-leverage risk or dependency;
- significant downstream implementation or migration work.

The duty is significance-gated. The agent should not manufacture objections, perform contrarianism, or turn settled/local/reversible work into interrogation. A useful operational test is: **would resolving this differently plausibly change what we build, test, accept, or regard as the problem?**

## Commitment semantics

Commitment does not require a new artifact type. Existing mechanisms can represent it initially:

- explicit human confirmation of the cycle goal;
- an accepted Understanding or Request;
- an accepted design/decision where design choice itself is the consequential commitment;
- an explicit human execution instruction that unambiguously refers to already-settled governed artifacts.

The process should make the transition visible enough that a speculative statement such as “maybe we should cache this” cannot silently become architecture. Conversely, when the human says “implement accepted DES-014” and no material contradiction is known, the agent should execute rather than reopen routine discourse.

Do not force every conversational turn into provenance. Preserve only causally important clarifications, challenges, resolutions, or commitments using normal Source/Understanding/Request/Design/Cycle history when they matter.

## Current gap in the repository

The repository already contains strong pieces of this behavior:

- `docs/ai-collaboration.md` defines inquiry versus execution and framing checks;
- `AGENTS.md` states that a human question or proposed solution is not automatically an established premise;
- `prompts/start-change.md` requires a confirmed Understanding and evidenced gap before consequential implementation;
- cycle planning is explicitly an interview and requires human-confirmed goals;
- evaluation distinguishes an incomplete current goal from new direction.

What is missing is the **unifying interaction contract**: discourse is not yet described as the default semantic interpretation of human input while meaning is open, commitment is not named as the transition that authorizes execution, and the agent's responsibility to challenge material human assumptions is not stated consistently as a positive duty across the cycle.

## Process implication

Strengthen normative docs, AI operating instructions, and active prompts so they consistently encode:

> **discourse → commitment → execution; material falsification → discourse**

Keep the implementation lightweight: no conversation-state ontology or mandatory per-message labels yet. Use existing accepted artifact states and human-confirmed cycle/understanding boundaries. Add formal machine-readable interaction state only if dogfooding later shows a concrete enforcement/query need.

## Confidence / limits

High confidence that task-oriented default interpretation can prematurely collapse ambiguity and that an explicit discourse/commitment boundary is useful for trustworthy development. Moderate confidence that current artifact statuses plus prompts are sufficient enforcement; dogfooding should test whether agents still operationalize tentative statements and whether a validator/state marker eventually earns its complexity.
