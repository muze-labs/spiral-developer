---
id: EVD-20260818-DGB8Z-11
---

# Verification Evidence: Hosted integration adapter revision

## Claim being verified

The current `IMP-20260818-DGB8Z-9` revision preserves the verified distributed-integration behavior while adding a dogfood GitHub workflow and hardening the reusable GitHub/GitLab adapters.

## Implementation under test

`IMP-20260818-DGB8Z-9@fd38289b51f39154728a1848f359bcca42082106`

## Evidence method

- [x] Automated test
- [x] Prospective integration exercise
- [x] Configuration syntax check
- [x] Repository integrity check
- [ ] Hosted-CI execution

## Result

After the adapter revision:

- `npm test`: **9/9 pass**;
- `spiral validate`: passes on **88 Turtle files / 1141 triples**;
- `spiral validate integration --base main --head HEAD`: passes for the current CYC-005 branch against local `main`, validating the prospective merged tree;
- `.github/workflows/spiral-integration.yml`, `examples/ci/github-spiral-integration.yml`, and `examples/ci/gitlab-spiral-integration.yml` parse as YAML;
- `git fsck --full` reports no repository-integrity error.

The GitHub adapter now exists both as a reusable example and as this repository's own workflow. The GitLab adapter explicitly requests full history so its ordinary merge-request path can construct a prospective merge tree reliably.

## Limits

This local evidence does not claim that the hosted workflow has already run successfully on GitHub or GitLab. Repository-host settings must also mark the check as required if it is to block integration. Those are deployment/configuration facts outside this local Git snapshot.
