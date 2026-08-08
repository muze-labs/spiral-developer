# Spiral Developer

Spiral Developer is an AI-native software-development process for Muze projects.

It assumes AI can perform substantial design and implementation work. Human control comes from making intent, constraints, decisions, evidence, provenance, and acceptance explicit enough that the software-producing system can be inspected, challenged, and corrected.

The central causal chain is:

> **intent → request → design → implementation → verification → acceptance**

The links are first-class. When something changes or fails, Spiral Developer should be able to traverse the chain, identify the earliest outdated or inadequate assumption, correct it, and propagate the consequence forward.

## Working model

- Start each feature or meaningful change on its own working branch.
- Let the AI operate the branch and create semantic commits as the work crystallizes.
- Treat Git history as evidence: causal commits are immutable and are never rebased, squashed, amended, or force-pushed away.
- Store human-facing intent, design, observations, and evidence as small version-controlled artifacts.
- Store the machine-readable causal graph in Turtle so ordinary RDF tooling can inspect and query it without an AI.
- Use Git commit hashes as artifact versions. Stable artifact IDs identify the thing; the commit identifies the historical version.
- Get meaningful feedback from intended users as early as possible. For Muze web work this usually means frontend-first development.
- Resolve the nearest important uncertainty and deliberately defer later risks unless they are existential.
- Once the interaction model is credible, implement reality in vertical slices.
- When a defect occurs, repair the software-producing environment at the earliest meaningful cause rather than merely patching generated output.
- Integrate completed work through a pull request evaluated by automated checks and human review.

## Who should read what

**New project experiment:** start with [`docs/quickstart.md`](docs/quickstart.md).

**AI collaborators:** start with [`AGENTS.md`](AGENTS.md).

**Human collaborators:** start with [`CONTRIBUTING.md`](CONTRIBUTING.md).

**Canonical process and semantics:**

- [`docs/vision.md`](docs/vision.md) — why this process exists.
- [`docs/process.md`](docs/process.md) — the normative development lifecycle.
- [`docs/artifact-model.md`](docs/artifact-model.md) — what is recorded and what the causal relations mean.
- [`docs/git-workflow.md`](docs/git-workflow.md) — feature branches, immutable commits, PRs, and merge-only history.
- [`docs/rdf-graph.md`](docs/rdf-graph.md) — Turtle representation of the causal graph.
- [`docs/brownfield.md`](docs/brownfield.md) — how to introduce the process into existing projects.
- [`docs/review.md`](docs/review.md) — automated and human review at the pull-request boundary.

Muze's organization-wide engineering principles remain an important culture source:

`https://github.com/muze-nl/.github/blob/main/maturity-policy.md`

## Repository structure

```text
spiral-developer/
  README.md
  AGENTS.md
  CONTRIBUTING.md
  docs/
    quickstart.md
    vision.md
    process.md
    artifact-model.md
    git-workflow.md
    rdf-graph.md
    brownfield.md
    review.md
    redesign-notes.md
  ontology/
    spiral-developer.ttl
    spiral-developer-shapes.ttl
  examples/
    causal-graph.ttl
  templates/
    ...
  catalogs/
    ...
  prompts/
    ...
```

A consuming project will normally grow a `.spiral/` area containing human artifacts and companion Turtle resources whose RDF union forms the causal graph. See [`docs/process.md`](docs/process.md) and [`docs/rdf-graph.md`](docs/rdf-graph.md).

## Status

This is deliberately a **document-first experimental process**, not a finished harness.

Use it with a capable coding agent on real work. Keep what repeatedly improves decisions, context, traceability, review, and verification. Remove ceremonial bookkeeping. Build automation only after the working process demonstrates which constraints and relationships are worth enforcing.
