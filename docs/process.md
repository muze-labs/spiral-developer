# Development Process

This is the normative Spiral Developer lifecycle for cycle work.

The process is iterative, not a waterfall. Upstream artifacts may be revised when reality teaches us something new. The purpose of traceability is to make those revisions and their consequences explicit.

Spiral operates on a **trust-but-verify** model. Give the agent substantial freedom for contained and reversible work because the verification architecture provides evidence and governance boundaries. Move verification or human authorization before actions whose unacceptable consequences could occur before the normal review boundary. See `trust-model.md`.

### Brownfield precondition: establish the project frame

Before the first normal cycle in an existing project, if durable project context is missing or materially stale, conduct the guided intake in `brownfield-intake.md`. Intake has an explicit durable status: **incomplete**, **complete**, or **stale**. Every required intake topic must receive an explicit disposition; `Unknown`, `Not relevant`, and `Deferred with reason` are valid dispositions and are preferable to silent omission.

While intake is active and `Incomplete` or `Stale`, every user-visible response must visibly say that intake remains unfinished and identify the remaining topics. The AI may investigate/project-read during this period, but it must not silently behave as though the project frame were complete. Normal cycle planning begins only after the human has confirmed the completed frame unless the human explicitly authorizes a documented exception. Such an exception does **not** mark intake complete: the unfinished status and remaining topics must stay visible until resolved.

After the human confirms the frame, the AI compares it with current project evidence and presents candidate risks, metric gaps, missing measurements, and uncertainties. The human prioritizes, rejects, accepts/defers, corrects, and adds concerns. That prioritized picture informs which uncertainty should drive the first normal cycle. Do not make a profile or maturity label authoritative merely because it was suggested.

This is a project-onboarding/reframing step, not something repeated before every cycle. Keep it conversational and persist durable conclusions in project context.

## 1. Analyze and plan the cycle

Normal Spiral work begins by agreeing one coherent **cycle goal** with the human: a project outcome, risk reduction, or important uncertainty to resolve. Use the current project context, prior cycle evaluation, prioritized risks/metrics, current evidence, new human direction, and any durable governing multi-cycle plan/roadmap to propose the next useful boundary. See `cycles.md` and `prompts/plan-cycle.md`.

When a governing plan/roadmap exists, **re-read it before selecting the next cycle**. Locate the current position in that plan, then reconcile the latest evidence and retained discoveries against it. State whether the proposed cycle continues the plan, revises it, or deliberately deviates from it. New evidence may justify changing the plan, but a recent discovery must not silently replace the broader direction. If no governing plan exists, record that proportionately rather than inventing one.

The planning interview should establish, proportionately:

- cycle goal;
- why this matters now;
- governing plan/roadmap and current position when one exists, plus a continue/revise/deviate decision;
- current starting evidence;
- evaluation basis;
- likely work;
- explicit non-goals;
- pause/re-plan conditions.

The initial task list is not a fixed sprint backlog. It is a hypothesis about what the goal may require. The **goal and non-goals** are the stable evaluation contract.

When risk drives cycle selection, prefer a cheap test of an uncertain upstream assumption when discovering it wrong later would invalidate substantial downstream work. Do not require numeric scoring: use strategy/business → domain/architecture → workflow/interface → implementation as a rough causal ordering and judge uncertainty, downstream leverage, late-discovery cost, and cheap falsifiability.

Size the cycle according to uncertainty and evaluation needs, not a blanket preference for tiny cycles. Early/unfamiliar work may need a small boundary; once assumptions and invariants are stable, prefer a larger coherent cycle when splitting would add ceremony without isolating a real uncertainty or decision. Small probes may exist inside a larger cycle.

For consequential direct human input, cycle planning may also satisfy the Understanding/evidenced-gap confirmation gate when it presents the same concrete outcome, current effective behavior, gap, and material assumptions. Do not demand duplicate confirmation for ceremony.

