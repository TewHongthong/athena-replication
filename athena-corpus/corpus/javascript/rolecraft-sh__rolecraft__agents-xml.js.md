# src/commands/agents-xml.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/commands/agents-xml.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
import { agentsXmlApi } from '../api/agents-xml.js'

export async function agentsXmlCommand(writeToFile = false) {
  const result = await agentsXmlApi(writeToFile)

  if (!result.xml) {
    console.log('No skills found in lockfile.')
    return
  }

  if (result.written) {
    console.log(`✅ Wrote skills XML to ${result.path}`)
  } else {
    console.log(result.xml)
  }
}
```
