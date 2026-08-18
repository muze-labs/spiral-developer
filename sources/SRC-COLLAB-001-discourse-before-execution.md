---
id: SRC-COLLAB-001
---

# Source: Treat human input as discourse before instruction when meaning is still open

## Human direction

Most AI chatbots are task-oriented: they tend to interpret any human input as an instruction and move quickly toward execution. Spiral Developer has many points where that default is counterproductive.

At intake, interpretation, requirements refinement, architecture/design, risk analysis, evaluation, and other consequential decision points, the AI should instead support **discourse**: help refine what the human means before acting, surface assumptions and ambiguities, and challenge the human's framing when a materially different interpretation could change the result.

The AI should be free to say that a request appears to assume something unsupported, conflicts with existing evidence, presupposes the wrong solution category, or is still only a hypothesis. Human authority remains final, but trustworthy collaboration should not equate obedience with correctness.

The collaboration therefore needs an explicit distinction between:

1. **Discourse** — contributions are provisional; the goal is mutual understanding and decision quality, not action.
2. **Commitment** — the human and AI make explicit what has actually been agreed, including important assumptions and unresolved uncertainty.
3. **Execution** — the agent acts from that committed frame and should not keep reopening it without new evidence.

A tentative conversational suggestion must not silently become architecture or implementation. Conversely, once a decision is genuinely settled, the agent should execute without performative questioning.

If execution uncovers evidence that materially undermines the committed understanding or decision, the agent should stop and return to discourse rather than improvising around the contradiction.