After the human confirms the cycle, create/update its `CYC-*` Markdown record. For ordinary repository-changing cycles, create one dedicated branch from the authoritative branch, normally:

```text
spiral/CYC-014-short-goal
```

Immediately verify the actual current branch against the active cycle ID. Repeat that branch/cycle check before each semantic causal commit and at evaluation; if the current branch still names another cycle, stop and correct the branch before continuing. Do not rely on conversational memory for this invariant.

Internal tasks do not normally receive separate branches or PRs. The cycle branch is the integration/review boundary; semantic commits preserve finer causal granularity. A non-code investigation/evaluation cycle may not need a development branch.

Before consequential design or implementation, load the current project context and explicitly adopted culture/warning profiles. Before each semantic causal commit that introduces or changes versioned references, validate the staged causal graph where tooling exists; CI then validates the introduced commit range as a backstop.

See `git-workflow.md`.

## 2. Establish current intent and its provenance

Before treating consequential **direct human input** as implementation-ready, establish two premises and put product modification behind them:

1. **Confirmed Understanding** — a concrete account of the outcome the agent believes the human wants, including material assumptions, has been presented to and confirmed/corrected by the human.
2. **Evidenced gap** — project evidence shows that the current effective system behavior does not already satisfy that Understanding.

A pasted ticket, issue, email, or chat instruction is input to this inquiry, not automatically an executable specification. Before confirmation, the agent may inspect the repository/runtime and run disposable or read-only probes needed to formulate the Understanding and gap, but it must not modify consequential product behavior.

Inspect enough of the system to answer questions such as:

- what does the relevant system actually do now?
- does the requested outcome already exist fully or partially?
- is it provided indirectly by a generic rule, inherited/shared abstraction, default, configuration, caller, composition, framework behavior, or another owner?
- do current tests, rendered/computed behavior, documentation, Spiral artifacts, callers, or Git history contradict factual premises in the request?
- is the apparent change actually an extension, exposure, repair, replacement, reuse, or no-op?

Do not limit this to literal or semantic text search. **Establish the behavior gap itself.** Choose evidence appropriate to the claim: reproduce a failure, exercise the current interface, inspect computed/rendered state, resolve effective configuration, run a focused probe, or use another discriminating observation. Absence of a dedicated implementation does not prove absence of behavior.

Before consequential product modification, present a compact checkpoint to the human:

> **My understanding:** …
> **Current effective behavior:** …
> **Evidenced gap:** …
> **Material assumptions:** …

Stop for confirmation or correction. If no gap can be established, do not invent implementation to match the task wording; report what appears already satisfied or uncertain. If later investigation falsifies either the confirmed Understanding or the evidenced gap, the gate closes again and inquiry resumes.

This is part of forming a trustworthy Understanding, not a new artifact class. Before crystallization, conversation may refine the wording freely; preserve only clarifications or source evidence that will matter causally later. Once a durable intent/understanding has caused accepted work, change it prospectively rather than rewriting history. Writing provenance after product code has already changed cannot retroactively satisfy this gate. Keep the guardrail proportional: do not stop genuinely trivial, unambiguous, local/reversible edits for ceremonial confirmation.

Create or identify the current request artifact only after this preflight is sufficiently settled, and do not automatically treat the request as the root of truth. Ask what caused the project to believe this is the needed outcome.

When origin or interpretation is materially useful, preserve the upstream chain:

> **source evidence → understanding → request**

A `SRC-*` source artifact identifies or captures what was actually expressed, observed, received, or mandated. Sources can include connected conversations, emails, tickets, meetings, contracts, regulations, observations, human reports, legacy material, or external artifacts. Chat is one source type, not a privileged root.

A `UND-*` understanding artifact records what the project currently believes one or more sources mean. Use it when clarification, interpretation, disagreement, reframing, or uncertainty could plausibly matter later. Link it to exact upstream source versions with `sd:interprets`.

If primary origin evidence is unavailable, preserve that fact explicitly. A source may record an attributed or inherited claim with `sd:sourceAvailability sd:Unavailable`; do not invent historical intent to complete the graph.

