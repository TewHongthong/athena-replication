# docs/site/app/_demos/empty-state.tsx

- source repo: sebafermanelli/sebs7n-ui
- repo url: https://github.com/sebafermanelli/sebs7n-ui
- license: MIT
- created_at: 2026-09-23T02:47:39Z
- file path: docs/site/app/_demos/empty-state.tsx
- commit: a774dd4d3e4c02918772d5c3182b80ce0a86db3b

```typescript
"use client"

import { FileTextIcon, SearchXIcon } from "lucide-react"
import { Button } from "sebs7n-ui/button"
import { EmptyState } from "sebs7n-ui/empty-state"

/**
 * Los dos vacíos
 * «Todavía no hay nada» y «el filtro no encontró nada» no son el mismo texto.
 */
export function Basico() {
  return (
    <div className="flex w-full flex-col gap-4">
      <EmptyState
        action={<Button variant="accent">Nueva factura</Button>}
        description="Cuando emitas la primera, va a aparecer acá con su estado y su vencimiento."
        icon={<FileTextIcon />}
        title="Todavía no emitiste ninguna factura"
      />
      <EmptyState
        action={<Button variant="outline">Limpiar filtros</Button>}
        description="Probá con otro rango de fechas o sacá el filtro de cliente."
        icon={<SearchXIcon />}
        title="Ninguna factura coincide con el filtro"
      />
    </div>
  )
}
```
