# src/utils/mcp-lock.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/utils/mcp-lock.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
import { readFile, writeFile } from 'node:fs/promises'
import { home } from './paths.js'
import { ensureParentDir } from './lockfile.js'

export function getMcpLockPath() {
  return home('.agents', '.mcp-lock.json')
}

export async function readMcpLock(lockPath = getMcpLockPath()) {
  try {
    const raw = await readFile(lockPath, 'utf-8')

    return JSON.parse(raw)
  } catch {
    return {
      version: 1,
      servers: {},
    }
  }
}

export async function writeMcpLock(data, lockPath = getMcpLockPath()) {
  await ensureParentDir(lockPath)

  await writeFile(lockPath, `${JSON.stringify(data, null, 2)}\n`, 'utf-8')
}

export async function addServerToMcpLock(
  serverName,
  entry,
  lockPath = getMcpLockPath(),
) {
  const lock = await readMcpLock(lockPath)
  const existing = lock.servers[serverName]

  const mergedAgents = existing?.agents
    ? [...new Set([...existing.agents, ...(entry.agents || [])])]
    : entry.agents || []

  lock.servers[serverName] = {
    ...entry,
    agents: mergedAgents,
  }

  await writeMcpLock(lock, lockPath)

  return lock
}

export async function removeServerFromMcpLock(
  serverName,
  agentToRemove,
  lockPath = getMcpLockPath(),
) {
  const lock = await readMcpLock(lockPath)

  if (!lock.servers[serverName]) {
    return lock
  }

  const remaining = (lock.servers[serverName].agents || []).filter(
    (agent) => agent !== agentToRemove,
  )

  if (remaining.length === 0) {
    delete lock.servers[serverName]
  } else {
    lock.servers[serverName].agents = remaining
  }

  await writeMcpLock(lock, lockPath)

  return lock
}
```
