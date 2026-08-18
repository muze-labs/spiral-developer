---
id: LES-018
---

# Lesson: Distinguish discourse from commitment before execution

## Observation / evidence

Spiral already contains safeguards against premature implementation: inquiry/execution language, framing checks, confirmed Understanding plus evidenced-gap preflight, human-confirmed cycle goals, and reopen-on-falsification behavior.

Human review exposed a broader interaction failure mode underneath those safeguards: a task-oriented AI tends to interpret nearly every human utterance as something to act on. In software development, many consequential utterances are not instructions at all. They are hypotheses, tentative solutions, incomplete requirements, examples, intuitions, or attempts to think through a problem collaboratively.

If the agent silently converts those contributions into action, it can create a clean causal history of a decision that was never actually made.

## Lesson

Treat **discourse, commitment, and execution as distinct collaboration semantics**.

While meaning or direction is materially open, default to discourse: refine meaning, inspect evidence, expose uncertainty, and challenge assumptions when resolving them differently could change what gets built, tested, accepted, or treated as the problem.

Do not merely permit challenge. During discourse, require the agent to surface material ambiguity, contradiction, unsupported premise, or alternative framing when ignoring it has meaningful downstream consequences. Keep this significance-gated so the process does not reward performative disagreement.

Only after a sufficiently explicit commitment should the agent treat the settled frame as authoritative input for execution. Once execution is justified, act decisively and avoid repeatedly reopening settled choices without new evidence.

If new evidence materially contradicts the commitment, stop execution and return to discourse rather than compensating around the contradiction downstream.

## Scope

Core Spiral collaboration behavior across intake, source interpretation, Understanding/Request formation, cycle planning, consequential design, risk analysis, evaluation, and execution handoffs.

This does not require every message to be labeled with a mode or every discussion turn to become an artifact. Preserve only causally important clarifications, challenges, resolutions, and commitments.

## Confidence / limits

High confidence in the semantic distinction and in the need to prevent tentative human input from becoming silent operational authority.

Moderate confidence that normative agent instructions, prompts, accepted artifact states, and explicit human-confirmed boundaries are enough to make the behavior reliable across different AI agents. Dogfooding should specifically test premature operationalization and unnecessary Socratic friction before introducing a formal interaction-state ontology or validator.

## Proposed consequence

Strengthen `AGENTS.md`, AI collaboration/trust/process/cycle guidance, active planning/change/evaluation prompts, and relevant templates so they consistently encode:

> **discourse → commitment → execution; materially falsifying evidence → discourse**

State explicitly that human input is evidence of intent or reasoning, not automatically an instruction, and that human authority over final commitments includes the right to be challenged before commitment.
