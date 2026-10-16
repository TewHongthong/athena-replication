# docs/site/app/_demos/label.tsx

- source repo: sebafermanelli/sebs7n-ui
- repo url: https://github.com/sebafermanelli/sebs7n-ui
- license: MIT
- created_at: 2026-09-23T02:47:39Z
- file path: docs/site/app/_demos/label.tsx
- commit: a774dd4d3e4c02918772d5c3182b80ce0a86db3b

```typescript
"use client"

import { useId } from "react"
import { Input } from "sebs7n-ui/input"
import { Label } from "sebs7n-ui/label"

/** Opcional y obligatorio */
export function Basico() {
  const cuit = useId()
  const alias = useId()
  return (
    <div className="flex w-full max-w-sm flex-col gap-4">
      <div className="flex flex-col gap-2">
        <Label htmlFor={cuit} required>
          CUIT
        </Label>
        <Input id={cuit} placeholder="30-71234567-9" required />
      </div>
      <div className="flex flex-col gap-2">
        <Label htmlFor={alias}>Alias</Label>
        <Input id={alias} placeholder="acme.pagos" />
      </div>
    </div>
  )
}
```
