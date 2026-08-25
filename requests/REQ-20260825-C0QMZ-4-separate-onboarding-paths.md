---
id: REQ-20260825-C0QMZ-4
---

# Request: Separate Onboarding Paths for Human and AI Agents

**Derived from:** `UND-20260825-C0QMZ-3` (Bootstrap Onboarding Gap)
**Priority:** High (blocker for new adoption)
**Status:** Active

## Request Statement

Create separate, optimized onboarding paths for human and AI agents to address the critical onboarding gap identified in UND-20260825-C0QMZ-3.

### What is being requested

1. **Create BOOTSTRAP.md**: A minimal, actionable onboarding document specifically for AI/automated agents that provides a clear path to complete their first Spiral Developer cycle
2. **Restructure quickstart.md**: Transform the existing quickstart.md into a human-only document with clear, progressive structure that doesn't require studying the entire methodology
3. **Update README.md**: Add a clear entry point directive at the top that directs non-human agents to AGENTS.md and references BOOTSTRAP.md

### Why this is requested

The current onboarding experience fails for both audiences:
- **AI Agents**: Cannot efficiently determine how to start; quickstart references 15+ files before first action; no BOOTSTRAP.md exists
- **Human Agents**: Quickstart is overwhelming; documentation is voluminous (~2,500 lines across 19 files); no clear drill-down path

This creates a **blocker-level risk**: New adopters may abandon Spiral Developer before understanding its value, undermining the project's core goal of enabling trustworthy AI-native development.

### Acceptance Criteria

#### BOOTSTRAP.md
- [ ] Exists at repository root
- [ ] Target audience: AI/automated agents explicitly stated
- [ ] Provides minimal path to complete first Spiral cycle
- [ ] References ≤5 other documents before first actionable step
- [ ] Validated by at least one AI agent successfully following the path

#### quickstart.md
- [ ] Target audience: Human agents explicitly stated
- [ ] Clear, progressive drill-down structure
- [ ] No more than 3 file references before first actionable step
- [ ] Human-friendly prose and formatting
- [ ] Validated by at least one human reviewer

#### README.md
- [ ] Clear entry point directive at top (within first 10 lines)
- [ ] Directs non-human agents to AGENTS.md
- [ ] References BOOTSTRAP.md for AI onboarding

### Out of Scope

- Redesigning the entire documentation structure
- Creating a tutorial system
- Adding new tooling
- Changing the core Spiral process
- Addressing all feedback items (only onboarding-focused)
- Creating new artifact types or relations

### Dependencies

- None (documentation-only changes)

### Constraints

- Must preserve all existing documentation content
- Must not break existing causal references
- Must follow Spiral Developer's own documentation standards
- Must be testable/validatable

### Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Separate paths create more confusion | Low | High | Validate with both audiences before acceptance |
| BOOTSTRAP.md becomes outdated | Medium | Medium | Link to AGENTS.md, include version info |
| quickstart.md still too complex | Medium | Medium | Iterate based on human feedback |
| README.md changes insufficient | Low | High | Test with first-time visitors |

### Success Metrics

- Time for AI agent to complete first cycle: < 1 hour (currently undefined)
- Time for human to understand Spiral basics: < 30 minutes (currently > 1 hour)
- Onboarding satisfaction score: > 4/5 (to be measured post-implementation)

### Related Artifacts

- **Source**: SRC-20260825-C0QMZ-2 (Bootstrap Onboarding Feedback)
- **Understanding**: UND-20260825-C0QMZ-3 (Bootstrap Onboarding Gap)
- **Cycle**: CYC-20260825-C0QMZ-1 (Bootstrap Onboarding for Human and AI Agents)

### Notes

This request operationalizes the understanding that the onboarding gap is a blocker. The proposed solution (separate paths) was explicitly recommended in the source feedback and validated by the understanding artifact.

The changes are intentionally minimal and focused to maximize the chance of successful validation while addressing the highest-leverage issue.
