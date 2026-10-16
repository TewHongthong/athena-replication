# src/commands/watch.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/commands/watch.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
import { watchApi } from '../api/watch.js'

function noopClose() {}

function printEvent(event) {
  switch (event.type) {
    case 'start':
      console.log(
        `\n👀 Watching ${event.slugs.length} skill(s) for changes...\n`,
      )
      break
    case 'skip':
      console.log(`   Skipping "${event.slug}" (${event.sourceType} source)`)
      break
    case 'watching':
      console.log(`   ✓ ${event.slug} → watching ${event.path}`)
      break
    case 'error':
      console.error(`   ✗ ${event.slug}: cannot watch (${event.error.message})`)
      break
    case 'syncing':
      console.log(
        `  [${event.startedAt.toLocaleTimeString()}] ${event.slug}: ${event.filename} changed, syncing...`,
      )
      break
    case 'synced':
      console.log(
        `  [${event.startedAt.toLocaleTimeString()}] ${event.slug}: ${event.ok ? 'synced successfully' : 'sync failed'}`,
      )
      break
  }
}

export async function watchCommand(slug, cwd = process.cwd(), options = {}) {
  let result
  try {
    result = await watchApi(slug, cwd, {
      dryRun: options.dryRun,
      onEvent: printEvent,
    })
  } catch (err) {
    if (err.userCode === 'WATCH_SKILL_NOT_FOUND') {
      console.error(err.message)
      return { watchers: [], skills: [], close: noopClose }
    }
    throw err
  }

  if (result.installedCount === 0) {
    console.log('No skills installed. Nothing to watch.')
    return { watchers: [], skills: [], close: noopClose }
  }

  if (result.skills.length === 0) {
    console.log('No local skills to watch.')
    return { watchers: [], skills: [], close: result.close || noopClose }
  }

  if (result.dryRun) {
    console.log(
      `\n📋 [dry-run] Would watch ${result.skills.length} skill(s):\n`,
    )
    for (const s of result.skills) {
      console.log(`   • ${s.slug} → ${s.path}`)
    }
    console.log()
    return {
      watchers: [],
      skills: result.skills.map((s) => s.slug),
      close: noopClose,
    }
  }

  return result
}
```
