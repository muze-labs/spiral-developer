# Muze AI-Native Development Vision

## Purpose

Software development is changing more fundamentally than simply becoming faster.

Current AI systems can already produce substantial amounts of useful software with relatively little direct human implementation. The limiting factor increasingly becomes whether the AI operates inside an environment that makes intent, desired properties, constraints, evidence, and prior decisions legible.

Muze's goal is therefore not to insert AI into the old development process. It is to develop an **AI-native software-development process** in which humans remain responsible for intent, judgment, meaningful feedback, and accountability while AI performs an increasing share of design exploration, implementation, verification, documentation, and traceability bookkeeping.

The central artifact is not merely source code.

It is the connected, versioned body of intent, decisions, implementation, and evidence that explains **why the system exists in its current form and whether it still satisfies the need that caused it to be built**.

AI also changes the economics of inquiry. It can elaborate a proposed solution so quickly and convincingly that a weak initial framing hardens before reality has tested it. Spiral Developer therefore treats consequential questions as **proposed search frames**, not automatic premises. During inquiry the AI may expose hidden assumptions or test a materially different framing; during execution it should stop reopening settled decisions without new evidence.

A useful principle is:

> **Capability is not endorsement. A good plan shows that a direction can be built, not that it is the right direction.**

See [`ai-collaboration.md`](ai-collaboration.md).

## 1. Start with meaningful feedback

Software development depends on short feedback loops. Useful feedback becomes much stronger when the intended audience interacts meaningfully with something that behaves enough like the requested system to provoke real behavior.

For much of Muze's work this leads to **frontend-first development**.

The first goal is to create an interactive representation quickly enough that intended users can spend meaningful time with it. At this stage optimize for learning and working feature behavior, not visual polish, complete usability work, production architecture, or infrastructure unless those are necessary for meaningful interaction.

Frontend-first is a specific instance of a broader principle:

> **Build the cheapest artifact capable of producing high-quality reality-based feedback.**

## 2. Treat intent formation as part of the causal system

A requirement is not ground truth merely because it has been written down. It is a project claim about what should be achieved.

Where origin or interpretation matters, distinguish:

- a **source** — what was actually expressed, observed, received, or mandated;
- an **understanding** — what we currently believe that source means for the system;
- a **request** — the operationalized outcome the project now intends to satisfy.

A source may be a connected conversation, email, ticket, meeting, contract, regulation, observation, human report, legacy artifact, or other evidence. Chat is not privileged. If the original source is unavailable, preserve that gap explicitly instead of manufacturing a plausible history.

An understanding can be corrected or superseded while the source remains unchanged. This lets Spiral Developer distinguish human expression from AI interpretation, clarification, reframing, and eventual accepted meaning.

A design represents the current understanding of how a request should be satisfied. An implementation realizes a design. Verification provides evidence about that realization. Acceptance provides evidence that the resulting behavior answers the originating intent.

Do not create source and understanding artifacts ceremonially for every simple request. Crystallize them when origin, interpretation, disagreement, or reframing could matter to later reasoning.

When reality changes our understanding, create a new version in a new commit. Do not rewrite history to pretend later knowledge existed earlier.

## 3. Preserve the causal chain

Every significant artifact should be able to answer:

> **Why does this exist?**

The extended chain, where origin and interpretation are material, is:

> **source evidence → understanding → request → design → implementation → verification → acceptance**

A simple direct request may remain the first durable artifact. Not everything needs direct client ancestry. Supporting plumbing may exist because a design needs it. External standards may constrain a design. Culture may rule out an otherwise valid implementation. Preserve the truthful connective chain rather than inventing requirements.

## 4. Let reality revise the model

Traceability must not freeze requirements.

A more complete loop is:

> **source evidence → understanding → request → interactive hypothesis → observed behavior → revised understanding/request → design → implementation → evidence → deployed behavior → observed behavior → …**

The intended audience is an external check against a perfectly consistent but wrong internal model.

## 5. Preserve framing uncertainty when it matters

Precision is useful once the problem is sufficiently understood. Before a consequential decision, however, an apparently precise request may already assume the architecture, abstraction, or solution category.

When a hidden premise could materially change downstream work, briefly ask whether the premise itself is established. Prefer the broader evidence-producing question when it is not. Do not perform this check for every local decision; use it where the cost of premature commitment is high.

The goal is controlled collapse: preserve meaningful alternatives during inquiry, then commit decisively when current evidence justifies doing so.

## 6. Resolve the nearest important uncertainty

At each stage ask:

> **What unresolved issue is most likely to prevent useful progress in the next development cycle?**

Classify risks by horizon: blocker, near-term, deferred, existential.

Do not solve later-cycle risks merely because AI makes speculative engineering cheap. Pull them forward only when they can invalidate the current direction.

## 7. Build reality in vertical slices

Once the interaction model has survived enough contact with users, replace simulation with reality through thin vertical slices that produce observable behavior.

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

What must remain inspectable and interrogable is the causal production system: relevant source evidence, interpretation/understanding, intent, context, culture, constraints, design, dependencies, agent/tool configuration where relevant, evidence, acceptance, and provenance.

Auditability means:

> **We can explain why the system became what it is, what evidence justified accepting it, and what must change when it proves wrong.**

## 11. Simplicity and maintainability remain constraints

AI can create complexity much faster than humans. It does not make complexity free.

Complexity increases the context, reasoning, verification, and intervention needed for later changes. Eventually even AI cannot economically extend a sufficiently tangled system.

Prefer fewer concepts, small decoupled components, clear boundaries, replaceable dependencies, browser-native mechanisms where appropriate, and a thin application layer.

A useful long-term measure of maintainability is:

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

The immediate goal is not a universal platform. First establish a working Muze process that can:

1. capture and version materially relevant sources, understanding, and intent;
2. expose consequential framing assumptions before they harden;
3. identify the nearest important uncertainty;
4. create an interactive hypothesis;
5. collect meaningful feedback;
6. revise understanding without losing history;
7. derive a traceable design;
8. implement reality in vertical slices;
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

> **Muze develops software by maintaining a short, reality-driven feedback loop between human intent and working systems. Intent itself is traceable when it matters: source evidence, interpretation, and request remain distinguishable. During inquiry, consequential questions remain open to reframing; during execution, AI performs much of the development work and preserves both the causal chain connecting understanding, request, design, implementation, and evidence and the implementation lineage that carries those causes through time. Current justification stays compact; history stays queryable. When the result fails, repair the earliest faulty part of that system rather than merely patching its output.**