Then capture a request that describes:

- who needs something;
- what meaningful outcome they need;
- observable behavior that would indicate success;
- assumptions and ambiguities;
- known constraints;
- non-goals.

When a material understanding artifact exists, link the request to its exact version with `sd:derivedFrom`. For simple direct requests, do not create source/understanding artifacts merely for ceremony.

Commit each artifact when it has crystallized enough to guide the next step. Its commit hash becomes the version referenced by downstream artifacts.

## 3. Check consequential framing

Before committing to a solution space, ask whether the request or proposed next step contains an assumption that would materially constrain downstream work.

Do this selectively. A framing check is useful for product direction, core abstractions, architecture, schemas, trust boundaries, irreversible changes, or other choices where a different framing would plausibly change what should be built or how success should be judged. It is usually noise for local, reversible implementation details.

When the premise is still open, state it briefly and reformulate the question at the level the evidence can actually support. For example:

> **Framing check:** “How should we add caching?” assumes caching is the right response. What latency/load problem are we trying to solve, and what evidence distinguishes caching from other responses?

A coherent design is not evidence that the framing was right. **Capability is not endorsement.** If a consequential direction looks unusually elegant, test at least one materially different framing before hardening it.

Record only assumptions or reframings that are causally useful later; do not create ceremony for routine decisions.

See `ai-collaboration.md`.

## 4. Find the most valuable uncertainty to reduce next

Ask:

> **Which important assumption is uncertain enough, and has enough downstream leverage, that testing it now is more valuable than discovering it wrong later?**

Use four rough causal positions as a thinking aid: strategy/business, domain/architecture, workflow/interface, and implementation. Earlier assumptions usually deserve disproportionate attention because more downstream work can depend on them; local reversible implementation choices normally deserve less de-risking effort.

For a material assumption/risk, consider its uncertainty, downstream dependency/blast radius, cost of late discovery, and the cheapest useful falsification or evidence-producing step available now. Prefer pulling a risk forward when that cheap early evidence can avoid substantial downstream rework.

For consequential decisions, apply any explicitly adopted warning profiles whose scope and significance gate fit the work. A warning prompts proportionate inspection; it is not an automatic blocker. If it exposes a durable project concern, record that concern through the ordinary `RSK-*` mechanism and preserve the exact warning-profile version/fragment that surfaced it. Do not create warning ceremony for trivial local choices.

Existing risk horizons (blocker, near-term, deferred, existential) remain available as lightweight disposition metadata for durable risks, but do not use horizon labels as a substitute for the leverage reasoning above and do not require them for every concern. A high-leverage discovery is still only an input to next-cycle selection; reconcile it with any governing plan.

## 5. Seek decision-quality evidence

Where product intent or interaction is uncertain, build or obtain the cheapest artifact/observation that can elicit high-quality reality-based feedback from the intended audience. Where the nearest uncertainty is technical, operational, legal, security-related, or otherwise non-interactional, choose the evidence-producing probe appropriate to that uncertainty.

The active culture profile may shape *how* the project usually seeks that evidence. For example, the Muze culture profile prefers frontend-first probes for ordinary interactive web work. Treat that as a defeasible preference, not a Spiral invariant.

Optimize for reducing the current uncertainty rather than polish, infrastructure, or speculative completeness unless those are necessary for the evidence being sought.

Record observations separately from interpretation. If feedback changes what the project believes the source or user need means, create or revise the relevant `UND-*` artifact and then revise the request when the operationalized outcome changes. Do not rewrite the older understanding or request.

## 6. Create a traceable design

Design the smallest system needed for the current validated understanding.

Each significant design element should be able to explain why it exists:

- which request outcome it satisfies;
- which feedback changed it;
- which culture influenced its chosen form and which culture/external/legacy constraint actually restricts it;
- which risk it addresses;
- which other design it technically supports.

Supporting plumbing does not need invented client ancestry. Preserve the truthful chain upward.

