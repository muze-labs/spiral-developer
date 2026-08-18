#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

try:
    from rdflib import Graph, Namespace
    from rdflib.namespace import DCTERMS, RDF, RDFS
except ImportError as exc:  # pragma: no cover - exercised by CLI error path, not normal tests
    print(json.dumps({
        "ok": False,
        "errors": [
            {
                "code": "rdf-parser-unavailable",
                "message": "Python package rdflib is required for Spiral Turtle validation; install requirements.txt",
            }
        ],
    }))
    raise SystemExit(2) from exc

SD = Namespace("https://muze.nl/ns/spiral-developer#")
DISTRIBUTED_ID_RE = re.compile(
    r"^(?P<type>[A-Z][A-Z0-9]{1,7})-(?P<date>\d{8})-(?P<workspace>[A-Z0-9]{2,12})-(?P<sequence>[1-9][0-9]*)$"
)
LIVE_STATUSES = {SD.Active, SD.Accepted}
NON_EFFECTIVE_STATUSES = {SD.Suspect, SD.Superseded, SD.Rejected}


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip() or f"git {' '.join(args)} failed"
        raise RuntimeError(detail)
    return result.stdout


def iter_worktree_turtle(repo: Path):
    for path in sorted(repo.rglob("*.ttl")):
        relative = path.relative_to(repo)
        if ".git" in relative.parts or "node_modules" in relative.parts:
            continue
        yield relative.as_posix(), path.read_text(encoding="utf-8")


def iter_tree_turtle(repo: Path, treeish: str):
    output = run_git(repo, "ls-tree", "-r", "--name-only", treeish)
    for raw_path in output.splitlines():
        path = raw_path.strip()
        if not path.endswith(".ttl") or path.startswith("node_modules/"):
            continue
        yield path, run_git(repo, "show", f"{treeish}:{path}")


def parse_documents(documents):
    union = Graph()
    subject_files: dict[str, list[str]] = defaultdict(list)
    parse_errors = []
    file_count = 0

    for path, text in documents:
        file_count += 1
        graph = Graph()
        try:
            graph.parse(data=text, format="turtle", publicID=f"urn:spiral:file:{path}")
        except Exception as exc:  # rdflib exposes parser-specific exception classes; preserve useful text
            parse_errors.append({
                "code": "invalid-turtle",
                "path": path,
                "message": f"{path}: {exc}",
            })
            continue
        for triple in graph:
            union.add(triple)
        for subject in set(graph.subjects(DCTERMS.identifier, None)):
            subject_files[str(subject)].append(path)

    return union, subject_files, parse_errors, file_count


def causal_properties(graph: Graph):
    result = {SD.causalReference}
    changed = True
    while changed:
        changed = False
        for child, parent in graph.subject_objects(RDFS.subPropertyOf):
            if parent in result and child not in result:
                result.add(child)
                changed = True
    result.discard(SD.supersedes)
    return result


def artifact_reference(graph: Graph, node):
    artifacts = list(graph.objects(node, SD.artifact))
    commits = list(graph.objects(node, SD.gitCommit))
    if len(artifacts) != 1 or len(commits) != 1:
        return None
    return str(artifacts[0]), str(commits[0])


def artifact_label(graph: Graph, subject) -> str:
    identifiers = list(graph.objects(subject, DCTERMS.identifier))
    if identifiers:
        return str(identifiers[0])
    return str(subject)


