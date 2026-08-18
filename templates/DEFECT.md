---
id: DEF-YYYYMMDD-WORKSPACE-N
---

<!-- Allocate a new ID with `spiral allocate <TYPE>`; do not choose a global next sequence. -->

# Defect / Root-Cause Analysis

## Failure

Observed behavior:

Expected behavior / acceptance reference:

## Reproduction

## Causal trace

Source / provenance (when relevant):

Understanding / interpretation (when relevant):

Request:

Design:

Implementation:

Verification that should have detected it:

Acceptance/production observation:

## Earliest meaningful root cause

- [ ] Missing/weak source provenance
- [ ] Source misinterpretation / wrong understanding
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

<!-- What should change in the production environment? Correct it in a new commit; do not rewrite the original history. -->

## Downstream propagation

<!-- Which artifacts become suspect/revised/regenerated? -->

## Regression evidence

<!-- Show that the original failure and useful nearby variants can no longer pass. -->
