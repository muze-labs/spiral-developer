# Redesign Notes: Spiral Assistant → Spiral Developer

This document records which ideas from the original Spiral Assistant survived the new AI-native vision. It exists to prevent accidental reintroduction of old assumptions simply because they were already written down.

The old repository is historical evidence, not specification.

## Retained

### Spiral cycles

`Analyze → Plan → Act → Evaluate` remains a useful rhythm.

It is now a container for causal/evidence-producing work rather than a status-document workflow.

### Frontend-first development

Retained and sharpened.

The primary goal of the early frontend is meaningful interaction by the intended audience. Working feature behavior comes before general usability polish and look-and-feel unless polish is necessary for meaningful interaction.

### Risk-driven development

Retained and sharpened around time horizon: blocker, near-term, deferred, existential.

Later-cycle risk should not drive current design unless existential.

### Complexity, abstraction, boundaries, replaceability

Retained strongly. AI makes code cheap and therefore makes restraint more important.

### Evidence before hardening

Retained. Evidence is now linked explicitly to the design/request claims it supports.

### Facts vs assumptions

Retained and extended with brownfield provenance classes: explicit, evidenced, inferred, unknown.

## Adapted

### “View intent”

The old AI-era document anticipated that code might cease to be the main durable artifact. This is now expanded into a versioned causal graph of intent, design, implementation, verification, and acceptance.

### Human legibility

Replaced by **causal auditability**.

Humans do not need to read or understand every generated line. They must be able to inspect and interrogate the production system, understand why important artifacts exist, and trace failures to an upstream cause.

### AI containment

Replaced by **bounded authority based on causal confidence, reversibility, risk, and evidence**.

AI may design and implement extensively in a well-governed area. Opaque legacy areas require more investigation and human judgment.

### Roadmap

The old roadmap remains useful as project context, but later possibilities must not become speculative current design. The primary unit of action is the next evidence-producing cycle.

### Boundary and abstraction reviews

The concepts remain valuable, but they are no longer mandatory standalone status documents. Use them when a current risk/design decision needs them.

## Removed or demoted

### Fixed maturity ladder and spider scoring

Removed from the core process.

The useful principle remains: quality must be sufficient for the current use and already-earned properties should not silently regress. Fixed 1–5 scoring across many dimensions risks becoming metric theater and competes with the more direct causal/evidence model.

### Eight mandatory Muze documents

Removed.

Create only artifacts that serve the current causal chain. The old document set encouraged parallel sources of truth and manual consistency work.

### AI as coach/reviewer only

Removed.

Spiral Developer assumes AI can perform substantial design and implementation work. Human control comes from explicit intent, constraints, meaningful feedback, evidence, acceptance, and auditability—not from forcing AI to remain advisory.

### Mandatory human understanding of generated code

Removed.

Code may be generated and never read line-by-line. The process must still be causally auditable and economically maintainable.

### Generated-code provenance as a special category

Demoted.

In an AI-native process, generated code is normal. Provenance should focus on why an artifact exists, what produced/accepted it, which versions it depends on, and what evidence supports it.

### Assistant maturity levels

Removed.

The repository itself should evolve based on real development evidence rather than an a priori ladder from prompt assistant to semi-agent.
