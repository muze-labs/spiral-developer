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

### Commitment boundary

The human explicitly asked to update the supplied current Spiral Developer repository with the discourse/commitment/execution model just agreed in the preceding discussion. That confirmation makes the described model authoritative enough for this process-change cycle; no separate product-gap confirmation is required because this repository change is itself the requested outcome.

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

- `f0dbe18b43c1c3b16ce87edbfb93a479e1e0974b` — `SRC-COLLAB-001` plus cycle record.
- `cd6464efd79c32b721d6b67c3d60c3ac090820da` — `UND-COLLAB-001`.
- `34f7ca1903333754ab411fdc085d1b2bbc736e8c` — `LES-018`.
- `cac4a3e4abc6e9bd4d66901aad6d963129ec5d5c` — prospective process/agent/prompt/template changes.
- `EVD-COLLAB-001` — verification evidence recorded at cycle evaluation.

Material implementation decisions or deviations from the initial likely work:

The change uses existing artifact statuses and human-confirmed boundaries as commitment signals rather than adding a new interaction-state ontology. The old term `inquiry` remains acknowledged as an activity inside the broader `discourse` state so historical material remains intelligible. The process makes challenge a positive duty only above a significance threshold and explicitly protects settled execution from performative re-litigation.

Out-of-scope discoveries retained for later:

Formal machine-readable interaction state/validator support is deliberately deferred until dogfooding shows a concrete enforcement or query need.

## Evaluate

Integrated result against cycle goal:

Spiral now has an explicit collaboration contract: **discourse → commitment → execution**, with a return to discourse when material evidence falsifies the committed frame. Human input is no longer semantically treated as automatic execution authority while meaning is still open.

Evidence / acceptance result:

`EVD-COLLAB-001` records structural integration, targeted agent/prompt assertions, Turtle parsing, Git-reference validation, repository-integrity checks, branch consistency, and the deliberate absence of a new interaction-state ontology. Automated verification passes; human evaluation of this process change remains pending.

Metric or risk movement:

The risk of premature operationalization is now addressed at the process level rather than only through special-case framing or implementation preflight gates. The agent is explicitly required to challenge material upstream assumptions before commitment while avoiding routine contrarian friction after commitment.

What changed in our understanding:

The missing distinction was not simply inquiry versus execution. The crucial boundary is between **conversation that is still producing meaning** and **a commitment that may legitimately cause action**. Commitment makes the transition explicit without requiring every conversational turn to become provenance.

Surprises / model mismatches:

Most of the required controls already existed independently: framing checks, confirmed Understanding, evidenced gap, accepted artifact status, human-confirmed cycle goals, and reopen-on-falsification behavior. The conceptual gap was that they were not unified strongly enough to counter the default task-oriented chatbot interaction model.

Known compromises:

The process currently relies on normative instructions, prompts, explicit human confirmation, and existing artifact status rather than a formal machine-readable interaction state or validator. That keeps ceremony low but means enforcement strength must be tested across agents.

Unresolved issues within current goal:

No structural inconsistency remains in the proposed process change. Human acceptance and dogfooding are still needed to establish whether agents reliably recognize tentative input and whether the challenge threshold produces useful disagreement rather than noise.

Candidate next-cycle inputs:

Dogfood adversarial conversational cases: tentative solution stated imperatively, human premise contradicted by repository evidence, clearly settled execution instruction, and evaluation feedback that may or may not re-open commitment. Add formal interaction-state tooling only if those tests show the current encoding is insufficient.

Human evaluation / feedback:

Pending review of this branch/update.

Cycle accepted, still open, or deliberately re-planned:

Still open pending human evaluation.

## Process learning

What context/constraint/evaluation helped:

Treating human input itself as a potentially fallible upstream source made the trust issue clearer: trustworthy collaboration cannot make the human the unquestioned root while simultaneously claiming to preserve justified causality. The agent needs room to improve the commitment before it becomes causal authority.

What bookkeeping was useless:

A new conversation transcript artifact, mandatory per-message mode label, or interaction-state ontology was not needed to encode the first useful version.

What should the environment learn from this cycle:

Do not optimize immediately from every human utterance. While consequential meaning is open, help establish and challenge the frame; make the commitment boundary explicit enough that tentative reasoning cannot silently cause durable behavior; then execute the committed decision faithfully until evidence justifies reopening it.
