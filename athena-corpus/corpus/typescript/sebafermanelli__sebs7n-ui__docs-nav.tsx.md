# docs/site/app/_components/docs-nav.tsx

- source repo: sebafermanelli/sebs7n-ui
- repo url: https://github.com/sebafermanelli/sebs7n-ui
- license: MIT
- created_at: 2026-09-23T02:47:39Z
- file path: docs/site/app/_components/docs-nav.tsx
- commit: a774dd4d3e4c02918772d5c3182b80ce0a86db3b

```typescript
"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import { SidebarGroup, SidebarGroupLabel, SidebarItem } from "sebs7n-ui/sidebar"

type Grupo = { id: string; title: string; items: { title: string; href: string }[] }

/** Los grupos de site.json, con los componentes del paquete: el sitio es su propia demo. */
export function DocsNav({ nav }: { nav: Grupo[] }) {
  const pathname = usePathname()
  return (
    <>
      {nav.map((grupo) => (
        <SidebarGroup key={grupo.id}>
          <SidebarGroupLabel>{grupo.title}</SidebarGroupLabel>
          {grupo.items.map((item) => (
            <SidebarItem active={pathname === item.href} key={item.href} render={<Link href={item.href} />}>
              {item.title}
            </SidebarItem>
          ))}
        </SidebarGroup>
      ))}
    </>
  )
}
```
