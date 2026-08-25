---
id: CYC-20260825-C0QMZ-1
---

# Cycle: Bootstrap Onboarding for Human and AI Agents

Repository branch: `spiral/CYC-20260825-C0QMZ-1-bootstrap-onboarding`
Branch verified: pending

## Analyze

### Project state / prior evaluation that makes this cycle relevant:

The feedback document "Spiral Developer Feedback.md" identifies significant onboarding friction for both human and AI agents. Key findings:

- Quickstart is unclear about its audience (human, AI, or both)
- README.md does not direct non-human agents to AGENTS.md
- "Who should read what" section appears after 40+ lines of prose in README
- Quickstart references 15+ other files before the user creates their first artifact
- The project lacks a BOOTSTRAP.md file for AI/automated agent onboarding
- Documentation is overwhelming (~2,500 lines across 19 files) with core concepts repeated 3-5 times

### Nearest important risk / uncertainty / desired movement:

**Risk:** New adopters (both human and AI) cannot efficiently determine how to start using Spiral Developer. The current quickstart contradicts its stated goal of not requiring users to "study the whole methodology."

**Uncertainty:** What is the minimal, correct onboarding path for different agent types (human developer, AI collaborator, reviewer)?

**Desired movement:** Separate concerns - create a dedicated, minimal BOOTSTRAP.md for AI/automated agents, and restructure quickstart.md to be human-only with clear progression.

### Relevant human direction / feedback:

- Feedback document explicitly recommends: "Rewrite the quickstart to be human-only, add a BOOTSTRAP.md for robots"
- References OpenClaw's BOOTSTRAP template as a model
- Multiple human and AI reviewers identified onboarding confusion as a high-priority issue

### Governing higher-level plan / direction:

None - this is an emergent cycle addressing feedback from active use.

### Current position in that plan:

N/A

### Current starting evidence:

- Feedback document: "Spiral Developer Feedback.md" (uncommitted)
- Existing quickstart.md: 121 lines, references multiple other documents before first action
- Existing README.md: No clear entry point for AI agents
- Existing AGENTS.md: 300+ lines, not referenced from README
- No BOOTSTRAP.md currently exists

## Plan

### Cycle goal

Create a minimal BOOTSTRAP.md file that provides AI/automated agents with a clear, actionable onboarding path to Spiral Developer, and restructure quickstart.md to be human-focused with a clear drill-down structure.

### Commitment boundary

Human confirmation that:
1. The cycle goal (separate AI and human onboarding) addresses the feedback
2. Creating BOOTSTRAP.md is the appropriate solution category
3. Restructuring quickstart.md is acceptable scope

### Why now / why this cycle boundary

Onboarding friction is a **blocker** for new adoption. Both human and AI feedback independently identified this as a high-priority issue. Addressing it in a dedicated cycle:

- Isolated uncertainty: Can we create effective separate onboarding paths?
- High leverage: Every new adopter benefits
- Testable: We can verify AI agents can follow BOOTSTRAP.md and humans can follow quickstart.md
- Small enough: Bounded change that doesn't require redesigning the entire documentation system

If we don't address this, new adopters will continue to struggle with where to start, increasing the risk that they abandon Spiral Developer before understanding its value.

### Plan continuity decision

no governing plan

### Current starting evidence

- Feedback from human and AI reviewers identifying onboarding confusion
- Existing quickstart.md analysis: 121 lines, 15+ file references before first action
- No BOOTSTRAP.md exists
- README.md lacks AI agent direction

### Evaluation basis

- BOOTSTRAP.md exists and provides a clear, minimal path for AI/automated agents to begin
- quickstart.md is restructured to be human-only with clear progression
- AI agents can successfully follow BOOTSTRAP.md to complete a minimal Spiral cycle
- Humans can successfully follow quickstart.md to understand and start using Spiral
- Both files are validated by at least one reviewer from each target audience

### Likely work

1. Crystallize feedback as Source artifact (SRC-*)
2. Create Understanding artifact (UND-*) interpreting the onboarding problem
3. Create Request artifact (REQ-*) for the onboarding improvements
4. Create Design artifact (DES-*) for BOOTSTRAP.md structure
5. Implement BOOTSTRAP.md
6. Implement restructured quickstart.md
7. Create Verification Evidence (EVD-*) that both paths work

### Explicit non-goals

- Redesigning the entire documentation structure
- Creating a tutorial system
- Adding new tooling
- Changing the core Spiral process
- Addressing all feedback items (only onboarding-focused ones)

### Pause / re-plan conditions

- Evidence that BOOTSTRAP.md cannot provide a minimal, effective onboarding path for AI agents
- Evidence that separating AI and human onboarding creates more confusion than it solves
- Discovery that the onboarding problem is actually caused by deeper architectural issues not addressable by documentation changes

## Act

Important artifacts / semantic commits produced:

Material implementation decisions or deviations from the initial likely work:

Out-of-scope discoveries retained for later:

## Evaluate

Integrated result against cycle goal:

Evidence / acceptance result:

Metric or risk movement:

What changed in our understanding:

Surprises / model mismatches:

Known compromises:

Unresolved issues within current goal:

Candidate next-cycle inputs (surface high-leverage assumptions only when material):

Human evaluation / feedback:

Cycle accepted, still open, or deliberately re-planned:

## Process learning

What context/constraint/evaluation helped:

What bookkeeping was useless:

What should the environment learn from this cycle:
