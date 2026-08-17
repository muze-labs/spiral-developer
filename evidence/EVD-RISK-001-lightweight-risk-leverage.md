---
id: EVD-RISK-001
---

# Verification Evidence: Lightweight risk leverage model

## What is being verified

Adoption of `LES-017`: Spiral should prioritize important uncertain assumptions by downstream leverage and cost of late discovery, using strategy/business → domain/architecture → workflow/interface → implementation as a rough reasoning aid, without introducing numeric scoring, a mandatory risk matrix, or a new process phase.

Implementation commit under verification: `4bfbb0692f5d0237ae2a825ba134a64e32fdc5f9`.

## Structural / consistency checks

- `catalogs/risks.md` now defines prioritization around important assumptions/uncertainties and explains the four rough causal positions, downstream leverage, late-discovery cost, and cheap falsification.
- `docs/vision.md`, `docs/process.md`, `docs/cycles.md`, `README.md`, and `AGENTS.md` use the leverage model for prioritization rather than requiring horizon-first classification.
- `prompts/plan-cycle.md` applies the model during existing Analyze/Plan and explicitly keeps governing-plan reconciliation authoritative over recency/risk salience.
- `prompts/evaluate-cycle.md` and `templates/CYCLE.md` surface newly exposed high-leverage assumptions as candidate next-cycle input only when material; they explicitly avoid manufacturing a risk list or choosing priority during Evaluate.
- `prompts/start-change.md` no longer requires every change to classify risks by horizon.
- `templates/REQUEST.md` no longer contains a mandatory risk/horizon table; durable `RSK-*` artifacts remain available when explicit identity/review is useful.
- Existing blocker/near-term/deferred/existential horizons remain available in live guidance as optional scheduling/disposition metadata for durable risks, preserving compatibility without making them the prioritization model.
- Brownfield intake guidance carries the same leverage/late-discovery reasoning into first-cycle selection.
- No new ontology class/property, score, matrix, risk-register artifact, or between-cycle state was introduced.

## Repository checks

- All 68 Turtle resources parse successfully with RDFLib.
- All 45 non-template/example exact `sd:gitCommit` references resolve to commits and are ancestors of the current branch; template/example placeholder hashes are intentionally excluded from this ancestry check.
- `git diff --check HEAD` reports no whitespace errors.
- `git fsck --no-reflogs --unreachable` reports no repository corruption.
- Active branch was mechanically verified as `spiral/CYC-003-risk-leverage` during the cycle.

## What this verification does not establish

Static consistency does not establish that agents will make better cycle choices, that the four causal positions are always sufficient, or that humans will find the leverage language clearer in practice. It also does not establish that horizon metadata should remain indefinitely.

Those are dogfooding questions. The change deliberately keeps the model qualitative and small so later experience can refine or remove it without creating process debt.

## Result

Spiral now has a lightweight risk-driven prioritization rule: prefer cheap tests of uncertain assumptions whose failure would invalidate substantial downstream work, while spending less effort de-risking local reversible implementation choices. The rule is integrated into existing cycle planning/evaluation and reconciled with governing-plan continuity rather than added as new ceremony.
