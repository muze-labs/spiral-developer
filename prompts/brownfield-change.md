# Brownfield Change Prompt

Apply the brownfield rule to this current change.

1. Read the durable intake status. If brownfield intake is missing, `Incomplete`, or materially `Stale`, run/resume `prompts/brownfield-intake.md` before treating this as the next normal cycle. Until it is complete, surface `Intake incomplete — remaining: ...` in every user-visible response while intake remains active rather than silently proceeding from a partial frame. Otherwise, before consequential product modification, enter discourse mode and treat the human input as reasoning/intent evidence rather than automatic execution authority; identify the behavior/capability at issue, not merely the files or ticket wording. If this project or subsystem is unfamiliar, assume your project-specific understanding is partial: build enough affinity to know where the behavior could originate, or ask the human for local guidance before making strong absence/duplication claims. Do not invent an affinity score or formal intake stage.
2. Characterize **current effective behavior**. Search for direct and indirect ownership/capability under different names, interfaces, generic/shared abstractions, inheritance, defaults, configuration, callers, tests, composition, or runtime behavior.
3. Establish an **evidenced gap** to the intended outcome using a probe appropriate to the claim. Do not infer a gap merely because no dedicated/local implementation is obvious.
4. Present **My understanding / Current effective behavior / Evidenced gap / Material assumptions** to the human and STOP for confirmation or correction. If there is no demonstrated gap, do not implement a duplicate/no-op change.
5. Ensure the change serves the active human-confirmed cycle goal. If no cycle is active, use `prompts/plan-cycle.md`. After confirmation, work on the dedicated cycle branch for repository-changing work and mechanically verify that the current branch names the active cycle before consequential repository work and before each semantic causal commit; do not rewrite existing history. If later evidence invalidates the Understanding or gap, stop and return to discourse.
6. Inspect history/docs/issues/callers only as far as needed for this change.
7. Record reconstructed claims as explicit, evidenced, inferred, or unknown.
8. Preserve important confidence and causal relationships in the relevant companion Turtle resources.
9. Identify current request/design constraints that require preserving or changing legacy behavior.
10. Define verification and acceptance evidence.
11. Keep unrelated cleanup out of scope.
12. If an existing `IMP-*` predecessor is reliably traceable, connect the new governed version with `sd:transforms`; otherwise preserve the lineage gap rather than inventing it. Record transition cause/change kind from this point forward.
13. Keep current effective provenance as the default context for future changes; do not require full-history replay.
14. Keep adjacent newly discovered work out of scope unless it is necessary to achieve/evaluate the current cycle goal or repair a cycle-caused regression; retain it for next-cycle planning.
15. When the cycle goal can be judged, enter explicit cycle evaluation before planning new direction.
16. After the change, leave this capability more traced than before.

Do not invent historical intent or implementation lineage to make the causal chain look complete.
