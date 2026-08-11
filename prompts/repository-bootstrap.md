# Repository Bootstrap Prompt

Use Spiral Developer as the governing process for this repository.

Read, in order:

1. `AGENTS.md`
2. `docs/vision.md`
3. `docs/process.md`
4. `docs/artifact-model.md`
5. `docs/git-workflow.md`
6. `docs/rdf-graph.md`
7. `docs/brownfield.md`
8. project-specific culture/context already present

Then inspect the repository only far enough to support the next real piece of work. In a brownfield repository, explicitly assume that early project-specific understanding is partial. Build affinity with the relevant area before making strong claims, and expect/ask for human guidance where local conventions or hidden cross-cutting behavior are not yet understood.

Do **not** attempt to reconstruct complete project history or manufacture a formal affinity model.

If `.spiral/` does not exist, propose/create only the minimal working structure: project context, explicitly adopted/local culture only when it will shape decisions, `.spiral/project.ttl` with a stable project namespace, and companion Turtle resources only as artifacts are introduced. Add `SRC-*` and `UND-*` artifacts only when origin or interpretation is materially useful; do not pre-create empty source/understanding inventories.

Produce:

- concise project context if missing;
- relevant culture sources/constraints;
- known opaque vs characterized areas relevant to current work;
- the best available source/understanding for current intent when material;
- a proposal for the first bounded request to bring under Spiral Developer, after confirming consequential direct human intent and checking whether the capability already exists or overlaps current repository behavior.

Separate explicit/evidenced/inferred/unknown legacy knowledge.

Do not create a large inventory merely because the repository is large.
