# Brownfield Change Prompt

Apply the brownfield rule to this current change.

1. Work on the dedicated feature branch; do not rewrite existing history.
2. Identify the behavior/capability being changed, not merely the files.
3. Characterize current observable behavior and relevant existing tests.
4. Inspect history/docs/issues/callers only as far as needed for this change.
5. Record reconstructed claims as explicit, evidenced, inferred, or unknown.
6. Preserve important confidence and causal relationships in the relevant companion Turtle resources.
7. Identify current request/design constraints that require preserving or changing legacy behavior.
8. Define verification and acceptance evidence.
9. Keep unrelated cleanup out of scope.
10. After the change, leave this capability more traced than before.

Do not invent historical intent to make the causal chain look complete.
