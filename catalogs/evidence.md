# Evidence Catalog

Evidence should match the claim being tested.

## Intent / interpretation evidence

Useful for establishing why a request represents the current need:

- retained or externally referenced source material with stable identity/version;
- attributed stakeholder statements or corrections;
- explicit clarification of ambiguous source language;
- comparison of materially different interpretations or framings;
- human/stakeholder confirmation of an interpretation when judgment is required;
- explicit `unavailable` provenance when only a report, recollection, or inherited claim remains.

A source proves what was available upstream, not that the project interpreted it correctly. An accepted understanding is itself a claim that may later be superseded.

## Meaningful-interaction evidence

Useful for questions about product intent and interaction:

- intended-user session with a working UI;
- observed task completion;
- behavior/decision changes during realistic use;
- user correction of an assumption;
- comparison of two interactive hypotheses.

A polished screenshot is usually weak evidence for actual interaction behavior.

## Design / implementation verification

Useful for showing implementation realizes design:

- focused automated tests;
- property/invariant tests;
- integration tests across a boundary;
- dependency replacement experiment;
- static analysis;
- benchmark/performance envelope;
- fault injection/recovery test;
- security/authorization checks.

## Acceptance evidence

Useful for showing the result satisfies request intent:

- acceptance scenarios derived from request outcomes;
- intended-audience interaction;
- stakeholder confirmation where appropriate;
- objective domain result;
- operational observation in realistic conditions.

## Evidence-quality questions

- Which claim would fail if this evidence failed?
- Can the evidence detect a plausible wrong implementation?
- Is it independent enough from the implementation to be meaningful?
- Does it test a design property or merely repeat internal structure?
- What does it explicitly *not* establish?
- If the same agent wrote code and test, what prevents it from weakening the test to fit the code?

## Provenance / graph evidence

Useful for establishing that the causal record itself is trustworthy:

- Turtle parses successfully;
- SHACL constraints pass;
- referenced full Git commit hashes exist;
- referenced artifacts/paths exist at the claimed historical commit where relevant;
- graph impact queries find expected downstream dependents after an upstream change;
- human spot-check confirms that machine links represent the decision actually made rather than a plausible reconstructed story;
- source artifacts accurately declare whether primary evidence is retained, referenced, or unavailable;
- understanding artifacts point to the exact source/evidence versions they actually interpreted.

Passing graph validation establishes structural/provenance integrity. It does **not** establish that the product behavior or design is correct.
