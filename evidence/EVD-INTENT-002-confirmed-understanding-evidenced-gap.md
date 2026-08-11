---
id: EVD-INTENT-002
---

# Verification Evidence: Confirmed Understanding + evidenced-gap implementation gate

## What is being verified

Adoption of `LES-008`: consequential direct human work must not modify product behavior until the human has confirmed the agent's concrete Understanding and project evidence establishes that the current effective behavior has a relevant unmet outcome.

## Mechanical / structural checks

- `AGENTS.md` defines the two-premise implementation gate and states that agent confidence cannot waive it.
- `prompts/start-change.md` requires inquiry first, a discriminating gap probe, a four-part human checkpoint, and an explicit **STOP** before product implementation.
- `prompts/brownfield-change.md` requires characterization of effective behavior and gap evidence rather than merely locating related code.
- `docs/process.md` defines Confirmed Understanding + Evidenced gap as preconditions for consequential product modification.
- `docs/ai-collaboration.md` states that absence of a dedicated implementation is not evidence that behavior is absent and gives examples of claim-appropriate probes.
- `docs/brownfield.md` explicitly covers indirect behavior from generic/shared code, inheritance, CSS cascade, defaults, configuration, composition, callers, framework behavior, and runtime state.
- `templates/UNDERSTANDING.md` now distinguishes current effective behavior from the evidenced gap.
- `docs/review.md` asks whether the checkpoint was confirmed before product modification and whether the gap was established behaviorally.
- `docs/trust-model.md` states that repository search alone or provenance written after implementation cannot substitute for the gate.
- `docs/quickstart.md`, `docs/vision.md`, `docs/artifact-model.md`, and `prompts/evaluate-cycle.md` use the same gate semantics.
- No new reality-check or gap artifact type was introduced.
- All repository Turtle resources parse with a standards-conforming RDF parser in the validation environment.
- Current durable exact artifact references resolve to real strict Git ancestors of the artifact version containing them.
- `git diff --check` and `git fsck` complete without structural errors relevant to this change.

## What this verification does not establish

Static documentation checks cannot prove that an agent will correctly decide the threshold for consequential work, choose a sufficiently discriminating probe, discover all indirect existing behavior, or actually stop in the user interaction at the checkpoint.

The strongest practical verification is therefore another dogfood task where:

1. the first human wording is plausibly misunderstandable;
2. the repository contains relevant behavior in a non-obvious/generic form;
3. the agent must show the checkpoint before product modification; and
4. implementation proceeds only if the human confirms an evidenced unmet outcome.

## Result

The previous advisory intent/reality preflight has been strengthened into an explicit implementation gate: **Confirmed Understanding + evidenced gap**. It is structurally integrated and ready for dogfooding.
