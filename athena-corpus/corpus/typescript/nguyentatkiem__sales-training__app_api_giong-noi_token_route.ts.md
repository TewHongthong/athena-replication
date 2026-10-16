# app/api/giong-noi/token/route.ts

- source repo: nguyentatkiem/sales-training
- repo url: https://github.com/nguyentatkiem/sales-training
- license: MIT
- created_at: 2026-09-26T15:57:03Z
- file path: app/api/giong-noi/token/route.ts
- commit: d9b494f9337c83c1aed3f0ee2c18ff135d553720

```typescript
import { NextResponse } from "next/server";
import { layPhien } from "@/services/xac-thuc";
import { voiWorkspace } from "@/services/workspace-guard";
import { tokenAzure } from "@/services/giong-noi";
export const dynamic = "force-dynamic";
export async function GET() {
  const phien = await layPhien(); if (!phien) return NextResponse.json({ loi: "Chưa đăng nhập" }, { status: 401 });
  const t = await voiWorkspace(phien.workspaceId, (q) => tokenAzure(q));
  if (!t) return NextResponse.json({ loi: "Workspace chưa cấu hình Azure Speech" }, { status: 404 });
  return NextResponse.json(t, { headers: { "cache-control": "no-store" } });
}
```
