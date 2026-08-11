# Interrogate Implementation Provenance Prompt

Answer a question such as “Why is this code here?” or “How did this behavior get this way?” using Spiral Developer provenance.

1. Resolve the code location/question to the relevant current `IMP-*` concern(s). Allow several implementation artifacts to overlap the same code region.
2. First answer **current/effective provenance**: traverse only the current implementation's causal justification relations (`implements`, `derivedFrom`, `supports`, `constrainedBy`, etc.) and explain the independent surviving causes that still justify present semantics.
3. Do not treat `sd:transforms` or `sd:changeCausedBy` as current justification. Historical reachability is not evidence that an old cause still applies.
4. If the user asks how the code evolved, or current provenance is insufficient, follow `sd:transforms` backward one version at a time. At each relevant version inspect `sd:changeCausedBy`, `sd:implementationChangeKind`, and changes in effective causal references.
5. Distinguish clearly between:
   - causes that still justify current behavior;
   - transition events that explain a historical change;
   - reasons that were superseded or removed;
   - behavior-preserving refactors that moved/reshaped code without intended semantic change;
   - unknown or missing lineage.
6. Use Git to retrieve exact referenced historical artifact versions. Git blame may help locate candidate history but is not itself causal evidence.
7. Stop historical traversal once the question is answered. Do not load the full lineage by default.
8. Cite exact artifact IDs/versions and relevant evidence. Prefer an explicit unknown over reconstructing a plausible story.

A useful answer can contain several causal branches. Do not force a current code fragment into one tidy chain when several independent decisions survive in it.
