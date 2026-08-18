#!/usr/bin/env node

import { randomInt } from 'node:crypto';
import {
  existsSync,
  mkdirSync,
  readFileSync,
  renameSync,
  rmSync,
  statSync,
  writeFileSync,
} from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { spawnSync } from 'node:child_process';

const RANDOM_WORKSPACE_ALPHABET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ';
const RANDOM_WORKSPACE_LENGTH = 5;
const WORKSPACE_RE = /^[A-Z0-9]{2,12}$/;
const TYPE_CODE_RE = /^[A-Z][A-Z0-9]{1,7}$/;
const LOCK_STALE_MS = 30_000;
const LOCK_WAIT_MS = 5_000;

const TYPE_ALIASES = new Map([
  ['source', 'SRC'],
  ['understanding', 'UND'],
  ['request', 'REQ'],
  ['design', 'DES'],
  ['implementation', 'IMP'],
  ['evidence', 'EVD'],
  ['verification', 'EVD'],
  ['acceptance', 'ACC'],
  ['feedback', 'FBK'],
  ['defect', 'DEF'],
  ['cycle', 'CYC'],
  ['constraint', 'EXT'],
  ['external-constraint', 'EXT'],
  ['risk', 'RSK'],
  ['lesson', 'LES'],
  ['culture', 'CUL'],
  ['warning-profile', 'WPF'],
  ['context', 'CTX'],
  ['legacy-context', 'LEG'],
]);

function fail(message, exitCode = 1) {
  console.error(`spiral: ${message}`);
  process.exit(exitCode);
}

