# app/api/suc-khoe/route.ts

- source repo: nguyentatkiem/sales-training
- repo url: https://github.com/nguyentatkiem/sales-training
- license: MIT
- created_at: 2026-09-26T15:57:03Z
- file path: app/api/suc-khoe/route.ts
- commit: d9b494f9337c83c1aed3f0ee2c18ff135d553720

```typescript
import { NextResponse } from "next/server";
import { pool } from "@/db/ket-noi";
import { cheDoAI } from "@/services/ai-gateway";
export const dynamic = "force-dynamic";
export async function GET() {
  let db = "ok", role: string | null = null, bypassRls: boolean | null = null;
  try {
    const r = await pool().query<{ role: string; bypass: boolean }>("select current_user as role, (select rolbypassrls from pg_roles where rolname = current_user) as bypass");
    role = r.rows[0].role; bypassRls = r.rows[0].bypass;
  } catch (e) { db = "loi: " + (e as Error).message.slice(0, 120); }
  // RLS chỉ có nghĩa khi role ứng dụng KHÔNG bypass — cảnh báo rõ để ops thấy ngay.
  const ok = db === "ok" && bypassRls === false;
  return NextResponse.json({ ok, db, role, rls_hieu_luc: bypassRls === false, ai: cheDoAI(), luc: new Date().toISOString() }, { status: db === "ok" ? 200 : 500 });
}
```
