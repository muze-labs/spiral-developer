---
id: EVD-BROWNFIELD-002
---

# Verification Evidence: Guided brownfield project intake

## What is being verified

Adoption of `LES-011`: initial Spiral adoption in an existing project should begin with a lightweight guided project intake that establishes a human-confirmed project frame, selects relevant risk-discovery/metric lenses, compares that frame with current project reality, and returns candidate risks/gaps to the human for prioritization before the first normal cycle.

Implementation commit under verification: `dcf0598f6b8aa05e636fa3b400a356d9ff1b6b30`.

## Mechanical / structural checks

- `docs/brownfield-intake.md` defines the intake purpose, when it is required, conversational question areas, risk-discovery/metric profile semantics, reality assessment, human prioritization, progressive teaching, and explicit limits against premature formalization.
- `prompts/brownfield-intake.md` gives the AI a runnable conversational setup prompt, including common-choice suggestions with `Other / Not sure / Not relevant`, human confirmation before assessment, evidence-grounded reality comparison, and human risk disposition.
- `templates/PROJECT_CONTEXT.md` can preserve goals/metrics, project posture, consequential prior decisions/reversibility, selected/excluded intake profiles, known/tolerated risks, feedback sources, and areas needing human guidance without introducing a new artifact class.
- `AGENTS.md`, `docs/process.md`, `docs/brownfield.md`, `docs/quickstart.md`, `CONTRIBUTING.md`, and repository/bootstrap/change prompts route initial or materially stale brownfield projects through intake before the next normal cycle.
- Starter Markdown profiles exist for general brownfield risk discovery, user-facing interaction risk discovery, exploratory-product metrics, and established-service metrics. Their text explicitly says they are prompts rather than requirements/findings/scorecards.
- The process distinguishes risk-discovery profiles from warning profiles and does not silently activate all available profiles.
- The process keeps final project priority with the human and explicitly permits rejecting/removing, accepting, deferring, reprioritizing, or adding candidate risks.
- No intake ontology class, maturity score, project-health score, rigid schema, or mandatory machine-readable profile format was introduced.
- All Turtle resources parse with the installed standards-conforming RDF parser.
- All current durable exact Git references resolve to strict ancestors of the artifact versions containing them.
- `git diff --check` reports no whitespace errors; `git fsck --no-reflogs` reports no structural corruption (dangling blobs are ordinary unreachable Git residue).

## What this verification does not establish

Static inspection does not show that the intake conversation is short enough, that the suggested choices are useful across real projects, that agents will ask the right follow-up questions, that humans will understand the explanations, or that the first starter profiles are the right reusable decomposition.

Those are deliberately left to dogfooding. In particular, the fixed question set/profile taxonomy should be treated as provisional until repeated real intakes show which distinctions actually improve project orientation and risk selection.

## Result

The repository now contains a first lightweight brownfield-intake path that can be used without prior Spiral expertise, while preserving human authority over project meaning and priority and keeping the reusable profile layer intentionally informal.
