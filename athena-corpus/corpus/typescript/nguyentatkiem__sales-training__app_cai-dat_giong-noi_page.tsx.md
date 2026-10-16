# app/cai-dat/giong-noi/page.tsx

- source repo: nguyentatkiem/sales-training
- repo url: https://github.com/nguyentatkiem/sales-training
- license: MIT
- created_at: 2026-09-26T15:57:03Z
- file path: app/cai-dat/giong-noi/page.tsx
- commit: d9b494f9337c83c1aed3f0ee2c18ff135d553720

```typescript
import Link from "next/link";
import { KhungShell } from "@/components/KhungShell";
import { FormGiongNoi } from "@/components/FormGiongNoi";
import { nguCanhTrang } from "@/services/trang";
import { layCauHinhGiong, AZURE_VOICES, ELEVEN_MODELS } from "@/services/giong-noi";
export const dynamic = "force-dynamic";
export default async function TrangGiongNoi() {
  const { phien, ws } = await nguCanhTrang();
  const ch = await ws((q) => layCauHinhGiong(q));
  return (
    <KhungShell phien={phien} duongDan="/cai-dat" tieuDe="Giọng nói AI" moTa="Kết nối ElevenLabs hoặc Azure Speech để khách ảo nói bằng giọng tự nhiên và nhận dạng giọng nói chính xác hơn. Khóa được mã hóa, chỉ dùng trong workspace này."
      hanhDong={<Link href="/cai-dat" className="nut">← Cài đặt</Link>}>
      <FormGiongNoi cauHinh={ch} azureVoices={AZURE_VOICES} elevenModels={ELEVEN_MODELS} quanLy={phien.vaiTro === "quan_ly"} />
    </KhungShell>
  );
}
```
