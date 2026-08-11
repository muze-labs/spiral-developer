---
id: SRC-CUL-MUZE-002
---

# Source: Human clarification of Muze culture scope

## Source kind

Human clarification in the Spiral Developer project discussion, responding to the earlier Muze design-principles / maturity-policy summary.

## What was actually expressed or observed

The reviewer clarified that the earlier summary mixes broadly applicable Muze engineering preferences with principles that apply mainly to Muze-owned reusable libraries and GitHub organizations.

In particular:

- the `@muze-nl` versus `@muze-labs` distinction is primarily for Muze's own libraries and should not leak into client projects;
- the stated audience of technically curious non-professional programmers applies specifically to Muze's own libraries/products, not generally to customer-facing work where Muze may not control the audience;
- optimizing for slow devices and connections is a useful preference in some Muze-owned contexts, but is not universally applicable to client work;
- across client work, Muze still values software being understandable enough that less-technical collaborators can inspect specific code or behavior and point to what should change;
- culture should therefore be scoped so a project adopts only the profiles that actually apply.

The reviewer agreed with separating broadly applicable Muze engineering culture from a narrower Muze-owned library stewardship culture.

## Origin / locator

Spiral Developer project discussion, 2026-08-11.

The originating conversation is not stored in this repository. The relevant clarification is retained here as source evidence.

The discussion referred to an attached `maturity-policy.md` / Muze design-principles summary with SHA-256:

`db97ba41f73f605e61deda4d441b076010cc09903a8eb42b5553687c7f954654`

The profile also continues to reference the canonical organization source at:

`https://github.com/muze-nl/.github/blob/main/maturity-policy.md`

## Primary evidence availability

retained

## Integrity / version

This Source artifact records the scope clarification prospectively. It does not alter what `CUL-MUZE-001` meant at earlier Git versions.

## Provenance confidence

explicit

## Limitations / uncertainty

The clarification establishes the intended scope distinction and the specific examples above. It does not claim that every Muze cultural principle has now been classified perfectly. Further review may move additional principles between general, library-specific, project-specific, or Spiral-core contexts.
