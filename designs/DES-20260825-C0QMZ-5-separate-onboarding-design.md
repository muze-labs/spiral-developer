---
id: DES-20260825-C0QMZ-5
---

# Design: Separate Onboarding Paths Structure

**Satisfies:** REQ-20260825-C0QMZ-4 (Separate Onboarding Paths for Human and AI Agents)  
**Status:** Active  
**Shaped by:** CUL-MUZE-001 (Muze Engineering Culture - prefers explicitness, bounded assumptions)

## Design Overview

This design addresses REQ-20260825-C0QMZ-4 by creating two distinct, optimized onboarding paths:
- **BOOTSTRAP.md**: Minimal, action-oriented path for AI/automated agents
- **quickstart.md**: Human-friendly, progressive drill-down path

The design follows the **hub-and-spoke** model recommended in the feedback, where each entry point serves its specific audience without requiring them to parse irrelevant information.

## BOOTSTRAP.md Design

### Purpose
Provide AI/automated agents with a **minimal viable path** to complete their first Spiral Developer cycle.

### Target Audience
- AI agents (LLMs, automated tools)
- Automated scripts
- Non-human agents that need actionable instructions

### Structure

```
BOOTSTRAP.md
├── Header (5 lines max)
│   ├── Title
│   ├── Purpose: "Minimal onboarding for AI/automated agents"
│   ├── Audience: "AI agents, automated tools"
│   └── Prerequisites: "Git, basic understanding of software development"
│
├── Section 1: What You Are (5 lines)
│   ├── "You are an AI/automated agent operating in a Spiral Developer project"
│   └── "Your goal: Complete a minimal Spiral cycle autonomously"
│
├── Section 2: Minimal Context (10 lines)
│   ├── "Spiral Developer is a trust-but-verify AI-native development process"
│   ├── "You must preserve causal provenance for all consequential work"
│   └── "Key files: AGENTS.md (your operating instructions)"
│
├── Section 3: First Steps (15 lines max, actionable)
│   ├── Step 1: Read AGENTS.md
│   ├── Step 2: Identify the project context (.spiral/project-context.md)
│   ├── Step 3: Check active cycles (.spiral/cycles/)
│   ├── Step 4: For new work: Allocate artifact ID with spiral CLI
│   └── Step 5: Create causal artifacts in order: SRC → UND → REQ → DES → IMP → EVD
│
├── Section 4: Validation Checklist (5 lines)
│   ├── ✓ Branch matches cycle ID
│   ├── ✓ All TTL files parse
│   ├── ✓ Historical references point to ancestors
│   └── ✓ Artifact IDs follow TYPE-YYYYMMDD-WORKSPACE-N format
│
├── Section 5: When to Stop and Ask (5 lines)
│   ├── "If uncertain about intent, meaning, or framing: return to discourse"
│   ├── "If modification would affect production behavior: stop and verify gap"
│   └── "If existing behavior already satisfies the need: report, don't implement"
│
└── Footer: Links to Full Documentation (5 lines)
    ├── "For humans: See quickstart.md"
    ├── "Full process: docs/process.md"
    └── "Ontology: ontology/spiral-developer.ttl"
```

### Content Requirements

| Requirement | Rationale |
|-------------|-----------|
| ≤ 50 lines total | AI agents need minimal, scannable content |
| ≤ 5 document references before first action | Quick time-to-first-action |
| Actionable steps only | AI agents need clear next steps |
| No walls of text | Low tolerance for prose parsing |
| Explicit audience declaration | Avoids confusion about who should read it |

### File Location
- Repository root: `BOOTSTRAP.md`

### Validation
- AI agent can parse and follow steps without human intervention
- All referenced files exist and are accessible
- Steps lead to a valid minimal Spiral cycle

---

## quickstart.md Design

### Purpose
Provide humans with a **clear, progressive drill-down** to understand and start using Spiral Developer.

### Target Audience
- Human developers new to Spiral Developer
- Project maintainers evaluating Spiral for adoption
- Reviewers who need to understand the process

### Structure

```
quickstart.md
├── Header
│   ├── Title
│   ├── Purpose: "Human-friendly introduction to Spiral Developer"
│   ├── Audience: "Human developers, maintainers, reviewers"
│   └── Prerequisites: "None - this is your starting point"
│
├── Section 1: What is Spiral Developer? (10 lines)
│   ├── Elevator pitch: "Trust-but-verify AI-native development process"
│   ├── Core value: "Autonomy through verification architecture"
│   └── One sentence: "Humans retain judgment; AI handles execution with provenance"
│
├── Section 2: Should You Read This? (5 lines)
│   ├── "If you're an AI agent: See BOOTSTRAP.md instead"
│   └── "If you're human: Continue here"
│
├── Section 3: The Spiral Model (15 lines)
│   ├── Diagram: Analyze → Plan → Act → Evaluate → (repeat)
│   ├── Outer cadence: Human-visible learning/integration boundary
│   └── Inner chain: source → understanding → request → design → implementation → verification → acceptance
│
├── Section 4: Quick Start (20 lines)
│   ├── Step 1: Read this document (quickstart.md)
│   ├── Step 2: Check if your project has .spiral/project-context.md
│   │   ├── If yes: You're in a Spiral project - see "Working in a Spiral Project" below
│   │   └── If no: See "Adopting Spiral in Your Project" below
│   └── Step 3: For brownfield projects: Run guided intake
│
├── Section 5: Working in a Spiral Project (15 lines)
│   ├── "If .spiral/ exists, Spiral is already set up"
│   ├── "Read AGENTS.md for your operating instructions"
│   ├── "Check .spiral/cycles/ for active cycles"
│   └── "Follow the existing project's conventions"
│
├── Section 6: Adopting Spiral in Your Project (10 lines)
│   ├── "For new projects: Start with docs/quickstart.md (this file)"
│   ├── "For existing projects: See docs/brownfield-intake.md"
│   └── "For evaluation: Try a small cycle and iterate"
│
├── Section 7: Drill Down (10 lines)
│   ├── "Need more detail? Explore these next:"
│   ├── "└── docs/vision.md - Why Spiral exists"
│   ├── "└── docs/process.md - The development lifecycle"
│   ├── "└── docs/trust-model.md - Trust-but-verify explained"
│   └── "└── AGENTS.md - AI agent operating instructions"
│
└── Footer
    ├── "AI agents: See BOOTSTRAP.md"
    └── "Questions: Open an issue or discussion"
```

