# app/api/dna/route.ts

- source repo: nguyentatkiem/sales-training
- repo url: https://github.com/nguyentatkiem/sales-training
- license: MIT
- created_at: 2026-09-26T15:57:03Z
- file path: app/api/dna/route.ts
- commit: d9b494f9337c83c1aed3f0ee2c18ff135d553720

```typescript
import { NextResponse } from "next/server";
import { layPhien } from "@/services/xac-thuc";
import { voiWorkspace } from "@/services/workspace-guard";
import { trichDnaTuVanBan } from "@/services/dna";
export const dynamic = "force-dynamic";
export const maxDuration = 180;
export async function POST(req: Request) {
  const phien = await layPhien();
  if (!phien || phien.vaiTro !== "quan_ly") return NextResponse.json({ loi: "Chỉ quản lý" }, { status: 403 });
  const b = (await req.json().catch(() => ({}))) as { van_ban?: string };
  try { return NextResponse.json(await voiWorkspace(phien.workspaceId, (q) => trichDnaTuVanBan(q, { workspaceId: phien.workspaceId, vanBan: String(b.van_ban ?? "") }))); }
  catch (e) { return NextResponse.json({ loi: (e as Error).message }, { status: 400 }); }
}
```