def validate_graph(graph: Graph, subject_files: dict[str, list[str]]):
    errors = []

    # One governed artifact definition per current Turtle file/IRI.
    for subject, files in sorted(subject_files.items()):
        unique_files = sorted(set(files))
        if len(unique_files) > 1:
            errors.append({
                "code": "duplicate-artifact-definition",
                "artifact": subject,
                "paths": unique_files,
                "message": f"artifact {subject} is defined in multiple Turtle files: {', '.join(unique_files)}",
            })

    identifiers: dict[str, set[str]] = defaultdict(set)
    distributed_slots: dict[tuple[str, int], set[str]] = defaultdict(set)
    artifact_subjects = set()
    for subject, identifier in graph.subject_objects(DCTERMS.identifier):
        artifact_subjects.add(subject)
        identifier_text = str(identifier)
        identifiers[identifier_text].add(str(subject))
        match = DISTRIBUTED_ID_RE.match(identifier_text)
        if match:
            slot = (match.group("workspace"), int(match.group("sequence")))
            distributed_slots[slot].add(identifier_text)

    for identifier, subjects in sorted(identifiers.items()):
        if len(subjects) > 1:
            errors.append({
                "code": "duplicate-artifact-identifier",
                "identifier": identifier,
                "artifacts": sorted(subjects),
                "message": f"dcterms:identifier {identifier} is used by multiple artifact IRIs",
            })

    for (workspace, sequence), ids in sorted(distributed_slots.items()):
        if len(ids) > 1:
            errors.append({
                "code": "duplicate-allocation-slot",
                "workspace": workspace,
                "sequence": sequence,
                "identifiers": sorted(ids),
                "message": (
                    f"workspace {workspace} local sequence {sequence} is consumed by multiple artifacts: "
                    + ", ".join(sorted(ids))
                ),
            })

    effective_properties = causal_properties(graph)
    if effective_properties == {SD.causalReference}:
        errors.append({
            "code": "causal-vocabulary-unavailable",
            "message": "could not derive any sd:causalReference subproperties from the loaded Turtle graph",
        })
        return errors

    current_statuses: dict[str, set] = {}
    for subject in artifact_subjects:
        current_statuses[str(subject)] = set(graph.objects(subject, SD.status))

    superseded_exact: dict[tuple[str, str], set[str]] = defaultdict(set)
    for superseder, ref_node in graph.subject_objects(SD.supersedes):
        # A tentative/rejected artifact may propose a supersession without making
        # it effective. Only live current artifacts retire exact upstream versions.
        if not set(graph.objects(superseder, SD.status)).intersection(LIVE_STATUSES):
            continue
        ref = artifact_reference(graph, ref_node)
        if ref:
            superseded_exact[ref].add(artifact_label(graph, superseder))

    for downstream in artifact_subjects:
        statuses = set(graph.objects(downstream, SD.status))
        if not statuses.intersection(LIVE_STATUSES):
            continue
        downstream_label = artifact_label(graph, downstream)

        for relation in effective_properties:
            for ref_node in graph.objects(downstream, relation):
                ref = artifact_reference(graph, ref_node)
                if not ref:
                    continue
                target_artifact, target_commit = ref
                relation_name = relation.split("#")[-1] if "#" in str(relation) else str(relation)

                superseders = superseded_exact.get((target_artifact, target_commit), set())
                if superseders:
                    errors.append({
                        "code": "stale-superseded-reference",
                        "artifact": downstream_label,
                        "relation": relation_name,
                        "upstream": target_artifact,
                        "gitCommit": target_commit,
                        "supersededBy": sorted(superseders),
                        "message": (
                            f"{downstream_label} {relation_name} references superseded exact version "
                            f"{target_artifact}@{target_commit}; superseded by {', '.join(sorted(superseders))}"
                        ),
                    })

                target_statuses = current_statuses.get(target_artifact, set())
                non_effective = target_statuses.intersection(NON_EFFECTIVE_STATUSES)
                if non_effective:
                    names = sorted(str(status).split("#")[-1] for status in non_effective)
                    errors.append({
                        "code": "reference-to-non-effective-artifact",
                        "artifact": downstream_label,
                        "relation": relation_name,
                        "upstream": target_artifact,
                        "gitCommit": target_commit,
                        "upstreamStatus": names,
                        "message": (
                            f"{downstream_label} {relation_name} depends on current non-effective artifact "
                            f"{target_artifact} with status {', '.join(names)}"
                        ),
                    })

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Spiral RDF snapshot invariants")
    parser.add_argument("--repo", required=True)
    parser.add_argument("--tree", default=None)
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    try:
        documents = iter_tree_turtle(repo, args.tree) if args.tree else iter_worktree_turtle(repo)
        graph, subject_files, parse_errors, file_count = parse_documents(documents)
        errors = parse_errors + validate_graph(graph, subject_files)
        payload = {
            "ok": not errors,
            "tree": args.tree,
            "turtleFiles": file_count,
            "triples": len(graph),
            "errors": errors,
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0 if not errors else 1
    except Exception as exc:
        print(json.dumps({
            "ok": False,
            "tree": args.tree,
            "errors": [{"code": "validator-failure", "message": str(exc)}],
        }, indent=2, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
