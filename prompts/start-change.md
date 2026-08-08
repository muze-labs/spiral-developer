# Start Change Prompt

Apply Spiral Developer to this requested change.

1. Identify the authoritative branch and create a dedicated `spiral/...` feature branch.
2. Capture the current request and observable desired outcomes.
3. Commit the request when it is sufficiently clear to guide the next step.
4. Identify ambiguity and the nearest important uncertainty.
5. Classify risks by horizon: blocker, near-term, deferred, existential.
6. For web interaction work, create the fastest functioning UI/probe capable of meaningful intended-user feedback. Do not optimize polish unless needed for the feedback.
7. Record explicit non-goals and later risks that should not shape current design.
8. Draft the smallest design elements needed and connect each in its companion Turtle resource to exact upstream commit hashes.
9. Define verification and acceptance evidence before hardening implementation.
10. If legacy behavior is touched, follow the brownfield process rather than guessing intent.
11. Implement only when causal context is sufficient for safe work.
12. Create semantic causal commits; never amend/rebase/squash them after creation.

Keep artifacts minimal. Do not create a template file unless it will be used.
