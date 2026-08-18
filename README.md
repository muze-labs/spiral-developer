# Spiral Developer

Spiral Developer is an AI-native software-development process built around **trust but verify**.

It assumes AI can perform substantial design and implementation work with more autonomy than conventional human-supervised coding workflows. That autonomy is justified by a verification architecture that makes intent, constraints, decisions, evidence, provenance, and acceptance explicit enough for the software-producing system to be inspected, challenged, rejected, and corrected. Permission to act is not an assumption of correctness.

The extended causal chain is:

> **source evidence → understanding → request → design → implementation → verification → acceptance**

Across repeated implementation changes, Spiral also preserves **implementation lineage**: the current effective reasons remain compact while exact predecessor versions and transition causes remain traversable through Git.

Source and understanding are crystallized when origin or interpretation is materially useful; a simple direct request may still be the first durable artifact. The links are first-class. When something changes or fails, Spiral Developer should be able to traverse the chain, identify the earliest outdated or inadequate assumption, correct it, and propagate the consequence forward.

## Working model

- Give the agent broad autonomy for contained/reversible work because consequential claims are independently verifiable; move verification before actions whose consequences would be unacceptable before review.
- Agree one coherent cycle goal before consequential execution; size cycles by uncertainty/evaluation coherence rather than defaulting to tiny cycles; for repository-changing work, normally use one cycle branch as the integration/review boundary and mechanically verify that the active branch matches the active cycle.
- Let the AI decompose the cycle into tasks and create multiple semantic commits without making every subtask a separate branch or human review boundary.
- Treat Git history as evidence: causal commits are immutable and are never rebased, squashed, amended, or force-pushed away.
- Prevent malformed versioned provenance before it enters immutable history: validate staged historical references against current Git ancestry, then validate introduced commit ranges in CI.
- Treat consequential human input as discourse until meaning is sufficiently settled: a human utterance may be a hypothesis or tentative solution rather than an instruction. Require the agent to surface material assumptions/alternative framings before commitment, then execute decisively from the committed frame and return to discourse if new evidence falsifies it.
- Store human-facing sources, interpreted understanding, intent, design, observations, and evidence as small version-controlled artifacts when they are causally useful.
- Treat requests as derived claims about intent, not unquestioned roots: preserve source and interpretation provenance when it matters, and make unavailable origins explicit rather than inventing them.
- Store the machine-readable causal graph in Turtle so ordinary RDF tooling can inspect and query it without an AI.
- Use Git commit hashes as artifact versions. Stable artifact IDs identify the thing; the commit identifies the historical version. New artifacts use distributed-safe `TYPE-YYYYMMDD-WORKSPACE-N` identities allocated per Git worktree; legacy sequential IDs remain valid.
- Distinguish current/effective implementation provenance from historical lineage. A materially revised governed `IMP-*` points to its immediate predecessor and transition cause without forcing future agents to replay the full history.
- Make active engineering culture explicit when it materially shapes an underdetermined design/implementation choice; do not confuse preference with requirement.
- Make adopted warning profiles explicit and versioned; use them to surface consequential patterns for inspection without silently turning them into universal rules or culture.
- Record reusable `LES-*` lessons and allow evidence to change project practice, culture, or Spiral core prospectively rather than silently changing the process.
- Obtain meaningful evidence before consequential commitments harden. The active culture profile may recommend a particular strategy, such as Muze's frontend-first approach for interactive web work.
- For brownfield adoption, begin with a guided project intake with explicit `Incomplete/Complete/Stale` state. Every required topic must be dispositioned; while incomplete, keep the remaining topics visible rather than silently moving on. Then compare the confirmed frame with reality and let the human prioritize the resulting candidate risks.
- Prefer cheap tests of uncertain assumptions whose failure would invalidate substantial downstream work; spend less de-risking effort on local reversible implementation choices, and keep durable risk horizons only where useful.
- When a durable multi-cycle plan/roadmap exists, re-read it before selecting the next cycle and explicitly continue, revise, or deliberately deviate from it; do not let the latest discovery silently become the roadmap.
- Before consequential commitments, treat the question as a proposed frame: surface hidden assumptions when a materially different framing could change what should be built.
- Distinguish **capability from endorsement**: a coherent AI-generated plan proves buildability, not that the direction is right.
- Once the relevant uncertainty has been reduced, implement the smallest observable slice that can be verified and accepted; active culture may shape the preferred slicing strategy.
- When a defect occurs, repair the software-producing environment at the earliest meaningful cause rather than merely patching generated output.
- Work inside an explicit human-confirmed cycle goal; evaluate the integrated result before selecting new direction, then merge accepted cycle history through a normal pull request/review boundary that revalidates the actual prospective combined state against the current target.

