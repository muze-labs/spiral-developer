---
id: UND-20260825-C0QMZ-3
---

# Understanding: Onboarding Gap Blocks New Adoption

**Source:** `SRC-20260825-C0QMZ-2` (Bootstrap Onboarding Feedback)
**Interpretation of:** Feedback from human and AI reviewers about Spiral Developer onboarding experience
**Provenance confidence:** Evidenced (based on concrete feedback from multiple reviewers)

## Interpretation

The feedback reveals a **critical onboarding gap** that prevents both human and AI agents from efficiently starting with Spiral Developer.

### What the source expresses

The source document ("Spiral Developer Feedback.md") contains structured feedback from multiple reviewers (human and AI) who evaluated the Spiral Developer project. Key findings include:

1. **Quickstart.md is ineffective**: References 15+ other files before the user creates their first artifact, contradicting its stated goal of not requiring users to "study the whole methodology"
2. **README.md doesn't direct AI agents**: No clear entry point for non-human agents; doesn't reference AGENTS.md
3. **Missing BOOTSTRAP.md**: No dedicated minimal onboarding path for AI/automated agents
4. **Documentation is overwhelming**: ~2,500 lines across 19 files with core concepts repeated 3-5 times
5. **Audience confusion**: quickstart.md unclear whether for human, AI, or both

### What this means for Spiral Developer

**Primary implication:** The project's documentation structure, while comprehensive, does not provide a **minimal viable onboarding path** for new adopters. This creates a paradox:

- The documentation is **too much** for newcomers to digest
- But it doesn't provide a **clear starting point** for different agent types
- The **signal-to-noise ratio** is low for onboarding purposes

This is a **blocker-level risk** because:
- New adopters may abandon Spiral Developer before understanding its value
- AI agents cannot efficiently determine how to start
- Humans cannot efficiently determine what to read first
- The project's own goal (trust-but-verify with AI autonomy) is undermined if agents cannot onboard

### Why this interpretation is valid

The interpretation is **evidenced** by:
1. Multiple independent reviewers (human and AI) identifying the same onboarding problems
2. Specific, concrete examples (quickstart references 15+ files, README lacks AI direction)
3. Explicit recommendation from human reviewer: "add a BOOTSTRAP.md for robots"
4. Alignment with AI feedback: "Documentation is overwhelming/voluminous"

### What would falsify this interpretation

This interpretation would be falsified if:
- Evidence shows that most new adopters successfully onboard without confusion
- The current quickstart.md is demonstrated to be effective for its target audience
- The documentation volume is shown to be appropriate and necessary
- New adopters report that the current structure works well for them

### How this understanding shapes action

This understanding implies that the **minimal viable fix** is to:

1. **Create BOOTSTRAP.md**: A minimal, actionable onboarding path specifically for AI/automated agents
2. **Restructure quickstart.md**: Make it human-only with clear, progressive drill-down
3. **Separate concerns**: Different entry points for different agent types

This approach:
- Addresses the highest-leverage issue (onboarding friction)
- Is testable (can verify AI agents follow BOOTSTRAP.md, humans follow quickstart.md)
- Is bounded (doesn't require redesigning entire documentation)
- Preserves existing documentation while adding clarity

### Confidence and gaps

**Confidence:** High - multiple independent sources, concrete examples, explicit recommendations

**Remaining gaps:**
- Exact content of BOOTSTRAP.md vs quickstart.md needs human input
- Validation that the proposed separation actually works for both audiences
- Measurement of whether this reduces onboarding time

**Next steps:**
- Create Request artifact (REQ-*) formalizing the onboarding improvements
- Create Design artifact (DES-*) for BOOTSTRAP.md structure
- Implement and test both onboarding paths
