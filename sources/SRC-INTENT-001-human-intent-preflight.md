---
id: SRC-INTENT-001
---

# Source: Human direction on clarifying intent before consequential work

## Source kind

Connected human dogfooding discussion about a failure observed while using Spiral Developer on a project.

## What was actually expressed or observed

A task was copied from Trello, including its URL, into Codex. Codex read the task, assumed it understood what was wanted, and immediately began working. The interpretation was not clarified early enough. The resulting work included unnecessary effort and duplicated capability that already existed in the repository in another form.

The desired guardrail was clarified as follows:

- direct human input of consequential intent should first be reflected back to the human so the agent's understanding can be confirmed or corrected before implementation continues;
- after that clarification, the agent should verify the factual premises relevant to the task against project reality rather than assuming the human's description of the existing system is correct;
- this verification includes checking whether the requested capability already exists fully or partially, including under different terminology, structure, or abstraction;
- if repository reality materially changes the apparent task, the understanding should return to the human for clarification instead of the agent silently choosing a new interpretation;
- no additional "reality check" artifact type is wanted: repository/reality checking belongs inside the loop that forms the Understanding;
- intent itself may be clarified conversationally before it is crystallized as durable project evidence; every initial wording or conversational false start does not need to become a durable artifact.

The human remains authoritative about what outcome is wanted, but is not assumed to be infallible about the current state of the software.

## Integrity / version

Captured prospectively after the dogfooding incident and subsequent clarification of the desired process behavior.

## Provenance confidence

Explicit.

## Limitations / uncertainty

The source establishes the guardrail and the observed failure mode. It does not require a new artifact class, prescribe one repository-search implementation, or require human confirmation for trivial/local/reversible edits where the interpretation cannot materially change the work.
