# Spiral Developer Vision

## Purpose

Software development is changing more fundamentally than simply becoming faster.

Current AI systems can already produce substantial amounts of useful software with relatively little direct human implementation. The limiting factor increasingly becomes whether the AI operates inside an environment that makes intent, desired properties, constraints, evidence, and prior decisions legible.

Spiral Developer's goal is not to insert AI into an old development process. It is to provide an **AI-native software-development process** in which humans remain responsible for intent, judgment, meaningful feedback, and accountability while AI performs an increasing share of design exploration, implementation, verification, documentation, and traceability bookkeeping.

The central artifact is not merely source code.

It is the connected, versioned body of intent, decisions, implementation, and evidence that explains **why the system exists in its current form and whether it still satisfies the need that caused it to be built**.

AI also changes the economics of inquiry. It can elaborate a proposed solution so quickly and convincingly that a weak initial framing hardens before reality has tested it. Spiral Developer therefore treats consequential human input as participation in **discourse**, not automatically as an instruction. While meaning is open, the AI should refine interpretation, expose hidden assumptions, and challenge a materially different framing when it could change the commitment or substantial downstream work. Only after a sufficiently explicit commitment should execution begin; once executing, the agent should stop reopening settled decisions without new evidence.

> **discourse → commitment → execution; materially falsifying evidence → discourse**

A useful principle is:

> **Capability is not endorsement. A good plan shows that a direction can be built, not that it is the right direction.**

See [`ai-collaboration.md`](ai-collaboration.md).

## Trust model: autonomy through verification

Spiral Developer is deliberately a **trust-but-verify** process. It gives a capable agent substantial freedom to investigate, design, implement, test, document, maintain provenance, and operate a cycle branch because the surrounding process is designed to verify consequential claims before they become authoritative.

> **Autonomy is earned by verification architecture, not by confidence in the agent.**

For contained and reversible work, verification can often happen after the agent acts but before merge or deployment. For actions whose consequences would be unacceptable before review, the verification or human-authorization boundary must move before the action. Human authority therefore governs meaning, risk, and irreversible consequences without requiring routine micromanagement of every generated line.

See [`trust-model.md`](trust-model.md).

## Outer development cadence

Spiral makes its feedback loop visible to the human:

> **Analyze → Plan → Act → Evaluate → Analyze …**

The human and AI agree one coherent cycle goal before consequential execution. The agent may decompose that goal into multiple tasks and semantic commits without turning each internal task into a separate human review boundary. Scope stays stable enough to make evaluation meaningful: adjacent discoveries are normally retained for later planning, while work necessary to achieve/evaluate the agreed goal remains inside the cycle.

Cycle size follows uncertainty and evaluation coherence rather than a universal preference for minimum size. Small cycles are useful while one finding may invalidate the next step; as governing assumptions stabilize, several related implementation/evidence steps should remain in one coherent cycle when splitting them would add ceremony without creating a meaningful decision boundary.

When the goal can be judged, the agent explicitly enters evaluation and presents the integrated result before new direction is chosen. Human feedback that shows the current goal is incomplete keeps the cycle open; genuinely new direction normally becomes input to the next planning interview.

This outer cadence is distinct from the causal chain inside a cycle. See [`cycles.md`](cycles.md).

## 1. Start with meaningful feedback

Trustworthy development needs evidence before consequential assumptions harden. Where user/product intent is uncertain, seek the cheapest artifact or observation capable of producing high-quality reality-based feedback. Where the uncertainty is technical, operational, legal, or security-related, a different evidence-producing probe may be more appropriate.

> **Build the cheapest artifact capable of producing evidence strong enough for the next consequential decision.**

Specific strategies for doing that—such as frontend-first development—belong in an active engineering culture profile rather than Spiral core. Recurring concerns a project wants surfaced for inspection belong in separately adopted warning profiles rather than being smuggled into core or culture. See [`culture.md`](culture.md) and [`warning-profiles.md`](warning-profiles.md).

## 2. Treat intent formation as part of the causal system

A requirement is not ground truth merely because it has been written down. It is a project claim about what should be achieved.

Where origin or interpretation matters, distinguish:

- a **source** — what was actually expressed, observed, received, or mandated;
- an **understanding** — what we currently believe that source means for the system;
- a **request** — the operationalized outcome the project now intends to satisfy.

A source may be a connected conversation, email, ticket, meeting, contract, regulation, observation, human report, legacy artifact, or other evidence. Chat is not privileged. If the original source is unavailable, preserve that gap explicitly instead of manufacturing a plausible history.

