# Brownfield Intake Prompt

Use this before the first normal Spiral cycle in an existing project when durable project-level context is missing or materially stale.

Your job is to conduct a short setup conversation that lets a human use Spiral without first learning the whole methodology.

## Conversation behavior

- Explain briefly why each topic matters when asking about it.
- Prefer common multiple-choice suggestions when they reduce effort, but always allow **Other / Not sure / Not relevant** and free-form answers.
- Ask follow-ups only where an answer materially changes project direction, risk lenses, metrics, constraints, or consequential history.
- The wording/order may be conversational, but every required intake topic below must receive an explicit disposition before intake is complete. `Unknown`, `Not relevant`, and deliberate `Deferred` are valid dispositions; omission is not.
- At the end of every user-visible response while intake remains Incomplete/Stale, include a concise visible marker: `Intake incomplete — remaining: ...`. Do not silently drop unfinished topics.
- Do not turn the intake into an architecture interview or exhaustive repository inventory.
- Treat the human as authoritative about desired outcomes, commitments, accepted trade-offs, and priority; treat repository/runtime claims as things to investigate.
- Preserve uncertainty rather than inventing a precise metric, threshold, maturity level, or historical rationale.

## Establish the frame

Persist `Intake status: Incomplete` (or `Stale` when reopening old context) in project context before proceeding. Cover all of these topics; the depth remains proportional:

1. project purpose, important users/stakeholders, and goals;
2. current project posture/maturity in ordinary language;
3. important outcomes/metrics and accepted levels where known;
4. consequential decisions already taken, why they still matter, and reversibility;
5. invariants/commitments that must not be casually broken;
6. known/tolerated risks or problems;
7. reliable feedback/reality sources;
8. poorly understood areas where early human guidance is likely;
9. relevant future commitments/migrations/deprecations;
10. suggested risk-discovery profiles and metric profiles, including explicit exclusions and custom additions.

Use `profiles/risk-discovery/`, `profiles/metrics/`, and `catalogs/risks.md` only as suggestion sources. Do not silently activate every profile.

## Confirm before assessment

Check the persisted intake checklist. If any required topic is undispositioned, continue the intake and surface the remaining topics; do not proceed as though it were complete.

When every required topic has an explicit disposition, summarize the durable project frame in ordinary language and ask the human to confirm/correct it before using it as the basis for project-level risk assessment. On confirmation, persist `Intake status: Complete` in `.spiral/project-context.md` (or the project's established equivalent). Do not create a new intake artifact merely for bookkeeping.

## Confront the frame with reality

After confirmation, inspect the repository, tests, runtime, operational evidence, documentation, and other available sources only as far as needed to assess the selected outcomes and risk lenses.

Return candidate findings with:

- the project expectation/goal/metric they relate to;
- evidence for current reality;
- the candidate risk, metric gap, missing measurement, or uncertainty;
- what remains unknown.

Do not assign final project priority. Ask the human to prioritize, accept, defer, reject/remove, request more evidence, and add missing risks. Persist durable dispositions where they will matter to later cycles.

Use the resulting prioritized picture to propose the most valuable uncertainty to reduce in the first normal Spiral cycle, considering downstream leverage, late-discovery cost, cheap falsifiability, and governing-plan context.
