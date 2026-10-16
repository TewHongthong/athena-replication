# src/commands/use.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/commands/use.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
import { apiUse } from '../api/use.js'

export async function useCommand(source, options = {}) {
  const result = await apiUse(source, options)

  if (options.list) {
    console.log(`\nFound ${result.skills.length} skill(s) from: ${source}\n`)
    for (const s of result.skills) {
      console.log(`  ${s.name}`)
      console.log(`    Slug:       ${s.slug}`)
      console.log(`    Owner:      ${s.owner}`)
      if (s.description) console.log(`    Description: ${s.description}`)
      console.log(`    Files:      ${s.files.join(', ')}`)
      console.log()
    }
    return
  }

  for (const resolved of result.skills) {
    console.log(`\n📦 Skill: ${resolved.name}`)
    console.log(`   Slug:     ${resolved.slug}`)
    console.log(`   Owner:    ${resolved.owner}`)
    if (resolved.description)
      console.log(`   Desc:     ${resolved.description}`)
    console.log(`   Files:    ${resolved.files.join(', ')}\n`)

    for (const file of resolved.files) {
      const content = resolved.fileContents?.[file]
      if (!content) continue
      const separator = `─── ${file} ${'─'.repeat(Math.max(0, 50 - file.length))}`
      console.log(separator)
      console.log(content)
      if (!content.endsWith('\n')) console.log()
      console.log()
    }
  }
}
```
