# Brownfield Change Prompt

Apply the brownfield rule to this current change.

1. Before consequential product modification, enter inquiry mode and identify the behavior/capability at issue, not merely the files or ticket wording. If this project or subsystem is unfamiliar, assume your project-specific understanding is partial: build enough affinity to know where the behavior could originate, or ask the human for local guidance before making strong absence/duplication claims. Do not invent an affinity score or formal intake stage.
2. Characterize **current effective behavior**. Search for direct and indirect ownership/capability under different names, interfaces, generic/shared abstractions, inheritance, defaults, configuration, callers, tests, composition, or runtime behavior.
3. Establish an **evidenced gap** to the intended outcome using a probe appropriate to the claim. Do not infer a gap merely because no dedicated/local implementation is obvious.
4. Present **My understanding / Current effective behavior / Evidenced gap / Material assumptions** to the human and STOP for confirmation or correction. If there is no demonstrated gap, do not implement a duplicate/no-op change.
5. After confirmation, work on the dedicated feature branch; do not rewrite existing history. If later evidence invalidates the Understanding or gap, stop and return to inquiry.
6. Inspect history/docs/issues/callers only as far as needed for this change.
7. Record reconstructed claims as explicit, evidenced, inferred, or unknown.
8. Preserve important confidence and causal relationships in the relevant companion Turtle resources.
9. Identify current request/design constraints that require preserving or changing legacy behavior.
10. Define verification and acceptance evidence.
11. Keep unrelated cleanup out of scope.
12. If an existing `IMP-*` predecessor is reliably traceable, connect the new governed version with `sd:transforms`; otherwise preserve the lineage gap rather than inventing it. Record transition cause/change kind from this point forward.
13. Keep current effective provenance as the default context for future changes; do not require full-history replay.
14. After the change, leave this capability more traced than before.

Do not invent historical intent or implementation lineage to make the causal chain look complete.
