# app/api/dang-nhap/route.ts

- source repo: nguyentatkiem/sales-training
- repo url: https://github.com/nguyentatkiem/sales-training
- license: MIT
- created_at: 2026-09-26T15:57:03Z
- file path: app/api/dang-nhap/route.ts
- commit: d9b494f9337c83c1aed3f0ee2c18ff135d553720

```typescript
// Đăng nhập dạng JSON (dùng cho kiểm thử tự động và tích hợp): POST {email, mat_khau} → đặt cookie phiên.
import { NextResponse } from "next/server";
import { dangNhap } from "@/services/xac-thuc";
export const dynamic = "force-dynamic";
export async function POST(req: Request) {
  const b = (await req.json().catch(() => ({}))) as { email?: string; mat_khau?: string };
  const kq = await dangNhap(String(b.email ?? ""), String(b.mat_khau ?? ""));
  return NextResponse.json(kq, { status: kq.ok ? 200 : 401 });
}
```