Commit design decisions at meaningful causal boundaries. Record their links to exact upstream Git versions in the design companion Turtle resource.

## 7. Implement the smallest observable real slice

Once the relevant hypothesis is credible enough, replace simulation with the smallest useful amount of real implementation that can produce evidence about the intended behavior/property. The active culture profile may prefer a particular strategy; Muze commonly prefers thin vertical slices for product work.

Keep implementation causally connected to the design it realizes and record material cultural influence with `sd:shapedBy` when that explains why one acceptable implementation form was chosen over another. Avoid unrelated cleanup and speculative future architecture.

When changing an already governed `IMP-*` unit, treat the current implementation resource as a compact checkpoint. Preserve current effective causal references that remain valid, update those whose semantics are actually superseded, and add:

- `sd:transforms` to the exact immediate predecessor implementation version(s);
- `sd:changeCausedBy` to the exact artifact version(s) that caused this revision;
- `sd:implementationChangeKind` (`BehaviorPreservingChange`, `SemanticChange`, or `MixedChange` for prospective governed work; `UnknownChange` only for reconstructed history whose transition semantics cannot be established).

Do this for material revisions, moves, replacements, splits, merges, and refactors—not formatting-only churn. Behavior-preserving refactors still retain lineage; verify preservation when it matters. Code locations may overlap across several `IMP-*` concerns.

For normal continued development, do **not** replay the full lineage by default. Work from current code, current effective provenance, relevant current design/tests/evidence, the new reason for change, and the immediate predecessor. Traverse older lineage only when current provenance is insufficient or a historical question requires it.

Create semantic implementation commits when the change has crystallized enough to serve as evidence for later verification.

### Keep cycle scope stable during Act

Multiple tasks/changes may emerge while pursuing the cycle goal. Do not silently turn every adjacent discovery into current work. A newly discovered item belongs in the active cycle when it is necessary to achieve the agreed goal, obtain the evidence needed to evaluate that goal, or repair a regression introduced by the cycle. Otherwise preserve it as feedback/risk/uncertainty/candidate next-cycle input.

If evidence invalidates the cycle goal or makes its scope unsafe/materially wrong, stop and return to the human for deliberate re-planning rather than drifting the scope.

See `implementation-lineage.md`.

## 8. Verify implementation against design

Verification answers:

> **Does this implementation realize the relevant design property?**

Use evidence appropriate to the claim: automated tests, property/invariant checks, integration exercises, static analysis, benchmarks, fault injection, security checks, or direct observation.

Verification should be capable of detecting plausible wrong implementations rather than merely restating internal structure.

Commit verification evidence after the implementation commit it verifies exists, so the graph can point to the exact implementation version.

## 9. Accept behavior against request

Acceptance answers:

> **Does this observable result satisfy the relevant request intent?**

Acceptance may use executable acceptance tests, intended-user interaction, stakeholder confirmation, objective domain results, or operational evidence.

Acceptance is not the same as implementation verification.

Commit acceptance evidence after the relevant request, design, implementation, and verification versions exist.

## 10. Evaluate the cycle and prepare the review boundary

When the AI believes the cycle goal can be judged, stop ordinary execution and enter **Evaluate** before selecting new direction. Use `prompts/evaluate-cycle.md`. Evaluation may retain candidate next-cycle inputs, but it does not by itself choose their priority. That happens in the next Analyze/Plan step after any governing plan/roadmap has been re-read and reconciled with the new evidence. Present the integrated result against the agreed goal: evidence/acceptance, metric or risk movement, surprises, changed understanding, unresolved issues within scope, known compromises, and out-of-scope discoveries retained for later.

If human evaluation shows the **same agreed goal is not yet satisfied**, keep the current cycle open and correct it on the same branch; then evaluate again. If feedback introduces genuinely **new direction**, retain it for the next Analyze/Plan interview instead of silently expanding scope. A human may deliberately re-scope the active cycle, but make that change explicit because it changes the evaluation contract.

