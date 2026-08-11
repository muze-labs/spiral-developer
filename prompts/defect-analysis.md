# Defect Analysis Prompt

Treat this defect as evidence about the software-producing system.

1. Create/use a dedicated defect branch when the defect requires a change.
2. Reproduce and characterize the failure.
3. Identify the request/acceptance behavior that is violated.
4. Start from current effective implementation provenance. Traverse older `sd:transforms` lineage only when needed to explain how the behavior accumulated; inspect `sd:changeCausedBy` and change kind at each relevant transition. Continue above the request into understanding/source provenance when the defect may originate there.
5. Identify which verification should have detected the problem and why it did not.
6. Find the earliest meaningful root cause: source evidence/provenance, interpretation/understanding, intent/request, context, design, constraint, abstraction/boundary, verification, acceptance, dependency/tool/model, stale/missing effective provenance, broken implementation lineage, or implementation.
7. Prefer correcting that upstream cause over directly patching generated code.
8. Make corrections in new commits; never rewrite the original causal commits.
9. Mark downstream artifacts affected by the correction as suspect/revise/regenerate as needed.
10. Add evidence for the original defect and useful related variants.
11. Ensure the corrected implementation version retains immediate lineage and truthful current effective provenance; do not leave superseded historical causes presented as current justification.
12. Record what the environment learned so the same class of defect is less likely to recur.
