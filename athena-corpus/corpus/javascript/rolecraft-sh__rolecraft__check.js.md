# src/api/check.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/api/check.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
import { readLock, getProjectLockPath } from '../utils/lockfile.js'
import { resolveSource } from '../utils/resolver.js'

export async function apiCheck(cwd = process.cwd()) {
  const globalLock = await readLock()
  const projectLock = await readLock(getProjectLockPath(cwd)).catch(() => ({
    skills: {},
  }))
  const allSkills = { ...globalLock.skills, ...projectLock.skills }

  const entries = Object.entries(allSkills)
  if (entries.length === 0) return { skills: [], updatesAvailable: 0, total: 0 }

  const results = []
  let updatesAvailable = 0

  for (const [slug, info] of entries) {
    const source = info.source
    if (!source) {
      results.push({ slug, status: 'skipped', reason: 'no source info' })
      continue
    }

    try {
      const resolved = await resolveSource(source)
      const oldHash = info.contentSha || ''
      const newHash = resolved.contentSha || ''

      if (oldHash && newHash && oldHash !== newHash) {
        results.push({
          slug,
          status: 'update_available',
          oldHash,
          newHash,
          source,
        })
        updatesAvailable++
      } else {
        results.push({ slug, status: 'up_to_date', hash: oldHash, source })
      }
    } catch {
      results.push({
        slug,
        status: 'error',
        reason: `could not check (source: ${source})`,
      })
    }
  }

  return { skills: results, updatesAvailable, total: results.length }
}
```
