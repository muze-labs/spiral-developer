# Brownfield Adoption

## Purpose

Most established software projects contain years of accumulated code, tests, configuration, decisions, historical compromises, integrations, and knowledge distributed across people and systems.

They do not begin with a clean causal chain.

Trying to reconstruct complete provenance before new work begins would be expensive, unreliable, and contrary to the purpose of this process.

> **The goal is not to document the past. The goal is to make future change increasingly traceable, auditable, and safe.**


## Begin with project intake

Before the first normal Spiral cycle in a brownfield project, establish a durable project-level frame through the guided intake in `brownfield-intake.md`. This is separate from the per-change Understanding/evidenced-gap gate. Intake asks what the project is for, what outcomes matter, which consequential decisions and constraints already shape it, what humans already know/tolerate, where reliable feedback comes from, and which reusable risk-discovery/metric profiles are relevant.

After the human confirms that frame, compare it with current project evidence. Present candidate risks, metric gaps, missing measurements, and uncertainties back to the human for prioritization, rejection, acceptance/deferment, correction, and additions. Use the resulting prioritized picture to choose the most valuable uncertainty to reduce in the first normal cycle, giving extra weight to uncertain upstream assumptions whose late discovery would invalidate substantial downstream work.

Keep the first version conversational. Reuse `.spiral/project-context.md`; do not create an intake artifact class, fixed maturity score, or one-message exhaustive questionnaire. **Do require complete coverage of the small required topic set**, with explicit `Unknown`, `Not relevant`, or deliberate deferral where appropriate. Persist `Incomplete/Complete/Stale` status and keep unfinished topics visible while intake is active. The intake should reduce the amount of Spiral documentation a human must understand before starting.

## Build affinity before confidence

Every established project is locally strange. An agent entering it should assume its understanding is partial, even when it understands the requested outcome correctly. Before making strong claims about what is absent, duplicated, broken, or safe to change, learn enough about the relevant project area to know where that behavior could actually come from.

This does not require a complete architecture model. Affinity can come from reading code/tests/docs, exercising the running system, following shared abstractions and callers, inspecting history, or asking a human who knows the area. The important behavior is epistemic: **expose uncertainty rather than project familiarity that has not been earned.**

Humans should expect more handholding early in brownfield collaboration. A project-specific correction such as “this behavior is controlled globally, not in the component” is high-value knowledge transfer, not evidence that the collaboration has failed. Preserve it durably only when it will materially help future work.

Do not introduce project-affinity scores, mandatory stages, or another artifact merely for this principle. Let human-AI collaboration infer what sufficient familiarity means in each project and subsystem; add more structure only when dogfooding demonstrates a need.

## Do not migrate the whole project

Capture new causality accurately from now on. Reconstruct old causality only when active work requires it.

Stable legacy code can remain opaque indefinitely if it is not relevant to current risk or change.

Investigate a legacy area when:

- a new feature depends on it;
- its behavior must change;
- a defect occurs in it;
- it blocks current progress;
- it carries substantial security, operational, or business risk;
- understanding it is necessary for an important design decision.

## Start with the next real piece of work

Migration starts with an ordinary bounded cycle, on a normal cycle branch when repository changes are involved, not a migration project.

Before adding or changing a capability in a brownfield system, establish the current **effective behavior** and evidence the gap to the intended outcome. Search by behavior and responsibility, not only by task wording or filenames. Look for full, partial, differently exposed, or differently named implementations in code, tests, documentation, callers, Spiral artifacts, and history where useful—but do not stop at finding related code.

The decisive question is:

> **What observable outcome is unmet in the current system, and what evidence demonstrates that gap?**

A capability may already be supplied indirectly by generic/shared code, inheritance, CSS cascade, defaults, configuration, composition, callers, framework behavior, or runtime state. Use a probe appropriate to the claim: characterization test, reproduction, rendered/computed inspection, API exercise, effective-config resolution, or equivalent. Absence of an obvious dedicated implementation is not enough.

Before consequential product modification, present the human with the intended Understanding, current effective behavior, evidenced gap, and material assumptions; stop for confirmation. If the evidence shows that the requested outcome is already satisfied, do not add duplicate/no-op implementation merely because the task asked for a change. If later evidence changes either premise, return to inquiry. Treat the findings as evidence used while forming the current Understanding, not as a mandatory new artifact.