An understanding can be corrected or superseded while the source remains unchanged. This lets Spiral Developer distinguish human expression from AI interpretation, clarification, reframing, and eventual accepted meaning.

A design represents the current understanding of how a request should be satisfied. An implementation realizes a design. Verification provides evidence about that realization. Acceptance provides evidence that the resulting behavior answers the originating intent.

Do not create source and understanding artifacts ceremonially for every simple request. For consequential direct human input, implementation waits behind two premises: a human-confirmed Understanding and evidence that current effective behavior does not already satisfy it. Investigate enough to establish both, present them to the human before product modification, and reopen discourse if either premise is later falsified. Crystallize source/understanding when origin, interpretation, disagreement, reframing, or those reality findings could matter to later reasoning.

When reality changes our understanding, create a new version in a new commit. Do not rewrite history to pretend later knowledge existed earlier.

## 3. Preserve the causal chain

Every significant artifact should be able to answer:

> **Why does this exist?**

The extended chain, where origin and interpretation are material, is:

> **source evidence → understanding → request → design → implementation → verification → acceptance**

A simple direct request may remain the first durable artifact after proportionate clarification. A pasted ticket or first human wording is not automatically implementation-ready: consequential work needs both confirmed Understanding and an evidenced unmet outcome before product behavior changes. Not everything needs direct client ancestry. Supporting plumbing may exist because a design needs it. External standards may constrain a design. Culture may rule out an otherwise valid implementation. Preserve the truthful connective chain rather than inventing requirements.

## 4. Let reality revise the model

Traceability must not freeze requirements.

A more complete loop is:

> **source evidence → understanding → request → interactive hypothesis → observed behavior → revised understanding/request → design → implementation → evidence → deployed behavior → observed behavior → …**

The intended audience is an external check against a perfectly consistent but wrong internal model.

## 5. Preserve framing uncertainty when it matters

Precision is useful once the problem is sufficiently understood. Before a consequential decision, however, an apparently precise request may already assume the architecture, abstraction, or solution category.

When a hidden premise could materially change downstream work, briefly ask whether the premise itself is established. Prefer the broader evidence-producing question when it is not. Do not perform this check for every local decision; use it where the cost of premature commitment is high.

The goal is controlled collapse: preserve meaningful alternatives during discourse, then commit decisively when current evidence justifies doing so.

## 6. Reduce high-leverage uncertainty early

At each stage ask:

> **Which uncertain assumption would be most expensive to discover wrong later, relative to the cost of testing it now?**

Reason about where the assumption sits in the causal chain: strategy/business → domain/architecture → workflow/interface → implementation. Earlier assumptions usually have a larger downstream blast radius, while local implementation choices are usually cheaper to reverse.

Prefer cheap evidence that tests uncertain, high-leverage assumptions before large amounts of downstream work depend on them. Do not solve every later-cycle risk merely because AI makes speculative engineering cheap, and do not spend equal risk effort on reversible implementation details.

## 7. Build the smallest useful real slice

Once the relevant hypothesis has survived enough evidence, replace simulation with the smallest real implementation slice that can produce an observable/verifiable result. The active culture profile may prefer a particular slicing strategy; Spiral core requires the slice to remain causally connected and evidentially useful, not that it be vertically structured in every project.

Each slice should remain connected to the request and design that justify it and to the evidence that will tell us it works.

When an existing governed implementation evolves, preserve both its current effective causes and its implementation lineage. This lets Spiral answer two different questions truthfully: **why is this behavior justified now?** and **how did this implementation accumulate into its current form?** Historical reachability is not current justification.

See [`implementation-lineage.md`](implementation-lineage.md).

## 8. Tests are evidence

Verification asks:

> **Does this implementation realize the relevant design?**

Acceptance asks:

> **Does this behavior satisfy the relevant request?**

Those claims should remain distinct.

If implementation verification passes but acceptance fails, the design may be wrong or incomplete. If acceptance criteria pass but users still reject the result, the request or interpretation was incomplete.

## 9. Fix the environment before the output

When a defect occurs, first ask:

> **Why was our software-producing environment capable of accepting this defect?**

The root cause may be missing or weak source evidence, a mistaken interpretation, request ambiguity, missing context, an incorrect design, a weak boundary, a missing invariant, shallow verification, a bad acceptance criterion, or an external dependency.

Correct the earliest meaningful cause, then propagate the correction forward and verify that the original defect and related variants no longer pass.

## 10. Audit the production system

