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



def parse_tree(repo: Path, treeish: str):
    graph, subject_files, parse_errors, file_count = parse_documents(iter_tree_turtle(repo, treeish))
    return graph, subject_files, parse_errors, file_count


def branch_matches_cycle(branch: str | None, identifier: str) -> bool:
    if not branch:
        return False
    prefix = f"spiral/{identifier}"
    return branch == prefix or branch.startswith(prefix + "-")


def cycle_for_branch(graph: Graph, branch: str | None):
    if not branch:
        return None
    matches = []
    for subject in set(graph.subjects(RDF.type, SD.Cycle)):
        identifiers = [str(value) for value in graph.objects(subject, DCTERMS.identifier)]
        for identifier in identifiers:
            if branch_matches_cycle(branch, identifier):
                matches.append((len(identifier), subject, identifier))
    if not matches:
        return None
    matches.sort(reverse=True, key=lambda item: item[0])
    _, subject, identifier = matches[0]
    return subject, identifier, set(graph.objects(subject, SD.status))


def candidate_cycle_paths(repo: Path, base: str, head: str):
    merge_base = run_git(repo, "merge-base", base, head).strip().splitlines()[0]
    changed = run_git(
        repo,
        "diff",
        "--name-only",
        f"{merge_base}..{head}",
        "--",
        ".spiral/cycles",
    )
    return sorted({path.strip() for path in changed.splitlines() if path.strip().endswith(".ttl")})


def cycle_for_path(graph: Graph, subject_files: dict[str, list[str]], path: str):
    matches = []
    for subject in set(graph.subjects(RDF.type, SD.Cycle)):
        if path not in subject_files.get(str(subject), []):
            continue
        identifiers = [str(value) for value in graph.objects(subject, DCTERMS.identifier)]
        if len(identifiers) == 1:
            matches.append((subject, identifiers[0], set(graph.objects(subject, SD.status))))
    if len(matches) == 1:
        return matches[0]
    return None


def validate_cycle_integration(
    repo: Path,
    graph: Graph,
    subject_files: dict[str, list[str]],
    base: str,
    head: str,
    base_branch: str | None,
    head_branch: str | None,
):
    errors = []
    changed_cycle_paths = candidate_cycle_paths(repo, base, head)

    if len(changed_cycle_paths) > 1:
        errors.append({
            "code": "multiple-candidate-cycles",
            "paths": changed_cycle_paths,
            "message": (
                "candidate changes multiple cycle records; one repository-changing cycle branch must integrate "
                "one cycle at a time: " + ", ".join(changed_cycle_paths)
            ),
        })
        return errors

    candidate_cycle = None
    if changed_cycle_paths:
        path = changed_cycle_paths[0]
        candidate_cycle = cycle_for_path(graph, subject_files, path)
        if candidate_cycle is None:
            errors.append({
                "code": "candidate-cycle-unreadable",
                "path": path,
                "message": f"candidate cycle record {path} does not resolve to exactly one sd:Cycle in the prospective graph",
            })
            return errors

        subject, identifier, statuses = candidate_cycle
        if SD.Accepted not in statuses or SD.Active in statuses:
            names = sorted(str(status).split("#")[-1] for status in statuses)
            errors.append({
                "code": "open-cycle-integration",
                "cycle": identifier,
                "status": names,
                "message": (
                    f"cycle {identifier} is not closed/Accepted in the candidate; unfinished cycle branches "
                    "must not integrate into accepted history"
                ),
            })

        if head_branch and not branch_matches_cycle(head_branch, identifier):
            errors.append({
                "code": "cycle-branch-mismatch",
                "cycle": identifier,
                "branch": head_branch,
                "message": (
                    f"candidate branch {head_branch} does not match cycle {identifier}; expected "
                    f"spiral/{identifier} or spiral/{identifier}-..."
                ),
            })

    if base_branch:
        base_graph, _, base_parse_errors, _ = parse_tree(repo, base)
        if not base_parse_errors:
            target_cycle = cycle_for_branch(base_graph, base_branch)
            if target_cycle:
                _, target_identifier, target_statuses = target_cycle
                candidate_identifier = candidate_cycle[1] if candidate_cycle else None
                if SD.Active in target_statuses and candidate_identifier != target_identifier:
                    errors.append({
                        "code": "open-cycle-target",
                        "cycle": target_identifier,
                        "branch": base_branch,
                        "message": (
                            f"target branch {base_branch} belongs to active cycle {target_identifier}; "
                            "another cycle must not integrate into an unfinished cycle branch"
                        ),
                    })

    return errors


def normalized_companion_stems(paths: set[str]):
    stems = set()
    for path in paths:
        if path.startswith("templates/") or path.startswith("examples/") or path.startswith("node_modules/"):
            continue
        if path.endswith(".ttl"):
            stems.add(path[:-4])
        elif path.endswith(".md"):
            stems.add(path[:-3])
    return stems


