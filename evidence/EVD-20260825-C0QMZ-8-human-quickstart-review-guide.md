---
id: EVD-20260825-C0QMZ-8
title: Human Review Guide for quickstart.md
---

# Evidence: Human Review Guide for quickstart.md

**Purpose:** Guide for human reviewer to validate quickstart.md  
**Satisfies:** Acceptance criterion for human validation from REQ-20260825-C0QMZ-4  
**Status:** Active  
**Type:** Review guide  
**Provenance confidence:** Evidenced  

---

## Overview

This document provides guidance for human reviewers to validate that `docs/quickstart.md` meets the acceptance criteria from REQ-20260825-C0QMZ-4 and DES-20260825-C0QMZ-5.

---

## Test Procedure for Human Reviewers

Following the test procedure defined in EVD-20260825-C0QMZ-6:

### Step 1: Read docs/quickstart.md
**Action:** Read the entire document from beginning to end  
**Duration:** ~5-10 minutes

### Step 2: Answer Validation Questions

After reading, answer the following:

#### Comprehension Check

1. **Can you explain what Spiral Developer is?**
   - Expected: Should be able to articulate that it's an AI-native software development process built around trust-but-verify
   - Look for: Elevator pitch in "What is Spiral Developer?" section

2. **Can you identify the first step for a new project?**
   - Expected: Should identify to check if `.spiral/` directory exists, then follow "Adopting Spiral in Your Project" section
   - Look for: Step 2 in "Quick Start" section

3. **Can you identify the first step for an existing project?**
   - Expected: Should identify to read AGENTS.md and check active cycles in `.spiral/cycles/`
   - Look for: "Working in a Spiral Project" section

4. **Can you explain the outer cadence and inner causal chain?**
   - Expected: Should identify "Analyze → Plan → Act → Evaluate" as outer cadence and "source → understanding → request → design → implementation → verification → acceptance" as inner chain
   - Look for: "The model" subsection in "What is Spiral Developer?"

### Step 3: Evaluate Structure

| Criterion | Check | Expected |
|-----------|-------|----------|
| Target audience explicitly stated | ✅ | "Audience: Human developers, maintainers, reviewers" in header |
| Clear, progressive drill-down structure | ✅ | Multiple sections building on each other |
| Human-friendly prose and formatting | ✅ | Clear headings, bullet points, code blocks |
| Cross-references to BOOTSTRAP.md | ✅ | At least 3 references to BOOTSTRAP.md for AI agents |
| No more than 3 file references before first actionable step | ✅ | Only BOOTSTRAP.md referenced before Step 1 |

---

## Acceptance Criteria Checklist

From REQ-20260825-C0QMZ-4:

- [ ] Target audience explicitly stated as human developers
- [ ] Clear, progressive drill-down structure
- [ ] No more than 3 file references before first actionable step
- [ ] Human-friendly prose and formatting
- [ ] Validated by at least one human reviewer (this review)

From DES-20260825-C0QMZ-5:

- [ ] Progressive disclosure (each section builds on previous)
- [ ] Clear section hierarchy
- [ ] Human-friendly prose
- [ ] Explicit audience
- [ ] Cross-references to BOOTSTRAP.md

---

## Document Structure Summary

**docs/quickstart.md** (345 lines, significantly expanded) contains:

**Note:** Document has been substantially updated with installation instructions, prerequisites, and human workflow guidance from Boot Human.md. The structure below reflects the original version; the current version includes additional sections: Your Role, Prerequisites, Installation, Human Workflow, What You MUST Do, Key Commands, and Brownfield Intake Checklist.

### Section 1: Header (Lines 1-6)
- Purpose: Human-friendly introduction
- Audience: Human developers, maintainers, reviewers
- Prerequisites: None

### Section 2: Should You Read This? (Lines 9-13)
- **Critical:** Directs AI agents to BOOTSTRAP.md
- Confirms human audience

### Section 3: What is Spiral Developer? (Lines 17-33)
- Elevator pitch
- Core value
- One sentence summary
- The model (outer cadence + inner chain)

### Section 4: Quick Start (Lines 36-53)
- Step 1: Read this document
- Step 2: Check project status
- Step 3: For brownfield projects (if applicable)

### Section 5: Working in a Spiral Project (Lines 65-94)
- What to do next
- Typical workflow
- Key files to know

### Section 6: Adopting Spiral in Your Project (Lines 96-122)
- For new projects
- For existing projects (brownfield)
- For evaluation

### Section 7: Drill Down (Lines 126-135)
- Links to deeper documentation

### Section 8: Next Steps (Lines 138-146)
- Clear action items for different scenarios

### Section 9: Questions? (Lines 149-154)
- Support resources

---

## What to Look For

### ✅ Should Be Present

1. **Audience clarity:** The document should clearly state it's for humans and direct AI agents elsewhere
2. **Progressive structure:** Information should build logically, not assume prior knowledge
3. **Actionable steps:** Each section should lead to clear next actions
4. **Cross-references:** Should link to BOOTSTRAP.md for AI agents in multiple places
5. **Scannability:** Should use headings, bullet points, and code blocks effectively

### ❌ Should NOT Be Present

1. **AI-specific instructions:** No sections that only make sense for AI agents
2. **Overwhelming references:** Should not reference 15+ files before first action (old quickstart problem)
3. **Ambiguous audience:** Should not be unclear who the document is for
4. **Walls of text:** Should not have long, uninterrupted paragraphs

---

## Review Checklist

**Reviewer:** _______________________  
**Date:** _______________________

- [ ] I have read docs/quickstart.md completely
- [ ] I can explain what Spiral Developer is
- [ ] I can identify the first step for a new project
- [ ] I can identify the first step for an existing project
- [ ] The document provides a clear, progressive introduction
- [ ] The audience (human developers) is clear throughout
- [ ] AI agents are directed to BOOTSTRAP.md
- [ ] The structure is logical and easy to follow
- [ ] The prose is human-friendly and approachable

**Overall Assessment:**
- [ ] ✅ PASS - Document meets all acceptance criteria
- [ ] ⚠️ CONDITIONAL - Minor issues noted
- [ ] ❌ FAIL - Major issues prevent acceptance

**Comments/Feedback:**
________________________________________________________
________________________________________________________
________________________________________________________

---

## Related Artifacts

- **Source:** SRC-20260825-C0QMZ-2 (Bootstrap Onboarding Feedback)
- **Understanding:** UND-20260825-C0QMZ-3 (Bootstrap Onboarding Gap)
- **Request:** REQ-20260825-C0QMZ-4 (Separate Onboarding Paths)
- **Design:** DES-20260825-C0QMZ-5 (Separate Onboarding Paths Structure)
- **Implementation:** docs/quickstart.md
- **Self-Validation:** EVD-20260825-C0QMZ-6 (Onboarding Paths Self-Validation)
- **AI Validation:** EVD-20260825-C0QMZ-7 (AI Agent Validation of BOOTSTRAP.md)
- **Cycle:** CYC-20260825-C0QMZ-1 (Bootstrap Onboarding for Human and AI Agents)
