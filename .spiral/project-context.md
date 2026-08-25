---
id: PROJ-20260825-DGB8Z-1
---

# Project Context: Spiral Developer

**Project IRI:** `https://muze.nl/projects/spiral-developer/`

**Intake status:** Complete

**Last updated:** 2026-08-25

This is the canonical Spiral Developer project repository — the AI-native software development process itself. Spiral Developer provides the process, norms, vocabulary, and tooling that other projects may adopt.

## 1. Purpose, users/stakeholders, and goals

**Purpose:**
Spiral Developer is an AI-native software-development process built around **trust but verify**. It provides a verification architecture that makes intent, constraints, decisions, evidence, provenance, and acceptance explicit enough that AI systems can operate with substantial autonomy while humans retain responsibility for intent, judgment, meaningful feedback, and accountability.

**Users/Stakeholders:**
- **Primary:** AI developers/collaborators (human and AI) using Spiral Developer in their projects
- **Secondary:** Project maintainers, reviewers, and auditors who need to verify AI-produced work
- **Tertiary:** Tooling developers building on top of Spiral Developer

**Goals:**
- Enable trustworthy AI-native development with explicit causal chains
- Support distributed development without coordination conflicts in provenance
- Provide a lightweight, verification-based process that scales from small to large projects
- Dogfood the process on itself (this project is the canonical reference)

## 2. Current posture

**Posture:** Actively growing, self-hosted, dogfood-first

This is a mature but evolving process. The project is actively maintained, with recent work focused on:
- Hardening process guardrails (branch identity checks, cycle sizing, intake completeness)
- Distributed development support (workspace-safe artifact allocation, integration validation)
- Discourse/commitment/execution semantics
- Implementation lineage and bounded context

The project operates in a **dogfood-first** mode: new process features are developed and validated on this repository before being documented as stable guidance.

## 3. Important measures/outcomes

**Health indicators:**
- Process coherence: Can an AI agent following Spiral documentation successfully and safely complete a cycle?
- Causal graph validity: All Turtle resources parse; historical references resolve to actual Git ancestors
- Distribution safety: Independent worktrees can allocate artifact IDs without collision
- Human review effectiveness: Reviewers can efficiently verify causal chains and accept/reject based on evidence

**Target thresholds:**
- Zero malformed causal commits in main branch
- Every accepted cycle passes prospective integration validation
- Every required brownfield intake topic explicitly dispositioned before active development

**Currently unmeasured:**
- Adoption rate across external projects
- Average cycle time for typical changes
- Human satisfaction with review workload

## 4. Consequential prior decisions

| Decision | Rationale | Reversibility |
|----------|-----------|---------------|
| **Trust-but-verify autonomy model** | AI capability outpaces human review; verification architecture must compensate | Low - fundamental to approach |
| **Git as version system** | Immutable history provides audit trail; no separate version system needed | Very low - would require new infrastructure |
| **Turtle for causal graph** | RDF provides typed relationships, standard tooling, queryability, validation | Low - changing format would break existing tooling |
| **Distributed-safe artifact IDs** | Prevents identity collisions in independent worktrees without central coordination | Medium - could add alternative schemes but legacy format remains |
| **Cycle as outer boundary** | Humans review integrated cycle results, not every AI step | Low - core process invariant |
| **Legacy ID preservation** | Existing artifacts keep original IDs; new artifacts use date-workspace-sequence format | High - new format doesn't affect old artifacts |
| **Markdown + Turtle dual representation** | Humans read Markdown; machines read Turtle; both are versioned together | Medium - could consolidate but dual format has advantages |

## 5. Important invariants and commitments

**Must not be broken:**
- Git commits containing causal artifacts are **immutable** (no amend, rebase, squash, force-push)
- Every `sd:historicalReference` in a committed Turtle file must point to a Git ancestor of that commit
- Accepted artifacts must not have current/effective causal dependencies on Superseded/Rejected artifacts
- Cycle branches must match their declared cycle identity
- Prospective integration must pass validation before merge

**Compatibility promises:**
- Ontology additions are backward-compatible; existing predicates retain their meaning
- Legacy artifact IDs (CYC-001, etc.) remain valid indefinitely
- The causal graph can be queried with standard RDF/SPARQL tooling

**Operational dependencies:**
- Git (immutable history model)
- Standard RDF/Turtle parsers for validation
- The vocabulary in `ontology/spiral-developer.ttl`

## 6. Known/tolerated problems

