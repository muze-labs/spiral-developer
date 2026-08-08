# Evidence Catalog

Evidence should match the claim being tested.

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
