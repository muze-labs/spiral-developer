# Quickstart

Spiral Developer is meant to be learned on real work, not installed as a heavyweight process.

The first experiment should be one bounded change or feature.

## 1. Add a small project area

A suggested starting structure is:

```text
.spiral/
  CULTURE.md
  PROJECT_CONTEXT.md
  requests/
  feedback/
  designs/
  evidence/
  acceptance/
  legacy/
  defects/
  cycles/
```

Copy only the templates you need. Do not create empty documents for completeness.

## 2. Establish culture and project context

Create `CULTURE.md` from `templates/CULTURE.md` and point it at the organization/project principles the agent should preserve.

Create `PROJECT_CONTEXT.md` with current direction, intended users, important constraints, and long-lived context.

Do not attempt to capture the entire project history.

## 3. Start with one current request

Create a request artifact from `templates/REQUEST.md`.

A good request describes intent and observable desired outcomes without prematurely prescribing implementation.

Mark assumptions and ambiguity explicitly.

## 4. Find the nearest important uncertainty

Before implementation, ask what is most likely to prevent useful progress next.

Record risks as:

- blocker;
- near-term;
- deferred;
- existential.

Solve the blocker/near-term risk. Record later risks. Pull a deferred risk forward only if it can invalidate the current direction.

## 5. Get meaningful interaction early

For normal Muze web work, create a functioning UI as quickly as possible so intended users can spend real time with the feature.

At this point optimize for **behavioral fidelity and learning**, not polish.

Use `templates/FEEDBACK.md` to record what actual interaction taught you. If feedback changes the request, create a new request revision rather than editing history away.

## 6. Create a traceable design

Use `templates/DESIGN.md`.

Every significant design element should identify why it exists:

- which request fragment it satisfies;
- which culture/external constraint shapes it;
- which supporting technical need it enables;
- which risk it addresses.

## 7. Implement the smallest real vertical slice

Once the interaction model is credible, implement a thin real path through the system.

The code itself is an implementation artifact. Record the design IDs/revisions it realizes in the cycle/evidence artifacts and, where useful, in commit or PR metadata.

Do not broaden the change to unrelated cleanup.

## 8. Connect verification and acceptance

Use `templates/EVIDENCE.md` for evidence that implementation realizes design.

Use `templates/ACCEPTANCE.md` for evidence that the resulting behavior satisfies the request.

These are not the same claim.

## 9. When something fails, repair the chain

Use `templates/DEFECT.md`.

Trace the failure upward. If the environment was underspecified, repair the request, design, context, constraint, or evaluator first. Then let implementation follow.

## 10. Evaluate the experiment

At the end of the cycle, ask:

- Did traceability help the AI make better decisions?
- Could we explain why each significant design/implementation choice existed?
- Did the process expose an upstream problem earlier?
- Which artifacts were useful during actual work?
- Which bookkeeping was ceremonial?
- Did the code remain simple and economical to extend?
- Did meaningful user interaction alter our understanding?

Change this process based on that evidence before adding automation.

## Existing projects

For an existing repository, read `02-brownfield-adoption.md` before starting. The default rule is:

> **Preserve causality accurately from now on; reconstruct history only where current work crosses it.**
