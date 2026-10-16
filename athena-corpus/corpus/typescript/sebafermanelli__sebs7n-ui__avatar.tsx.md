# docs/site/app/_demos/avatar.tsx

- source repo: sebafermanelli/sebs7n-ui
- repo url: https://github.com/sebafermanelli/sebs7n-ui
- license: MIT
- created_at: 2026-09-23T02:47:39Z
- file path: docs/site/app/_demos/avatar.tsx
- commit: a774dd4d3e4c02918772d5c3182b80ce0a86db3b

```typescript
"use client"

import { Avatar, AvatarFallback, AvatarImage } from "sebs7n-ui/avatar"

/** Con imagen y con iniciales */
export function Basico() {
  return (
    <div className="flex items-center gap-4">
      <Avatar size="sm">
        <AvatarFallback>SF</AvatarFallback>
      </Avatar>
      <Avatar>
        <AvatarImage alt="" src="https://avatars.githubusercontent.com/u/9919?s=96&v=4" />
        <AvatarFallback>GH</AvatarFallback>
      </Avatar>
      <Avatar size="lg">
        <AvatarFallback>MR</AvatarFallback>
      </Avatar>
    </div>
  )
}
```
