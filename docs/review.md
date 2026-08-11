# Pull-Request Review

A Spiral Developer pull request is not merely a code diff. It is a proposal to admit a feature's causal history and resulting behavior into authoritative project reality.

## PR summary

The AI should prepare a concise review surface containing:

- **Source / understanding** — when material, the origin evidence, interpretation that produced intent, exact versions, and any unavailable primary provenance.
- **Request** — artifact ID and exact Git version(s).
- **Feedback** — important intended-user observations that changed understanding.
- **Design** — important design artifacts and versions, including material cultural influence when it explains why one acceptable approach was chosen.
- **Implementation** — semantic implementation commits, affected capabilities, current effective provenance, and lineage/transition metadata for revised governed units.
- **Verification** — evidence that implementation realizes design.
- **Acceptance** — evidence that behavior satisfies request intent.
- **Legacy context** — reconstructed constraints and confidence where applicable.
- **New dependencies** — additions and why they are justified.
- **Deferred risks** — known issues deliberately not solved now.
- **Warnings** — materially relevant signals from explicitly adopted warning profiles and their disposition, when any affected the change.
- **Lessons** — new `LES-*` observations that may change future project practice/culture/warning profiles/process, when the cycle produced one.
- **Unresolved questions** — anything the reviewer must understand before acceptance.

The PR template in `.github/pull_request_template.md` is a starting point, not a bureaucratic form.

## Automated review

CI/CD should continue normal project checks and progressively add non-AI checks for Spiral Developer artifacts.

Useful checks include:

- source/build/tests/lint/security checks required by the project;
- Turtle syntax parsing;
- SHACL validation of the causal graph;
- all referenced full Git hashes exist in repository history;
- staged/pre-commit historical references are prevented from pointing outside current `HEAD` ancestry;
- introduced commit ranges are checked version-by-version so a bad reference cannot be hidden by later removal;
- referenced artifact IDs exist;
- referenced repository paths existed at the claimed commit where practical;
- no required causal edge is missing for accepted design/evidence artifacts;
- governed implementation revisions with `sd:transforms` declare a change kind and, for prospective/non-unknown revisions, a transition cause;
- all `sd:historicalReference` relations resolve backward in Git history; strict ancestry is the primary DAG invariant, while generic cycle detection is only defensive;
- lineage references resolve to real historical implementation versions without being mistaken for current causal justification;
- acceptance criteria were not silently weakened after implementation without a traceable upstream reason;
- new dependencies or widened permissions are surfaced.

Not all checks need to exist initially. Add automation when the manual process demonstrates its value.

## Human review

Humans review meaning and judgment.

Ask:

1. For consequential direct human input, did the agent present a concrete Understanding **and evidenced gap** to the human and receive confirmation before product behavior was modified?
2. Did the gap evidence establish current **effective behavior**, including indirect/shared mechanisms, rather than merely search for related or similarly named implementation?
3. If no gap was established—or later evidence falsified it—did the agent stop/reopen inquiry instead of creating or continuing unnecessary implementation?
4. If reconnaissance materially changed the apparent task, was that change returned to the human rather than silently reinterpreted by the agent?
5. Where origin or interpretation matters, can we distinguish what was actually expressed/observed from what the project concluded it meant?
6. Is missing, secondary, or unavailable source provenance represented honestly rather than silently reconstructed?
7. Does the request accurately operationalize the accepted understanding of current client/user intent?
8. Does the request or design contain a consequential framing assumption that was never tested because the AI could elaborate it convincingly?
9. Where intent was uncertain, was feedback obtained through meaningful enough interaction?
10. Does each important design decision have a truthful reason?
11. Are supporting technical choices distinguished from direct client intent?
12. Does verification test the design claim rather than simply mirror implementation?
13. Does acceptance actually demonstrate the request outcome?
14. Are assumptions and legacy inferences represented honestly?
15. Are complexity, dependencies, and new boundaries justified? Where requirements underdetermined the choice, is material culture influence explicit and distinguishable from a hard constraint?
16. Have deferred risks stayed deferred unless evidence required otherwise?
17. Can we trace a surprising result back through the production system, including above the request layer when necessary?
18. For revised governed implementation, can we distinguish current effective justification from historical lineage and transition causes?
19. Did a refactor preserve lineage even when behavior was intended to remain unchanged?
20. Is old history being loaded only when needed, or has provenance bookkeeping begun to make normal agent context grow with codebase age?
21. Did an adopted warning profile identify a consequential concern, and is its disposition proportionate and evidence-grounded rather than automatic?
22. Did this cycle reveal a reusable lesson, and is its proposed scope no broader than the evidence supports?
23. Does the autonomy used in this change stay inside a verification/reversibility envelope appropriate to its consequences?

Code review remains available and important when direct inspection is the best evidence for a risky or subtle claim. It is not the only route to human control.

## Review outcomes

A reviewer may:

- approve;
- request an upstream source/understanding/request/design/evidence correction;
- request additional evidence;
- reject the direction;
- identify a new risk or assumption;
- require direct code/security/operations review.

Corrections happen in new commits on the feature branch. Do not amend/rebase old causal commits.

## Merge

After required checks and human review pass, merge with a normal merge commit.

Do not squash or rebase the feature history.
