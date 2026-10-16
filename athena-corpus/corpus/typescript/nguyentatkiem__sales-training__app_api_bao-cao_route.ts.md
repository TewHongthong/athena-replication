# app/api/bao-cao/route.ts

- source repo: nguyentatkiem/sales-training
- repo url: https://github.com/nguyentatkiem/sales-training
- license: MIT
- created_at: 2026-09-26T15:57:03Z
- file path: app/api/bao-cao/route.ts
- commit: d9b494f9337c83c1aed3f0ee2c18ff135d553720

```typescript
import { NextResponse } from "next/server";
import { layPhien } from "@/services/xac-thuc";
import { voiWorkspace } from "@/services/workspace-guard";
import { baoCaoDoi, csvBaoCao } from "@/services/bao-cao";
export const dynamic = "force-dynamic";
export async function GET(req: Request) {
  const phien = await layPhien();
  if (!phien || phien.vaiTro !== "quan_ly") return NextResponse.json({ loi: "Chỉ quản lý" }, { status: 403 });
  const ngay = Math.min(365, Math.max(1, Number(new URL(req.url).searchParams.get("ngay") ?? 30) || 30));
  const { dong } = await voiWorkspace(phien.workspaceId, (q) => baoCaoDoi(q, ngay));
  return new NextResponse(csvBaoCao(dong), { headers: { "content-type": "text/csv; charset=utf-8", "content-disposition": `attachment; filename="bao-cao-dao-tao-${ngay}-ngay.csv"` } });
}
```
