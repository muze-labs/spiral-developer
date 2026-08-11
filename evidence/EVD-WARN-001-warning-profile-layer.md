---
id: EVD-WARN-001
---

# Verification Evidence: Replaceable warning-profile layer

## What is being verified

The first Spiral Developer warning-profile mechanism and bundled starter profile.

## Mechanical checks

- All repository Turtle resources parse with the installed standards-conforming `rdflib` Turtle parser.
- All durable artifact references under `sources/`, `understandings/`, `lessons/`, `cultures/`, `warning-profiles/`, and `evidence/` resolve to real Git commits reachable from the source version's current ancestry at commit time.
- The ontology defines `sd:WarningProfile` separately from `sd:Culture` and defines `sd:adoptsWarningProfile` as explicit project-context adoption of an exact profile version.
- Project-context templates support culture and warning-profile adoption independently.
- The bundled warning profile contains a significance gate and seven operational signals: premature closure, authority drift, evidence overreach, composition risk, optionality loss, meaningful exclusion, and model closure.
- Core documentation states that warning profiles are replaceable inspection lenses, not automatic blockers or hidden engineering culture.

## Human-semantic checks still required

Mechanical validation cannot establish that the initial signal definitions are useful, proportionate, or complete. Dogfooding should evaluate warning fatigue, false positives, hidden assumptions, and whether the warnings improve professional judgment without turning normal development into debate.

## Limitations

`pyshacl` is not installed in the current validation environment, so SHACL validation was not executed for this change. Turtle syntax and exact durable Git-reference integrity were checked separately.

## Result

The mechanism is structurally ready for dogfooding. The bundled profile remains optional and replaceable.
