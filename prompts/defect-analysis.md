# Defect Analysis Prompt

Treat this defect as evidence about the software-producing system.

1. Reproduce and characterize the failure.
2. Identify the request/acceptance behavior that is violated.
3. Trace the relevant design and implementation chain.
4. Identify which verification should have detected the problem and why it did not.
5. Find the earliest meaningful root cause: intent, context, design, constraint, abstraction/boundary, verification, acceptance, dependency/tool/model, or implementation.
6. Prefer correcting that upstream cause over directly patching generated code.
7. Mark downstream artifacts affected by the correction as suspect/revise/regenerate as needed.
8. Add evidence for the original defect and useful related variants.
9. Record what the environment learned so the same class of defect is less likely to recur.
