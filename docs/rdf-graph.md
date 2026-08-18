# RDF Causal Graph

## Why Turtle

Spiral Developer stores causal relationships as RDF in Turtle syntax.

This gives the graph useful properties independent of any particular AI model or harness:

- relationships are explicit and typed;
- stable IRIs identify artifacts;
- normal RDF parsers can inspect the graph;
- SPARQL can query it;
- SHACL can validate structural constraints;
- the graph can later interoperate with Solid or other linked-data systems;
- Git still provides immutable historical versions.

Turtle is the canonical machine-readable representation of causal relationships. Markdown remains the preferred human-facing representation for substantial sources, interpretations, intent, design, observations, and evidence.

## The graph is logical, not one file

Do **not** put all causal statements in one large `graph.ttl`.

A monolithic file would become a merge-conflict hotspot when several cycle branches are active. RDF naturally allows one logical graph to be assembled from many Turtle documents.

Prefer a companion Turtle resource beside each durable human artifact:

```text
.spiral/
  project.ttl
  culture.md
  culture.ttl
  warning-profiles/
  project-context.md
  sources/
    SRC-001.md
    SRC-001.ttl
  understandings/
    UND-001.md
    UND-001.ttl
  requests/
    REQ-001.md
    REQ-001.ttl
  feedback/
    FBK-001.md
    FBK-001.ttl
  designs/
    DES-001.md
    DES-001.ttl
  implementations/
    IMP-001.md          # optional when useful to humans
    IMP-001.ttl
  evidence/
    EVD-001.md
    EVD-001.ttl
  acceptance/
    ACC-001.md
    ACC-001.ttl
  legacy/
    LEG-001.md
    LEG-001.ttl
  defects/
    DEF-001.md
    DEF-001.ttl
  cycles/
    CYC-001.md
    CYC-001.ttl
```

The **causal graph** is the RDF union of the project's `.spiral/**/*.ttl` resources.

This has three benefits:

1. unrelated cycle branches usually modify different Turtle files;
2. an artifact's machine metadata travels with the human artifact it describes;
3. a version-aware tool can retrieve one artifact's historical Turtle directly from Git without loading the whole repository history.

Create only resources the project actually needs.

## Vocabulary

Spiral Developer's provisional vocabulary is defined in:

```text
ontology/spiral-developer.ttl
```

The namespace is:

```text
https://muze.nl/ns/spiral-developer#
```

Publishing/dereferencing that namespace is desirable later but is not required for the initial repository experiment.

Each consuming project should choose a stable project namespace. Prefer a durable HTTP(S) IRI when one naturally exists; otherwise use a project-specific URN during experimentation.

Example:

```turtle
@prefix sd: <https://muze.nl/ns/spiral-developer#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix project: <https://example.org/projects/widget/spiral/> .
```

## Stable artifact identity

A design companion resource might contain:

```turtle
project:DES-001
    a sd:Design ;
    dcterms:identifier "DES-001" ;
    sd:repositoryPath ".spiral/designs/DES-001.md" ;
    sd:status sd:Active .
```

The artifact IRI identifies the conceptual artifact across time.

The **version** is the Git commit containing that Turtle/Markdown state.

## Source and understanding example

When origin and interpretation matter, represent them as ordinary versioned artifacts:

```turtle
project:SRC-001
    a sd:Source ;
    dcterms:identifier "SRC-001" ;
    sd:repositoryPath ".spiral/sources/SRC-001.md" ;
    sd:status sd:Accepted ;
    sd:sourceAvailability sd:Referenced ;
    sd:provenanceConfidence sd:Explicit .

project:UND-001
    a sd:Understanding ;
    dcterms:identifier "UND-001" ;
    sd:repositoryPath ".spiral/understandings/UND-001.md" ;
    sd:status sd:Accepted ;
    sd:provenanceConfidence sd:Evidenced ;
    sd:interprets [
        a sd:ArtifactReference ;
        sd:artifact project:SRC-001 ;
        sd:gitCommit "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ] .

project:REQ-001
    a sd:Request ;
    dcterms:identifier "REQ-001" ;
    sd:repositoryPath ".spiral/requests/REQ-001.md" ;
    sd:status sd:Accepted ;
    sd:derivedFrom [
        a sd:ArtifactReference ;
        sd:artifact project:UND-001 ;
        sd:gitCommit "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    ] .
```

`sd:Source` records the existence and epistemic quality of origin evidence; human-facing source artifacts carry locators, excerpts, dates, hashes, or attribution where useful. `sd:Understanding` records the interpretation that was actually used. This keeps source fact separate from project meaning.

A source can also use `sd:sourceAvailability sd:Unavailable` when the project only has a report, memory, inherited requirement, or other secondary trace. Missing provenance is represented rather than filled in.

## Referring to an exact upstream version

A downstream relation uses `sd:ArtifactReference`:

