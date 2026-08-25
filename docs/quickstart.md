# Quickstart

**Purpose:** Human-friendly introduction to Spiral Developer  
**Audience:** Human developers, maintainers, reviewers  
**Prerequisites:** None - this is your starting point

---

## Should You Read This?

**If you're an AI agent or automated tool:** See [BOOTSTRAP.md](../BOOTSTRAP.md) instead. That document provides a minimal, actionable path for non-human agents.

**If you're human:** Continue here. This guide will help you understand Spiral Developer and start using it effectively.

---

## What is Spiral Developer?

**Elevator pitch:** Spiral Developer is an **AI-native software development process** built around **trust but verify**.

**Core value:** Autonomy through verification architecture. AI systems can operate with substantial freedom because the surrounding process is designed to verify consequential claims before they become authoritative.

**One sentence:** Humans retain responsibility for intent, judgment, and accountability; AI handles design, implementation, and provenance bookkeeping with autonomy.

**The model:**
```
Outer cadence (human-visible):
  Analyze → Plan → Act → Evaluate → (repeat)

Inner causal chain:
  source → understanding → request → design → implementation → verification → acceptance
```

---

## Quick Start

### Step 1: Read This Document

You're doing it now! This quickstart provides a progressive introduction. Read through the sections that follow to understand the basics.

### Step 2: Check Project Status

Check if your project has Spiral Developer set up:

```bash
# Check if .spiral/ directory exists
ls -la .spiral/ 2>/dev/null
```

- **If `.spiral/` exists:** Your project already uses Spiral. See ["Working in a Spiral Project"](#working-in-a-spiral-project) below.
- **If `.spiral/` does NOT exist:** You're starting fresh. See ["Adopting Spiral in Your Project"](#adopting-spiral-in-your-project) below.

### Step 3: For Brownfield Projects

If you're bringing Spiral to an existing project, complete the **guided brownfield intake** before starting your first cycle:

1. Read [docs/brownfield-intake.md](../docs/brownfield-intake.md)
2. Work through the 11 required intake topics
3. Document the results in `.spiral/project-context.md`
4. Mark intake status as **Complete**

---

## Working in a Spiral Project

If `.spiral/` already exists in your project, Spiral Developer is already set up.

### What to Do Next

1. **Read AGENTS.md** - This contains the operating instructions for AI agents working in your project
2. **Check active cycles** - Look in `.spiral/cycles/` for any in-progress work
3. **Follow existing conventions** - Use the same artifact structure and naming as other cycles

### Typical Workflow

For repository-changing work:

1. Agree on a **cycle goal** with your team
2. Create a cycle branch: `spiral/CYC-YYYYMMDD-WORKSPACE-N-short-goal`
3. Create causal artifacts as needed (SRC, UND, REQ, DES, IMP, EVD)
4. Verify branch matches cycle ID before each commit
5. Commit, push, and create a PR for review

### Key Files to Know

| File | Purpose |
|------|---------|
| `AGENTS.md` | AI agent operating instructions |
| `.spiral/project-context.md` | Project-level context and intake state |
| `.spiral/cycles/CYC-*.md` | Active and accepted cycles |
| `docs/process.md` | Canonical development lifecycle |

---

## Adopting Spiral in Your Project

### For New Projects

Start here: This quickstart document is your entry point. Work through it to understand Spiral, then:

1. Set up your `.spiral/` directory structure
2. Complete project intake (even for greenfield)
3. Start your first cycle

### For Existing Projects (Brownfield)

Before your first normal Spiral cycle:

1. **Complete brownfield intake** - See [docs/brownfield-intake.md](../docs/brownfield-intake.md)
2. **Document project context** - Create `.spiral/project-context.md`
3. **Identify active culture** - If applicable, adopt a culture profile
4. **Validate with a small cycle** - Try Spiral on one bounded piece of work

### For Evaluation

If you're evaluating Spiral Developer for potential adoption:

1. Read this quickstart
2. Explore the [docs/](.) directory for details
3. Try a small, low-risk cycle to test the process
4. Assess whether the verification architecture works for your team

---

## Drill Down

Need more detail? Explore these next:

- **[docs/vision.md](../docs/vision.md)** - Why Spiral Developer exists and its core principles
- **[docs/trust-model.md](../docs/trust-model.md)** - The trust-but-verify model explained
- **[docs/process.md](../docs/process.md)** - The canonical development lifecycle
- **[docs/cycles.md](../docs/cycles.md)** - The outer Analyze/Plan/Act/Evaluate cadence
- **[AGENTS.md](../AGENTS.md)** - AI agent operating instructions (for reference)

---

## Next Steps

Once you've read through this quickstart:

1. **AI agents:** You should be reading [BOOTSTRAP.md](../BOOTSTRAP.md) instead
2. **New projects:** Complete intake and start your first cycle
3. **Existing projects:** Complete brownfield intake, then start your first cycle
4. **Evaluators:** Try a small experiment and assess the results

---

## Questions?

- Open a GitHub issue for technical questions
- Open a GitHub discussion for general discussion
- Check the [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines

---

*AI agents: See [BOOTSTRAP.md](../BOOTSTRAP.md) for your onboarding path*
