# Start Change Prompt

Apply Spiral Developer to this requested change.

1. Identify the authoritative branch. For consequential direct human input, **do not modify product behavior yet**.
2. Enter inquiry mode. Inspect enough of the human input and current system to formulate a concrete Understanding and to establish current **effective behavior**. Search by behavior/responsibility, not only ticket wording; follow generic/shared rules, inheritance, defaults, configuration, callers, composition, tests, rendered/computed behavior, and runtime effects where relevant.
3. Establish an **evidenced gap**: what observable part of the confirmed-looking outcome is actually unmet now? Use a discriminating probe appropriate to the claim (for example reproduce the bug, exercise the API, inspect computed style/state, resolve effective configuration, or run a focused characterization). Finding no dedicated implementation is not enough.
4. Present the human with this checkpoint and **STOP**:
   - **My understanding:** the outcome you believe they want;
   - **Current effective behavior:** what the system already does;
   - **Evidenced gap:** what is demonstrably missing/wrong;
   - **Material assumptions:** anything that would materially change the work.
   Ask the human to confirm or correct it. Do not continue into product implementation in the same turn merely because the interpretation seems obvious to you.
5. If no relevant gap can be established, do not invent implementation to satisfy the task wording. Report what appears already satisfied or uncertain and ask what, if anything, should change.
6. After human confirmation, create/use the dedicated `spiral/...` feature branch and crystallize source/understanding/request artifacts where useful. Repository/runtime evidence belongs inside Understanding formation and does not require another artifact type. If later evidence falsifies either the confirmed Understanding or the gap, stop implementation and return to inquiry/human clarification.
7. Identify the best available source for the clarified current intent. Where provenance or interpretation matters, crystallize a `SRC-*` source and `UND-*` understanding before the request; explicitly mark unavailable primary evidence rather than reconstructing it.
8. Capture the current request and observable desired outcomes, deriving it from the accepted understanding when one was material.
9. If the request or proposed solution contains a consequential assumption, briefly perform a framing check: identify the assumption and a less constraining question when a different framing could materially change the work. Do not do this for routine local choices.
10. Commit the request when it is sufficiently clear to guide the next step.
11. Identify ambiguity and the nearest important uncertainty.
12. Classify risks by horizon: blocker, near-term, deferred, existential.
13. Choose the smallest evidence-producing probe for the nearest uncertainty. Apply an active culture preference such as frontend-first only when the project has adopted it and it fits the uncertainty; do not mistake the preference for a Spiral invariant.
14. Record explicit non-goals and later risks that should not shape current design.
15. Identify active culture preferences that materially shape underdetermined design choices; distinguish them from hard constraints and record `sd:shapedBy` only when useful.
16. Draft the smallest design elements needed and connect each in its companion Turtle resource to exact upstream commit hashes.
17. Define verification and acceptance evidence before hardening implementation.
18. If legacy behavior is touched, follow the brownfield process rather than guessing intent.
19. Implement only when causal context is sufficient for safe work. If revising a governed `IMP-*`, work from current effective provenance rather than replaying full history; record the immediate predecessor with `sd:transforms`, the transition reason with `sd:changeCausedBy`, and the change kind.
20. Preserve effective implementation causes that remain valid and remove/update only those actually superseded. Treat behavior-preserving refactors as lineage events when they materially revise the governed implementation, and verify preservation when important.
21. Before each semantic causal commit that adds or changes Spiral Turtle, run available staged/pre-commit graph validation. New/changed historical references must point to commits already reachable from current `HEAD`; do not knowingly make malformed provenance durable and plan to repair it later.
22. Create semantic causal commits; never amend/rebase/squash them after creation.
23. Where CI/range tooling exists, validate the introduced causal history as a commit range rather than only the final snapshot.

Keep artifacts minimal. Do not create a template file unless it will be used.
