# app/api/giong-noi/kiem-tra/route.ts

- source repo: nguyentatkiem/sales-training
- repo url: https://github.com/nguyentatkiem/sales-training
- license: MIT
- created_at: 2026-09-26T15:57:03Z
- file path: app/api/giong-noi/kiem-tra/route.ts
- commit: d9b494f9337c83c1aed3f0ee2c18ff135d553720

```typescript
import { NextResponse } from "next/server";
import { layPhien } from "@/services/xac-thuc";
import { voiWorkspace } from "@/services/workspace-guard";
import { kiemTraAzure, kiemTraEleven } from "@/services/giong-noi";
export const dynamic = "force-dynamic";
export async function POST(req: Request) {
  const phien = await layPhien(); if (!phien || phien.vaiTro !== "quan_ly") return NextResponse.json({ loi: "Chỉ quản lý" }, { status: 403 });
  const b = (await req.json().catch(() => ({}))) as { nha?: string; key?: string; region?: string };
  const r = await voiWorkspace(phien.workspaceId, (q) => (b.nha === "azure" ? kiemTraAzure(q, b.key, b.region) : kiemTraEleven(q, b.key)));
  return NextResponse.json(r);
}
```
