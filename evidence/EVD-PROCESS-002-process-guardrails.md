---
id: EVD-PROCESS-002
---

# Verification Evidence: Branch, cycle-sizing, and intake guardrails

## What is being verified

Adoption of `LES-013`, `LES-014`, and `LES-015`: Spiral should actively verify cycle branch identity, size outer cycles by uncertainty/risk/evaluation coherence rather than habitual smallness, and keep incomplete brownfield intake explicitly visible until every required topic is dispositioned and human-confirmed.

Implementation commit under verification: `216c9c6a24a22619b7fcdaf6a8100299256104e8`.

## Structural / consistency checks

- `AGENTS.md`, `docs/git-workflow.md`, `docs/cycles.md`, `prompts/plan-cycle.md`, `prompts/start-change.md`, `prompts/brownfield-change.md`, `prompts/evaluate-cycle.md`, and `templates/CYCLE.md` require direct inspection of actual Git branch state at cycle open, before semantic causal commits, and during evaluation for normal repository-changing cycles.
- The cycle record now has explicit `Repository branch` and `Branch verified` fields.
- `AGENTS.md`, `docs/cycles.md`, `prompts/plan-cycle.md`, `README.md`, `CONTRIBUTING.md`, and `templates/CYCLE.md` distinguish small evidence-producing steps from the outer cycle boundary and direct cycle sizing toward uncertainty, risk, and coherent evaluation.
- `templates/PROJECT_CONTEXT.md` persists intake state as `Incomplete`, `Complete`, or `Stale` and provides a compact required-topic disposition table in which `Pending` cannot count as complete.
- Brownfield intake guidance and prompts require every topic to receive an explicit disposition while preserving `Unknown`, `Not relevant`, and justified deferral as first-class outcomes.
- While intake remains active and incomplete/stale, normative agent guidance requires user-visible interactions to state that intake remains incomplete and surface the remaining topics rather than silently proceeding.
- No branch-management helper, intake runtime/state-machine, cycle-size scoring mechanism, or new ontology vocabulary was introduced.
- All 57 Turtle resources present before this evidence commit parsed successfully with RDFLib.
- All 36 exact Git references that resolve to real commits in this repository are ancestors of the branch head. The 17 unresolved 40-character values are deliberate illustrative placeholders in `examples/` and `templates/`, not durable project provenance.
- Changed guidance paths were checked for existence. Apparent missing `.spiral/...` paths are examples of paths expected in consuming projects, not repository-local broken links.
- `git diff --check` reported no whitespace errors before the implementation commit.
- `git fsck --no-reflogs` reports no Git object/database errors relevant to this cycle.
- Actual branch state at evaluation is `spiral/CYC-001-process-guardrails`, matching active cycle `CYC-001`.

## Causal-reference checks

- `UND-PROCESS-002` interprets the exact committed version of `SRC-PROCESS-002` at `1c1c60364025fa1b280df9d35ebfbc15257d7057`.
- `LES-013`, `LES-014`, and `LES-015` each derive from the exact committed version of `UND-PROCESS-002` at `1e75fd993c4555658dddca88a21f660086ca8ddf`.
- The process implementation commit records all three lesson versions in Git trailers at `b09e4c9324c82a9fb5b3e0fc50eaa9958d513fff`.
- No existing historical commit was amended, rebased, squashed, or rewritten to add these references.

## Scenario consistency checks

1. **Agent remains on an older cycle branch** — branch verification blocks a new semantic causal commit until the mismatch is corrected or explicitly justified.
2. **Early work contains one risky unknown at a time** — small cycles remain appropriate because each result may invalidate subsequent work.
3. **Later work contains several related steps under stable assumptions** — planning guidance prefers one coherent cycle rather than several tiny cycles merely because there are several tasks/commits.
4. **An intake topic is unknown** — it may be explicitly dispositioned `Unknown`; completion does not require fabricated certainty.
5. **An intake topic has not been considered** — it remains `Pending`, so intake cannot silently present itself as complete.
6. **Intake spans several interactions** — unfinished topics remain visible in each user-visible intake interaction until completion or explicit reframing.

## What this verification does not establish

Static repository consistency does not establish that every future agent will obey the branch check, choose good cycle boundaries, or present intake reminders with ideal conversational ergonomics. Those are dogfooding questions for later cycles.

The current solution also does not machine-enforce intake status transitions or branch naming through dedicated tooling. That complexity is deliberately deferred until evidence shows that explicit Git checks and durable Markdown state are insufficient.

## Result

The three dogfooding failures are now represented as a preserved causal chain and prospectively hardened in the process without rewriting prior history or adding substantial machinery. Further dogfooding can test whether the explicit checks are sufficient before stronger automation is considered.
