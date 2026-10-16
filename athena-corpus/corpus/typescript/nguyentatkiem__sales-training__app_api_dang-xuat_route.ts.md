# app/api/dang-xuat/route.ts

- source repo: nguyentatkiem/sales-training
- repo url: https://github.com/nguyentatkiem/sales-training
- license: MIT
- created_at: 2026-09-26T15:57:03Z
- file path: app/api/dang-xuat/route.ts
- commit: d9b494f9337c83c1aed3f0ee2c18ff135d553720

```typescript
import { NextResponse } from "next/server";
import { dangXuat } from "@/services/xac-thuc";
export async function POST() { await dangXuat(); return NextResponse.json({ ok: true }); }
/** GET /api/dang-xuat?ve=/duong-dan — xóa cookie rồi chuyển hướng (dùng khi phiên cũ không còn hợp lệ). */
export async function GET(req: Request) {
  await dangXuat();
  const ve = new URL(req.url).searchParams.get("ve") || "/dang-nhap";
  return NextResponse.redirect(new URL(ve.startsWith("/") ? ve : "/dang-nhap", req.url));
}
```
