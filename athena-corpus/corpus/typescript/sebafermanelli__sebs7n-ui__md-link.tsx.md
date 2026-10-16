# docs/site/app/_components/md-link.tsx

- source repo: sebafermanelli/sebs7n-ui
- repo url: https://github.com/sebafermanelli/sebs7n-ui
- license: MIT
- created_at: 2026-09-23T02:47:39Z
- file path: docs/site/app/_components/md-link.tsx
- commit: a774dd4d3e4c02918772d5c3182b80ce0a86db3b

```typescript
import { FileTextIcon } from "lucide-react"
import { buttonVariants } from "sebs7n-ui/variants/button"

/** El mismo contenido en texto plano, para un agente. */
export function MdLink({ href }: { href: string }) {
  return (
    <a className={buttonVariants({ variant: "outline", size: "sm" })} href={`${href}.md`}>
      <FileTextIcon />
      Ver como .md
    </a>
  )
}
```
