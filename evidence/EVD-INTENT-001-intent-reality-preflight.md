---
id: EVD-INTENT-001
---

# Verification Evidence: Intent confirmation and repository-reality preflight

## What is being verified

Adoption of `LES-007`: consequential direct human input is clarified with the human before implementation commits to a direction, then reconciled with relevant project reality—including existing/overlapping capability—inside Understanding formation rather than through a new artifact type.

## Mechanical / structural checks

- `AGENTS.md` explicitly requires human confirmation of consequential direct intent before execution and repository-reality/overlap reconciliation afterward.
- `docs/process.md` defines the pre-crystallization loop and states that repository reconnaissance belongs inside Understanding formation rather than a new artifact class.
- `docs/ai-collaboration.md` distinguishes human authority over desired intent from factual claims about the current system and describes the confirm → inspect → re-clarify → crystallize loop.
- `prompts/start-change.md` stops consequential implementation before confirmation, searches semantically for existing/overlapping capability after confirmation, and returns materially changed interpretations to the human.
- `docs/brownfield.md` and `prompts/brownfield-change.md` ask what already owns or approximates the requested behavior before adding a new capability.
- `templates/UNDERSTANDING.md` provides an optional place to preserve repository reality/overlap findings when they materially affect interpretation.
- `docs/review.md` asks whether confirmation, repository reconciliation, and re-clarification occurred where material.
- No new reality-check artifact class or ontology relation was introduced for this guardrail.
- All repository Turtle resources parse with the installed standards-conforming `rdflib` parser.
- Current durable artifact references under `sources/`, `understandings/`, `lessons/`, `cultures/`, `warning-profiles/`, and `evidence/` resolve to real strict Git ancestors of the artifact version containing them.
- `git diff --check` and `git fsck` complete without structural repository errors relevant to this change.

## Human-semantic checks still required

Dogfooding must determine whether the significance threshold is useful. The process should prevent confident misinterpretation and accidental duplicate work without causing agents to ask ceremonial confirmation questions for trivial, obvious, reversible edits.

Repository search quality also remains empirical: the documentation requires semantic overlap reconnaissance, but static validation cannot prove an agent will discover an existing capability expressed through sufficiently different terminology or abstraction.

## Limitations

`pyshacl` is not installed in the current validation environment, so SHACL validation was not executed. Example/template Turtle files intentionally contain placeholder hashes; exact Git-reference validation therefore applies to durable process artifacts rather than illustrative/template resources.

## Result

The clarified intent/reality preflight is structurally integrated into the main Spiral Developer entry points and is ready for dogfooding. Its practical threshold and retrieval effectiveness remain explicit experimental questions.
