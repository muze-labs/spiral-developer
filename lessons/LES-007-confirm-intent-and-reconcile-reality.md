---
id: LES-007
---

# Lesson: Confirm intent and reconcile it with reality before acting

## Observation / evidence

During dogfooding, an agent received a pasted Trello task, assumed it understood the intended change, and immediately implemented it. Clarification arrived too late. The work duplicated capability already present in the repository and included unnecessary implementation.

The failure had two independent causes: the agent had not established that its interpretation matched the human's intent, and neither party had reconciled the task description with the actual existing software before committing to a solution.

## Lesson

For consequential work, direct human input is not implementation-ready by default. First confirm the intended outcome with the human. Then inspect project reality—including existing or overlapping capability—while forming the Understanding. If reality materially changes the interpretation, return to clarification before implementation.

The human is authoritative about desired intent, not automatically about factual repository state. The agent is responsible for checking the latter rather than treating the task description as a complete model of the system.

## Scope

Spiral-process candidate. Applies to consequential new/change requests, especially brownfield work and task descriptions copied from external systems.

## Confidence / limits

High confidence in the failure mode and guardrail. The significance threshold should be tuned through dogfooding so routine local edits do not acquire needless confirmation ceremony.

## Proposed consequence

Make "confirm intent, then reconcile with project reality" an explicit start-of-change preflight. Keep repository reconnaissance inside Understanding formation rather than creating another artifact type.

## Outcome after adoption

To be evaluated through dogfooding. Watch for both accidental duplication/misinterpretation and the opposite failure: agents asking for confirmation when the work is genuinely trivial and unambiguous.