### Content Requirements

| Requirement | Rationale |
|-------------|-----------|
| Progressive disclosure | Humans can stop at any point and have useful understanding |
| Clear section hierarchy | Easy navigation and scanning |
| Human-friendly prose | Written for human reading, not machine parsing |
| Explicit audience | Clarifies this is for humans |
| Cross-references to BOOTSTRAP.md | Ensures AI agents find their path |

### File Location
- Repository root: `docs/quickstart.md` (moved from current location if different)

### Validation
- Human reviewer can follow the path and understand Spiral basics
- Clear progression from overview to detail
- Each section builds on the previous one

---

## README.md Updates

### Changes Required

1. **Add entry point directive at top** (within first 10 lines):
   ```markdown
   # Spiral Developer
   
   **For AI/automated agents:** See [BOOTSTRAP.md](BOOTSTRAP.md)
   **For human developers:** See [docs/quickstart.md](docs/quickstart.md)
   
   Spiral Developer is an AI-native software-development process...
   ```

2. **Update "Who should read what" section** to reference new structure:
   - Clarify that BOOTSTRAP.md is for AI agents
   - Clarify that quickstart.md is for humans
   - Keep existing document references

### File Location
- Repository root: `README.md` (update in place)

---

## Design Decisions

### Decision 1: Separate Files vs. Single File with Sections

**Chosen:** Separate files (BOOTSTRAP.md + quickstart.md)  
**Rationale:** 
- Different audiences have different needs
- AI agents need minimal, actionable content
- Humans benefit from progressive disclosure
- Separation allows optimization for each audience

**Alternatives considered:**
- Single file with audience-specific sections: Would require agents to parse irrelevant content
- Single file with conditional content: Not feasible with static Markdown

### Decision 2: BOOTSTRAP.md at Repository Root

**Chosen:** Repository root  
**Rationale:** 
- AI agents typically start at repository root
- Matches OpenClaw convention referenced in feedback
- High visibility ensures discovery

**Alternatives considered:**
- `.spiral/BOOTSTRAP.md`: Less discoverable for AI agents starting fresh
- `docs/BOOTSTRAP.md`: Mixed with human documentation, harder to find

### Decision 3: quickstart.md Location

**Chosen:** `docs/quickstart.md`  
**Rationale:** 
- Part of the human documentation
- Consistent with existing docs/ structure
- Humans expect documentation in docs/

**Note:** If quickstart.md currently exists at repository root, move it to docs/.

---

## Implementation Notes

### For BOOTSTRAP.md
- Use concise, imperative language
- Number all steps explicitly
- Avoid walls of text (> 3 lines)
- Every reference should be actionable
- Include a validation checklist

### For quickstart.md
- Use clear headings and subheadings
- Include a simple diagram of the Spiral model
- Use progressive disclosure (summary → detail)
- Include "Should you read this?" section early
- Link to BOOTSTRAP.md prominently

### For README.md
- Minimal changes to preserve existing content
- Add entry point directive at top
- Update cross-references
- Preserve all existing links and structure

---

## Assumptions

| Assumption | Validation Plan | Risk if Wrong |
|-----------|----------------|--------------|
| AI agents start at repository root | Test with AI agent | Low discoverability |
| Humans expect docs in docs/ | Human feedback | Confusing location |
| Separate paths reduce confusion | A/B test both approaches | Increased friction |
| BOOTSTRAP.md can be < 50 lines | Iterate based on validation | Too verbose |

---

## Success Criteria

This design is successful if:
1. AI agents can complete their first Spiral cycle using only BOOTSTRAP.md
2. Humans can understand Spiral basics using only quickstart.md
3. Both paths are validated by at least one representative from their target audience
4. README.md changes improve entry point clarity

---

## Related Artifacts

- **Request:** REQ-20260825-C0QMZ-4 (Separate Onboarding Paths for Human and AI Agents)
- **Understanding:** UND-20260825-C0QMZ-3 (Bootstrap Onboarding Gap)
- **Source:** SRC-20260825-C0QMZ-2 (Bootstrap Onboarding Feedback)
- **Cycle:** CYC-20260825-C0QMZ-1 (Bootstrap Onboarding for Human and AI Agents)

---

## Open Questions

1. Should BOOTSTRAP.md include a minimal example of a complete cycle?
2. Should quickstart.md include a troubleshooting section?
3. Should we add a third entry point for reviewers/auditors?
