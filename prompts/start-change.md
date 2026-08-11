# Start Change Prompt

Apply Spiral Developer to this requested change.

1. Identify the authoritative branch. For consequential direct human input, **do not begin implementation yet**.
2. Reflect back the outcome you believe the human wants and any material assumption that would cause substantially different work. Ask the human to confirm or correct the interpretation. Skip this only for genuinely trivial/local/reversible work where material ambiguity is implausible.
3. After confirmation, reconcile the interpretation with project reality before crystallizing it: search relevant code, tests, documentation, Spiral artifacts, callers, and history where useful for existing or overlapping capability, including differently named or structured implementations. Do not rely only on literal task wording.
4. If project reality materially changes the apparent task, report what you found and return to human clarification before implementation. Do not silently reinterpret "build X" into "extend/reuse/repair Y".
5. Create a dedicated `spiral/...` feature branch once the work is sufficiently understood. Crystallize the clarified intent as source/understanding/request artifacts only where useful; repository reconnaissance belongs inside Understanding formation and does not require another artifact type.
6. Identify the best available source for the clarified current intent. Where provenance or interpretation matters, crystallize a `SRC-*` source and `UND-*` understanding before the request; explicitly mark unavailable primary evidence rather than reconstructing it.
7. Capture the current request and observable desired outcomes, deriving it from the accepted understanding when one was material.
8. If the request or proposed solution contains a consequential assumption, briefly perform a framing check: identify the assumption and a less constraining question when a different framing could materially change the work. Do not do this for routine local choices.
9. Commit the request when it is sufficiently clear to guide the next step.
10. Identify ambiguity and the nearest important uncertainty.
11. Classify risks by horizon: blocker, near-term, deferred, existential.
12. Choose the smallest evidence-producing probe for the nearest uncertainty. Apply an active culture preference such as frontend-first only when the project has adopted it and it fits the uncertainty; do not mistake the preference for a Spiral invariant.
13. Record explicit non-goals and later risks that should not shape current design.
14. Identify active culture preferences that materially shape underdetermined design choices; distinguish them from hard constraints and record `sd:shapedBy` only when useful.
15. Draft the smallest design elements needed and connect each in its companion Turtle resource to exact upstream commit hashes.
16. Define verification and acceptance evidence before hardening implementation.
17. If legacy behavior is touched, follow the brownfield process rather than guessing intent.
18. Implement only when causal context is sufficient for safe work. If revising a governed `IMP-*`, work from current effective provenance rather than replaying full history; record the immediate predecessor with `sd:transforms`, the transition reason with `sd:changeCausedBy`, and the change kind.
19. Preserve effective implementation causes that remain valid and remove/update only those actually superseded. Treat behavior-preserving refactors as lineage events when they materially revise the governed implementation, and verify preservation when important.
20. Before each semantic causal commit that adds or changes Spiral Turtle, run available staged/pre-commit graph validation. New/changed historical references must point to commits already reachable from current `HEAD`; do not knowingly make malformed provenance durable and plan to repair it later.
21. Create semantic causal commits; never amend/rebase/squash them after creation.
22. Where CI/range tooling exists, validate the introduced causal history as a commit range rather than only the final snapshot.

Keep artifacts minimal. Do not create a template file unless it will be used.
