# Development Process

This is the normative Spiral Developer lifecycle for feature work.

The process is iterative, not a waterfall. Upstream artifacts may be revised when reality teaches us something new. The purpose of traceability is to make those revisions and their consequences explicit.

## 1. Create a working branch

Start each feature or meaningful change on a dedicated branch from the current authoritative branch.

Prefer:

```text
spiral/<request-id>-<short-name>
```

The branch is an evolving proposed reality. The authoritative branch remains accepted project reality.

See `git-workflow.md`.

## 2. Capture current intent

Create or identify the current request artifact.

A good request describes:

- who needs something;
- what meaningful outcome they need;
- observable behavior that would indicate success;
- assumptions and ambiguities;
- known constraints;
- non-goals.

Commit the request once it is meaningful enough to guide the next step. That commit hash becomes the version referenced by downstream artifacts.

## 3. Find the nearest important uncertainty

Ask:

> **What unresolved issue is most likely to prevent useful progress in the next development cycle?**

Classify risks by horizon:

- blocker;
- near-term;
- deferred;
- existential.

Resolve the blocker or nearest risk. Record later risks. Pull a deferred risk forward only if it can invalidate the current direction.

## 4. Seek meaningful interaction

Where product intent or interaction is uncertain, build the cheapest artifact that can elicit high-quality reality-based feedback from the intended audience.

For ordinary Muze web work, use frontend-first development: create enough functioning UI for intended users to spend real time with the feature.

Optimize for behavioral fidelity and learning, not visual polish, generic usability work, production infrastructure, or speculative completeness unless those are required for meaningful interaction.

Record observations separately from interpretation. If feedback changes intent, create a new request version in a new commit. Do not rewrite the older request.

## 5. Create a traceable design

Design the smallest system needed for the current validated understanding.

Each significant design element should be able to explain why it exists:

- which request outcome it satisfies;
- which feedback changed it;
- which culture/external/legacy constraint restricts it;
- which risk it addresses;
- which other design it technically supports.

Supporting plumbing does not need invented client ancestry. Preserve the truthful chain upward.

Commit design decisions at meaningful causal boundaries. Record their links to exact upstream Git versions in the design companion Turtle resource.

## 6. Implement reality in vertical slices

Once the interaction model is credible enough, replace simulation with reality through the smallest useful vertical slice.

A slice should connect enough of the actual system to produce observable behavior, for example:

> **interface → domain behavior → state → integration → observable result**

Keep implementation causally connected to the design it realizes. Avoid unrelated cleanup and speculative future architecture.

Create semantic implementation commits when the change has crystallized enough to serve as evidence for later verification.

## 7. Verify implementation against design

Verification answers:

> **Does this implementation realize the relevant design property?**

Use evidence appropriate to the claim: automated tests, property/invariant checks, integration exercises, static analysis, benchmarks, fault injection, security checks, or direct observation.

Verification should be capable of detecting plausible wrong implementations rather than merely restating internal structure.

Commit verification evidence after the implementation commit it verifies exists, so the graph can point to the exact implementation version.

## 8. Accept behavior against request

Acceptance answers:

> **Does this observable result satisfy the relevant request intent?**

Acceptance may use executable acceptance tests, intended-user interaction, stakeholder confirmation, objective domain results, or operational evidence.

Acceptance is not the same as implementation verification.

Commit acceptance evidence after the relevant request, design, implementation, and verification versions exist.

## 9. Prepare the pull request

When the AI believes the request is satisfied, it prepares a pull request containing both the result and the causal case for accepting it.

The PR should expose:

- request/version;
- significant feedback;
- design/version;
- implementation commits;
- verification;
- acceptance;
- new dependencies;
- legacy assumptions/confidence;
- deferred risks;
- unresolved questions.

CI evaluates mechanical and executable claims. Human review evaluates meaning, judgment, risk, and sufficiency of evidence.

See `review.md`.

## 10. Merge without rewriting history

Accepted feature work is integrated with a normal merge commit.

The feature commits retain their original hashes. Merge means the causal history was reviewed and admitted into authoritative project history.

Never squash or rebase causal history merely to make the log look tidy.

## Defect loop

A defect is evidence that some part of the software-producing system was inadequate.

Use:

> **observe failure → trace upward → locate earliest meaningful cause → correct upstream artifact/environment → propagate downward → verify → accept**

Possible root causes include request ambiguity, missing context, incorrect design, weak boundaries, missing verification, wrong acceptance criteria, dependency behavior, or implementation error.

Fix the earliest meaningful cause and create new commits. Never amend old causal history to make it appear that the correct understanding existed earlier.

## Process learning

At the end of a significant cycle ask:

- Did intended users provide meaningful feedback where needed?
- Did we reduce the nearest important uncertainty?
- Did traceability improve agent or human reasoning?
- Did we add unjustified complexity or dependencies?
- Did we accidentally solve deferred problems?
- Did a defect improve the production environment?
- Which artifacts/links were useful?
- Which bookkeeping was ceremonial?

The process itself should improve from evidence.
