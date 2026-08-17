---
id: LES-013
---

# Lesson: Validate cycle branch state instead of relying on memory

## Observation / evidence

Interpreted evidence: `UND-PROCESS-002` (from `SRC-PROCESS-002`).

During SimplyStore dogfooding, several later cycles were executed while the repository remained on a branch named for an earlier cycle. The process documented one-cycle-one-branch, but neither prompts nor evaluation required the agent to compare the active `CYC-*` identity with actual Git state. The mismatch therefore persisted unnoticed.

## Lesson

A branch convention that matters to provenance cannot remain a remembered instruction. Spiral should mechanically inspect the current branch at cycle start, before consequential semantic commits, and at evaluation, and compare it with the active cycle identity.

## Scope

Repository-changing Spiral cycles.

## Confidence / limits

High confidence that active validation would have exposed the observed dogfooding error. This does not require a universal helper program: a direct Git-state check is sufficient, while project-local tooling may automate it.

## Proposed consequence

Make branch/cycle validation explicit in normative Git/cycle guidance, prompts, agent instructions, and the cycle record. Preserve explicit exceptions for non-repository or unusual integration boundaries.
