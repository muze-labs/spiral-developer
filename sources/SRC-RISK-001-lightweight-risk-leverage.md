---
id: SRC-RISK-001
---

# Source: Use downstream leverage to prioritize development risk

## Human direction

Ground Spiral Developer's risk assessment more closely in practical risk-driven software development without adding heavy ceremony.

The important observation is that the impact of a wrong assumption depends strongly on **where it sits in the development chain**. An incorrect strategy or business assumption can invalidate most downstream work, while a wrong implementation detail is usually much cheaper to correct locally.

Use a rough recurring division when reasoning about important assumptions:

1. **Strategy / business** — assumptions about the problem, audience, value, direction, or business outcome.
2. **Domain / architecture** — assumptions about the conceptual model, boundaries, data model, architecture, or major dependencies.
3. **Workflow / interface** — assumptions about how people or systems interact with the product and how work should flow.
4. **Implementation** — local technical choices whose consequences are normally more contained and reversible.

For an important assumption or uncertainty, consider:

- how uncertain it is;
- how much downstream work depends on it / its likely blast radius if wrong;
- how expensive it would be to discover the mistake later;
- the cheapest useful way to falsify or reduce the uncertainty now.

Prefer cycles that cheaply test uncertain assumptions with large downstream consequences. Do not spend equivalent effort de-risking local implementation choices that are cheap to reverse.

Use this mainly when **selecting a cycle** and when **closing/evaluating a cycle** reveals new high-leverage assumptions. Avoid scores, probability/impact matrices, formal risk registers, or mandatory new risk artifacts unless later dogfooding shows they earn their complexity.
