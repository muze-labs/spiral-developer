---
id: DES-20260818-DGB8Z-8
---

# Design: Prospective distributed integration validator

## Design goal

Provide the smallest executable validator that can falsify a prospective Spiral integration when independently valid branches combine into an incoherent current causal graph.

## CLI surface

```text
spiral validate
spiral validate integration --base <target> --head <candidate>
```

`spiral validate` inspects the checked-out current tree.

`spiral validate integration` asks Git to construct the prospective merged tree for the supplied target and candidate. It validates that tree without checking it out and without modifying either branch. If Git reports merge conflicts, the command fails with an ordinary Git-conflict diagnostic and does not attempt causal validation of a nonexistent clean result.

## Parser boundary

The Node CLI delegates RDF inspection to a small helper that uses a standards-conforming Turtle parser. The helper has a deliberately narrow JSON/result contract so the parser/runtime can be replaced later without changing the CLI/invariant surface.

For the first dogfood implementation the helper uses Python `rdflib`; the dependency is explicit in `requirements.txt`. This is an implementation convenience, not a Spiral invariant.

## Current/effective dependency rule

The ontology remains the source of truth for which predicates are causal references. The validator reads `ontology/spiral-developer.ttl`, computes the transitive `rdfs:subPropertyOf sd:causalReference` set, and treats those predicates as current/effective causal relations **except `sd:supersedes` itself**.

`sd:supersedes` is excluded from the dependency check because its purpose is to point at the exact version being retired; considering that edge stale would make every supersession self-invalidating.

`sd:transforms` and `sd:changeCausedBy` are already outside `sd:causalReference`, so implementation lineage and transition provenance do not become current/effective dependencies accidentally.

## Live artifacts

The first gate treats artifacts with current status `sd:Active` or `sd:Accepted` as live/effective for causal-coherence checking.

Artifacts explicitly marked `sd:Suspect`, `sd:Superseded`, or `sd:Rejected` may remain in the current graph, but a live artifact may not silently depend on them through a current/effective causal relation.

`sd:Draft` is not considered execution authority and is not used as a blocker in this first integration slice; later process work may tighten draft semantics if dogfooding shows a concrete need.

## Stale exact-version rule

Let a live artifact `D` have a current/effective causal reference via relation `R` to exact artifact version `(A, T)`.

The prospective state is mechanically stale when either:

1. some current artifact `S` has `sd:supersedes` pointing to the exact same pair `(A, T)`; or
2. artifact identity `A` is currently present with status `Suspect`, `Superseded`, or `Rejected`.

The validator reports `D`, `R`, `A`, `T`, and (for case 1) the superseding artifact(s).

This check intentionally does **not** decide whether the newer artifact is semantically better. It only establishes that the downstream current/effective claim still relies on an upstream version whose current lifecycle has materially changed.

## Clearing staleness

The first implementation has no generic "ignore staleness" flag. A live downstream artifact must be reconciled by changing its effective provenance to a current justified version/interpretation, or by moving the affected artifact itself out of live/effective status.

If an artifact is marked non-effective while another live artifact still depends on it, rule 2 propagates the integration failure downstream. This prevents simply marking one intermediate node `Suspect` from leaving an accepted implementation apparently well-founded.

A future explicit revalidation/exception relation may be added only if dogfooding produces a legitimate case that cannot be represented by updating effective provenance without falsifying history.

## Distributed allocation collision rule

For new-format identifiers matching:

```text
<TYPE>-<YYYYMMDD>-<WORKSPACE>-<N>
```

`WORKSPACE + N` is one allocation slot because `N` is defined as the single sequence shared across all artifact types and dates in a workspace.

The validator fails if two distinct artifact identifiers consume the same `(WORKSPACE, N)` pair. This detects the exceptional case where two independent workspaces accidentally chose the same workspace namespace even if their differing type/date prefixes avoided a filename conflict.

Legacy identifiers are not interpreted through this rule.

The validator also rejects duplicate current `dcterms:identifier` values or the same artifact IRI being defined as a governed artifact in multiple Turtle files.

## Prospective tree mechanism

Use:

```text
git merge-tree --write-tree <base> <head>
```

when available to construct the tree Git would produce for a clean merge without rewriting branch history. The resulting tree object is inspected directly through Git object reads; no working-tree mutation is required.

This first implementation can fail clearly when the installed Git does not support the required `merge-tree --write-tree` behavior rather than silently substituting weaker semantics.

## Validation layers intentionally separated

This slice is a **current/prospective snapshot integration check**. It does not claim to implement the existing full staged/range historical-reference validator described in `docs/causal-validation.md`.

That distinction must remain visible in CLI output/docs so passing integration validation is not misrepresented as a complete audit of all preserved causal history.

## Verification scenarios

1. clean independent additions with distinct workspace allocation slots pass;
2. duplicate `(workspace, sequence)` across different IDs fails;
3. branch B live design references old request version while target branch A supersedes that exact request version: B alone passes, prospective integration fails;
4. reconciling B to a current accepted upstream version passes;
5. marking the stale design `Suspect` clears its own stale dependency, but an accepted implementation depending on that suspect design still fails;
6. ordinary textual merge conflict fails as a Git conflict, not as a causal-staleness diagnosis;
7. malformed Turtle fails through the RDF parser.

## Deferred questions

- packaging/runtime consolidation for the CLI after dogfooding;
- complete historical range validation;
- optional host-specific examples/configuration;
- an explicit semantic revalidation exception only if real use proves it necessary.
