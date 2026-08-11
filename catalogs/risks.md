# Risk Catalog

Use this as a prompt for thinking, not a checklist.

Every active risk should have a **horizon**: blocker, near-term, deferred, or existential.

## Product / feedback

- Requirement is treated as ground truth even though it is an interpretation of a weaker or ambiguous source.
- AI interpretation silently becomes “human intent” without preserving the distinction.
- Primary requirement source is unavailable but the graph implies direct provenance.
- Wrong problem or audience.
- Leading request/prompt prematurely assumes the solution category or acceptance model.
- AI elaborates a plausible first framing so convincingly that alternatives stop being investigated.
- Feedback is based on descriptions/screenshots rather than meaningful interaction.
- Prototype polish creates false confidence.
- Client intent changed but downstream design still reflects an old version.
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
- Scale drift: enlarging product/system boundaries mainly because the larger model is more elegant.

## Causal / evidence

- Design element has no truthful reason for existing.
- Test mirrors implementation rather than verifying design.
- Acceptance verifies design instead of request intent.
- Upstream artifact changed without downstream re-evaluation.
- Reconstructed legacy inference is treated as fact.
- Important source statement, interpretation, clarification, or decision exists only in chat/history and has not been crystallized when its causal role matters.
- Same agent weakens tests/evals to make its implementation pass.
- Git blame or “all commits touching this function” is mistaken for causal implementation provenance.
- Historical reachability is presented as current justification even though an old cause was superseded.
- A semantic change silently drops a still-effective cause or carries forward a cause that no longer applies.
- A behavior-preserving refactor severs lineage because “nothing semantic changed.”
- Implementation lineage is reconstructed speculatively to make history look complete.
- Full implementation history is loaded into routine agent context, causing reasoning cost to grow with codebase age.
- Formatting/generated churn is recorded as lineage noise and overwhelms meaningful transitions.
- Source regions are forced into one-IMP ownership even though several independent implementation concerns overlap.

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

## Git / provenance graph

- Causal history is squashed, rebased, amended, or force-pushed after downstream references exist.
- Companion Turtle resources and human-facing artifacts disagree about the causal chain.
- A causal relation points to the current artifact rather than the exact upstream commit that informed the decision.
- Machine data stores abbreviated Git hashes that later become ambiguous.
- Graph structure becomes an end in itself and grows faster than its value for reasoning/audit.
- Important semantic work remains only in commit prose or chat and never becomes a durable artifact/graph relation.
