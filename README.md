# Spiral Developer

Spiral Developer is an AI-native development process for Muze projects.

It assumes AI can do substantial implementation work. Human control comes from making intent, constraints, design, evidence, provenance, and acceptance explicit enough that the software-producing system can be inspected, challenged, and corrected.

The central development chain is:

> **intent → request → design → implementation → verification → acceptance**

The links are first-class. When something fails or changes, Spiral Developer should be able to traverse the chain, find the earliest faulty or outdated assumption, fix that upstream cause, and propagate the correction forward.

## Core principles

- Seek meaningful feedback from the intended audience as early as possible.
- For web work, use **frontend-first** development: build enough working behavior for real interaction before polishing usability or look-and-feel.
- Resolve the uncertainty most likely to block useful progress next. Record later risks; pull them forward only when they are existential.
- After the interaction model is credible, implement reality in vertical slices.
- Preserve causal links from each significant artifact back to the intent that justifies it.
- Treat technical plumbing as explicit supporting work, not invented client intent.
- Version artifacts and references so later changes do not rewrite history.
- Fix the software-producing environment before patching generated output when a defect exposes a missing constraint, context item, design rule, or evaluator.
- Optimize for simplicity, maintainability, replaceability, and causal auditability.
- In legacy projects, preserve causality accurately from now on and reconstruct old context only when active work needs it.

Muze's organization-wide design principles remain an important culture source. The canonical policy currently lives at:

`https://github.com/muze-nl/.github/blob/main/maturity-policy.md`

## Repository structure

```text
spiral-developer/
  README.md
  AGENTS.md
  docs/
    00-quickstart.md
    01-vision.md
    02-brownfield-adoption.md
    03-development-loop.md
    04-causal-artifact-model.md
    05-redesign-notes.md
  templates/
    CULTURE.md
    PROJECT_CONTEXT.md
    REQUEST.md
    FEEDBACK.md
    DESIGN.md
    EVIDENCE.md
    ACCEPTANCE.md
    LEGACY_CONTEXT.md
    DEFECT.md
    CYCLE.md
  catalogs/
    risks.md
    complexity-and-boundaries.md
    evidence.md
  prompts/
    repository-bootstrap.md
    start-change.md
    brownfield-change.md
    evaluate-cycle.md
    defect-analysis.md
```

## Status

This is deliberately a **document-first experimental process**, not a finished harness.

Use the templates manually with a capable coding agent on real work. Keep what repeatedly improves decisions, context, traceability, and verification. Remove bookkeeping that becomes ceremonial. Build automation only after the manual process demonstrates which relationships actually matter.

Start with [`docs/00-quickstart.md`](docs/00-quickstart.md).
