---
id: EVD-20260818-DGB8Z-17
---

# Verification Evidence: Active cycle delta detection gap

## Claim being challenged

`IMP-20260818-DGB8Z-16@90991c8ce8f4d10a55016976240c977e52c80387` was intended to prevent an unfinished cycle branch from integrating into accepted history.

## Evidence method

- [x] Dogfood prospective-integration probe against the actual CYC-005 branch
- [x] Implementation inspection
- [ ] Corrective implementation verified

## Probe

From `spiral/CYC-005-distributed-development`, with `main` at the historical merge that already contains the still-`Active` CYC-005 record:

```sh
node bin/spiral.mjs validate integration \
  --base main \
  --head HEAD \
  --base-branch main \
  --head-branch spiral/CYC-005-distributed-development
```

## Result

The command returned `validation: ok` even though CYC-005 is still `sd:Active`.

The reason is prospective candidate-cycle discovery: `candidate_cycle_paths()` only considered changed `.ttl` files below `.spiral/cycles`. The historical premature merge placed the Active CYC-005 TTL on `main`; continued CYC-005 work had not changed that TTL, so the branch did not present a candidate cycle to the closure gate.

This falsifies the stronger claim that the first implementation revision would mechanically block this actual Active cycle branch from integrating.

## Required correction

Candidate-cycle discovery must treat changes to either companion form of a cycle record (`.md` or `.ttl`) as evidence that the candidate is operating on that cycle and resolve the canonical `.ttl` record for status/identity validation. A regression probe should cover a pre-existing Active cycle whose candidate delta changes only its Markdown record.

## Limits

This is evidence of one prospective-delta detection gap, not a rejection of the overall branch-isolation design. The existing validation behavior for newly introduced/TTL-changed cycle records and explicit convergence remains separately covered by the automated suite.
