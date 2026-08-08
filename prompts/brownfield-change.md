# Brownfield Change Prompt

Apply Spiral Developer to this change in an existing codebase.

Before modifying legacy behavior:

1. establish the exact repository/worktree baseline;
2. identify the behavior/capability being changed, not merely the files;
3. characterize current observable behavior and relevant existing tests;
4. inspect history/docs/issues/callers only as far as needed for this change;
5. record reconstructed claims as explicit, evidenced, inferred, or unknown;
6. identify current request/design constraints that require preserving or changing legacy behavior;
7. define verification and acceptance evidence;
8. keep unrelated cleanup out of scope;
9. after the change, leave this capability more traced than before.

Do not invent historical intent to make the causal chain look complete.
