# Quickstart

**Purpose:** Human-friendly introduction to Spiral Developer  
**Audience:** Human developers, maintainers, reviewers  
**Prerequisites:** None - this is your starting point

---

## Should You Read This?

**If you're an AI agent or automated tool:** See [BOOTSTRAP.md](../BOOTSTRAP.md) instead. That document provides a minimal, actionable path for non-human agents.

**If you're human:** Continue here. This guide will help you understand Spiral Developer and start using it effectively.

---

## Understanding Spiral Developer

Spiral Developer is an AI-native software development process built on a trust-but-verify model. AI systems operate with autonomy within a framework that verifies consequential changes before they become authoritative. Humans retain responsibility for intent, judgment, and accountability, while AI handles design, implementation, and provenance tracking.

**The model:**
```
Outer cadence (human-visible):
  Analyze → Plan → Act → Evaluate → (repeat)

Inner causal chain:
  source → understanding → request → design → implementation → verification → acceptance
```

### Your Role

As a human in the Spiral Developer process, **you are the authority** over:

- **Meaning:** What the project should achieve
- **Intent:** Why changes are needed
- **Acceptance:** Whether outcomes satisfy requirements
- **Judgment:** Risk appetite and consequential decisions

The AI agent handles execution, but **you** provide the direction and make the final calls.

---

## Prerequisites

### Tools Required

```bash
# Git (2.30+)
git --version  # Verify installed

# Python (3.10+ for CLI tools)
python3 --version

# RDF validation (pick one)
pip install rdflib pyshacl  # Python-based
# OR
brew install jena            # macOS, Java-based
# OR
sudo apt-get install jena    # Debian/Ubuntu
```

### Knowledge Required

- Basic Git: checkout, branch, commit, push, pull, merge
- Your project's domain and goals
- What "done" looks like for your features
- VS Code workspace management (optional but recommended)

---

## Getting Started

### Check Project Status

In your project folder run the following:
```bash
test -d ".spiral/" && echo "Exists"
```

