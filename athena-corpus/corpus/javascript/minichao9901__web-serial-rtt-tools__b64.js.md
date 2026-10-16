# app/core/b64.js

- source repo: minichao9901/web-serial-rtt-tools
- repo url: https://github.com/minichao9901/web-serial-rtt-tools
- license: Apache-2.0
- created_at: 2026-09-26
- file path: app/core/b64.js
- commit: f64bcb46aa6899341636bcdf14851cb66800698a

```javascript
/** base64 ↔ 字节（桥的 WebSocket 里传二进制用；分块避免 apply 参数上限）。 */

export function toB64(bytes){
  const b = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
  let s = '';
  for (let i = 0; i < b.length; i += 8192) s += String.fromCharCode.apply(null, b.subarray(i, i + 8192));
  return btoa(s);
}

export function fromB64(str){
  if (!str) return new Uint8Array(0);
  const bin = atob(str);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}
```