Then establish the current request and follow the normal process. When the current intent itself comes from inherited or historical claims, use `SRC-*`/`UND-*` only where that provenance matters; an unavailable original source is an acceptable explicit gap. When the work enters legacy territory, characterize only enough of that behavior to proceed safely.

The first AI-native slice will mix explicit new knowledge with existing behavior whose origin is only partly understood. That is acceptable as long as the distinction remains visible.

## Mark provenance confidence

Use these classes for reconstructed knowledge:

- **explicit** — directly stated and currently authoritative;
- **evidenced** — strongly supported by existing artifacts;
- **inferred** — plausible interpretation supported by some evidence but not established;
- **unknown** — behavior exists, but its reason is not known.

Represent important confidence claims in the Turtle graph so non-AI tools can distinguish them.

Unknown is better than invented certainty.

## Use AI for targeted archaeology

Relevant evidence may include source, tests, Git history, commits, issues, documentation, schemas, migrations, callers, configuration, operational history, and developer recollection.

The question is not “What is the complete history of this module?”

It is:

> **What do we need to know about this existing behavior to change it safely now?**

Separate observations from explanations.

## Characterize behavior before explaining it

Prefer establishing observable behavior first.

A characterization test may initially mean only:

> **This is what the current system does.**

It does not automatically mean the behavior is desired.

The current request/design decides what must remain.

## Migrate behavior, not directories

Trace the capability or vertical slice being changed, even when it crosses UI, domain logic, APIs, storage, and tests.

Do not clean or document every unrelated part of every touched file.

## Touch it, improve its traceability

After changing an area, future work should have less archaeology to repeat.

A touched capability should normally leave behind:

- relevant source/understanding provenance when current intent required interpretation;
- an explicit current request;
- a behavioral baseline where relevant;
- relevant design decisions;
- known legacy constraints;
- assumptions and uncertainties;
- verification evidence;
- acceptance evidence;
- causal links among those artifacts;
- current effective implementation provenance and prospective lineage when a governed implementation unit is subsequently revised.


## Establish lineage prospectively

Do not reconstruct an entire implementation lineage merely because an old module is touched. If a reliable predecessor version can be identified, record it; otherwise preserve the gap rather than inventing one. If the predecessor is known but the transition cause or semantic character is not, use `sd:UnknownChange` and leave the unknown cause absent rather than manufacturing an explanation.

From the point an `IMP-*` unit becomes governed, future material revisions should record `sd:transforms`, `sd:changeCausedBy`, and `sd:implementationChangeKind`. This makes the migration asymmetrical: old history may remain incomplete, but new history should not become opaque again.

The current `IMP-*` version should remain the default context for the next change. Older lineage is loaded only when needed, so each governed change should reduce repeated archaeology rather than create a growing mandatory context window.

## Defects are migration opportunities

A legacy defect can follow:

> **failure → characterize → reconstruct relevant context → locate earliest faulty/missing assumption → improve environment → repair/regenerate → verify**

The investigation was necessary anyway; preserve what it taught so the area becomes more governed.

## Do not rewrite history

A current interpretation of an old module is a current interpretation unless historical evidence proves otherwise.

Record current purpose separately from historical origin.

Git history itself is not rewritten to make old decisions appear cleaner or more intentional than they were.

## Capture developer knowledge when relevant

Do not interview everyone about everything.

When active work reaches an area, ask targeted questions and preserve useful answers with provenance. A recollection can be valuable without becoming unquestioned fact. When it materially causes a current requirement, it can be captured as a `SRC-*` human report with the original primary evidence marked unavailable, then interpreted through `UND-*`.

## Use confidence to bound autonomy

A useful mental model for project areas is:

- **opaque** — no trustworthy causal model;
- **characterized** — observable responsibilities/dependencies known;
- **traced** — current behavior linked to current intent/design/evidence;
- **governed** — future changes are expected to preserve the process.

The less understood an area is, the more conservatively an agent should modify it.

## Avoid opportunistic cleanup

Cheap AI refactoring can enlarge change surfaces and erase undocumented historical behavior.

Refactor when it directly enables the current change, reduces an immediate risk, or is valuable enough to become explicit work of its own.

## Preserve legacy tests until understood

An unexplained old test may be the strongest surviving evidence of a requirement or compatibility constraint.

Do not delete it until you understand what information would be lost.

## Migration principle

> **Do not reconstruct the past for its own sake. Preserve causality accurately from now on, and whenever new work crosses into legacy software, reconstruct only enough relevant context to change it safely. Each change should leave the system easier to understand, test, interrogate, and evolve than it was before.**