For repository-changing work, prepare a pull request containing both the integrated cycle result and the causal case for accepting it. The PR may be the human evaluation surface; do not create a redundant pre-PR approval ceremony.

The PR should expose:

- cycle goal, integrated result, evaluation status, and retained out-of-scope discoveries;
- source/understanding provenance when material;
- request/version;
- significant feedback;
- design/version, including material `sd:shapedBy` culture influence;
- implementation commits, current effective provenance, and lineage/transition metadata for revised governed implementation units;
- verification;
- acceptance;
- new dependencies;
- legacy assumptions/confidence;
- deferred risks;
- unresolved questions;
- lessons learned when this cycle produced a reusable `LES-*` claim.

CI evaluates mechanical and executable claims. Human review evaluates meaning, judgment, risk, and sufficiency of evidence.

See `review.md`.

## 11. Merge, then return to Analyze/Plan

Accepted repository-changing cycle work is integrated with a normal merge commit.

The cycle commits retain their original hashes. Merge means the cycle outcome and causal history were reviewed and admitted into authoritative project history. After acceptance/merge, return to Analyze/Plan and use the evaluation plus new project state to agree the next cycle goal.

Never squash or rebase causal history merely to make the log look tidy.

## Defect loop

A defect is evidence that some part of the software-producing system was inadequate.

Use:

> **observe failure → trace upward → locate earliest meaningful cause → correct upstream artifact/environment → propagate downward → verify → accept**

Possible root causes include missing or weak source evidence, source misinterpretation, request ambiguity, missing context, incorrect design, weak boundaries, missing verification, wrong acceptance criteria, dependency behavior, stale/missing effective implementation provenance, broken implementation lineage, or implementation error.

Fix the earliest meaningful cause and create new commits. Never amend old causal history to make it appear that the correct understanding existed earlier.

If the defect is an invalid causal/historical reference that already entered Git history, preserve the violating commit, record the detection and correction prospectively, and repair the production environment so equivalent references are rejected before future semantic commits. A later correction may make the current snapshot valid; it does not make the earlier historical reference valid.

When the defect does not fit the current request/design model cleanly, explicitly ask whether the problem is in the implementation **or in the framing that produced the implementation**. Cheap regeneration is a reason to repair upstream assumptions, not a reason to protect already-generated code.

## Process learning

At the end of a significant cycle, ask whether the experience contains a reusable lesson. When an observation could plausibly change future work, capture it as a `LES-*` artifact rather than relying on memory or silently changing agent instructions.

A lesson is a defeasible generalization, not automatically a new rule. Apply it first at the narrowest justified scope: project practice, culture profile when it describes a repeated preference, warning profile when it describes a recurring concern to inspect, and Spiral core only when it changes a general trust/process invariant when it changes a general trust/process invariant. Preserve process/culture changes prospectively so older decisions remain explainable under the versions active when they were made. See `process-evolution.md`.

At the end of a significant cycle ask:

- Did intended users provide meaningful feedback where needed?
- Where intent interpretation mattered, could we distinguish source evidence from our understanding of it?
- Did we reduce the uncertainty that was most valuable to test at this stage, especially where downstream leverage made late discovery expensive?
- Did traceability improve agent or human reasoning?
- On repeated work in a governed implementation area, did current effective provenance reduce archaeology rather than require full-history replay?
- Did any superseded historical cause remain incorrectly presented as current justification?
- Did we add unjustified complexity or dependencies?
- Did we accidentally solve deferred problems?
- Did a defect improve the production environment?
- Did a consequential framing assumption go unchallenged until downstream work made it expensive?
- Did the AI contribute useful independent search, or merely elaborate the first plausible direction?
- Did we enlarge scope mainly to make the architecture/model cleaner?
- Which artifacts/links were useful?
- Which bookkeeping was ceremonial?

The process itself should improve from evidence. Lessons should also be evaluated later and may be refined, superseded, or retired when experience contradicts them.
