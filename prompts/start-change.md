# Start Change Prompt

Apply Spiral Developer to this requested change.

1. Identify the authoritative branch and create a dedicated `spiral/...` feature branch.
2. Identify the best available source for the current intent. Where provenance or interpretation matters, crystallize a `SRC-*` source and `UND-*` understanding before the request; explicitly mark unavailable primary evidence rather than reconstructing it.
3. Capture the current request and observable desired outcomes, deriving it from the accepted understanding when one was material.
4. If the request or proposed solution contains a consequential assumption, briefly perform a framing check: identify the assumption and a less constraining question when a different framing could materially change the work. Do not do this for routine local choices.
5. Commit the request when it is sufficiently clear to guide the next step.
6. Identify ambiguity and the nearest important uncertainty.
7. Classify risks by horizon: blocker, near-term, deferred, existential.
8. Choose the smallest evidence-producing probe for the nearest uncertainty. Apply an active culture preference such as frontend-first only when the project has adopted it and it fits the uncertainty; do not mistake the preference for a Spiral invariant.
9. Record explicit non-goals and later risks that should not shape current design.
10. Identify active culture preferences that materially shape underdetermined design choices; distinguish them from hard constraints and record `sd:shapedBy` only when useful.
11. Draft the smallest design elements needed and connect each in its companion Turtle resource to exact upstream commit hashes.
12. Define verification and acceptance evidence before hardening implementation.
13. If legacy behavior is touched, follow the brownfield process rather than guessing intent.
14. Implement only when causal context is sufficient for safe work. If revising a governed `IMP-*`, work from current effective provenance rather than replaying full history; record the immediate predecessor with `sd:transforms`, the transition reason with `sd:changeCausedBy`, and the change kind.
15. Preserve effective implementation causes that remain valid and remove/update only those actually superseded. Treat behavior-preserving refactors as lineage events when they materially revise the governed implementation, and verify preservation when important.
16. Before each semantic causal commit that adds or changes Spiral Turtle, run available staged/pre-commit graph validation. New/changed historical references must point to commits already reachable from current `HEAD`; do not knowingly make malformed provenance durable and plan to repair it later.
17. Create semantic causal commits; never amend/rebase/squash them after creation.
18. Where CI/range tooling exists, validate the introduced causal history as a commit range rather than only the final snapshot.

Keep artifacts minimal. Do not create a template file unless it will be used.
