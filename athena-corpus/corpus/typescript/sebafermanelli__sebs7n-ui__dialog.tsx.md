# docs/site/app/_demos/dialog.tsx

- source repo: sebafermanelli/sebs7n-ui
- repo url: https://github.com/sebafermanelli/sebs7n-ui
- license: MIT
- created_at: 2026-09-23T02:47:39Z
- file path: docs/site/app/_demos/dialog.tsx
- commit: a774dd4d3e4c02918772d5c3182b80ce0a86db3b

```typescript
"use client"

import { useId, useState } from "react"
import { Button } from "sebs7n-ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "sebs7n-ui/dialog"
import { Input } from "sebs7n-ui/input"
import { Label } from "sebs7n-ui/label"

/**
 * Básico
 * El trigger usa `render={<Button … />}`, no `asChild`.
 */
export function Basico() {
  const id = useId()
  return (
    <Dialog>
      <DialogTrigger render={<Button variant="outline" />}>Editar cliente</DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Editar cliente</DialogTitle>
          <DialogDescription>Los cambios se aplican a las facturas nuevas, no a las emitidas.</DialogDescription>
        </DialogHeader>
        <div className="flex flex-col gap-2">
          <Label htmlFor={id}>Razón social</Label>
          <Input defaultValue="Acme S.A." id={id} />
        </div>
        <DialogFooter>
          <DialogClose render={<Button variant="ghost" />}>Cancelar</DialogClose>
          <DialogClose render={<Button variant="accent" />}>Guardar</DialogClose>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}

/**
 * Controlado, con carga
 * `open` en el estado de la app: el diálogo se cierra cuando termina la operación.
 */
export function Controlado() {
  const [abierto, setAbierto] = useState(false)
  const [guardando, setGuardando] = useState(false)
  return (
    <Dialog onOpenChange={setAbierto} open={abierto}>
      <DialogTrigger render={<Button />}>Emitir factura</DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Emitir la factura 0014</DialogTitle>
          <DialogDescription>Se envía a AFIP y después no se puede editar.</DialogDescription>
        </DialogHeader>
        <DialogFooter>
          <DialogClose render={<Button variant="ghost" />}>Cancelar</DialogClose>
          <Button
            loading={guardando}
            onClick={() => {
              setGuardando(true)
              setTimeout(() => {
                setGuardando(false)
                setAbierto(false)
              }, 1400)
            }}
            variant="accent"
          >
            Emitir
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
```
