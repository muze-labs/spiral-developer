import assert from 'node:assert/strict';
import {
  cpSync,
  mkdirSync,
  mkdtempSync,
  rmSync,
  writeFileSync,
} from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { execFileSync, spawnSync } from 'node:child_process';
import test from 'node:test';

const cli = resolve('bin/spiral.mjs');
const ontology = resolve('ontology/spiral-developer.ttl');

function git(cwd, ...args) {
  return execFileSync('git', args, { cwd, encoding: 'utf8' }).trim();
}

function spiralResult(cwd, ...args) {
  return spawnSync(process.execPath, [cli, ...args], {
    cwd,
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'pipe'],
  });
}

function write(root, path, content) {
  const full = join(root, path);
  mkdirSync(dirname(full), { recursive: true });
  writeFileSync(full, content, 'utf8');
}

function initRepo(root) {
  git(root, 'init', '-q');
  git(root, 'config', 'user.email', 'spiral-test@example.invalid');
  git(root, 'config', 'user.name', 'Spiral Test');
  mkdirSync(join(root, 'ontology'), { recursive: true });
  cpSync(ontology, join(root, 'ontology/spiral-developer.ttl'));
}

function commitAll(root, message) {
  git(root, 'add', '.');
  git(root, 'commit', '-q', '-m', message);
  return git(root, 'rev-parse', 'HEAD');
}

function requestTurtle({ id = 'REQ-BASE', supersedesCommit = null } = {}) {
  const supersedes = supersedesCommit ? ` ;\n    sd:supersedes [\n        a sd:ArtifactReference ;\n        sd:artifact project:${id} ;\n        sd:gitCommit "${supersedesCommit}"\n    ]` : '';
  return `@prefix sd: <https://muze.nl/ns/spiral-developer#> .\n@prefix dcterms: <http://purl.org/dc/terms/> .\n@prefix project: <https://example.test/project/> .\n\nproject:${id}\n    a sd:Request ;\n    dcterms:identifier "${id}" ;\n    sd:repositoryPath "requests/${id}.md" ;\n    sd:status sd:Accepted${supersedes} .\n`;
}

function designTurtle({ id = 'DES-B', requestId = 'REQ-BASE', requestCommit, status = 'Accepted' }) {
  return `@prefix sd: <https://muze.nl/ns/spiral-developer#> .\n@prefix dcterms: <http://purl.org/dc/terms/> .\n@prefix project: <https://example.test/project/> .\n\nproject:${id}\n    a sd:Design ;\n    dcterms:identifier "${id}" ;\n    sd:repositoryPath "designs/${id}.md" ;\n    sd:status sd:${status} ;\n    sd:satisfies [\n        a sd:ArtifactReference ;\n        sd:artifact project:${requestId} ;\n        sd:gitCommit "${requestCommit}"\n    ] .\n`;
}

function implementationTurtle({ id = 'IMP-C', designId = 'DES-B', designCommit }) {
  return `@prefix sd: <https://muze.nl/ns/spiral-developer#> .\n@prefix dcterms: <http://purl.org/dc/terms/> .\n@prefix project: <https://example.test/project/> .\n\nproject:${id}\n    a sd:Implementation ;\n    dcterms:identifier "${id}" ;\n    sd:repositoryPath "implementations/${id}.md" ;\n    sd:status sd:Accepted ;\n    sd:implements [\n        a sd:ArtifactReference ;\n        sd:artifact project:${designId} ;\n        sd:gitCommit "${designCommit}"\n    ] .\n`;
}

