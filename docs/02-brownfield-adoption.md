# Brownfield Adoption

## Purpose

Most Muze projects contain years of accumulated code, tests, configuration, decisions, historical compromises, integrations, and knowledge distributed across developers.

They do not begin with a clean causal chain.

Trying to reconstruct complete provenance before new work begins would be expensive, unreliable, and contrary to the purpose of this process.

> **The goal is not to document the past. The goal is to make future change increasingly traceable, auditable, and safe.**

## 1. Do not migrate the whole project

Capture new causality accurately from now on. Reconstruct old causality only when active work requires it.

Stable legacy code can remain opaque indefinitely if it is not relevant to current risk or change.

Investigate a legacy area when:

- a new feature depends on it;
- its behavior must change;
- a defect occurs in it;
- it blocks current progress;
- it carries substantial security, operational, or business risk;
- understanding it is necessary for an important design decision.

## 2. Start with the next real piece of work

Migration starts with ordinary development, not a migration project.

Create the current request and follow the normal causal process. When the work enters legacy territory, characterize only enough of that behavior to proceed safely.

The first AI-native slice will therefore mix explicit new knowledge with existing behavior whose origin is only partly understood. That is acceptable as long as the distinction remains visible.

## 3. Mark provenance confidence

Use these classes for reconstructed knowledge:

- **explicit** — directly stated and currently authoritative;
- **evidenced** — strongly supported by existing artifacts;
- **inferred** — plausible interpretation supported by some evidence but not established;
- **unknown** — behavior exists, but its reason is not known.

Unknown is better than invented certainty.

## 4. Use AI for targeted archaeology

Relevant evidence may include source, tests, Git history, commits, issues, documentation, schemas, migrations, callers, configuration, operational history, and developer recollection.

The question is not “What is the complete history of this module?”

It is:

> **What do we need to know about this existing behavior to change it safely now?**

Separate observations from explanations.

## 5. Characterize behavior before explaining it

Prefer establishing observable behavior first.

A characterization test may initially mean only:

> **This is what the current system does.**

It does not automatically mean the behavior is desired.

The current request/design decides what must remain.

## 6. Migrate behavior, not directories

Trace the capability or vertical slice being changed, even when it crosses UI, domain logic, APIs, storage, and tests.

Do not clean or document every unrelated part of every touched file.

## 7. Touch it, improve its traceability

After changing an area, future work should have less archaeology to repeat.

A touched capability should normally leave behind:

- an explicit current request;
- a behavioral baseline where relevant;
- relevant design decisions;
- known legacy constraints;
- assumptions and uncertainties;
- verification evidence;
- acceptance evidence;
- causal links among those artifacts.

## 8. Defects are migration opportunities

A legacy defect can follow:

> **failure → characterize → reconstruct relevant context → locate earliest faulty/missing assumption → improve environment → repair/regenerate → verify**

The investigation was necessary anyway; preserve what it taught so the area becomes more governed.

## 9. Do not rewrite history

A 2026 interpretation of a 2014 module is a 2026 interpretation unless historical evidence proves otherwise.

Record current purpose separately from historical origin.

## 10. Capture developer knowledge when relevant

Do not interview everyone about everything.

When active work reaches an area, ask targeted questions and preserve useful answers with provenance. A recollection can be valuable without becoming unquestioned fact.

## 11. Use confidence to bound autonomy

A useful mental model for project areas is:

- **opaque** — no trustworthy causal model;
- **characterized** — observable responsibilities/dependencies known;
- **traced** — current behavior linked to current intent/design/evidence;
- **governed** — future changes are expected to preserve the process.

The less understood an area is, the more conservatively an agent should modify it.

## 12. Avoid opportunistic cleanup

Cheap AI refactoring can enlarge change surfaces and erase undocumented historical behavior.

Refactor when it directly enables the current change, reduces an immediate risk, or is valuable enough to become explicit work of its own.

## 13. Preserve legacy tests until understood

An unexplained old test may be the strongest surviving evidence of a requirement or compatibility constraint.

Do not delete it until you understand what information would be lost.

## 14. Version knowledge with software

Artifacts should have stable identities and revisions. Downstream artifacts should refer to the upstream revisions actually used.

Git is the initial historical store. The exact machine representation can evolve later.

## Migration principle

> **Do not reconstruct the past for its own sake. Preserve causality accurately from now on, and whenever new work crosses into legacy software, reconstruct only enough relevant context to change it safely. Each change should leave the system easier to understand, test, interrogate, and evolve than it was before.**
