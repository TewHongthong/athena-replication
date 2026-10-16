# src/api/completions.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/api/completions.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
import { bashScript, fishScript, zshScript } from '../commands/completions.js'

export function completionApi(shell) {
  switch (shell) {
    case 'bash':
      return bashScript()
    case 'zsh':
      return zshScript()
    case 'fish':
      return fishScript()
    default:
      throw new Error(`Unknown shell: ${shell}`)
  }
}
```