test('integration catches causal staleness introduced only by combining branches', () => {
  const root = mkdtempSync(join(tmpdir(), 'spiral-integration-'));
  try {
    initRepo(root);
    write(root, 'requests/REQ-BASE.ttl', requestTurtle());
    const baseline = commitAll(root, 'baseline request');
    git(root, 'branch', 'target');
    git(root, 'switch', '-q', '-c', 'candidate');

    write(root, 'designs/DES-B.ttl', designTurtle({ requestCommit: baseline }));
    commitAll(root, 'candidate design');
    const candidate = git(root, 'rev-parse', 'HEAD');

    const candidateLocal = spiralResult(root, 'validate');
    assert.equal(candidateLocal.status, 0, candidateLocal.stderr || candidateLocal.stdout);

    git(root, 'switch', '-q', 'target');
    write(root, 'requests/REQ-BASE.ttl', requestTurtle({ supersedesCommit: baseline }));
    commitAll(root, 'supersede baseline request');

    const combined = spiralResult(root, 'validate', 'integration', '--base', 'target', '--head', candidate);
    assert.equal(combined.status, 1, combined.stdout + combined.stderr);
    assert.match(combined.stdout, /validation: failed/);
    assert.match(combined.stderr, /stale-superseded-reference/);
    assert.match(combined.stderr, /DES-B satisfies references superseded exact version/);

    // The later branch reconciles by merging the current target first, then revising
    // its effective provenance to the target's current request version.
    git(root, 'switch', '-q', 'candidate');
    git(root, 'merge', '-q', '--no-edit', 'target');
    const targetCommit = git(root, 'rev-parse', 'target');
    write(root, 'designs/DES-B.ttl', designTurtle({ requestCommit: targetCommit }));
    commitAll(root, 'revalidate design against current request');

    const reconciled = spiralResult(root, 'validate', 'integration', '--base', 'target', '--head', 'candidate');
    assert.equal(reconciled.status, 0, reconciled.stderr || reconciled.stdout);
    assert.match(reconciled.stdout, /validation: ok/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test('live dependency on a suspect artifact remains an integration error', () => {
  const root = mkdtempSync(join(tmpdir(), 'spiral-status-propagation-'));
  try {
    initRepo(root);
    write(root, 'requests/REQ-BASE.ttl', requestTurtle());
    const requestCommit = commitAll(root, 'request');
    write(root, 'designs/DES-B.ttl', designTurtle({ requestCommit }));
    const designCommit = commitAll(root, 'design');
    write(root, 'designs/DES-B.ttl', designTurtle({ requestCommit, status: 'Suspect' }));
    write(root, 'implementations/IMP-C.ttl', implementationTurtle({ designCommit }));
    commitAll(root, 'mark design suspect but keep live implementation');

    const result = spiralResult(root, 'validate');
    assert.equal(result.status, 1, result.stdout + result.stderr);
    assert.match(result.stderr, /reference-to-non-effective-artifact/);
    assert.match(result.stderr, /IMP-C implements depends on current non-effective artifact/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test('rejected superseder does not retire an otherwise effective upstream version', () => {
  const root = mkdtempSync(join(tmpdir(), 'spiral-rejected-superseder-'));
  try {
    initRepo(root);
    write(root, 'requests/REQ-BASE.ttl', requestTurtle());
    const requestCommit = commitAll(root, 'request');
    write(root, 'designs/DES-B.ttl', designTurtle({ requestCommit }));
    commitAll(root, 'design');
    write(root, 'requests/REQ-REJECTED.ttl', `@prefix sd: <https://muze.nl/ns/spiral-developer#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix project: <https://example.test/project/> .

project:REQ-REJECTED
    a sd:Request ;
    dcterms:identifier "REQ-REJECTED" ;
    sd:repositoryPath "requests/REQ-REJECTED.md" ;
    sd:status sd:Rejected ;
    sd:supersedes [
        a sd:ArtifactReference ;
        sd:artifact project:REQ-BASE ;
        sd:gitCommit "${requestCommit}"
    ] .
`);
    commitAll(root, 'rejected alternative request');

    const result = spiralResult(root, 'validate');
    assert.equal(result.status, 0, result.stderr || result.stdout);
    assert.match(result.stdout, /validation: ok/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test('distributed allocation slot collision is detected even when artifact IDs differ', () => {
  const root = mkdtempSync(join(tmpdir(), 'spiral-slot-collision-'));
  try {
    initRepo(root);
    const make = (subject, id, kind) => `@prefix sd: <https://muze.nl/ns/spiral-developer#> .\n@prefix dcterms: <http://purl.org/dc/terms/> .\n@prefix project: <https://example.test/project/> .\nproject:${subject} a sd:${kind} ; dcterms:identifier "${id}" ; sd:repositoryPath "${subject}.md" ; sd:status sd:Active .\n`;
    write(root, 'sources/a.ttl', make('A', 'SRC-20260818-ABCDE-1', 'Source'));
    write(root, 'requests/b.ttl', make('B', 'REQ-20260819-ABCDE-1', 'Request'));
    commitAll(root, 'colliding slots');

    const result = spiralResult(root, 'validate');
    assert.equal(result.status, 1, result.stdout + result.stderr);
    assert.match(result.stderr, /duplicate-allocation-slot/);
    assert.match(result.stderr, /workspace ABCDE local sequence 1/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test('ordinary Git merge conflicts stop integration before causal validation', () => {
  const root = mkdtempSync(join(tmpdir(), 'spiral-git-conflict-'));
  try {
    initRepo(root);
    write(root, 'README.md', 'base\n');
    commitAll(root, 'baseline');
    git(root, 'branch', 'target');
    git(root, 'switch', '-q', '-c', 'candidate');
    write(root, 'README.md', 'candidate\n');
    commitAll(root, 'candidate change');
    git(root, 'switch', '-q', 'target');
    write(root, 'README.md', 'target\n');
    commitAll(root, 'target change');

    const result = spiralResult(root, 'validate', 'integration', '--base', 'target', '--head', 'candidate');
    assert.notEqual(result.status, 0);
    assert.match(result.stderr, /prospective merge has Git conflicts/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test('malformed Turtle fails through parser validation', () => {
  const root = mkdtempSync(join(tmpdir(), 'spiral-invalid-turtle-'));
  try {
    initRepo(root);
    write(root, 'bad.ttl', '@prefix x: <https://example.test/> . x:a x:b [ .');
    commitAll(root, 'invalid turtle');
    const result = spiralResult(root, 'validate');
    assert.equal(result.status, 1, result.stdout + result.stderr);
    assert.match(result.stderr, /invalid-turtle/);
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});
