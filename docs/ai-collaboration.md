# AI Collaboration and Framing

Spiral Developer assumes AI can do more than execute a settled specification. During inquiry it can also search, challenge, reframe, and expose assumptions. That extra capability is useful only when it does not turn every decision into debate.

The governing distinction is:

> **Execution mode collapses a sufficiently understood problem into a solution. Inquiry mode keeps consequential uncertainty open long enough to discover whether the problem itself has been framed correctly.**

## 1. Treat consequential questions as proposed frames

A prompt or request often contains assumptions about what kind of problem exists and what kind of answer would count. For local, reversible work this is normally fine. For consequential choices, the AI should briefly inspect the frame before optimizing inside it.

A framing check is warranted when accepting an implicit premise could materially constrain:

- product direction or user intent;
- a core abstraction, architecture, schema, or boundary;
- an irreversible migration or external dependency;
- security, authorization, privacy, or trust boundaries;
- a large body of downstream implementation;
- an acceptance model that would make later alternatives difficult to see.

When such an assumption is still genuinely open, use a compact intervention such as:

> **Framing check:** this assumes X. If X is still open, a less constraining question is Y.

Then continue with the broader inquiry where useful. Do not turn framing checks into ceremony, and do not challenge settled premises merely to appear independent.

## 2. Treat understanding as a claim

The AI's interpretation of a human or external source is not identical to the source itself. When the distinction is consequential, preserve it.

A useful upstream chain is:

> **source evidence → interpretation/understanding → request**

The source may be a connected conversation, email, issue, regulation, meeting, observation, human report, or other evidence. A connected chat is not a privileged root; it is simply one source whose evolution can often be captured precisely.

Crystallize only causally important moments: a statement, clarification, reframing, disagreement, or accepted interpretation that materially changed the request. Do not preserve conversational connective tissue merely because it exists.

When primary evidence is missing, preserve the attributed claim and the gap. `unknown` or `unavailable` is preferable to a plausible reconstruction.

This permits later interrogation to answer not only “why does this design exist?” but also “why did we believe this requirement represented the need?”

## 3. Capability is not endorsement

A capable AI can often produce a coherent design and implementation plan for many plausible directions. The existence of a good plan therefore does not validate the direction.

Before endorsing a high-consequence design, distinguish:

- **Can this be built well?**
- **Is this the right problem and solution space to commit to now?**

When a consequential proposal appears unusually elegant, test at least one materially different framing before treating elegance as evidence.

## 4. Collapse deliberately

Software development requires turning uncertainty into commitments. The objective is not to keep everything open indefinitely. It is to commit at the lowest level justified by current evidence.

During inquiry:

- preserve unresolved assumptions explicitly;
- compare competing framings when the choice is consequential;
- prefer evidence-producing probes over speculative completeness;
- allow an honest result of “not enough evidence yet.”

During execution:

- follow the accepted frame decisively;
- avoid repeatedly reopening settled decisions without new evidence;
- generate implementation, verification, and documentation quickly;
- preserve the causal chain so upstream decisions can still be revisited later.

## 5. Resist scale drift

A difficult local problem can often be made elegant by enlarging the abstraction, product, or system boundary. Sometimes that reveals the correct architecture. Sometimes it is architecture astronautics.

Before enlarging scope to make a design cleaner, ask:

> **Does the larger boundary serve current user value or a current risk, or does it mainly make our model prettier?**

Do not solve a larger problem merely because AI makes the larger solution cheap to generate.

## 6. Trace surprises upstream

When implementation or evaluation produces a surprising result, do not assume the correction belongs in code. Trace the causal chain upward:

> **source evidence → understanding → request → design → implementation → verification → acceptance**

Ask where the first inadequate assumption entered. A test failure may reveal an implementation defect, but it may also reveal a misread source, mistaken interpretation, mistaken requirement, wrong abstraction, bad acceptance model, or an incorrectly framed request.

The value of cheap AI regeneration is that upstream corrections can be propagated rather than protected by sunk implementation cost. Preserve the reasoning and evidence that let the software be rebuilt; do not treat generated code as the primary irreversible asset.

## 7. Independent search without performative disagreement

Good collaboration is neither obedience nor automatic contrarianism. The AI should contribute materially different possibilities when they could change an important decision, but it should not manufacture alternatives when the frame is already well supported.

A useful test is:

> **Would a different framing plausibly change what we build, what we test, or what we regard as success?**

If yes, surface it before commitment. If no, keep the cycle moving.

## 8. Evaluate the collaboration itself

At significant cycle boundaries, occasionally ask:

- Did the AI merely elaborate the first proposed framing, or did it contribute independent search where that mattered?
- Did a framing challenge prevent wasted downstream work?
- Did we reopen an upstream assumption because of evidence, or only patch output?
- Did disagreement improve the result, or add noise?
- Did we collapse uncertainty at an appropriate point?

These are process-learning questions, not mandatory metrics. Preserve only the practices that repeatedly improve decisions and outcomes.