```turtle
project:DES-001
    sd:satisfies [
        a sd:ArtifactReference ;
        sd:artifact project:REQ-001 ;
        sd:gitCommit "1111111111111111111111111111111111111111" ;
        sd:fragment "outcome-1"
    ] .
```

The hash must be the **full Git commit hash** in machine data.

This says that the design was based on the request as it existed at that exact historical commit, not whatever `REQ-001` says today.

## Why artifacts do not store their own hash

A Git commit hash depends on the commit contents. Therefore a commit cannot contain its own final hash without changing it.

Spiral Developer avoids the circularity:

1. commit the upstream artifact and companion Turtle;
2. Git now gives that version a hash;
3. the downstream artifact records the upstream hash in its own Turtle resource.

This naturally encourages semantic causal commit boundaries.

## Versioned historical-reference invariant

Relations that point to exact prior artifact versions are grouped under `sd:historicalReference`. This is an integrity category, not a claim that all such relations have the same causal meaning.

For every persisted source version, the referenced target commit must be a **strict Git ancestor** of the source commit. Causal provenance (`sd:causalReference` and its subproperties), historical predecessor lineage (`sd:transforms`), and implementation transition provenance (`sd:changeCausedBy`) all obey this historical rule.

This backward-only Git-ancestry invariant makes the versioned reference graph a DAG by construction. Conceptual artifact identities may recur across revisions without creating a versioned cycle. Validate staged changes before commit and introduced commit ranges in CI; see `causal-validation.md`.

## Canonical relations

The vocabulary includes:

- `sd:derivedFrom`
- `sd:interprets`
- `sd:satisfies`
- `sd:supports`
- `sd:constrainedBy`
- `sd:shapedBy`
- `sd:adoptsCulture`
- `sd:adoptsWarningProfile`
- `sd:implements`
- `sd:verifies`
- `sd:accepts`
- `sd:observes`
- `sd:supersedes`

Each relation points to an `sd:ArtifactReference` when an exact historical upstream version matters. `sd:shapedBy` is current explanatory provenance for a defeasible culture influence; `sd:adoptsCulture` records which culture profile/version project context intentionally made active. `sd:adoptsWarningProfile` similarly activates an exact replaceable warning lens without making its signals hard constraints. See `culture.md` and `warning-profiles.md`.

Historical transition modeling also uses deliberately separate relations:

- `sd:transforms` — exact predecessor artifact version(s); for implementations this is normal implementation lineage, and for distributed convergence it can preserve both parent lineages of any governed artifact;
- `sd:changeCausedBy` — implementation-specific exact artifact version(s) that caused an implementation transition.

These are **not** subproperties of `sd:causalReference`: lineage/transition history is not automatically current justification. See `implementation-lineage.md` and `distributed-development.md`.

## Implementation lineage example

The current implementation resource contains only the current projection plus immediate lineage/transition metadata:

```turtle
project:IMP-023
    a sd:Implementation ;
    dcterms:identifier "IMP-023" ;
    sd:repositoryPath ".spiral/implementations/IMP-023.md" ;
    sd:implementationLocation "src/session/validate.js#validateSession" ;
    sd:implements [
        a sd:ArtifactReference ;
        sd:artifact project:DES-014 ;
        sd:gitCommit "1111111111111111111111111111111111111111"
    ] ;
    sd:transforms [
        a sd:ArtifactReference ;
        sd:artifact project:IMP-023 ;
        sd:gitCommit "3333333333333333333333333333333333333333"
    ] ;
    sd:changeCausedBy [
        a sd:ArtifactReference ;
        sd:artifact project:DEF-031 ;
        sd:gitCommit "4444444444444444444444444444444444444444"
    ] ;
    sd:implementationChangeKind sd:SemanticChange .
```

Here `sd:implements` is part of current/effective provenance. `sd:transforms` and `sd:changeCausedBy` describe how this version came to exist. A historical interrogation loads the predecessor resource from the referenced Git commit and continues backward only when needed.

`sd:implementationLocation` is repeatable. Several implementation concerns may legitimately locate the same path or symbol.

## Provenance confidence

Any artifact whose grounding matters can carry confidence explicitly. This is especially useful for reconstructed legacy context, reported sources, and interpretation claims:

```turtle
project:LEG-004
    a sd:LegacyContext ;
    dcterms:identifier "LEG-004" ;
    sd:repositoryPath ".spiral/legacy/LEG-004.md" ;
    sd:provenanceConfidence sd:Inferred .
```

Available values are:

- `sd:Explicit`
- `sd:Evidenced`
- `sd:Inferred`
- `sd:Unknown`

Unknown is valid data.

## Source availability

`sd:Source` uses one of:

- `sd:Retained` — primary source material is preserved in or with the project;
- `sd:Referenced` — primary evidence is externally identifiable/retrievable;
- `sd:Unavailable` — only a secondary report, memory, inherited claim, or similar trace remains.

