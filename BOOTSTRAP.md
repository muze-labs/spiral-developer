# BOOTSTRAP.md

**Purpose:** Minimal onboarding for AI/automated agents in Spiral Developer projects  
**Audience:** AI agents, automated tools, non-human software agents  
**Prerequisites:** Git installed, basic understanding of software development  

---

## What You Are

You are an AI or automated agent operating in a **Spiral Developer** project. Your goal is to complete a minimal Spiral cycle autonomously while preserving causal provenance.

---

## Minimal Context

Spiral Developer is a **trust-but-verify**, AI-native development process. As an AI agent, you must:

- Preserve causal provenance for all consequential work
- Follow the collaboration sequence: **discourse → commitment → execution**
- Stop and return to discourse when intent/meaning is uncertain
- Verify gap before modifying product behavior
- Never rewrite Git history (no amend, rebase, squash, force-push)

**Key files:**
- `AGENTS.md` - Your operating instructions (read this first)
- `.spiral/project-context.md` - Project-level context and intake state
- `.spiral/cycles/` - Active and accepted cycles

---

## First Steps

### Step 1: Read Your Operating Instructions
```
Read AGENTS.md completely before starting any work.
```

### Step 2: Check Project Context
```
Check if .spiral/project-context.md exists:
- If YES: Project has completed brownfield intake. Note the intake status.
- If NO: Project may need intake. Check docs/brownfield-intake.md.
```

### Step 3: Check Active Cycles
```
List active cycles: ls .spiral/cycles/*.ttl
Check status: grep "sd:status" .spiral/cycles/*.ttl
- sd:Active = Cycle in progress
- sd:Accepted = Cycle completed, ready for integration
```

### Step 4: Allocate Artifact ID (for new work)
```
Initialize workspace (if needed): spiral workspace init
Allocate artifact: spiral allocate <TYPE>
Example: spiral allocate source
Returns: SRC-YYYYMMDD-WORKSPACE-N
```

### Step 5: Create Causal Artifacts in Order
```
For new work, create artifacts in this order:
1. SRC-* (Source) - Crystallize origin evidence
2. UND-* (Understanding) - Interpret what it means
3. REQ-* (Request) - Formalize what should be done
4. DES-* (Design) - How to satisfy the request
5. IMP-* (Implementation) - The actual change
6. EVD-* (Evidence) - Verification that it works

For each artifact:
- Create .md file with frontmatter
- Create .ttl file with machine-readable metadata
- Include sd:historicalReference to the commit containing it
```

---

## Validation Checklist

Before committing causal artifacts, verify:

- [ ] Branch name matches cycle ID (e.g., `spiral/CYC-YYYYMMDD-WORKSPACE-N-...`)
- [ ] All .ttl files parse as valid Turtle
- [ ] All sd:historicalReference targets are Git ancestors of the commit
- [ ] Artifact IDs follow TYPE-YYYYMMDD-WORKSPACE-N format
- [ ] No commits are amended, rebased, squashed, or force-pushed

---

## When to Stop and Ask

Return to **discourse** (ask human for clarification) if:

- Intent, meaning, or framing is uncertain
- A materially different framing could change the commitment or downstream work
- You cannot establish both Understanding and evidenced gap before product modification
- The request is ambiguous or underspecified

Stop and **verify gap** before modifying if:

- Consequential product behavior might already satisfy the Understanding
- You need to investigate effective behavior (not just code existence)
- The task involves changes to production code, configuration, schema, or migrations

Report instead of implementing if:

- Existing behavior already satisfies the need
- No relevant gap can be established
- You are unsure whether a gap exists

---

## Links to Full Documentation

For humans: See [docs/quickstart.md](docs/quickstart.md)  
Full process: [docs/process.md](docs/process.md)  
Trust model: [docs/trust-model.md](docs/trust-model.md)  
Ontology: [ontology/spiral-developer.ttl](ontology/spiral-developer.ttl)  
All docs: [docs/](docs/)
