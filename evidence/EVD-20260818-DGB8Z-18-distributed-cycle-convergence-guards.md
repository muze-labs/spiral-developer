---
id: EVD-20260818-DGB8Z-18
---

# Verification Evidence: Distributed cycle convergence guards

## Claim being verified

`IMP-20260818-DGB8Z-16@2fbd4d0d002a54a5c56fc8a12062ffc5d6f733d9` implements the CYC-005 distributed-cycle safeguards agreed during human review: conservative local allocation recovery, branch-scoped cycle closure/integration, and explicit predecessor-preserving convergence for parallel revisions of one governed artifact.

## Implementation under test

`IMP-20260818-DGB8Z-16@2fbd4d0d002a54a5c56fc8a12062ffc5d6f733d9`

## Evidence method

- [x] Automated test suite
- [x] Repository snapshot validation
- [x] Actual CYC-005 prospective-integration dogfood probe
- [x] Negative regression probe derived from earlier falsifying evidence
- [ ] Hosted-CI execution of the revised branch/closure gate

## Result

The automated suite passes **14/14** tests, including probes that:

- fast-forward stale checkout-local allocator state above the highest visible slot in the same workspace namespace;
- reject an Active candidate cycle;
- reject a candidate branch whose supplied branch name does not match its cycle;
- reject integration of a different cycle into an Active cycle target;
- detect a pre-existing Active cycle when the candidate changes only the cycle Markdown companion;
- reject a clean two-parent Git merge when both parent histories revised the same governed artifact but the convergence version does not preserve both exact predecessor lineages;
- accept that convergence after the merge version carries both required `sd:transforms` references.

The repository worktree validates successfully after the correction.

The actual CYC-005 branch was then probed against local `main` after updating its cycle Markdown while deliberately leaving the cycle TTL `sd:Active`:

```sh
node bin/spiral.mjs validate integration \
  --base main \
  --head HEAD \
  --base-branch main \
  --head-branch spiral/CYC-005-distributed-development
```

At candidate commit `0d241c80908729bd5bda32763435f827008b5d63`, validation exited non-zero with:

```text
ERROR [open-cycle-integration] cycle CYC-005 is not closed/Accepted in the candidate; unfinished cycle branches must not integrate into accepted history
```

That is the intended result. It directly demonstrates that the corrected gate blocks this historically problematic Active branch from integrating again.

## Relationship to earlier evidence

`EVD-20260818-DGB8Z-17` recorded a failed dogfood probe against the first IMP-16 revision. That evidence showed that TTL-only candidate-cycle discovery could miss continued work on an Active cycle whose TTL already existed on the target. The current revision is causally linked to that finding and the new Markdown-only regression probe covers the failure mode.

## Limits

- Branch/cycle correspondence requires branch metadata from the integration environment; the provided GitHub/GitLab adapters supply it, but this revised behavior has not yet been observed on a hosted runner.
- Parallel-convergence detection currently covers stable companion paths in ordinary two-parent merges; rename/move identity matching and octopus merges remain outside this slice.
- Presence of both predecessor references proves that neither causal lineage was silently erased; it does not by itself prove that the semantic reconciliation is correct. Human/verification review remains required.
