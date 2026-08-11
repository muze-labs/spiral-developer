# Quickstart

Use Spiral Developer on one bounded real feature. Do not bootstrap a heavyweight process first.

## 1. Add the project area

A practical initial structure is:

```text
.spiral/
  project.ttl
  culture.md
  culture.ttl
  project-context.md
  sources/
  understandings/
  requests/
  feedback/
  designs/
  implementations/
  evidence/
  acceptance/
  legacy/
  defects/
  cycles/
```

Copy only templates that will be used. Do not create empty artifacts for completeness.

Start `.spiral/project.ttl` from `templates/PROJECT.ttl` and `.spiral/culture.ttl` from `templates/CULTURE.ttl`. Create other companion `.ttl` resources beside human-facing artifacts as they are introduced; `examples/causal-graph.ttl` shows the logical RDF union.

## 2. Establish culture and project context

Capture durable project context and point at organization/project principles the agent should preserve.

Do not attempt to reconstruct complete project history.

## 3. Start a feature branch

Create a branch from the authoritative branch, normally:

```text
spiral/REQ-001-short-name
```

From here onward, normal causal commits are immutable evidence.

## 4. Capture origin, understanding, and request as needed

Start from the best available evidence for why the change is wanted. This may already be the current human instruction, or it may be a conversation, email, issue, meeting, contract, regulation, observation, inherited requirement, or external artifact.

When the source identity or the interpretation could matter later, create `.spiral/sources/SRC-001.md` from `templates/SOURCE.md` and `.spiral/sources/SRC-001.ttl` from `templates/SOURCE.ttl`. Record whether the primary evidence is `sd:Retained`, `sd:Referenced`, or `sd:Unavailable`, and declare the source claim's provenance confidence.

When meaning had to be interpreted, clarified, challenged, or reframed, create `.spiral/understandings/UND-001.md` from `templates/UNDERSTANDING.md` and `.spiral/understandings/UND-001.ttl` from `templates/UNDERSTANDING.ttl`. Link it with `sd:interprets` to the exact source version(s) it interprets and declare the interpretation's provenance confidence.

Then create `.spiral/requests/REQ-001.md` from `templates/REQUEST.md` and a companion Turtle resource. A good request expresses the operationalized intent and observable desired outcomes without prematurely prescribing implementation. When an `UND-*` artifact materially caused it, link the request to that exact version with `sd:derivedFrom`.

Do not create `SRC-*` or `UND-*` artifacts merely to fill folders. For a simple direct request, `REQ-*` may still be the first durable artifact.

Commit each crystallized upstream artifact before creating downstream references to it.

## 5. Check the frame, then find the nearest important uncertainty

If the request proposes a consequential solution or boundary, briefly test whether that premise is established before designing around it. Do not do this for every local decision. Use it where a different framing could materially change product direction, architecture, schema, trust boundaries, irreversible work, or acceptance.

Then find the nearest important uncertainty.

Classify risks as blocker, near-term, deferred, or existential.

Resolve the blocker/near-term risk. Record later risks. Pull a deferred risk forward only if it can invalidate the current direction.

## 6. Get meaningful interaction early

For normal Muze web work, create functioning UI quickly enough that intended users can spend real time with the feature.

Optimize first for behavioral fidelity and learning, not polish.

Record important feedback. If it changes the interpretation of the need, update or supersede the relevant `UND-*` artifact first; if the operationalized outcome changes, commit a new request state. Never rewrite the earlier causal history.

## 7. Create design and causal links

Create a design artifact from `templates/DESIGN.md` and a companion Turtle resource from `templates/ARTIFACT.ttl`. In the Turtle resource, link the design to the exact request commit it satisfies or derives from.

Commit the design + companion Turtle resource.

## 8. Implement a real vertical slice

Implement the smallest useful real path.

Represent the implementation as an `IMP-*` Turtle resource when it is useful to trace as a unit; `templates/IMPLEMENTATION.ttl` is the starting point. Link it to the exact design commit and use repeatable `sd:implementationLocation` locators when code-location interrogation will be useful. Multiple `IMP-*` concerns may overlap on the same location.

On the first implementation version there is no lineage edge. On later material revisions of a governed implementation, preserve current effective causal references and add `sd:transforms` to the immediate predecessor, `sd:changeCausedBy` to the transition reason, and `sd:implementationChangeKind`. Do not replay or copy the full history into the current resource.

Commit the implementation + companion Turtle resource. See `implementation-lineage.md`.

## 9. Verify and accept

Create verification evidence and a companion Turtle resource that points to the implementation commit it verifies.

Create acceptance evidence and a companion Turtle resource that points to the request version it accepts and the relevant evidence/design versions.

Commit these as subsequent causal steps so their upstream hashes already exist.

## 10. Prepare the pull request

Fill the PR with the causal case, not merely the code summary.

Run normal project CI plus any graph checks available.

A human reviews source/understanding provenance where material, intent, design, evidence, risk, and behavior. Direct code review is used where it provides valuable evidence.

## 11. Merge, do not rewrite

Integrate with a normal merge commit.

Never squash/rebase causal feature history merely for tidiness.

## First experiment questions

After the feature is merged, ask:

- Did the graph help the AI or reviewer reason about the change?
- Was the exact-version provenance useful?
- Did intended-user interaction change our understanding?
- Where interpretation mattered, could we distinguish source evidence from the understanding derived from it?
- Did missing primary provenance remain visible instead of being silently reconstructed?
- Did the AI expose any consequential framing assumption before it became expensive downstream?
- Did we confuse a well-elaborated solution with evidence that it was the right solution?
- Did any artifact become ceremonial bookkeeping?
- Could a defect or disagreement be traced to the correct upstream layer?
- Could current implementation justification be distinguished from historical reasons that had been superseded?
- On a repeated change to a governed area, how much old history did the agent actually need to reload?
- Did the code remain simple and economical to change?

Adjust the process before adding more automation.
