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
spiral/CYC-20260818-K7M4-12-account-deactivation
spiral/CYC-20260819-N3Q8P-4-expiry-race
```

The cycle branch is the normal integration/review boundary. It may contain multiple requests, design/implementation steps, investigations, and semantic commits that all serve the same coherent cycle goal. Internal tasks do not normally receive separate branches or pull requests.

### Validate the active cycle branch

Branch naming is a process invariant that must be **checked against Git state**, not remembered from conversation. When a repository-changing cycle opens:

1. read the active `CYC-*` identity;
2. inspect the actual branch (`git branch --show-current` or equivalent);
3. verify that the branch is `spiral/<active-cycle-id>-...`;
4. record the branch/check in the cycle record;
5. repeat the check before each semantic causal commit and during cycle evaluation.

If the current branch still names an older cycle, stop repository-changing work and switch/create the correct branch before continuing. Do not rename/rewrite a branch in a way that rewrites already-published causal commits; preserve history and use a corrective branch/merge strategy appropriate to the actual repository state. Explicitly document rare cases where no dedicated cycle branch is appropriate.

Repository-local tooling may automate this check, but lack of a helper script does not waive it.

A non-code investigation/evaluation cycle may not need a development branch. Cross-repository or irreversible operational work may need a different integration boundary; follow the trust model instead of forcing this convention.

The branch contains an evolving proposed reality. The authoritative branch remains accepted project reality.

An Active cycle branch is therefore **not** an integration source for the authoritative branch or another Active cycle branch. Finish evaluation and record human acceptance (`sd:Accepted`) before proposing it for integration. The reverse direction is allowed: accepted authoritative work may be merged into an Active cycle so the open cycle can reconcile against the latest accepted reality.


## Distributed allocation

Do not allocate new Spiral artifact/cycle identities by scanning the authoritative branch for the highest sequence. Concurrent branches can observe the same state and allocate the same next value.

Use the worktree-local allocator described in `distributed-development.md`. New IDs use `TYPE-YYYYMMDD-WORKSPACE-N`; historical sequential IDs remain valid. The allocator state lives outside the committed tree, so unrelated workspaces do not create bookkeeping merge conflicts merely by creating new artifacts.

Ordinary source conflicts remain ordinary Git conflicts. Distributed causal consistency is revalidated at the integration boundary rather than prevented by locking writers during development.

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

Spiral-Artifact: IMP-20260818-K7M4-18
Spiral-Design: DES-20260818-K7M4-17@2bc31aa
Spiral-Request: REQ-20260818-K7M4-14@1a2f9e1
```

Trailers are human/navigation summaries. The companion Turtle resources remain authoritative for machine-readable causal links and store full hashes. Do not require humans to maintain these trailers manually when the AI can do it.

### Commit attribution

An agent's work is credited with a `Co-Authored-By` trailer. The human remains the author and the committer.

```text
Co-Authored-By: <Model Name> <ai+<model-slug>@muze.nl>
```

**MUST NOT** place an agent in the author or committer field. Git binds a signature to the committer, so an agent in that position gains nothing the trailer does not already give, and forfeits the verified attribution the human's signed commit provides. The commit stays signed and attributable to a verified account; the trailer records the agent alongside it.

#### Deriving the model identity

- `<Model Name>` is the model's published display name, used however the catalogue renders it. Many catalogues prefix `Vendor: ` and many deliberately omit it. Follow the catalogue for the model in hand rather than imposing a form.
- `<model-slug>` is the model part of a catalogue identifier: after the vendor namespace, before any `:variant` suffix. For example `somevendor/space-bunny-alpha` yields `space-bunny-alpha`. The namespace is dropped because it is routing metadata rather than part of the model's name, and because it is redundant: no catalogue slug is shared by two vendors.
- Identify the model from what the agent's own tooling reports for the session, rather than by assumption. How to obtain that is tool-specific and is deliberately not specified here.

#### Why not the vendor's own address

A model's own vendor no-reply address is never used, however publicly it is documented. It asserts a vendor relationship in permanent history, on an address we neither control nor can have verified, and which the vendor may change or retire. The address belongs to whoever did the work.

#### Why the address is subaddressed

`ai+<model-slug>@muze.nl` is subaddressed deliberately, so that creating `ai@muze.nl` as a catch-all later requires no change to any existing history.

#### Relationship to the navigation trailers

`Co-Authored-By` is attribution, not navigation. It is not a Spiral causal reference, carries no `sd:` meaning, and does not participate in the single-authoritative-graph rule. The `Spiral-*` trailers above remain the navigation summaries. Both may appear in the same commit without merging their purposes.

#### `:variant` suffixes

**Collapse the variant and credit the base model.** A `:variant` suffix does not enter the slug: `somevendor/space-bunny-alpha:high` yields `space-bunny-alpha`.