## Who should read what

**New project experiment:** start with [`docs/quickstart.md`](docs/quickstart.md).

**AI collaborators:** start with [`AGENTS.md`](AGENTS.md).

**Human collaborators:** start with [`CONTRIBUTING.md`](CONTRIBUTING.md).

**Canonical process and semantics:**

- [`docs/vision.md`](docs/vision.md) — why this process exists.
- [`docs/trust-model.md`](docs/trust-model.md) — trust-but-verify, agent autonomy, and when verification must become a pre-action gate.
- [`docs/process.md`](docs/process.md) — the normative development lifecycle.
- [`docs/cycles.md`](docs/cycles.md) — the outer Analyze/Plan/Act/Evaluate cadence, scope stability, and cycle review boundary.
- [`docs/ai-collaboration.md`](docs/ai-collaboration.md) — discourse → commitment → execution, framing resistance, and upstream correction.
- [`docs/artifact-model.md`](docs/artifact-model.md) — what is recorded and what the causal relations mean.
- [`docs/git-workflow.md`](docs/git-workflow.md) — cycle branches, immutable commits, PRs, and merge-only history.
- [`docs/distributed-development.md`](docs/distributed-development.md) — worktree-local artifact allocation and distributed integration boundaries.
- [`docs/causal-validation.md`](docs/causal-validation.md) — pre-commit prevention, strict Git-ancestry invariants, range validation, and history audits.
- [`docs/rdf-graph.md`](docs/rdf-graph.md) — Turtle representation of the causal graph.
- [`docs/implementation-lineage.md`](docs/implementation-lineage.md) — effective provenance, implementation history, and bounded agent context across repeated changes.
- [`docs/culture.md`](docs/culture.md) — explicit, versioned, defeasible engineering culture as causal influence.
- [`docs/warning-profiles.md`](docs/warning-profiles.md) — replaceable warning lenses, significance gates, and risk/disposition semantics.
- [`docs/process-evolution.md`](docs/process-evolution.md) — first-class lessons, scope/promotion, and changing the process without falsifying its past.
- [`docs/brownfield.md`](docs/brownfield.md) — how to introduce the process into existing projects.
- [`docs/brownfield-intake.md`](docs/brownfield-intake.md) — guided brownfield setup, profile selection, reality assessment, and human risk prioritization.
- [`docs/review.md`](docs/review.md) — automated and human review at the pull-request boundary.

Spiral core is intentionally separated from organization-specific engineering preferences and from optional warning lenses. The repository ships a first explicit Muze culture profile at [`cultures/muze-engineering.md`](cultures/muze-engineering.md) and a replaceable warning profile at [`warning-profiles/human-impact-and-epistemic.md`](warning-profiles/human-impact-and-epistemic.md); projects may adopt, extend, replace, or decline either independently.

## Repository structure

```text
spiral-developer/
  README.md
  AGENTS.md
  CONTRIBUTING.md
  docs/
    quickstart.md
    vision.md
    trust-model.md
    process.md
    ai-collaboration.md
    artifact-model.md
    git-workflow.md
    causal-validation.md
    rdf-graph.md
    implementation-lineage.md
    culture.md
    warning-profiles.md
    process-evolution.md
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
  cultures/
    ...
  warning-profiles/
    ...
  profiles/
    risk-discovery/
    metrics/
  lessons/
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
