---
id: SRC-DIST-002
---

# Source: Distributed integration validation and a minimal Spiral CLI

## Human direction

Further discourse during `CYC-005` exposed a second distributed-development failure mode beyond identifier collisions.

Two branches may each be locally valid and touch different files while still becoming causally inconsistent when combined. For example, one branch may supersede an upstream Request while another branch, created from the earlier target state, adds a downstream Design based on the old Request. Git can merge those files cleanly even though the resulting causal state now needs review.

The human agreed that Spiral should **not** prevent this divergence while work is independent. Instead:

> Creation and development may remain decentralized; the later integration is responsible for reconciling causal inconsistency against the target state it will actually join.

A cycle may therefore be valid on its own branch yet become non-mergeable after the authoritative target changes. The pre-merge/integration check must evaluate the candidate against the **current target / prospective merged state**, not merely against the target tip that existed when the branch or merge request was opened.

This should become part of Spiral intake/integration expectations. A repository should know its intended integration target and the mechanism by which pre-merge Spiral checks are enforced. GitHub/GitLab/other hosting should use their normal required-check or pre-merge mechanisms where available; plain Git may use CI, hooks, or explicit maintainer validation. Platform adapters should not define separate Spiral semantics.

The recurring need for commands such as artifact creation and prospective-integration validation also justifies introducing a repository-local `spiral` command in this cycle rather than continuing to accumulate hypothetical helper commands in documentation.

The agreed scope is deliberately narrow:

> `spiral` becomes the executable reference implementation for **mechanically checkable Spiral invariants needed by this distributed-development cycle**, not a complete automation of the Spiral process.

The first useful surface should cover distributed-safe creation and validation, including local repository validation and validation of a prospective integration. Status/introspection may be included where needed to make those operations reliable. Discourse, meaningful human judgment, evidence quality, and other non-mechanical process semantics must remain outside automated enforcement merely because a CLI now exists.

## Confirmed boundaries

- A clean Git merge is necessary but not sufficient for Spiral integration.
- Acceptance of a cycle means it is ready to propose for integration; integration validity is re-evaluated against the actual current target.
- The later merge bears the responsibility for resolving newly exposed causal inconsistency.
- Normal textual/source conflicts remain normal Git conflicts.
- Hosting-specific CI/configuration should invoke shared Spiral validation rather than duplicate the model.
- `CYC-005` should include the minimum `spiral` CLI substrate needed to make these guarantees executable.
- Building a comprehensive workflow engine or automating discourse/commitment semantics is not part of this direction.

## Bootstrap limitation

This source still uses the legacy sequential `SRC-DIST-002` identity because `CYC-005` has not yet selected or implemented the distributed identifier mechanism. That is bootstrap compatibility, not a design decision.
