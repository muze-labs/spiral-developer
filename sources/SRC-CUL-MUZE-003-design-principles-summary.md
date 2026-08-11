---
id: SRC-CUL-MUZE-003
---

# Source: Muze design-principles and package-maturity summary

## Source kind

Attached Markdown summary supplied in the Spiral Developer project discussion.

## What was actually expressed or observed

The supplied summary states:

> Muze builds web software for technically curious non-professional programmers, without making the tools unattractive to professionals.

It records preferences for:

- simplicity over completeness;
- small, decoupled, single-concern libraries;
- correct abstractions that do not cross conceptual boundaries;
- browser-native standards where possible;
- lightweight abstractions only when they make developer code simpler;
- stable, long-term APIs;
- components and frameworks that are easy to adapt or replace;
- standards-based or open-source hosting stacks that avoid lock-in;
- software small enough to work well on slow devices and connections;
- a view-source philosophy that invites developers to look under the hood and learn.

It also states the trade-off tendency to prefer composability, replaceability, web-platform alignment, and long-term simplicity over convenience, popularity, or feature completeness.

The summary further describes the Muze package namespace policy:

- `@muze-nl` should be a production-readiness trust signal;
- experimental libraries should use `@muze-labs` until mature enough for the main Muze production-readiness signal;
- moving from `@muze-labs` to `@muze-nl` is a release-readiness decision, not only naming cleanup.

## Origin / locator

Attached file `maturity-policy.md` in the Spiral Developer project discussion, 2026-08-11.

Canonical organization source named in the summary/current culture profile:

`https://github.com/muze-nl/.github/blob/main/maturity-policy.md`

## Primary evidence availability

retained

## Integrity / version

SHA-256 of the supplied attachment:

`db97ba41f73f605e61deda4d441b076010cc09903a8eb42b5553687c7f954654`

The source meaning above was transcribed from that attachment for repository-local provenance.

## Provenance confidence

explicit

## Limitations / uncertainty

The summary itself does not distinguish which principles apply organization-wide from those intended mainly for Muze-owned libraries/products. That scope distinction is supplied separately by `SRC-CUL-MUZE-002` and must be considered when deriving active culture profiles.