The variants that exist are serving modes rather than different models. They keep the same weights and the same context length while differing in price and turnaround. Anything that genuinely changes model identity is already a separate catalogue entry, and is therefore credited separately by construction.

A co-author line records which model wrote the code, not how it was served.

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

If the authoritative branch moves while cycle work continues, merge it into the cycle branch rather than rebasing. When governed artifacts may have changed on both histories, prefer:

```text
git merge --no-commit main
```

(or the project's authoritative branch), then inspect the combined change **before creating the merge commit**.

Resolve ordinary source conflicts on the cycle branch. If both parent histories materially revised the same stable governed artifact, the merge commit is an explicit convergence version: reconcile effective provenance deliberately and add `sd:transforms` references to the latest predecessor version from **both** parent lineages. A clean auto-merge is not sufficient evidence that two independently evolved meanings were reconciled.

Then create/preserve the merge commit. Do not create a semantic merge and plan to amend it later, and do not rebase the cycle branch onto the new authoritative tip once causal commits exist. See `distributed-development.md`.

## Pull request

When the AI believes the cycle goal can be judged, it enters cycle evaluation. For repository changes, the pull request can carry that integrated evaluation; human feedback there may keep the same cycle branch open for correction. Do not require a separate review before the PR merely to mark the phase transition.

The PR is evaluated by:

- CI/CD and other automated checks;
- human review of intent, design, evidence, risk, and result.

Cycle acceptance means the branch is ready to propose for integration; it does not freeze the target branch. An Active cycle must not be merged. Immediately before merge, revalidate the actual combined state with `spiral validate integration --base <current-target> --head <candidate> --base-branch <target-name> --head-branch <cycle-branch-name>` when branch names are available, or validate the hosting platform's exact prospective merged/queued commit. If the target changes after a prior check, the old result is stale and must not authorize the merge. See `distributed-development.md`.

See `review.md`.

## Merge-only integration

Accepted work is integrated with a normal merge commit.

Configure repository hosting, where practical, to:

- require pull/merge requests for the authoritative branch;
- disallow force pushes;
- require CI checks including Spiral prospective integration validation;
- use a merge queue/train or equivalent serialization mechanism when multiple accepted changes can race to integrate, if the hosting platform provides one;
- disable squash merge for Spiral Developer work;
- disable rebase merge for Spiral Developer work;
- permit/require merge commits.

The merge commit means:

> **The cycle outcome and its causal history were reviewed as a unit and admitted into authoritative project history.**

## Git hashes as versions

Stable artifact identity and artifact version are different things:

```text
REQ-20260818-K7M4-14                 stable identity
REQ-20260818-K7M4-14@a12f9e1         human shorthand for a historical version
```

The Turtle graph stores full hashes, not abbreviations.

Do not store an artifact's own commit hash inside the commit that creates it; that is impossible because the commit hash depends on the commit contents. Only downstream artifacts need to record the already-existing upstream hash.


## Governed artifact convergence and `sd:transforms`

`sd:transforms` is a general historical predecessor-version relation on governed artifacts. Most artifact edits do not need a transform edge merely because text changed, but one case is mechanically important in distributed work: when a merge combines parent histories that both materially revised the same stable artifact, the merge version must preserve both immediate predecessor versions with `sd:transforms`. This prevents Git conflict resolution or clean auto-merge from silently erasing one lineage.

Implementation artifacts additionally use the same relation for normal implementation lineage, with implementation-specific transition metadata described below.

## Implementation lineage and Git ancestry

Implementation lineage depends on Git being an immutable historical store. When a governed `IMP-*` is materially revised, the new version can refer backward to the already-known predecessor commit with `sd:transforms`. The current commit still does not need to know its own hash.

A lineage reference should normally resolve to an implementation version that is an ancestor of the current revision commit. Split/merge/replacement cases may reference multiple predecessor `IMP-*` identities, but they still point backward to exact historical versions.

Version-aware validation therefore applies the same historical-reference invariant used by causal provenance: the target version must already exist and, once persisted, its commit must be a strict Git ancestor of the source implementation version. `sd:transforms` and `sd:changeCausedBy` share historical-integrity rules with causal references without becoming current causal justification.

Validate this before commit where possible, over the introduced commit range in CI, and through an explicit history audit when required. Snapshot-only validation cannot prove that an invalid historical edge was never introduced and later removed.

These checks establish historical integrity, not semantic correctness. A behavior-preserving refactor still needs behavioral evidence when preservation matters. See `causal-validation.md`.

## Exceptional destructive rewrites

Normal development must never rewrite causal history.

If an exceptional legal or security incident requires repository-level history rewriting (for example, purging an accidentally committed secret), treat it as a provenance incident rather than normal cleanup. Rotate/revoke affected credentials immediately, document the rewrite, and revalidate causal references because commit identities may have changed.
