---
id: SRC-PROCESS-003
---

# Source: Dogfooding feedback on plan drift and recency bias

## Human direction

During continued SimplyStore dogfooding with the updated Spiral Developer process, the human observed that the cycle mechanics were working but the AI had begun to lose sight of the larger implementation plan:

> “the spiral development cycle works, but the AI is prone to be distracted/derailed because of recent work/discoveries, and forgetting to keep an eye on the bigger plan.”

The immediate example was that, after an adversarial OD-JSONTag durability cycle exposed the boundary where framing validation could no longer detect well-formed alteration, the AI began jumping toward full integrity checks. The human explicitly asked it to re-read the original SimplyStore implementation plan before choosing the next cycle.

The human then requested that the latest Spiral Developer repository be updated to address this process weakness.

## Provenance note

The relevant human wording and concrete SimplyStore dogfooding example are retained here because they directly motivate a Spiral process change. The original conversational transport is not required to interpret the observation.
