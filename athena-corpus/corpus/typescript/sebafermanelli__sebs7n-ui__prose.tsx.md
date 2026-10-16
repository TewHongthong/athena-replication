# docs/site/app/_components/prose.tsx

- source repo: sebafermanelli/sebs7n-ui
- repo url: https://github.com/sebafermanelli/sebs7n-ui
- license: MIT
- created_at: 2026-09-23T02:47:39Z
- file path: docs/site/app/_components/prose.tsx
- commit: a774dd4d3e4c02918772d5c3182b80ce0a86db3b

```typescript
import { marked } from "marked"

marked.use({
  gfm: true,
  async: false,
  renderer: {
    // Anclas en los títulos, para que el índice lateral y los enlaces profundos funcionen.
    heading({ text, depth, tokens }) {
      const plano = this.parser.parseInline(tokens)
      const id = slugify(text)
      return `<h${depth} id="${id}">${plano}</h${depth}>\n`
    },
    // Las tablas de color y tipografía son anchas: van en una caja con scroll propio.
    table(token) {
      const html = (marked.Renderer.prototype.table as (t: typeof token) => string).call(this, token)
      return `<div class="tabla">${html}</div>`
    },
  },
})

export function slugify(text: string) {
  return text
    .toLowerCase()
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "")
}

export function headings(markdown: string) {
  return markdown
    .split("\n")
    .filter((line) => /^##\s/.test(line))
    .map((line) => {
      const text = line.replace(/^##\s+/, "").replace(/[*`]/g, "")
      return { text, id: slugify(line.replace(/^##\s+/, "")) }
    })
}

export function Prose({ markdown }: { markdown: string }) {
  const html = marked.parse(markdown) as string
  // El markdown es nuestro: sale de content/pages/ y de los .md del repo.
  return <div className="prose" dangerouslySetInnerHTML={{ __html: html }} />
}
```
