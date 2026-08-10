# Start Change Prompt

Apply Spiral Developer to this requested change.

1. Identify the authoritative branch and create a dedicated `spiral/...` feature branch.
2. Capture the current request and observable desired outcomes.
3. If the request or proposed solution contains a consequential assumption, briefly perform a framing check: identify the assumption and a less constraining question when a different framing could materially change the work. Do not do this for routine local choices.
4. Commit the request when it is sufficiently clear to guide the next step.
5. Identify ambiguity and the nearest important uncertainty.
6. Classify risks by horizon: blocker, near-term, deferred, existential.
7. For web interaction work, create the fastest functioning UI/probe capable of meaningful intended-user feedback. Do not optimize polish unless needed for the feedback.
8. Record explicit non-goals and later risks that should not shape current design.
9. Draft the smallest design elements needed and connect each in its companion Turtle resource to exact upstream commit hashes.
10. Define verification and acceptance evidence before hardening implementation.
11. If legacy behavior is touched, follow the brownfield process rather than guessing intent.
12. Implement only when causal context is sufficient for safe work.
13. Create semantic causal commits; never amend/rebase/squash them after creation.

Keep artifacts minimal. Do not create a template file unless it will be used.
