# Pull-Request Review

A Spiral Developer pull request is not merely a code diff. It is a proposal to admit a feature's causal history and resulting behavior into authoritative project reality.

## PR summary

The AI should prepare a concise review surface containing:

- **Request** — artifact ID and exact Git version(s).
- **Feedback** — important intended-user observations that changed understanding.
- **Design** — important design artifacts and versions.
- **Implementation** — semantic implementation commits and affected capabilities.
- **Verification** — evidence that implementation realizes design.
- **Acceptance** — evidence that behavior satisfies request intent.
- **Legacy context** — reconstructed constraints and confidence where applicable.
- **New dependencies** — additions and why they are justified.
- **Deferred risks** — known issues deliberately not solved now.
- **Unresolved questions** — anything the reviewer must understand before acceptance.

The PR template in `.github/pull_request_template.md` is a starting point, not a bureaucratic form.

## Automated review

CI/CD should continue normal project checks and progressively add non-AI checks for Spiral Developer artifacts.

Useful checks include:

- source/build/tests/lint/security checks required by the project;
- Turtle syntax parsing;
- SHACL validation of the causal graph;
- all referenced full Git hashes exist in repository history;
- referenced artifact IDs exist;
- referenced repository paths existed at the claimed commit where practical;
- no required causal edge is missing for accepted design/evidence artifacts;
- acceptance criteria were not silently weakened after implementation without a traceable upstream reason;
- new dependencies or widened permissions are surfaced.

Not all checks need to exist initially. Add automation when the manual process demonstrates its value.

## Human review

Humans review meaning and judgment.

Ask:

1. Is the request an accurate representation of current client/user intent?
2. Where intent was uncertain, was feedback obtained through meaningful enough interaction?
3. Does each important design decision have a truthful reason?
4. Are supporting technical choices distinguished from direct client intent?
5. Does verification test the design claim rather than simply mirror implementation?
6. Does acceptance actually demonstrate the request outcome?
7. Are assumptions and legacy inferences represented honestly?
8. Are complexity, dependencies, and new boundaries justified?
9. Have deferred risks stayed deferred unless evidence required otherwise?
10. Can we trace a surprising result back through the production system?

Code review remains available and important when direct inspection is the best evidence for a risky or subtle claim. It is not the only route to human control.

## Review outcomes

A reviewer may:

- approve;
- request an upstream request/design/evidence correction;
- request additional evidence;
- reject the direction;
- identify a new risk or assumption;
- require direct code/security/operations review.

Corrections happen in new commits on the feature branch. Do not amend/rebase old causal commits.

## Merge

After required checks and human review pass, merge with a normal merge commit.

Do not squash or rebase the feature history.
