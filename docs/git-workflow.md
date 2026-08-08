# Git Workflow: History Is Evidence

Git is not only source control in Spiral Developer. It is the immutable historical store used to identify the exact versions that participated in causal decisions.

> **Git history is evidence. Causal history is corrected prospectively, never rewritten retrospectively.**

## Authoritative branch

Each project has an authoritative integration branch, normally `main` unless the project says otherwise.

Direct feature development on the authoritative branch is not part of the Spiral Developer workflow.

## Feature branches

Each feature or meaningful change starts on a dedicated branch from the current authoritative branch.

Suggested naming:

```text
spiral/REQ-017-account-deactivation
spiral/DEF-009-expiry-race
```

The branch contains an evolving proposal: intent, design, implementation, evidence, and acceptance.

## AI as Git operator

When tools and permissions allow it, the AI should perform routine Git operations:

- create the working branch;
- stage only relevant files;
- update the relevant companion Turtle resources;
- create semantic commits;
- merge the authoritative branch into the feature branch when needed;
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
- vertical slice implemented;
- verification evidence established;
- acceptance evidence recorded;
- root-cause correction made.

Downstream commits can then refer to the exact upstream commit hash.

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

If the authoritative branch moves while feature work continues:

```text
git merge main
```

(or the project's authoritative branch).

Resolve conflicts on the feature branch and preserve the merge commit.

Do not rebase the feature branch onto the new authoritative tip once causal commits exist.

## Pull request

When the AI believes the request is satisfied, it proposes the feature branch through a pull request.

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

> **The branch's causal history was reviewed as a unit and admitted into authoritative project history.**

## Git hashes as versions

Stable artifact identity and artifact version are different things:

```text
REQ-017                 stable identity
REQ-017@a12f9e1         human shorthand for a historical version
```

The Turtle graph stores full hashes, not abbreviations.

Do not store an artifact's own commit hash inside the commit that creates it; that is impossible because the commit hash depends on the commit contents. Only downstream artifacts need to record the already-existing upstream hash.

## Exceptional destructive rewrites

Normal development must never rewrite causal history.

If an exceptional legal or security incident requires repository-level history rewriting (for example, purging an accidentally committed secret), treat it as a provenance incident rather than normal cleanup. Rotate/revoke affected credentials immediately, document the rewrite, and revalidate causal references because commit identities may have changed.
