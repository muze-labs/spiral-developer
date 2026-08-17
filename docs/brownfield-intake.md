# Brownfield Project Intake

## Purpose

A new AI collaborator can understand an individual task while still lacking the project-level context needed to judge what matters, where the project is fragile, or which gap deserves the next cycle.

For an existing project adopting Spiral Developer, begin with a short **guided intake conversation** before the first normal development cycle. The intake is a setup/quickstart step, not an architecture inventory or certification exercise.

> **The human establishes what matters. The AI investigates where the project actually is. The human prioritizes what to do about the resulting risks.**

The intake also reduces adoption cost: a human should not have to read the whole Spiral methodology before using it. Explain the purpose of each question when it becomes relevant, offer common choices where they help, and keep custom, uncertain, and not-relevant answers first-class.

## Intake state is explicit

Intake is a stateful workflow, not a conversational suggestion. Persist one of:

- **Incomplete** — required topics remain undispositioned;
- **Complete** — every required topic has an explicit disposition and the human has confirmed the durable frame;
- **Stale** — a previously complete frame is materially out of date and must be reopened.

While intake is active and the state is **Incomplete** or **Stale**, every user-visible response must include a short marker such as:

> **Intake incomplete:** remaining topics — consequential prior decisions; feedback sources; future direction.

Do not let missing answers disappear merely because the conversation moved on. `Unknown`, `Not relevant`, and a deliberate `Deferred` are explicit answers; silence is not. The intake may span several interactions and may include repository investigation, but a normal development cycle should not be selected from an implicitly partial project frame unless the human explicitly authorizes and records an exception. An exception does not convert the intake to `Complete`; the incomplete marker and remaining topics continue to appear until the frame is actually completed.

## When intake is required

Run an intake when:

- Spiral is first introduced to a brownfield project and durable project-level context is missing;
- the project's purpose, important commitments, constraints, or operating posture have materially changed;
- an inherited `.spiral/project-context.md` is clearly too weak or stale to guide current risk discovery.

Do not repeat the full intake for every feature. Update the durable context prospectively when important answers change.

## Required intake coverage

The wording and order are deliberately conversational, but **coverage is not optional**. Before intake can become Complete, explicitly disposition each of these areas:

1. **Purpose, users/stakeholders, and goals** — what the project is for, who depends on it, and which outcomes matter.
2. **Current posture** — for example exploratory/prototype, actively growing, established service/product, maintenance, migration, or another project-specific description. This is context, not a maturity score.
3. **Important measures/outcomes** — quantitative metrics, qualitative outcomes, thresholds/targets where known, and important things the project does not yet know how to measure.
4. **Consequential prior decisions** — architectural, product, data, API, operational, contractual, regulatory, dependency, or organizational choices that constrain future direction; why they still matter and how reversible they really are.
5. **Important invariants and commitments** — compatibility promises, user expectations, operational dependencies, legal/security constraints, accessibility expectations, ownership boundaries, and other things that must not be casually broken.
6. **Known/tolerated problems** — risks, debt, awkwardness, workarounds, or failures the humans already know about, including concerns intentionally accepted or deferred.
7. **Reality/feedback sources** — users, production behavior, support, tests, monitoring, analytics, audits, operators, benchmarks, client feedback, or other observations that can contradict assumptions.
8. **Knowledge gaps / affinity needs** — areas where project understanding is weak, stale, or concentrated in particular humans and where early handholding is expected.
9. **Relevant future direction** — known commitments, migrations, deprecations, deadlines, planned changes, or existing multi-cycle plans/roadmaps that alter what is worth optimizing now. When a durable governing plan exists, retain its reference and current position so later cycle planning can re-read it rather than relying on recency.
10. **Risk-discovery and metric-profile disposition** — which suggested/custom lenses are used, excluded, narrowed, deferred, or explicitly not relevant.

Do not force a fabricated answer where the honest state is `Unknown`. Missing measurement or unclear ownership may itself become an uncertainty worth surfacing. Completion means every topic was considered and explicitly dispositioned, not that every topic has a precise answer.

## Risk-discovery profiles

A **risk-discovery profile** is a reusable Markdown prompt describing classes of project-specific problems worth looking for. It does not assert that those risks exist.

During intake, the AI may suggest profiles that appear relevant and explain why. The human should be able to:

- adopt a suggested profile;
- exclude or defer it;
- narrow its applicability;
- add a project-specific lens that Spiral did not suggest.

The repository contains deliberately small starter profiles under `profiles/risk-discovery/`. `catalogs/risks.md` remains a broad general prompt. Do not convert profile contents into project requirements without evidence and human judgment.

Risk-discovery profiles are distinct from **warning profiles**. Warning profiles challenge consequential decisions/solutions for recurring patterns worth noticing. Risk-discovery profiles help decide where to inspect project health and current exposure.

## Metric profiles

A **metric profile** is a reusable Markdown prompt describing measurements or qualitative outcomes that commonly matter in a project posture. It is not a universal scorecard.

Maturity/posture may help the AI suggest a profile, but project purpose and consequence override generic maturity assumptions. A prototype can be safety-critical; a mature internal utility can remain low consequence.

The human can adopt, ignore, alter, or add metrics. "We care about this but do not know how to measure it" is a valid result and should remain visible rather than being replaced by an invented proxy.

Starter profiles live under `profiles/metrics/`.

## Reality assessment after intake

Once the human confirms the intake summary, the AI should inspect the project far enough to compare the confirmed frame with current evidence. Prefer reality contact over repository guesswork where behavior is observable.

Report a concise set of **candidate** findings such as:

- a required metric appears below its accepted level;
- an important metric is not currently measurable;
- a consequential commitment is not protected by tests or operational checks;
- an adopted risk lens exposes a substantiated current concern;
- evidence contradicts a claimed project assumption;
- a relevant area is too poorly understood to assess responsibly.

Separate evidence from inference and unknowns. Do not manufacture findings merely to populate every selected profile.

## Human prioritization

The AI does not decide project priority merely because it found a gap. Present the evidence-grounded candidates to the human and ask for disposition.

The human can mark a candidate as important now, lower priority, accepted, deferred, not actually a risk, or in need of more evidence. The human can also add risks the AI missed or correct the project frame.

The resulting prioritized risk/uncertainty picture informs the next normal Spiral cycle: choose the nearest important uncertainty or problem whose resolution can produce useful progress.

## Progressive teaching

The intake should teach Spiral just in time. Prefer a brief explanation beside a question over links to prerequisite reading. For example:

> **Which outcomes tell you this project is healthy?**
> This gives me something to compare with current reality. Common answers for established services include reliability, latency, recovery time, accessibility, support burden, or a project-specific user outcome. "Other" and "not sure yet" are valid.

The human can ask for more explanation, but should not need to understand the provenance graph, warning system, or process ontology before completing setup.

## Keep the first version light

For now:

- keep intake status, required-topic dispositions, and durable answers in `.spiral/project-context.md` or equivalent durable project context;
- keep reusable risk-discovery and metric profiles as ordinary Markdown;
- do not introduce an intake artifact class, maturity score, project-health score, or large schema;
- require complete **topic coverage**, but not fixed wording, fixed answer choices, or a one-message questionnaire;
- treat repeated custom answers as evidence that the reusable profiles may need improvement, not as automatic global mutations.

Dogfood the conversation first. Add machine-readable structure only after repeated use shows what deserves to become invariant.
