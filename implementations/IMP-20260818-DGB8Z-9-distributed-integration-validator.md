---
id: IMP-20260818-DGB8Z-9
---

# Implementation: Distributed integration validator

## Scope

Repository-local validation for current Spiral graph coherence and for the exact prospective state formed by combining a current integration target with a candidate branch.

## Observable behavior

- `spiral validate` validates the checked-out Turtle snapshot.
- `spiral validate integration --base <target> --head <candidate>` asks Git to construct the prospective merge tree and validates that tree without rewriting or checking out either branch.
- ordinary Git merge conflicts stop prospective validation and remain ordinary Git conflicts;
- duplicate artifact definitions/identifiers and duplicate distributed `(WORKSPACE, sequence)` allocation slots fail validation;
- a live (`Active`/`Accepted`) artifact may not retain a current/effective causal dependency on an exact version superseded by another live artifact;
- a live artifact may not depend on an upstream artifact currently marked `Suspect`, `Superseded`, or `Rejected`;
- a rejected/tentative superseder does not itself retire an otherwise effective upstream version;
- malformed Turtle fails through a standards-conforming RDF parser;
- GitHub/GitLab/plain-Git guidance remains a thin adapter around the same repository-local validation semantics;
- brownfield intake now records the authoritative integration target and pre-merge validation boundary.

## Repository locations

| Path / symbol | Role |
|---|---|
| `bin/spiral.mjs` | CLI orchestration, snapshot validation, and prospective merge-tree construction. |
| `bin/spiral-rdf.py` | Narrow RDF/Turtle snapshot validator using `rdflib`. |
| `requirements.txt` | Declares the first dogfood RDF parser dependency. |
| `test/spiral-integration.test.mjs` | Distributed causal-staleness, collision, conflict, and parser probes. |
| `docs/distributed-development.md` | Normative distributed integration model and host-adapter guidance. |
| `docs/git-workflow.md`, `docs/review.md`, `docs/quickstart.md`, `AGENTS.md` | Pre-merge revalidation process guidance. |
| `docs/brownfield-intake.md`, `prompts/brownfield-intake.md`, `templates/PROJECT_CONTEXT.md` | Intake integration-context requirement. |
| `examples/ci/github-spiral-integration.yml` | Thin GitHub Actions adapter example. |
| `examples/ci/gitlab-spiral-integration.yml` | Thin GitLab CI adapter example. |

## Effective provenance

Implements the current `DES-20260818-DGB8Z-8` design version, including its clarification that only live/effective superseders retire an exact upstream version.

## Important implementation decisions

The Node CLI uses `git merge-tree --write-tree` to obtain a prospective merge tree without modifying branch history. The RDF layer is intentionally kept behind a small process/JSON boundary so using Python `rdflib` in this first dogfood slice does not make Python part of Spiral's normative model.

The causal-relation set is derived from the repository ontology via transitive `rdfs:subPropertyOf sd:causalReference`, with `sd:supersedes` excluded from downstream dependency checking. This avoids hard-coding a second causal vocabulary in the validator while preserving the distinction between effective provenance and implementation-history relations.

The host examples distinguish platforms that supply an exact prospective merged/queued commit from ordinary branch-only pipelines. In either case, the adapter invokes Spiral's repository-local semantics rather than reproducing them.

## New dependencies / capabilities / permissions

The first integration-validation slice adds Python 3 plus `rdflib>=7,<8` as a local validation dependency. It adds no network capability and no repository write capability during validation. Git remains responsible for merge computation.

## Known limits

- This validates current/prospective graph coherence, not every historical commit/range invariant described in `docs/causal-validation.md`.
- The Python + Node two-runtime packaging is provisional dogfood infrastructure.
- Hosting examples are templates; projects must adapt runtime installation, protected-branch configuration, and required-check settings to their environment.
- The validator deliberately does not decide whether a superseding artifact is substantively correct or whether evidence is convincing.
