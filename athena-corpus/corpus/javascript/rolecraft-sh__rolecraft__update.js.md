# src/commands/update.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/commands/update.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
import { apiUpdate } from '../api/update.js'

export async function updateCommand(slug, options = {}) {
  if (options.dryRun) {
    const result = await apiUpdate(slug, process.cwd(), { dryRun: true })
    console.log(`\n📋 [dry-run] Would update skill:\n`)
    console.log(`   Skill:   ${result.slug}`)
    console.log(`   Source:  ${result.source} (${result.sourceType})`)
    console.log(`   Targets: ${result.targets.join(', ')}\n`)
    return
  }

  const result = await apiUpdate(slug, process.cwd())
  console.log(`\n🔄 Updating skill: ${result.slug}`)
  console.log(`   Source: ${result.source} (${result.sourceType})`)
  console.log(`   Targets: ${result.targets.join(', ')}\n`)
  console.log('✅ Updated successfully:\n')
  for (const r of result.results) {
    console.log(`   ${r.label} → ${r.path}`)
  }
}
```
