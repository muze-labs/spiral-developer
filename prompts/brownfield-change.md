# Brownfield Change Prompt

Apply the brownfield rule to this current change.

1. Before consequential implementation, confirm the intended outcome with the human if the direct request could support materially different interpretations.
2. Identify the behavior/capability being changed, not merely the files. Search first for existing or overlapping ownership/capability under different names, interfaces, tests, or abstractions.
3. Characterize current observable behavior and relevant existing tests. If the existing system materially changes what the task appears to require, return to the human and clarify before proceeding.
4. Work on the dedicated feature branch; do not rewrite existing history.
5. Inspect history/docs/issues/callers only as far as needed for this change.
6. Record reconstructed claims as explicit, evidenced, inferred, or unknown.
7. Preserve important confidence and causal relationships in the relevant companion Turtle resources.
8. Identify current request/design constraints that require preserving or changing legacy behavior.
9. Define verification and acceptance evidence.
10. Keep unrelated cleanup out of scope.
11. If an existing `IMP-*` predecessor is reliably traceable, connect the new governed version with `sd:transforms`; otherwise preserve the lineage gap rather than inventing it. Record transition cause/change kind from this point forward.
12. Keep current effective provenance as the default context for future changes; do not require full-history replay.
13. After the change, leave this capability more traced than before.

Do not invent historical intent or implementation lineage to make the causal chain look complete.