function runGit(args) {
  const result = spawnSync('git', args, {
    cwd: process.cwd(),
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  if (result.status !== 0) {
    const detail = result.stderr.trim() || result.stdout.trim();
    throw new Error(detail || `git ${args.join(' ')} failed`);
  }
  return result.stdout.trim();
}

function resolveStateDir() {
  if (runGit(['rev-parse', '--is-inside-work-tree']) !== 'true') {
    throw new Error('current directory is not inside a Git worktree');
  }
  const gitDir = runGit(['rev-parse', '--path-format=absolute', '--git-dir']);
  return join(resolve(gitDir), 'spiral');
}

function sleep(ms) {
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
}

function withAllocationLock(stateDir, fn) {
  mkdirSync(stateDir, { recursive: true });
  const lockDir = join(stateDir, 'allocation.lock');
  const started = Date.now();

  while (true) {
    try {
      mkdirSync(lockDir);
      break;
    } catch (error) {
      if (error?.code !== 'EEXIST') throw error;
      try {
        if (Date.now() - statSync(lockDir).mtimeMs > LOCK_STALE_MS) {
          rmSync(lockDir, { recursive: true, force: true });
          continue;
        }
      } catch (statError) {
        if (statError?.code !== 'ENOENT') throw statError;
      }
      if (Date.now() - started > LOCK_WAIT_MS) {
        throw new Error(`timed out waiting for allocator lock at ${lockDir}`);
      }
      sleep(10);
    }
  }

  try {
    return fn();
  } finally {
    rmSync(lockDir, { recursive: true, force: true });
  }
}

function atomicWrite(path, value) {
  mkdirSync(dirname(path), { recursive: true });
  const tmp = `${path}.tmp-${process.pid}-${randomInt(1_000_000_000)}`;
  writeFileSync(tmp, value, { encoding: 'utf8', mode: 0o600 });
  renameSync(tmp, path);
}

function normalizeWorkspaceId(value) {
  const normalized = value.trim().toUpperCase();
  if (!WORKSPACE_RE.test(normalized)) {
    throw new Error('workspace ID must contain 2–12 ASCII letters/digits and no separators');
  }
  return normalized;
}

function randomWorkspaceId() {
  let result = '';
  for (let i = 0; i < RANDOM_WORKSPACE_LENGTH; i += 1) {
    result += RANDOM_WORKSPACE_ALPHABET[randomInt(RANDOM_WORKSPACE_ALPHABET.length)];
  }
  return result;
}

function workspacePath(stateDir) {
  return join(stateDir, 'workspace-id');
}

function sequencePath(stateDir) {
  return join(stateDir, 'sequence');
}

function readWorkspaceId(stateDir) {
  const path = workspacePath(stateDir);
  if (!existsSync(path)) return null;
  return normalizeWorkspaceId(readFileSync(path, 'utf8'));
}

function initializeWorkspaceLocked(stateDir, requested = null) {
  const existing = readWorkspaceId(stateDir);
  const normalizedRequested = requested ? normalizeWorkspaceId(requested) : null;

  if (existing) {
    if (normalizedRequested && normalizedRequested !== existing) {
      throw new Error(`workspace is already initialized as ${existing}; refusing to change it to ${normalizedRequested}`);
    }
    return existing;
  }

  const workspace = normalizedRequested || randomWorkspaceId();
  atomicWrite(workspacePath(stateDir), `${workspace}\n`);
  if (!existsSync(sequencePath(stateDir))) atomicWrite(sequencePath(stateDir), '0\n');
  return workspace;
}

function readSequence(stateDir) {
  const path = sequencePath(stateDir);
  if (!existsSync(path)) return 0;
  const raw = readFileSync(path, 'utf8').trim();
  if (!/^(0|[1-9][0-9]*)$/.test(raw)) {
    throw new Error(`invalid allocator sequence in ${path}: ${JSON.stringify(raw)}`);
  }
  const value = Number(raw);
  if (!Number.isSafeInteger(value)) throw new Error(`allocator sequence is too large in ${path}`);
  return value;
}

function normalizeType(input) {
  const raw = input.trim();
  const alias = TYPE_ALIASES.get(raw.toLowerCase());
  if (alias) return alias;
  const code = raw.toUpperCase();
  if (!TYPE_CODE_RE.test(code)) {
    throw new Error('artifact type must be a known name or a 2–8 character uppercase code');
  }
  return code;
}

function localDateStamp(date = new Date()) {
  const year = String(date.getFullYear()).padStart(4, '0');
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}${month}${day}`;
}

function allocate(typeInput) {
  const type = normalizeType(typeInput);
  const stateDir = resolveStateDir();
  return withAllocationLock(stateDir, () => {
    const workspace = initializeWorkspaceLocked(stateDir);
    const next = readSequence(stateDir) + 1;
    if (!Number.isSafeInteger(next)) throw new Error('allocator sequence exhausted JavaScript safe integer range');
    atomicWrite(sequencePath(stateDir), `${next}\n`);
    return `${type}-${localDateStamp()}-${workspace}-${next}`;
  });
}

function initWorkspace(requested) {
  const stateDir = resolveStateDir();
  return withAllocationLock(stateDir, () => initializeWorkspaceLocked(stateDir, requested));
}

function status() {
  const stateDir = resolveStateDir();
  const workspace = readWorkspaceId(stateDir);
  const sequence = readSequence(stateDir);
  console.log(`workspace: ${workspace || '(uninitialized)'}`);
  console.log(`sequence: ${sequence}`);
  console.log(`next-sequence: ${sequence + 1}`);
  console.log(`state: ${stateDir}`);
}

function help() {
  console.log(`Spiral Developer CLI\n\nUsage:\n  spiral workspace init [ID]\n  spiral status\n  spiral allocate <TYPE>\n\nCommands:\n  workspace init [ID]  Initialize this Git worktree's stable allocation namespace.\n                       Without ID, generate a 5-character random namespace.\n  status               Show worktree-local allocator state.\n  allocate <TYPE>      Allocate and print TYPE-YYYYMMDD-WORKSPACE-N.\n\nExamples:\n  spiral workspace init AUKE\n  spiral allocate source\n  spiral allocate DES\n`);
}

try {
  const args = process.argv.slice(2);
  if (args.length === 0 || args[0] === '--help' || args[0] === '-h' || args[0] === 'help') {
    help();
  } else if (args[0] === 'status' && args.length === 1) {
    status();
  } else if (args[0] === 'allocate' && args.length === 2) {
    console.log(allocate(args[1]));
  } else if (args[0] === 'workspace' && args[1] === 'init' && args.length <= 3) {
    console.log(initWorkspace(args[2] || null));
  } else {
    fail('unknown or incomplete command; run `spiral --help`');
  }
} catch (error) {
  fail(error instanceof Error ? error.message : String(error));
}