Human auditability does not require a person to understand every generated line.

What must remain inspectable and interrogable is the causal production system: relevant source evidence, interpretation/understanding, intent, context, adopted culture and warning profiles, constraints, design, dependencies, agent/tool configuration where relevant, evidence, acceptance, and provenance.

Auditability means:

> **We can explain why the system became what it is, what evidence justified accepting it, and what must change when it proves wrong.**

## 11. Complexity must remain explainable and verifiable

AI can create complexity much faster than humans. It does not make complexity free. Complexity increases the context, reasoning, verification, and intervention needed for later changes.

Spiral core therefore requires consequential complexity, dependencies, and boundaries to be justified and auditable. It does **not** prescribe one universal architectural aesthetic when several trustworthy choices remain available. Preferences such as small decoupled components, browser-native mechanisms, replaceable dependencies, or simplicity over completeness belong in engineering culture profiles unless a project promotes one into an explicit constraint.

A useful long-term diagnostic remains:

> **How much agent computation and human intervention does the next correct change require?**


## 12. Let causal context compound instead of decay

Ordinary codebases tend to accumulate hidden intent, compatibility behavior, refactor residue, and unexplained constants. An AI agent entering an old area increasingly spends effort rediscovering reasons that earlier developers once knew.

Spiral Developer is designed to replace that growing archaeology burden with a bounded maintenance cost: the current implementation version carries a compact projection of the causes that still matter, while full lineage stays queryable in Git. Normal development should consume current causal context and the immediate predecessor, not replay the entire project history.

This creates an important **hypothesis to test**, not a guarantee:

> **A governed codebase may become easier for an AI agent to change correctly as useful causal context accumulates, rather than progressively harder as undocumented history accumulates.**

If true, AI effectiveness can compound with continued development. Dogfooding should measure whether governed areas require less archaeology, less historical context loading, and less human recovery of old decisions over time. A lineage design that forces full-history replay has failed this objective even if its provenance is complete.

## 13. Human attention moves upward

Humans increasingly spend less time expressing solutions as code and more time on:

- understanding client intent;
- observing intended users;
- resolving ambiguity;
- defining desired properties;
- maintaining architectural culture;
- judging trade-offs;
- deciding whether evidence is sufficient;
- challenging the system when its model of reality is wrong.

AI increasingly handles implementation, routine investigation, test generation, traceability, impact analysis, documentation, and repetitive verification.

## 14. The source code is part of a larger artifact

The durable project increasingly includes a versioned network of source evidence, interpretations, intent, requests, assumptions, designs, decisions, constraints, code, tests, acceptance evidence, operational observations, and provenance.

Source code remains what runs, but it need not carry all accumulated knowledge implicitly.

The long-term aim is:

> **an executable and inspectable body of intent, decisions, and evidence from which working software can be produced and evolved.**

## 15. AI should make discipline cheaper, not optional

Requirements traceability, executable specifications, decision records, impact analysis, documentation, and provenance have often been too expensive to maintain manually.

AI can perform much of this mechanical cognitive work cheaply.

Humans should spend their scarce attention on meaning, judgment, and reality.

## 16. What we are trying to build

The immediate goal is not a universal platform. First establish a working process that can:

1. capture and version materially relevant sources, understanding, and intent;
2. expose consequential framing assumptions before they harden;
3. identify the most valuable uncertainty to reduce, considering downstream leverage and late-discovery cost;
4. create an interactive hypothesis;
5. collect meaningful feedback;
6. revise understanding without losing history;
7. derive a traceable design;
8. implement the smallest useful real slice with its shaping culture/constraints explicit where material;
9. preserve effective implementation provenance and lineage across repeated material revisions;
10. keep routine agent context bounded while historical implementation remains queryable;
11. connect verification to design;
12. connect acceptance to intent;
13. identify consequences of upstream changes;
14. diagnose defects by traversing causality and, when needed, implementation history;
15. improve the generating environment;
16. regenerate or modify implementation;
17. continuously verify that the system still answers the intended need.

Only after this works convincingly should it become a larger harness.

## Working principle

> **Spiral Developer gives an AI agent substantial freedom inside a verifiable production environment. Intent is traceable when it matters: source evidence, interpretation, and request remain distinguishable. Consequential choices preserve not only what required the result, but also the culture, constraints, and evidence that shaped how it was produced. Current justification stays compact; history and evolving beliefs remain queryable. When reality changes our understanding, revise the relevant artifact, culture, lesson, or process prospectively rather than falsifying the past.**
