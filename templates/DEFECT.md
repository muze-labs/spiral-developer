---
id: DEF-001
revision: 1
status: active
observes: []
---

# Defect / Root-Cause Analysis

## Failure

Observed behavior:

Expected behavior / acceptance reference:

## Reproduction

## Causal trace

Request:

Design:

Implementation:

Verification that should have detected it:

Acceptance/production observation:

## Earliest meaningful root cause

- [ ] Request ambiguity/wrong intent
- [ ] Missing/wrong design constraint
- [ ] Missing culture/external/legacy constraint
- [ ] Missing or irrelevant context
- [ ] Bad abstraction/boundary
- [ ] Weak/missing verification
- [ ] Wrong acceptance criterion
- [ ] Dependency/tool/model behavior
- [ ] Implementation failure despite adequate upstream model
- [ ] Unknown

Explanation:

## Upstream correction

<!-- What should change in the production environment? -->

## Downstream propagation

<!-- Which artifacts must become suspect/revised/regenerated? -->

## Regression evidence

<!-- Show that the original failure and useful nearby variants can no longer pass. -->
