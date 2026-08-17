---
id: UND-PROCESS-002
---

# Understanding: Process boundaries must remain visible as uncertainty changes

## Interpreted intent

The dogfooding feedback identifies three related failures of process visibility rather than three unrelated documentation edits:

1. **Cycle identity is not self-checking.** Spiral already says repository-changing cycles normally use dedicated branches, but an agent can continue on an older cycle branch without noticing. Because Git history is evidence, branch/cycle agreement must be actively inspected at the moments where causal history is created and judged.
2. **Cycle granularity is being mistaken for task granularity.** Small evidence-producing steps are useful under uncertainty, but the outer cycle is an integration/evaluation boundary. Once governing assumptions are stable, repeatedly opening tiny cycles adds ceremony without increasing justified trust.
3. **Brownfield intake has no durable completeness signal.** The intentionally conversational intake can skip a topic without leaving evidence that the project frame is still incomplete. Intake therefore needs explicit state plus complete disposition of a small required topic set, while still allowing `Unknown`, `Not relevant`, and justified deferral.

## Current effective behavior / evidenced gap

Repository inspection before implementation established that:

- branch-per-cycle guidance existed, but prompts/evaluation did not require comparing the active `CYC-*` with actual Git branch state before later semantic commits;
- the process emphasized reducing uncertainty with small evidence-producing steps but did not explicitly distinguish those steps from the size of the outer cycle;
- `docs/brownfield-intake.md` explicitly avoided a fixed questionnaire and `PROJECT_CONTEXT` had no intake state/checklist, so omitted intake topics could disappear silently.

These gaps match the failures observed during SimplyStore dogfooding.

## Desired outcome

Harden Spiral Developer so that:

- branch/cycle mismatch is surfaced mechanically through direct Git-state checks at cycle open, before semantic causal commits, and during evaluation;
- cycle planning asks for a sizing rationale based on uncertainty, risk, and evaluation coherence rather than treating smaller as inherently better;
- brownfield intake persists `Incomplete/Complete/Stale` state, gives every required topic an explicit disposition, and keeps unfinished topics visible in user interactions while intake remains active.

Do this with the smallest process changes that make omission visible. Do not introduce a branch manager, formal intake engine, or cycle-size scoring system unless later evidence requires them.

## Confidence and uncertainty

High confidence in the three gaps because each is supported both by direct human dogfooding feedback and by inspection of the then-current process texts/templates. The exact wording and enforcement points may need refinement after further dogfooding.
