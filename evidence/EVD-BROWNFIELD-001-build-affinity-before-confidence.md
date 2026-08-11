---
id: EVD-BROWNFIELD-001
---

# Verification Evidence: Build affinity before brownfield confidence

## What is being verified

Adoption of `LES-009`: unfamiliar brownfield work should explicitly assume partial project-specific understanding, build enough affinity with the relevant area before making strong claims, and treat early human handholding as useful knowledge transfer rather than process failure.

## Mechanical / structural checks

- `AGENTS.md` states **Build affinity before confidence** in the brownfield guidance and explicitly rejects affinity scores/stages/artifacts as a default mechanism.
- `docs/brownfield.md` provides both agent-facing and human-facing guidance: learn enough about the relevant area to know where behavior may originate; expose uncertainty; expect more human guidance early.
- `docs/ai-collaboration.md` connects project affinity to the adequacy of evidenced-gap scope without changing the confirmed-Understanding/evidenced-gap gate.
- `prompts/start-change.md` and `prompts/brownfield-change.md` tell agents to assume partial local project understanding and seek human guidance when needed before strong absence/duplication claims.
- `prompts/repository-bootstrap.md` makes partial initial project understanding explicit while still forbidding full-history reconstruction or a formal affinity model.
- `docs/quickstart.md` tells humans that early handholding is expected knowledge transfer, not process failure.
- `docs/review.md` asks whether an unfamiliar-area gap claim was supported by sufficient project affinity or human guidance.
- No new ontology class, confidence score, mandatory intake stage, or project artifact type was introduced.
- All Turtle resources parse with the installed standards-conforming RDF parser.
- Current durable exact Git references resolve to strict ancestors of the artifact versions containing them.
- `git diff --check` completes without whitespace errors; `git fsck` reports no structural repository corruption (unreachable blobs are ordinary Git residue and are not referenced by the branch).

## What this verification does not establish

Static checks cannot determine how much project affinity is enough in a particular codebase or subsystem. Nor can they prove that an agent will recognize when its search scope is too shallow. The intended next evidence is continued dogfooding across unfamiliar brownfield areas, allowing human-AI collaboration to discover what useful local orientation looks like before adding further architecture.

## Result

The process now explicitly treats initial brownfield unfamiliarity as normal and requires confidence to follow earned local project understanding rather than general model capability, while intentionally leaving the practical form of that affinity to the collaboration.
