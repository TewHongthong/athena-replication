# src/utils/templates/index.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/utils/templates/index.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
import * as basic from './basic.js'
import * as codeReview from './code-review.js'
import * as gitWorkflow from './git-workflow.js'
import * as testing from './testing.js'
import * as security from './security.js'
import * as react from './react.js'

const TEMPLATES = {
  basic: basic,
  'code-review': codeReview,
  'git-workflow': gitWorkflow,
  testing: testing,
  security: security,
  react: react,
}

export function getTemplateNames() {
  return Object.keys(TEMPLATES)
}

export function getTemplate(name) {
  const tmpl = TEMPLATES[name]
  if (!tmpl) {
    const available = getTemplateNames().join(', ')
    throw new Error(
      `Unknown template: "${name}". Available templates: ${available}`,
    )
  }
  return {
    name,
    description: tmpl.description,
    generate: tmpl.generate,
  }
}

export function generateSkill(templateName, opts) {
  const tmpl = getTemplate(templateName)
  return tmpl.generate(opts)
}
```
