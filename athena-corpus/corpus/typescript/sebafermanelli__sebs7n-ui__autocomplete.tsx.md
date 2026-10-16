# docs/site/app/_demos/autocomplete.tsx

- source repo: sebafermanelli/sebs7n-ui
- repo url: https://github.com/sebafermanelli/sebs7n-ui
- license: MIT
- created_at: 2026-09-23T02:47:39Z
- file path: docs/site/app/_demos/autocomplete.tsx
- commit: a774dd4d3e4c02918772d5c3182b80ce0a86db3b

```typescript
"use client"

import {
  Autocomplete,
  AutocompleteContent,
  AutocompleteEmpty,
  AutocompleteInput,
  AutocompleteItem,
  AutocompleteList,
} from "sebs7n-ui/autocomplete"
import { Label } from "sebs7n-ui/label"

const CIUDADES = ["Barcelona", "Bogotá", "Buenos Aires", "Córdoba", "Lima", "Madrid", "Montevideo", "Rosario", "Santiago"]

/**
 * Texto libre con sugerencias
 * Un valor que no está en la lista también vale.
 */
export function Basico() {
  return (
    <div className="flex w-full max-w-sm flex-col gap-2">
      <Label htmlFor="ciudad">Ciudad</Label>
      <Autocomplete items={CIUDADES}>
        <AutocompleteInput id="ciudad" placeholder="Escribí o elegí" />
        <AutocompleteContent>
          <AutocompleteEmpty />
          <AutocompleteList>
            {(item: string) => (
              <AutocompleteItem key={item} value={item}>
                {item}
              </AutocompleteItem>
            )}
          </AutocompleteList>
        </AutocompleteContent>
      </Autocomplete>
    </div>
  )
}
```
