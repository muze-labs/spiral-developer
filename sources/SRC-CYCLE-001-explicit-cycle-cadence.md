---
id: SRC-CYCLE-001
---

# Source: Make the outer Spiral cycle the visible unit of work

## Human direction

Spiral Developer already uses an iterative Analyze/Plan/Act/Evaluate-style feedback idea, but in practical use the visible interaction has collapsed into giving an AI a task and watching it execute a feature/change lifecycle.

Make the outer cycle explicit and usable:

- begin a cycle by agreeing a clear **cycle goal**: one coherent project outcome, risk reduction, or important uncertainty to resolve;
- a cycle may require multiple tasks, causal artifacts, and commits;
- tasks are implementation/work decomposition inside the cycle, not separate human review boundaries;
- ordinary repository-changing work should normally use one cycle branch rather than one branch per subtask;
- keep cycle scope stable during execution: newly discovered unrelated work is normally recorded for later planning rather than silently absorbed;
- work discovered to be necessary to satisfy the agreed cycle goal, or to repair a regression caused by the cycle, may remain inside the cycle;
- finish execution by entering an explicit **evaluation phase** in which the human can inspect the integrated result and evidence and give feedback;
- evaluation feedback that shows the agreed goal is not yet met keeps the same cycle open for correction;
- feedback that introduces genuinely new direction should normally become input to the next cycle rather than scope-creeping the current one;
- after evaluation/acceptance, switch back to an interview-style reorientation/planning mode and agree the next cycle goal.

The cycle should remain a learning/integration boundary, not become a sprint-sized arbitrary task bucket. Preserve the existing causal artifacts, per-change Understanding/evidenced-gap gate, verification, acceptance, immutable Git history, and human authority over consequential direction.

Keep the system usable. Do not introduce a workflow engine, task tracker, formal cycle state machine, or mandatory branch per subtask. Prefer clear prompts, Markdown, and existing `CYC-*` concepts unless later dogfooding demonstrates a need for more structure.