- **If `.spiral/` exists:** Your project already uses Spiral. Proceed to [Your Workflow](#your-workflow).
- **If `.spiral/` does NOT exist:** Follow the setup steps below.

### Set Up Spiral Developer

1. **Clone the framework:**
   ```bash
   cd /path/to/your/workspace
   git clone https://github.com/muze-labs/spiral-developer.git .spiral-core
   ```

2. **Create your project in a separate folder:**
   ```bash
   mkdir my-project
   cd my-project
   git init
   ```

3. **(Recommended) Set up VS Code Workspace:**
   
   Use [VS Code Multi-Root Workspaces](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces):
   
   ```bash
   cat > my-project.code-workspace << 'EOF'
   {
     "folders": [
       {"path": "../.spiral-core"},
       {"path": "."}
     ],
     "settings": {}
   }
   EOF
   code my-project.code-workspace
   ```

4. **Initialize Spiral in your project:**
   
   Tell your AI agent:
   ```
   "Set up Spiral Developer in this project. The framework is available at ../.spiral-core/"
   ```
   
   The AI will create the `.spiral/` directory structure and link to the framework resources.

---

## Your Workflow

### The Human Loop

Your workflow follows these 6 steps:

#### Step 1: Provide Initial Request

**You say:**
```
"I want to add user authentication to the app."
"We need to fix the payment processing bug."
"Let's refactor the data layer for better performance."
```

The AI responds with a **pre-flight checkpoint:**

```
**My understanding:** [concrete outcome]
**Current effective behavior:** [what system does now]
**Evidenced gap:** [proof it's not satisfied]
**Material assumptions:** [list]

Is this correct?
```

#### Step 2: Confirm or Correct Understanding

**Your job:** Review the AI's understanding and either:
- **Confirm:** "Yes, that's correct. Proceed."
- **Correct:** "No, I meant [clarification]."
- **Question:** "I'm not sure about [assumption]. What do you think?"

**Important:** If the AI's understanding is wrong, **do not let it proceed**. Clarify first.

#### Step 3: Confirm the Cycle Goal

After you confirm understanding, the AI proposes a **cycle goal** and you must explicitly accept it.

#### Step 4: Periodic Check-ins

The AI will ask you questions during implementation. **Answer them.**

#### Step 5: Evaluate the Cycle

When the AI presents completed work, **review and accept or request changes.**

#### Step 6: Review and Merge

**You must merge PRs.** The AI cannot merge to main.

### Typical Workflow for Repository-Changing Work

1. Agree on a **cycle goal** with your team
2. The AI will create a cycle branch: `spiral/CYC-YYYYMMDD-WORKSPACE-N-short-goal`
3. The AI will create causal artifacts as needed (SRC, UND, REQ, DES, IMP, EVD)
4. The AI will verify branch matches cycle ID before each commit
5. The AI will commit, push, and create a PR for review

### Key Files to Know

| File | Purpose |
|------|---------|
| `AGENTS.md` | AI agent operating instructions |
| `.spiral/project-context.md` | Project-level context and intake state |
| `.spiral/cycles/CYC-*.md` | Active and accepted cycles |
| `docs/process.md` | Canonical development lifecycle |

---

## Your Responsibilities

### What You MUST Do

1. **Confirm Understanding** - Verify AI's interpretation matches your intent
2. **Confirm Cycle Goal** - Explicitly accept proposed cycle goal
3. **Accept or Reject** - Review cycle results, decide if goal is met
4. **Merge PRs** - You must merge; AI cannot merge to main

### What You DON'T Need to Do

The AI handles:
- Writing artifact files (SRC, UND, REQ, etc.)
- Creating Turtle/RDF causal graphs
- Running validation checks
- Managing Git branches (except merging to main)
- Writing commit messages
- Running tests and verification
- Maintaining causal history
- Creating PR descriptions

---

## Adoption Paths

### Brownfield Intake Checklist

When starting a brownfield project these are the questions to expect you will need an answer for.

1. **Project Purpose** - What does this project do?
2. **Important Outcomes** - What matters most?
3. **Prior Decisions** - What architectural choices were made?
4. **Constraints** - What limitations exist?
5. **Known Problems** - What issues are tolerated?
6. **Future Direction** - Where is this project going?
7. **Feedback Sources** - How do you get user feedback?

**Your job:** Answer these. The AI records them as intake artifacts.

### For Existing Projects (Brownfield)

Before your first normal Spiral cycle:

1. **Complete brownfield intake** - Answer the 7 questions above, or see [docs/brownfield-intake.md](../docs/brownfield-intake.md)
2. **Document project context** - The AI will create a project-context.md file that should contain information about the project readable by a human.
3. **Identify active culture** - If applicable, adopt a culture profile
4. **Validate with a small cycle** - Try Spiral on one bounded piece of work

### For Evaluation

If you're evaluating Spiral Developer for potential adoption:

1. Read this quickstart
2. Explore the [docs/](.) directory for details
3. Try a small, low-risk cycle to test the process
4. Assess whether the verification architecture works for your team

---

## Key Actions & Commands

### Key Commands YOU Run

| Action | Command |
|--------|---------|
| Get framework | `git clone https://github.com/muze-labs/spiral-developer.git .spiral-core` |
| Create project | `mkdir project && cd project && git init` |
| VS Code workspace | Create `.code-workspace` with both folders |
| Review changes | `git checkout spiral/CYC-* && git diff main` |
| Merge cycle | `git merge --no-ff spiral/CYC-*` |

### Drill Down

Need more detail? Explore these next:

- **[docs/vision.md](../docs/vision.md)** - Why Spiral Developer exists and its core principles
- **[docs/trust-model.md](../docs/trust-model.md)** - The trust-but-verify model explained
- **[docs/process.md](../docs/process.md)** - The canonical development lifecycle
- **[docs/cycles.md](../docs/cycles.md)** - The outer Analyze/Plan/Act/Evaluate cadence
- **[AGENTS.md](../AGENTS.md)** - AI agent operating instructions (for reference)

---

## Next Steps & Resources

### Next Steps

Once you've read through this quickstart:

1. **AI agents:** You should be reading [BOOTSTRAP.md](../BOOTSTRAP.md) instead
2. **New projects:** Clone framework, set up workspace, and start your first cycle
3. **Existing projects:** Complete brownfield intake, then start your first cycle
4. **Evaluators:** Try a small experiment and assess the results

### Resources

- **Framework:** https://github.com/muze-labs/spiral-developer
- **VS Code Workspaces:** https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces
- **Framework Docs:** Available in `.spiral-core/docs/` after cloning

### Questions?

- Open a GitHub issue for technical questions
- Open a GitHub discussion for general discussion
- Check the [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines

---

*AI agents: See [BOOTSTRAP.md](../BOOTSTRAP.md) for your onboarding path*
