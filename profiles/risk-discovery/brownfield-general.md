# Risk-discovery profile: Brownfield general

Use this as a prompt for investigation, not a checklist and not a claim that these risks exist.

Consider whether the project has material exposure around:

- hidden or indirect behavior that is easy to duplicate or break;
- compatibility promises encoded mainly in old behavior/tests;
- stale assumptions about dependencies, runtime, data, or deployment;
- consequential decisions whose original rationale or current reversibility is unclear;
- important behavior with weak characterization or observability;
- knowledge concentrated in a few people or poorly understood subsystems;
- deferred migrations/deprecations whose assumptions have changed;
- accumulated workarounds that interact in ways local changes may not reveal.

Prefer evidence about effective behavior and current dependencies over inference from file structure. Surface only concerns that are significant for this project.
