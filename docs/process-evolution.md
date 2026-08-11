# Process Evolution and Lessons Learned

Spiral Developer is not a fixed methodology.

Its trust invariants, defaults, culture profiles, artifact model, and tooling are all hypotheses about how to create software whose production history deserves justified trust. Experience may show that some of them are incomplete, too expensive, misleading, or simply wrong.

The process should therefore be able to **learn without falsifying its own past**.

## Lessons are first-class claims

Use a `LES-*` lesson artifact when an observation is likely to change how future work should be approached.

A lesson should distinguish:

- **what happened** — the concrete observation/evidence;
- **what we think it means** — the generalization;
- **where we think it applies** — local project, culture/profile, or Spiral process;
- **confidence and counterexamples** — how strongly the evidence supports the generalization;
- **proposed consequence** — what should change, if anything;
- **later outcome** — whether adopting the lesson helped, harmed, or needs revision.

Where possible, link a lesson to the exact evidence/artifact versions it generalizes from using normal causal references such as `sd:derivedFrom` or `sd:observes`. If the original evidence is external or unavailable, capture that provenance honestly rather than inventing it.

A lesson is **not automatically a rule**. It is evidence-informed advice that may justify a later change.

## Three propagation levels

A lesson can affect increasingly general layers:

### 1. Project practice

Use the lesson locally when the evidence is specific to this repository, product, team, or environment.

Examples:

- a particular integration needs a preflight check;
- this user group gives better feedback from a working prototype than static mockups;
- this codebase's generated schema is not safe to edit manually.

### 2. Culture profile

Promote a lesson into a culture profile when it repeatedly describes how a team or organization prefers to make underdetermined choices.

Culture remains defeasible. It should guide decisions when several trustworthy choices remain available, not masquerade as a universal trust invariant.

### 3. Spiral core/process

Change Spiral core only when the lesson affects justified trust, process integrity, verification, causal auditability, or another property the methodology itself claims to provide across projects.

A process-level change deserves stronger evidence than a local workaround. Prefer repeated observations, a clear failure mode, or a direct contradiction of an existing invariant.

## Preserve the old process version

When a lesson changes process or culture:

1. preserve the lesson and evidence that motivated the change;
2. change the process/culture prospectively in a new Git commit/version;
3. do not rewrite older project history to make it appear that the new rule or preference already existed;
4. allow historical interrogation to explain decisions under the process and culture that were active at the time.

This permits a trustworthy answer such as:

> “We used to prefer X. Experience Y led us to adopt Z. This older implementation predates that change and was reasonable under the culture/process version then in force.”

Changing our mind is therefore represented as **new evidence and a new version**, not as inconsistency to hide.

## Process-level lessons log

The Spiral Developer repository keeps a small `lessons/` log for lessons that may shape the methodology itself. Consuming projects should normally keep project lessons under `.spiral/lessons/` using `LES-*` identities.

Do not create a lesson for every retrospective observation. Record one when it could plausibly change a future decision, a culture preference, a verification boundary, or the process itself.

## Evaluate adopted lessons

A lesson can also be wrong or overgeneralized.

After adopting one, later cycles should be allowed to ask:

- Did this change prevent or expose the problem we cared about?
- Did it create new ceremony or failure modes?
- Is its scope too broad?
- Has new evidence contradicted it?
- Should the lesson be refined, superseded, or retired?

The learning loop is therefore:

> **experience → evidence → lesson → local change → evaluation → possible culture/process change**

The goal is an evolvable production environment, not an ever-growing rulebook.
