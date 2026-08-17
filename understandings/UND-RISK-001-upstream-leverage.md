---
id: UND-RISK-001
---

# Understanding: Prioritize risk by uncertainty and downstream leverage

## Interpretation

Spiral Developer already has extensive risk-discovery material and a durable `RSK-*` mechanism, but its live guidance does not yet make clear **how to prioritize among risks without turning risk work into ceremony**.

The intended model is lightweight and cycle-oriented:

- treat risk primarily as an important **assumption or uncertainty** whose being wrong could materially obstruct the project goal or make later correction substantially more expensive;
- reason about its position in the causal/development chain because earlier assumptions normally have a larger downstream dependency surface;
- use four rough positions as a thinking aid, not a formal taxonomy: strategy/business, domain/architecture, workflow/interface, and implementation;
- consider uncertainty, downstream blast radius/dependency, cost of late discovery, and the cheapest useful falsification/reduction experiment;
- prefer pulling forward risks where a cheap early test can avoid expensive downstream rework;
- remain comparatively relaxed about low-level implementation uncertainty when it is local and cheap to reverse.

The four positions should **not** become ontology enums, scoring fields, a probability-impact matrix, or a mandatory risk register. They are reasoning prompts for selecting and evaluating cycles.

Existing risk horizons may remain useful as lightweight scheduling/disposition metadata for durable `RSK-*` artifacts, but they should not substitute for leverage reasoning. In particular, a locally severe implementation issue can be urgent while still having less architectural blast radius than an uncertain upstream premise.

## Process implication

Risk reasoning belongs mainly at two existing boundaries:

1. **Analyze/Plan** — when choosing the next cycle, ask which unresolved assumption has enough uncertainty and downstream leverage that testing it now is valuable compared with continuing planned work.
2. **Evaluate** — when a cycle exposes new assumptions, surface the materially high-leverage ones as candidate next-cycle inputs before returning to planning. Do not manufacture a list when nothing important emerged.

Plan continuity still governs next-cycle selection: a newly exposed high-leverage risk is an input to reconciliation with the roadmap, not an automatic replacement for it.

This does not require a new process phase or formal between-cycle state. It strengthens the reasoning already present in Analyze/Plan and Evaluate.

## Deliberate limits

- no numeric risk scores;
- no mandatory risk matrix;
- no new artifact for every assumption;
- no requirement to stop ordinary work for every implementation uncertainty;
- no change to the existing warning-profile distinction;
- no formalization of the four positions unless dogfooding later demonstrates a concrete query/automation need.
