# Redesign Notes: Spiral Assistant → Spiral Developer

This document records which ideas from the original Spiral Assistant survived the AI-native redesign. The old repository is historical evidence, not specification.

## Retained

- `Analyze → Plan → Act → Evaluate` as a useful spiral rhythm.
- Frontend-first development, sharpened around meaningful intended-user interaction.
- Risk-driven development, sharpened around blocker / near-term / deferred / existential horizons.
- Complexity, abstraction, boundaries, replaceability, and simplicity as economic properties.
- Evidence before hardening a design.
- Separation of facts from assumptions.

## Adapted

### “View intent”

Expanded into a versioned causal graph of intent, design, implementation, verification, and acceptance.

### Human legibility

Replaced by **causal auditability**. Humans do not need to read every generated line; the software-producing system must be inspectable and interrogable.

### AI containment

Replaced by bounded authority based on causal confidence, risk, reversibility, evidence, and the feature-branch / PR governance boundary.

### Roadmap

Later possibilities remain useful context, but must not become speculative current design. The next evidence-producing cycle is the unit of action.

### Boundary and abstraction reviews

Retained as useful techniques, not mandatory parallel status documents.

## Removed or demoted

### Fixed maturity ladder and spider scoring

Removed from the core process. Quality must be sufficient and earned properties must not silently regress, but generic scoring risks metric theater.

### Eight mandatory Muze documents

Removed. Create only artifacts that serve the current causal chain.

### AI as coach/reviewer only

Removed. AI may perform substantial design and implementation work.

### Mandatory human understanding of generated code

Removed. Causal auditability and maintainability matter more than universal line-by-line comprehension.

### Generated-code provenance as a special category

Demoted. Generated code is normal; provenance focuses on why artifacts exist, which exact upstream versions caused them, and what evidence supports them.

### Numeric artifact revisions

Removed in favor of Git commit hashes. Stable IDs identify artifacts; Git identifies versions.

## Added after the first redesign

### Feature-branch ownership

AI normally operates a feature branch from request through pull request.

### Git history as evidence

Causal commits are immutable. Normal integration is merge-only; no squash/rebase history rewriting.

### Turtle causal graph

Causal relationships are stored canonically as RDF/Turtle so ordinary linked-data tooling can inspect and query them independently of AI.

### Inquiry/execution and framing resistance

Added after extended AI collaboration exposed a recurring failure mode: a capable agent can make a user's first plausible framing increasingly coherent without testing whether the framing itself is correct. Spiral Developer now distinguishes inquiry from execution, treats consequential prompts as proposed frames, uses lightweight framing resistance at important branching points, and explicitly states that capability is not endorsement. It also adds scale resistance and upstream reframing to the defect/evaluation loop.