This is deliberately separate from provenance confidence. A source can be retained but ambiguous, or unavailable but still operationally important.

## Version-aware traversal

The checked-out Turtle resources describe the current project state. Historical causal states remain in Git rather than being copied forever into the current graph.

To follow a causal chain through exact historical versions, a non-AI tool can:

1. start with an artifact IRI and commit version;
2. use Git to read that artifact's `.ttl` resource at that commit;
3. parse its outgoing causal references;
4. for each reference, load the referenced artifact's Turtle resource at `sd:gitCommit`;
5. continue until the desired boundary is reached.

For example, conceptually:

```text
git show <commit>:.spiral/designs/DES-001.ttl
```

This keeps current resources small while preserving complete historical evidence.

Plain SPARQL answers questions over whatever graph snapshot/dataset has been loaded. A version-aware provenance tool combines RDF/SPARQL with Git to traverse across snapshots.

## Current-state queries

A conventional RDF store can load all current `.spiral/**/*.ttl` files as one graph and query them without AI.

Find all current causal references to a request:

```sparql
PREFIX sd: <https://muze.nl/ns/spiral-developer#>
PREFIX project: <https://example.org/projects/widget/spiral/>

SELECT ?artifact ?relation ?commit ?fragment
WHERE {
  ?artifact ?relation ?reference .
  ?reference a sd:ArtifactReference ;
             sd:artifact project:REQ-001 ;
             sd:gitCommit ?commit .
  OPTIONAL { ?reference sd:fragment ?fragment }
  FILTER (?relation IN (
    sd:derivedFrom,
    sd:interprets,
    sd:satisfies,
    sd:supports,
    sd:constrainedBy,
    sd:implements,
    sd:verifies,
    sd:accepts,
    sd:observes,
    sd:supersedes
  ))
}
```

Find sources whose primary evidence is unavailable:

```sparql
PREFIX sd: <https://muze.nl/ns/spiral-developer#>

SELECT ?source
WHERE {
  ?source a sd:Source ;
          sd:sourceAvailability sd:Unavailable .
}
```

Find inferred legacy context:

```sparql
PREFIX sd: <https://muze.nl/ns/spiral-developer#>

SELECT ?artifact
WHERE {
  ?artifact a sd:LegacyContext ;
            sd:provenanceConfidence sd:Inferred .
}
```

Find artifacts currently marked suspect:

```sparql
PREFIX sd: <https://muze.nl/ns/spiral-developer#>

SELECT ?artifact
WHERE {
  ?artifact sd:status sd:Suspect .
}
```


## Implementation lineage queries

Find current implementation concerns that locate a code region:

```sparql
PREFIX sd: <https://muze.nl/ns/spiral-developer#>

SELECT ?implementation
WHERE {
  ?implementation a sd:Implementation ;
                  sd:implementationLocation "src/session/validate.js#validateSession" .
}
```

Find the immediate predecessor and transition cause of a current implementation version:

```sparql
PREFIX sd: <https://muze.nl/ns/spiral-developer#>
PREFIX project: <https://example.org/projects/widget/spiral/>

SELECT ?previousArtifact ?previousCommit ?causeArtifact ?causeCommit ?kind
WHERE {
  project:IMP-023 sd:transforms ?previous ;
                  sd:changeCausedBy ?cause ;
                  sd:implementationChangeKind ?kind .
  ?previous sd:artifact ?previousArtifact ;
            sd:gitCommit ?previousCommit .
  ?cause sd:artifact ?causeArtifact ;
         sd:gitCommit ?causeCommit .
}
```

A complete historical traversal then loads each predecessor's Turtle resource at `?previousCommit` and repeats. A current/effective provenance query should intentionally ignore `sd:transforms` and `sd:changeCausedBy` unless the question asks about history.

## Validation

Starter SHACL constraints are in:

```text
ontology/spiral-developer-shapes.ttl
```

They intentionally validate only high-value structural properties at first, such as:

- artifact IDs and human-artifact paths;
- source artifacts declaring primary evidence availability and provenance confidence;
- understanding artifacts interpreting at least one upstream artifact version and declaring provenance confidence;
- implementation revisions with lineage declaring predecessor reference(s), a change kind, and transition cause(s) when known/required;
- full commit hashes on artifact references;
- verification evidence having something to verify;
- acceptance evidence having something to accept.

A CI job can load the union of `.spiral/**/*.ttl` and apply the shapes.

Do not overfit the ontology or shapes before real project use reveals what matters.

## Avoid duplicate truth

Do not encode the same causal relationship in Markdown front matter, Git trailers, and Turtle as three competing authoritative graphs.

The companion Turtle resources are authoritative for machine-readable causal links.

Git trailers and PR text may repeat important links for navigation, but they are summaries of the canonical RDF data.
