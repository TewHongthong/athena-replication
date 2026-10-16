# docs/site/app/_demos/alert-dialog.tsx

- source repo: sebafermanelli/sebs7n-ui
- repo url: https://github.com/sebafermanelli/sebs7n-ui
- license: MIT
- created_at: 2026-09-23T02:47:39Z
- file path: docs/site/app/_demos/alert-dialog.tsx
- commit: a774dd4d3e4c02918772d5c3182b80ce0a86db3b

```typescript
"use client"

import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogClose,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "sebs7n-ui/alert-dialog"
import { Button } from "sebs7n-ui/button"

/**
 * Confirmar algo destructivo
 * `AlertDialogAction` no cierra sola: se envuelve en `AlertDialogClose` o se controla `open`.
 */
export function Basico() {
  return (
    <AlertDialog>
      <AlertDialogTrigger render={<Button variant="destructive" />}>Eliminar factura</AlertDialogTrigger>
      <AlertDialogContent>
        <AlertDialogHeader>
          <AlertDialogTitle>¿Eliminar la factura 0012?</AlertDialogTitle>
          <AlertDialogDescription>
            Se borra del listado y del resumen del mes. No se puede deshacer.
          </AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
          <AlertDialogCancel />
          <AlertDialogClose render={<AlertDialogAction variant="destructive" />}>Eliminar</AlertDialogClose>
        </AlertDialogFooter>
      </AlertDialogContent>
    </AlertDialog>
  )
}
```
