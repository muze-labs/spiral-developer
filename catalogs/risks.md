# Risk Catalog

Use this as a prompt for thinking, not a checklist.

Every active risk should have a **horizon**: blocker, near-term, deferred, or existential.

## Product / feedback

- Wrong problem or audience.
- Feedback is based on descriptions/screenshots rather than meaningful interaction.
- Prototype polish creates false confidence.
- Client intent changed but downstream design still reflects an old revision.
- Acceptance criteria are internally consistent but fail to represent real user need.

## Complexity / architecture

- Complexity creep.
- Wrong abstraction producing special cases.
- Boundary confusion or hidden coupling.
- Framework/dependency gravity.
- Thick application layer.
- Vocabulary drift between users, design, tests, and code.
- Agent-generated bloat that increases future reasoning/context cost.
- Speculative infrastructure for deferred risks.

## Causal / evidence

- Design element has no truthful reason for existing.
- Test mirrors implementation rather than verifying design.
- Acceptance verifies design instead of request intent.
- Upstream artifact changed without downstream re-evaluation.
- Reconstructed legacy inference is treated as fact.
- Important decision exists only in chat/history and has not been crystallized.
- Same agent weakens tests/evals to make its implementation pass.

## Brownfield

- Hidden compatibility behavior.
- Old tests preserve unknown but important behavior.
- Opportunistic cleanup widens the change surface.
- Legacy area is modified with more autonomy than its causal confidence supports.

## Data / security / operations

- Premature schema hardening.
- Irreversible migration before intent/design is stable.
- Trust/authorization boundary ambiguity.
- Secrets/privacy constraints missing from context.
- Operational behavior cannot be observed well enough to diagnose failure.
- External service behavior assumed rather than evidenced.
