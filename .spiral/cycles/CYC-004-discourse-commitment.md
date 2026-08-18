---
id: CYC-004
---

# Cycle: Distinguish discourse, commitment, and execution

Repository branch: `spiral/CYC-004-discourse-commitment`
Branch verified: verified at cycle open against actual Git branch state; re-check before each semantic causal commit and during evaluation.

## Analyze

Project state / prior evaluation that makes this cycle relevant:

Spiral already distinguishes inquiry from execution, requires framing checks for consequential assumptions, and gates consequential implementation on a human-confirmed Understanding plus an evidenced gap. Human discussion exposed a deeper interaction problem: those rules still sit inside the conventional chatbot assumption that human input is generally a task to execute unless a special guardrail intervenes.

Important risk / uncertainty / desired movement:

Make Spiral's normal collaboration semantics explicitly discourse-oriented wherever meaning or direction is still open. Human utterances should be treated as contributions to shared reasoning rather than automatically as instructions. The agent should have a positive duty to challenge material assumptions, while retaining decisive execution after genuine commitment.

Relevant human direction / feedback:

Captured in `SRC-COLLAB-001`.

Governing higher-level plan / direction:

Spiral Developer's trust goal: justified agent autonomy through inspectable causality, explicit uncertainty, evidence, and human control. This cycle refines how human intent becomes a trustworthy causal input rather than changing the overall development lifecycle.

Current position in that plan:

This follows earlier intent-preflight and framing-resistance work. It generalizes those protections from a pre-implementation checkpoint into an explicit interaction model spanning the cycle.

## Plan

### Cycle goal

Encode **discourse → commitment → execution** as a normative collaboration model so an AI following Spiral does not silently operationalize tentative human input, is expected to challenge materially consequential assumptions during deliberation, and returns to discourse when new evidence undermines a settled frame.

### Why now / why this cycle boundary

The repository already contains most ingredients independently: inquiry/execution language, accepted artifact states, human-confirmed cycle goals, framing checks, and reopen-on-falsification behavior. The gap is primarily semantic integration and agent-operating guidance, making this a coherent process change without requiring a new artifact class or workflow engine.

### Plan continuity decision

`continue` — strengthens the existing trustworthy-collaboration direction and intent provenance model rather than introducing a competing process.

### Current starting evidence

- `docs/ai-collaboration.md` distinguishes inquiry and execution but does not make commitment an explicit transition.
- `AGENTS.md` says a human question/proposed solution is not automatically an established premise, but still frames the exception mainly around consequential direct input and implementation gates.
- cycle planning already uses an interview and human-confirmed goal; evaluation already distinguishes correction from new direction.
- artifact states already include `accepted`, so commitment can initially be represented using existing artifacts/status plus explicit human confirmation rather than new ontology.

### Evaluation basis

An AI following the normative docs/prompts should be told clearly that:

- human input is not automatically an instruction while meaning is open;
- discourse is the default at consequential interpretation/decision boundaries;
- the agent must surface material ambiguity, contradiction, or alternative framing when ignoring it could change the commitment;
- challenges should be proportional and non-performative;
- execution begins only from a sufficiently explicit commitment;
- tentative suggestions do not silently become durable decisions;
- materially falsifying evidence closes the execution gate and returns the collaboration to discourse;
- settled, low-ambiguity execution should not be burdened with ritual questioning.

### Likely work

- retain the human direction as source evidence;
- interpret it into one reusable process lesson;
- update AI collaboration, trust/process/cycle guidance, agent instructions, prompts, templates, vision/README where useful;
- verify consistency, Turtle parsing, Git-reference validity, branch state, and repository integrity.

### Explicit non-goals

- no new conversational transcript artifact for every utterance;
- no requirement to label every message with a mode;
- no general obligation to disagree with the human;
- no new ontology class or formal interaction state machine unless later dogfooding demonstrates a concrete automation/query need;
- no weakening of human authority over final commitments;
- no duplicate confirmation ceremony when commitment is already explicit and evidenced.

### Pause / re-plan conditions

Pause if encoding the model would require treating every conversational turn as provenance, if it creates routine Socratic friction during settled execution, or if existing artifact/status semantics cannot represent commitment without ambiguity relevant to trustworthy operation.

## Act

Important artifacts / semantic commits produced:

Pending.

Material implementation decisions or deviations from the initial likely work:

Pending.

Out-of-scope discoveries retained for later:

None yet.

## Evaluate

Integrated result against cycle goal:

Pending.

Evidence / acceptance result:

Pending.

Metric or risk movement:

Pending.

What changed in our understanding:

Pending.

Surprises / model mismatches:

Pending.

Known compromises:

Pending.

Unresolved issues within current goal:

Pending.

Candidate next-cycle inputs:

Pending.

Human evaluation / feedback:

Pending review of this branch/update.

Cycle accepted, still open, or deliberately re-planned:

Still open pending implementation and human evaluation.

## Process learning

Pending cycle evaluation.
