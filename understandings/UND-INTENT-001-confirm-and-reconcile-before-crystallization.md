---
id: UND-INTENT-001
---

# Understanding: Confirm intent and reconcile it with project reality before crystallization

## Current interpretation

For consequential direct human work requests, Spiral should not treat the first wording as implementation-ready merely because it is explicit or arrives through a task system such as Trello.

There are two different claims to establish before implementation commits to a direction:

1. **Did the agent understand what the human wants?** The human is authoritative here. The agent should reflect the intended outcome and material assumptions back to the human and obtain confirmation or correction before consequential implementation continues.
2. **Does the interpreted request match project reality?** Neither the human nor the agent should be assumed correct here. The agent should inspect relevant repository evidence and behavior, including existing/overlapping capability, tests, project artifacts, documentation, and history where useful.

The repository/reality check is not a new artifact type. It is part of forming a trustworthy Understanding. If that check reveals that the task already exists, overlaps another capability, or rests on an incorrect premise in a way that materially changes the work, the Understanding is not yet settled: return the finding to the human and clarify again.

The pre-crystallization conversation may freely improve the wording of intent. Spiral should preserve causally important clarification, but should not require every shorthand phrase, mistaken premise, or conversational correction to become a durable artifact. Once an intent/understanding has become durable and has caused consequential accepted work, later changes are prospective history rather than silent rewrites.

## Sources considered

- `SRC-INTENT-001`, the explicit human dogfooding feedback and clarification.
- The current repository's existing framing-check, source/understanding, and brownfield guidance.

## Repository reality / overlap audit

The existing process already contains useful adjacent mechanisms:

- `docs/ai-collaboration.md` treats understanding as a claim and supports clarification/reframing;
- `docs/process.md` distinguishes source, understanding, and request;
- `docs/brownfield.md` requires characterizing relevant existing behavior rather than inventing legacy intent;
- `prompts/start-change.md` performs framing checks before consequential design;
- `docs/review.md` asks whether request/design framing assumptions were actually tested.

However, none of these currently makes the observed preflight explicit: **confirm the agent's interpretation of consequential direct human intent with the human before acting, then reconcile that interpretation with existing project reality and overlapping capability before crystallizing the change.** This gap allows an agent to optimize confidently inside both a misunderstood request and an incorrect human model of the repository.

## Clarifications / reframing

| Question / assumption | Alternative or clarification | Evidence / resolution |
|---|---|---|
| Must raw direct human input immediately become durable source/intent evidence? | No. Clarify conversationally first unless preserving the original source is itself causally important. | Explicit human direction. |
| Is human confirmation enough to make implementation safe? | No. It establishes intended outcome, not factual correctness about the current software. | Dogfooding incident and explicit clarification. |
| Does repository reconnaissance need a new artifact? | No. It belongs inside the loop that forms the Understanding; preserve findings only when they are causally useful. | Explicit human direction. |
| Is exact-text search sufficient to detect existing work? | No. Existing or partial capability may use different terminology, structure, APIs, tests, or abstractions. | Observed duplication failure. |
| Must every tiny edit stop for human confirmation? | No. Apply the guardrail when materially different interpretations or existing-state assumptions could cause materially different work. | Explicit scope limitation in source. |

## Provenance confidence

Evidenced.

## Remaining uncertainty

Dogfooding should determine the right threshold for "consequential" and how much repository reconnaissance is enough in different project sizes. The process should avoid turning the guardrail into a ritualistic confirmation step that adds no information.

## Consequence

Strengthen Spiral's start-of-change guardrail so consequential direct human input is clarified with the human before execution, then reconciled with repository reality and existing/overlapping capability before durable Understanding/Request artifacts drive implementation.
