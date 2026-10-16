# src/api/bundle.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/api/bundle.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
import { loadBundleSources, installBundleSources } from './bundle-internal.js'

export async function bundleApi(sources, options = {}) {
  const { sources: skillSources } = await loadBundleSources(sources)
  if (skillSources.length === 0) {
    return { installed: 0, failed: 0, results: [] }
  }
  if (options.dryRun) {
    return { dryRun: true, skills: skillSources }
  }
  return installBundleSources(skillSources, options)
}
```
