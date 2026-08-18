import assert from 'node:assert/strict';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { execFileSync, spawn } from 'node:child_process';
import test from 'node:test';

const cli = resolve('bin/spiral.mjs');

function git(cwd, ...args) {
  return execFileSync('git', args, { cwd, encoding: 'utf8' }).trim();
}

function spiral(cwd, ...args) {
  return execFileSync(process.execPath, [cli, ...args], { cwd, encoding: 'utf8' }).trim();
}

function initRepo(path) {
  git(path, 'init', '-q');
  git(path, 'config', 'user.email', 'spiral-test@example.invalid');
  git(path, 'config', 'user.name', 'Spiral Test');
  git(path, 'commit', '--allow-empty', '-q', '-m', 'baseline');
}

function workspaceFrom(id) {
  const match = id.match(/^[A-Z][A-Z0-9]*-\d{8}-([A-Z0-9]+)-(\d+)$/);
  assert.ok(match, `unexpected ID shape: ${id}`);
  return { workspace: match[1], sequence: Number(match[2]) };
}

function spawnSpiral(cwd, ...args) {
  return new Promise((resolvePromise, reject) => {
    const child = spawn(process.execPath, [cli, ...args], { cwd, stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = '';
    let stderr = '';
    child.stdout.on('data', (chunk) => { stdout += chunk; });
    child.stderr.on('data', (chunk) => { stderr += chunk; });
    child.on('error', reject);
    child.on('close', (code) => {
      if (code === 0) resolvePromise(stdout.trim());
      else reject(new Error(stderr.trim() || `spiral exited ${code}`));
    });
  });
}

test('chosen workspace stays stable and one sequence spans artifact types', () => {
  const root = mkdtempSync(join(tmpdir(), 'spiral-allocator-'));
  try {
    initRepo(root);
    assert.equal(spiral(root, 'workspace', 'init', 'auke'), 'AUKE');

    const first = spiral(root, 'allocate', 'source');
    const second = spiral(root, 'allocate', 'DES');
    assert.match(first, /^SRC-\d{8}-AUKE-1$/);
    assert.match(second, /^DES-\d{8}-AUKE-2$/);
    assert.doesNotMatch(first, /-001$/);

    const status = spiral(root, 'status');
    assert.match(status, /^workspace: AUKE$/m);
    assert.match(status, /^sequence: 2$/m);
    assert.match(status, /^next-sequence: 3$/m);
    assert.equal(git(root, 'status', '--porcelain'), '');

    assert.throws(
      () => spiral(root, 'workspace', 'init', 'OTHER'),
      /already initialized as AUKE/,
    );
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test('independent clone and linked worktree get independent default namespaces', () => {
  const root = mkdtempSync(join(tmpdir(), 'spiral-distributed-'));
  try {
    const primary = join(root, 'primary');
    const clone = join(root, 'clone');
    const worktree = join(root, 'worktree');
    execFileSync('mkdir', ['-p', primary]);
    initRepo(primary);

    git(root, 'clone', '-q', primary, clone);
    git(primary, 'worktree', 'add', '-q', '-b', 'parallel-worktree', worktree);

    const primaryId = spiral(primary, 'allocate', 'REQ');
    const cloneId = spiral(clone, 'allocate', 'REQ');
    const worktreeId = spiral(worktree, 'allocate', 'REQ');

    const p = workspaceFrom(primaryId);
    const c = workspaceFrom(cloneId);
    const w = workspaceFrom(worktreeId);

    assert.equal(p.sequence, 1);
    assert.equal(c.sequence, 1);
    assert.equal(w.sequence, 1);
    assert.equal(new Set([p.workspace, c.workspace, w.workspace]).size, 3);
    assert.match(p.workspace, /^[0-9A-HJKMNP-TV-Z]{5}$/);
    assert.match(c.workspace, /^[0-9A-HJKMNP-TV-Z]{5}$/);
    assert.match(w.workspace, /^[0-9A-HJKMNP-TV-Z]{5}$/);

    assert.equal(git(primary, 'status', '--porcelain'), '');
    assert.equal(git(clone, 'status', '--porcelain'), '');
    assert.equal(git(worktree, 'status', '--porcelain'), '');
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test('concurrent allocations in one workspace are serialized', async () => {
  const root = mkdtempSync(join(tmpdir(), 'spiral-concurrent-'));
  try {
    initRepo(root);
    spiral(root, 'workspace', 'init', 'TEAM1');
    const ids = await Promise.all(
      Array.from({ length: 12 }, () => spawnSpiral(root, 'allocate', 'EVD')),
    );
    const sequences = ids.map((id) => workspaceFrom(id).sequence).sort((a, b) => a - b);
    assert.deepEqual(sequences, Array.from({ length: 12 }, (_, index) => index + 1));
    assert.equal(new Set(ids).size, 12);
    assert.equal(git(root, 'status', '--porcelain'), '');
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});
