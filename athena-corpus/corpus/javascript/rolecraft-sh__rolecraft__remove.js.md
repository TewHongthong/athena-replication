# src/commands/remove.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/commands/remove.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
import { apiRemove } from '../api/remove.js'

export async function removeCommand(slug, options = {}) {
  if (options.dryRun) {
    const result = await apiRemove(slug, process.cwd(), { dryRun: true })
    console.log(`\n📋 [dry-run] Would remove skill:\n`)
    console.log(`   Skill:  ${result.slug}`)
    for (const d of result.dirs) {
      console.log(
        `   ${d.scope === 'global' ? 'Global' : 'Project'}: ${d.path}`,
      )
    }
    console.log()
    return
  }

  const result = await apiRemove(slug, process.cwd())
  console.log(`✅ Removed ${result.slug}.`)
}
```
