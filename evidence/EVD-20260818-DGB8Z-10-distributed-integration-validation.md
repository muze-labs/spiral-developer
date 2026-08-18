---
id: EVD-20260818-DGB8Z-10
---

# Verification Evidence: Distributed integration validation

## Claim being verified

The second `CYC-005` implementation slice makes distributed integration mechanically checkable: local branches can remain independent, while the later integration is blocked when the actual combined state contains Spiral identity collisions or causally stale current/effective provenance that Git's textual merge does not expose.

## Why this evidence exists

`REQ-20260818-DGB8Z-7` requires a shared repository-local validator for local and prospective integrated state. `DES-20260818-DGB8Z-8` defines the deliberately mechanical boundary: Git owns ordinary merge conflicts; Spiral checks current/effective causal coherence in the combined graph and does not decide semantic truth.

## Implementation under test

| Artifact/path/symbol | Commit | Role |
|---|---|---|
| `IMP-20260818-DGB8Z-9` | `17d9681fcf7c9a7627ea75d309918488120410d3` | Distributed integration validator implementation. |
| `bin/spiral.mjs` | `17d9681fcf7c9a7627ea75d309918488120410d3` | CLI and prospective Git merge-tree orchestration. |
| `bin/spiral-rdf.py` | `17d9681fcf7c9a7627ea75d309918488120410d3` | Current/prospective RDF graph validator. |
| `test/spiral-integration.test.mjs` | `17d9681fcf7c9a7627ea75d309918488120410d3` | Disposable-repository integration probes. |

## Evidence method

- [x] Automated test
- [x] Property/invariant check
- [x] Static/syntax check
- [ ] Benchmark
- [x] Manual observation
- [x] Integration exercise
- [ ] Other:

## Result

`npm test` passes **9 tests**: the original three allocator tests plus six integration-validation probes.

The integration probes establish:

1. **causal staleness appears only after combination** — a candidate branch that adds an accepted design against an accepted request passes `spiral validate` locally; a target branch independently supersedes the exact request version; `spiral validate integration` against target + candidate fails with `stale-superseded-reference`;
2. **later merge can reconcile** — after the candidate merges the new target and updates its effective design provenance to the current request version, prospective integration passes;
3. **non-effective status propagates** — an accepted implementation depending on a design currently marked `Suspect` fails with `reference-to-non-effective-artifact`, preventing an intermediate status change from leaving a downstream accepted claim apparently well-founded;
4. **only effective superseders retire versions** — a `Rejected` artifact containing `sd:supersedes` does not invalidate an otherwise effective upstream version;
5. **distributed allocation collisions are detected** — distinct artifact IDs that reuse the same `(WORKSPACE, local sequence)` slot fail even when different type/date prefixes avoid a filename collision;
6. **ordinary source conflict remains Git's problem** — a textual conflict makes prospective merge construction fail before Spiral attempts causal diagnosis;
7. **malformed Turtle fails through the RDF parser** rather than being interpreted by formatting-dependent extraction.

Repository-level checks after the implementation commit:

- `spiral validate` passes on the working repository: **87 Turtle files / 1123 triples**;
- `spiral validate integration --base main --head HEAD` passes on the actual CYC-005 candidate against the repository's current local `main`, validating the prospective combined tree;
- a separate governed-artifact historical-reference probe checks **59** current exact historical references (excluding templates/examples) and finds all target commits present and strict ancestors of their current source artifact versions;
- both CI adapter YAML examples parse successfully;
- `git fsck --full` reports no repository-integrity error;
- `git diff --check` passes before the implementation commit.

## Hosting-adapter review

The repository documentation/examples were checked against current official hosting documentation during this cycle:

- GitHub documents `pull_request` as using a pull-request merge ref/merge commit and requires workflows that are required checks in Merge Queue to also handle the separate `merge_group` event. The example therefore reconstructs target + candidate for ordinary pull requests and validates GitHub's exact merge-group snapshot for queued integration.
- GitLab documents ordinary merge-request pipelines as source-branch-only, merged-results pipelines as testing a temporary source+target merge, and merge trains as extending this to earlier queued merge requests. The example therefore constructs the prospective merge explicitly for ordinary MR pipelines and validates the already-combined snapshot when GitLab supplies one.

Official references:

- https://docs.github.com/actions/using-workflows/events-that-trigger-workflows#pull_request
- https://docs.github.com/actions/using-workflows/events-that-trigger-workflows#merge_group
- https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/
- https://docs.gitlab.com/ci/pipelines/merged_results_pipelines/
- https://docs.gitlab.com/ci/pipelines/merge_trains/

## Failure cases / limits

- The GitHub/GitLab files are adapter examples; they were syntax-checked and reviewed against host documentation but were not executed on those hosted CI systems in this local dogfood run.
- A required check still has to be enabled in repository-host settings; committing an adapter alone cannot make branch protection/merge policy mandatory.
- Snapshot/prospective validation does not replace the complete historical/range validation described in `docs/causal-validation.md`.
- The first implementation uses both Node and Python (`rdflib`). The parser boundary is narrow, but packaging/runtime consolidation remains a later concern unless dogfooding makes it important.
- The validator detects mechanically explicit supersession/status changes. It cannot detect a semantically obsolete dependency when the graph itself failed to record the upstream change.

## Evidence quality

The central staleness test uses real temporary Git branches and commits, not a mocked graph merge. It demonstrates the precise distributed failure mode: each branch is locally coherent, Git can combine the files, but the resulting causal state is unacceptable until the later candidate reconciles. The negative rejected-superseder case prevents the validator from equating every proposed supersession edge with an effective decision.
