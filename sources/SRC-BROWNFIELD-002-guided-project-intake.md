---
id: SRC-BROWNFIELD-002
---

# Source: Guided brownfield project intake

## Human direction

Brownfield Spiral Developer needs an obligatory intake discussion before the next normal development cycle when the project has not yet established durable project-level context.

The intake should transfer enough project meaning for an AI collaborator to reason about direction and risk without requiring the human to first read and understand the full Spiral methodology. It should work like a quickstart/setup conversation: explain briefly why a question matters when asking it, offer common choices where useful, and always permit custom answers, uncertainty, or "not relevant".

The intake should establish at least:

- what the project is for and its important goals;
- which outcomes or metrics matter and, where known, what levels are acceptable;
- consequential decisions already taken that constrain future direction, including how reversible they really are;
- important constraints/invariants and things that must not be casually broken;
- known tolerated problems or risks;
- reliable feedback/reality sources;
- project areas that are poorly understood or likely to require early human guidance;
- relevant future direction or commitments that materially change what should be optimized now.

Reusable plain-Markdown **risk-discovery profiles** may suggest classes of project-specific problems worth investigating. The intake should make explicit which profiles to consult, which to ignore/defer, and any custom concerns. These profiles are discovery lenses, not claims that the project has those risks.

Reusable plain-Markdown **metric profiles** may suggest outcomes or measurements that commonly matter for projects in a particular posture or maturity. They are prompts, not a universal scorecard; project purpose and consequence can override maturity-based suggestions, and qualitative outcomes or "we do not know how to measure this" are valid.

After the human confirms the intake summary, the AI should inspect the actual project and compare current evidence with the desired state. It should report substantiated candidate risks, metric gaps, missing measurements, and important uncertainties. The human then prioritizes, rejects/accepts/defers, edits, removes, and adds risks before the next Spiral cycle is chosen.

Do not formalize this into a maturity score, large schema, rigid wizard, or exhaustive ontology yet. Keep the intake conversational and preserve its durable conclusions in ordinary Markdown project context. New answer options or recurring project-specific concerns may later become evidence for improving the general profiles, but should not mutate them automatically.
