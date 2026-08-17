# Repository Bootstrap Prompt

Use Spiral Developer as the governing process for this repository.

Read, in order:

1. `AGENTS.md`
2. `docs/vision.md`
3. `docs/process.md`
4. `docs/cycles.md`
5. `docs/artifact-model.md`
6. `docs/git-workflow.md`
7. `docs/rdf-graph.md`
8. `docs/brownfield.md`
9. `docs/brownfield-intake.md`
10. project-specific culture/context already present

If this is an existing project and durable project-level context is missing, `Incomplete`, or materially `Stale`, **run/resume `prompts/brownfield-intake.md` before planning the next normal cycle**. Persist the intake status/checklist and keep remaining topics visible in every user-visible response while intake remains active until all are explicitly dispositioned and human-confirmed. Do not require the human to read the process first. Persist confirmed durable conclusions in project context, then compare them with current evidence and ask the human to prioritize the resulting candidate risks/gaps.

Then inspect the repository only far enough to support planning the next real cycle. In a brownfield repository, explicitly assume that early project-specific understanding is partial. Build affinity with the relevant area before making strong claims, and expect/ask for human guidance where local conventions or hidden cross-cutting behavior are not yet understood.

Do **not** attempt to reconstruct complete project history or manufacture a formal affinity model.

If `.spiral/` does not exist, propose/create only the minimal working structure: project context, explicitly adopted/local culture only when it will shape decisions, `.spiral/project.ttl` with a stable project namespace, and companion Turtle resources only as artifacts are introduced. Add `SRC-*` and `UND-*` artifacts only when origin or interpretation is materially useful; do not pre-create empty source/understanding inventories.

Produce:

- concise project context if missing;
- relevant culture sources/constraints;
- known opaque vs characterized areas relevant to current work;
- the best available source/understanding for current intent when material;
- when intake was required: a human-confirmed project frame, selected/excluded risk-discovery and metric profiles, and an evidence-grounded candidate risk/metric-gap picture with human disposition;
- a proposal for the first coherent cycle goal, with why-now, evaluation basis, likely work, non-goals, and pause/re-plan conditions; use the normal Understanding/evidenced-gap checkpoint where consequential direct human intent is part of that goal.

Separate explicit/evidenced/inferred/unknown legacy knowledge.

Do not create a large inventory merely because the repository is large.
