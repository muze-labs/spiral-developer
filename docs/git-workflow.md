# Git Workflow: History Is Evidence

Git is not only source control in Spiral Developer. It is the immutable historical store used to identify the exact versions that participated in causal decisions.

> **Git history is evidence. Causal history is corrected prospectively, never rewritten retrospectively.**

## Authoritative branch

Each project has an authoritative integration branch, normally `main` unless the project says otherwise.

Direct consequential cycle development on the authoritative branch is not part of the Spiral Developer workflow.

## Cycle branches

For ordinary repository-changing work, one **cycle** starts on one dedicated branch from the current authoritative branch after the human confirms the cycle goal.

Suggested naming:

```text
spiral/CYC-017-account-deactivation
spiral/CYC-018-expiry-race
```

The cycle branch is the normal integration/review boundary. It may contain multiple requests, design/implementation steps, investigations, and semantic commits that all serve the same coherent cycle goal. Internal tasks do not normally receive separate branches or pull requests.

A non-code investigation/evaluation cycle may not need a development branch. Cross-repository or irreversible operational work may need a different integration boundary; follow the trust model instead of forcing this convention.

The branch contains an evolving proposed reality. The authoritative branch remains accepted project reality.

## AI as Git operator

When tools and permissions allow it, the AI should perform routine Git operations:

- create the cycle branch;
- stage only relevant files;
- update the relevant companion Turtle resources;
- create semantic commits;
- merge the authoritative branch into the cycle branch when needed;
- push the branch;
- prepare/open the pull request.

Humans should not have to type commit hashes into causal records as ordinary clerical work.

## Commit boundaries

Do not commit every exploratory edit.

Uncommitted exploration is disposable.

Create a commit when a development fact has crystallized enough to become useful evidence, for example:

- current request captured;
- meaningful feedback recorded;
- design decision established;
- meaningful observable implementation slice established;
- verification evidence established;
- acceptance evidence recorded;
- root-cause correction made.

Downstream commits can then refer to the exact upstream commit hash.

### Validate before the causal commit

Because a semantic causal commit becomes immutable evidence, validate new or changed versioned references **before** creating it where tooling is available. Prevention is stronger than discovering a malformed reference after the commit has entered preserved history.

For staged content, the prospective source commit does not exist yet. A referenced target commit must therefore already be reachable from current `HEAD`; referencing `HEAD` itself is valid because it becomes a strict ancestor of the new commit. After commit creation, persisted validation requires the target to be a strict ancestor of the source commit.

Projects with machine-enforced provenance should make staged/pre-commit validation blocking for changed Spiral Turtle and repeat the check over the introduced commit range in CI. Use a standards-conforming RDF/Turtle parser.

See `causal-validation.md`.

### Commit messages

Use concise semantic commit subjects. Optional Git trailers can make `git log` easier to navigate, for example:

```text
Implement account deactivation slice

Spiral-Artifact: IMP-017
Spiral-Design: DES-009@2bc31aa
Spiral-Request: REQ-017@1a2f9e1
```

Trailers are human/navigation summaries. The companion Turtle resources remain authoritative for machine-readable causal links and store full hashes. Do not require humans to maintain these trailers manually when the AI can do it.

## Immutable causal commits

Once a semantic causal commit exists, do not rewrite it.

Do **not**:

- `git commit --amend` it;
- interactive-rebase it;
- squash it;
- reset it away;
- force-push a rewritten version;
- use a squash/rebase merge that destroys its identity.

If it was wrong, create a new commit that corrects or supersedes it.

This is not untidiness. The mistaken understanding and its later correction are part of the evidence.

## Bringing the branch up to date

If the authoritative branch moves while cycle work continues:

```text
git merge main
```

(or the project's authoritative branch).

Resolve conflicts on the cycle branch and preserve the merge commit.

Do not rebase the cycle branch onto the new authoritative tip once causal commits exist.

## Pull request

When the AI believes the cycle goal can be judged, it enters cycle evaluation. For repository changes, the pull request can carry that integrated evaluation; human feedback there may keep the same cycle branch open for correction. Do not require a separate review before the PR merely to mark the phase transition.

The PR is evaluated by:

- CI/CD and other automated checks;
- human review of intent, design, evidence, risk, and result.

See `review.md`.

## Merge-only integration

Accepted work is integrated with a normal merge commit.

Configure repository hosting, where practical, to:

- require pull requests for the authoritative branch;
- disallow force pushes;
- require CI checks;
- disable squash merge for Spiral Developer work;
- disable rebase merge for Spiral Developer work;
- permit/require merge commits.

The merge commit means:

> **The cycle outcome and its causal history were reviewed as a unit and admitted into authoritative project history.**

## Git hashes as versions

Stable artifact identity and artifact version are different things:

```text
REQ-017                 stable identity
REQ-017@a12f9e1         human shorthand for a historical version
```

The Turtle graph stores full hashes, not abbreviations.

Do not store an artifact's own commit hash inside the commit that creates it; that is impossible because the commit hash depends on the commit contents. Only downstream artifacts need to record the already-existing upstream hash.


## Implementation lineage and Git ancestry

Implementation lineage depends on Git being an immutable historical store. When a governed `IMP-*` is materially revised, the new version can refer backward to the already-known predecessor commit with `sd:transforms`. The current commit still does not need to know its own hash.

A lineage reference should normally resolve to an implementation version that is an ancestor of the current revision commit. Split/merge/replacement cases may reference multiple predecessor `IMP-*` identities, but they still point backward to exact historical versions.

Version-aware validation therefore applies the same historical-reference invariant used by causal provenance: the target version must already exist and, once persisted, its commit must be a strict Git ancestor of the source implementation version. `sd:transforms` and `sd:changeCausedBy` share historical-integrity rules with causal references without becoming current causal justification.

Validate this before commit where possible, over the introduced commit range in CI, and through an explicit history audit when required. Snapshot-only validation cannot prove that an invalid historical edge was never introduced and later removed.

These checks establish historical integrity, not semantic correctness. A behavior-preserving refactor still needs behavioral evidence when preservation matters. See `causal-validation.md`.

## Exceptional destructive rewrites

Normal development must never rewrite causal history.

If an exceptional legal or security incident requires repository-level history rewriting (for example, purging an accidentally committed secret), treat it as a provenance incident rather than normal cleanup. Rotate/revoke affected credentials immediately, document the rewrite, and revalidate causal references because commit identities may have changed.
