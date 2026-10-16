# src/api/init.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/api/init.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
import { mkdir, writeFile } from 'node:fs/promises'
import { join } from 'node:path'
import { normalizeSlug } from '../utils/lockfile.js'

export async function initApi(name) {
  const skillName = name || 'my-skill'
  const slug = skillName.includes('/') ? skillName : skillName
  const displayName = slug.includes('/') ? slug.split('/')[1] : slug
  const dirName = normalizeSlug(slug)
  const dir = join(process.cwd(), dirName)
  const owner = slug.includes('/') ? slug.split('/')[0] : 'local'

  await mkdir(dir, { recursive: true })

  const content = `---
name: ${displayName}
slug: ${slug}
owner: ${owner}
description: Describe what this skill does
---

Write your skill instructions here.
`

  await writeFile(join(dir, 'SKILL.md'), content)

  return { path: join(dir, 'SKILL.md'), slug, name: displayName, owner }
}
```