| Problem | Impact | Status | Notes |
|---------|--------|--------|-------|
| **No automated intake tracking** | Intake state is manual; can become stale | Accepted | Tracking via explicit status in project context |
| **SHACL validation incomplete** | Not all structural constraints have SHACL shapes | Accepted | Validation exists for critical invariants; others added as needed |
| **Limited tooling ecosystem** | Few external tools consume Spiral Turtle | Accepted | Process is designed to work with standard RDF tooling |
| **Documentation drift** | Docs may lag behind practice | Deferred | Addressed during each cycle's documentation step |

## 7. Reality/feedback sources

**Primary feedback sources:**
- **Dogfooding:** This project itself - every cycle is a test of the process
- **Git history:** Audit trail for all changes; the primary reality source
- **Pull request reviews:** Human review of cycle outcomes
- **Integration validation:** `spiral validate` tooling checks before merge

**Secondary feedback sources:**
- External project adoption reports (currently limited)
- Issue tracker discussions
- Contributor feedback

**Missing/weak feedback:**
- Systematic user studies of external adopters
- Automated telemetry from Spiral-enabled projects

## 8. Knowledge gaps / affinity needs

**Areas where understanding is developing:**
- Optimal cycle sizing heuristics across different project types
- Best practices for warning profile adoption and scoping
- Metrics for process effectiveness beyond "did it prevent a mistake"

**Areas needing human guidance:**
- Decisions about expanding Spiral scope (e.g., to non-software artifacts)
- Prioritization of tooling improvements vs. documentation improvements
- Trade-offs between process rigor and adoption friction

## 9. Relevant future direction

**Active direction (current focus):**
- Complete CYC-005: Distributed development cycle (workspace allocation, integration validation)
- Harden process guardrails (branch identity verification, intake completeness)

**Near-term roadmap:**
- Improve `spiral validate` tooling coverage
- Add SHACL shapes for remaining critical invariants
- Document process evolution patterns

**Known commitments:**
- Maintain backward compatibility with existing Spiral artifacts
- Continue dogfood-first development model
- Keep the process lightweight and verification-focused

**Planned changes:**
- Migration of remaining legacy artifact references to use full Git hashes
- Progressive enhancement of validation tooling

**Governed by:** No external multi-cycle plan document; direction emerges from cycle evaluations and is captured in cycle artifacts.

## 10. Risk-discovery and metric-profile disposition

**Adopted profiles:**
- **Risk-discovery:** None explicitly adopted at project level; cycles adopt as needed
- **Metric:** None explicitly adopted at project level; process health measured by invariant adherence

**Available profiles (not adopted):**
- `profiles/risk-discovery/*` - available for use but not automatically active
- `profiles/metrics/*` - available for use but not automatically active

**Excluded profiles:** None

**Narrowed applicability:** Not applicable - no profiles currently adopted

**Custom lenses:** The project itself serves as its own lens; dogfooding provides direct feedback

## 11. Integration context

**Authoritative integration branch:** `main`

**Pre-merge validation boundary:** Pull request review with `spiral validate integration`

**Integration mechanism:**
- Cycle branches (`spiral/CYC-*`) are created for each cycle
- Cycle branches are never merged into each other
- Accepted cycles are integrated via PR merge into `main`
- Before merge: `spiral validate integration --base <main-hash> --head <pr-hash> --base-branch main --head-branch <cycle-branch>`

**Merge mechanism:** Standard Git merge (no rebase, no squash)

**Serialization:** No merge queue/train currently; PRs are reviewed and merged sequentially

**Hosted enforcement:** GitHub PR checks; manual pre-merge validation via CLI

## Active culture and warning profiles

**Adopted culture:** `cultures/muze-engineering.md` (CUL-MUZE-001)
- Preferred: frontend-first probes, replaceable dependencies, explicitness over magic
- Scope: Applies to Spiral Developer's own implementation and examples

**Adopted warning profiles:** None at project level

## Notes on recursion

This project is the Spiral Developer process itself. This creates beneficial recursion:

- Every improvement to Spiral is immediately available to Spiral's own development
- Every cycle in this project is a real-world test of the process
- Process documentation and examples are co-located with their implementation

However, care is needed:

- Changes to core Spiral semantics must be carefully versioned
- Documentation updates must be consistent with implemented behavior
- The project must maintain coherence even while the process evolves

The recursion is a feature, not a bug. It means Spiral Developer is always eating its own dogfood.