def changed_paths(repo: Path, start: str, end: str):
    output = run_git(repo, "diff", "--name-only", f"{start}..{end}")
    return {line.strip() for line in output.splitlines() if line.strip()}


def subject_for_companion_stem(graph: Graph, subject_files: dict[str, list[str]], stem: str):
    ttl_path = stem + ".ttl"
    matches = []
    for subject in set(graph.subjects(DCTERMS.identifier, None)):
        if ttl_path in subject_files.get(str(subject), []):
            matches.append(subject)
    if len(matches) == 1:
        return matches[0]
    return None


def latest_companion_commit(repo: Path, ancestor: str, tip: str, stem: str):
    output = run_git(
        repo,
        "log",
        "-1",
        "--format=%H",
        f"{ancestor}..{tip}",
        "--",
        stem + ".md",
        stem + ".ttl",
    ).strip()
    return output or None


def transform_refs(graph: Graph, subject):
    refs = set()
    for node in graph.objects(subject, SD.transforms):
        ref = artifact_reference(graph, node)
        if ref:
            refs.add(ref)
    return refs


def validate_merge_convergence(repo: Path, base: str, head: str):
    errors = []
    merges = run_git(repo, "rev-list", "--reverse", "--merges", f"{base}..{head}").splitlines()

    for merge_commit in [value.strip() for value in merges if value.strip()]:
        parents = run_git(repo, "show", "-s", "--format=%P", merge_commit).strip().split()
        if len(parents) != 2:
            continue
        left, right = parents
        merge_bases = run_git(repo, "merge-base", left, right).strip().splitlines()
        if not merge_bases:
            continue
        ancestor = merge_bases[0]

        left_stems = normalized_companion_stems(changed_paths(repo, ancestor, left))
        right_stems = normalized_companion_stems(changed_paths(repo, ancestor, right))
        divergent_stems = sorted(left_stems.intersection(right_stems))
        if not divergent_stems:
            continue

        merge_graph, merge_files, merge_parse_errors, _ = parse_tree(repo, merge_commit)
        left_graph, left_files, left_parse_errors, _ = parse_tree(repo, left)
        right_graph, right_files, right_parse_errors, _ = parse_tree(repo, right)
        if merge_parse_errors or left_parse_errors or right_parse_errors:
            # Snapshot parser errors are reported by the normal validation path for the prospective tree.
            # Do not manufacture lineage conclusions from an unreadable parent snapshot.
            continue

        for stem in divergent_stems:
            merge_subject = subject_for_companion_stem(merge_graph, merge_files, stem)
            left_subject = subject_for_companion_stem(left_graph, left_files, stem)
            right_subject = subject_for_companion_stem(right_graph, right_files, stem)
            if merge_subject is None or left_subject is None or right_subject is None:
                continue
            if str(merge_subject) != str(left_subject) or str(merge_subject) != str(right_subject):
                continue

            left_commit = latest_companion_commit(repo, ancestor, left, stem)
            right_commit = latest_companion_commit(repo, ancestor, right, stem)
            if not left_commit or not right_commit or left_commit == right_commit:
                continue

            refs = transform_refs(merge_graph, merge_subject)
            required = {(str(merge_subject), left_commit), (str(merge_subject), right_commit)}
            missing = sorted(required.difference(refs), key=lambda item: item[1])
            if missing:
                identifier = artifact_label(merge_graph, merge_subject)
                errors.append({
                    "code": "unreconciled-parallel-artifact-revision",
                    "artifact": identifier,
                    "mergeCommit": merge_commit,
                    "predecessors": [left_commit, right_commit],
                    "missingPredecessors": [commit for _, commit in missing],
                    "message": (
                        f"merge {merge_commit[:12]} combines independent revisions of {identifier} without "
                        "sd:transforms references to both immediate predecessor versions "
                        f"{left_commit[:12]} and {right_commit[:12]}"
                    ),
                })

    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Spiral RDF snapshot invariants")
    parser.add_argument("--repo", required=True)
    parser.add_argument("--tree", default=None)
    parser.add_argument("--integration-base", default=None)
    parser.add_argument("--integration-head", default=None)
    parser.add_argument("--base-branch", default=None)
    parser.add_argument("--head-branch", default=None)
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    try:
        documents = iter_tree_turtle(repo, args.tree) if args.tree else iter_worktree_turtle(repo)
        graph, subject_files, parse_errors, file_count = parse_documents(documents)
        errors = parse_errors + validate_graph(graph, subject_files)
        if args.integration_base and args.integration_head:
            errors += validate_cycle_integration(
                repo,
                graph,
                subject_files,
                args.integration_base,
                args.integration_head,
                args.base_branch,
                args.head_branch,
            )
            errors += validate_merge_convergence(repo, args.integration_base, args.integration_head)
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
