# Plan Cycle Prompt

Use this when no active cycle exists, after a cycle has been evaluated/accepted, or when the human explicitly asks to re-plan the current cycle.

Treat this as an interview, not a form dump. Read current project context and prior evaluation/risk evidence first, then ask only the questions needed to agree a coherent next goal.

## 1. Analyze current state

Summarize briefly:

- relevant project goal/context;
- previous cycle outcome when any;
- prioritized risks/metric gaps/feedback that appear relevant;
- important uncertainty or consequence that makes the next choice matter.

Do not assume the newest request is automatically the highest-priority direction.

## 2. Propose one cycle goal

Propose one bounded goal expressed as an outcome, risk reduction, or uncertainty resolution—not as an arbitrary task bundle.

Present:

**Proposed cycle goal:** …
**Why now:** …
**Current evidence / starting state:** …
**Evaluation basis:** …
**Likely work:** …
**Explicit non-goals:** …
**Material assumptions / pause conditions:** …

Ask the human to confirm, correct, narrow, or replace the goal.

For consequential direct human input, include the normal Understanding/current effective behavior/evidenced gap/material assumptions checkpoint when applicable. If the human confirms that complete checkpoint here, do not ask for duplicate confirmation later merely because implementation decomposes into several tasks.

## 3. Open the cycle

After confirmation:

- create/update the `CYC-*` Markdown record from `templates/CYCLE.md` and companion identity resource from `templates/CYCLE.ttl`;
- for ordinary repository-changing work, create/use one `spiral/CYC-...` cycle branch;
- define only the initial likely work; do not pretend the task decomposition is exhaustive;
- begin Act using normal Source/Understanding/Request/Design/Implementation/Evidence/Acceptance artifacts as needed.

During Act, do not absorb unrelated newly discovered work. Preserve it for evaluation/next-cycle planning unless it is necessary to achieve the current goal, obtain required evaluation evidence, or repair a regression caused by the cycle.
