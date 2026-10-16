# app/ui/toast.js

- source repo: minichao9901/web-serial-rtt-tools
- repo url: https://github.com/minichao9901/web-serial-rtt-tools
- license: Apache-2.0
- created_at: 2026-09-26
- file path: app/ui/toast.js
- commit: f64bcb46aa6899341636bcdf14851cb66800698a

```javascript
/** 右下角提示条。 */
export function toast(msg, kind = 'info', ms = 3400){
  const box = document.getElementById('toasts');
  if (!box) return;
  const el = document.createElement('div');
  el.className = 'toast t-' + kind;
  el.textContent = msg;
  box.appendChild(el);
  setTimeout(() => {
    el.style.transition = 'opacity .25s';
    el.style.opacity = '0';
    setTimeout(() => el.remove(), 260);
  }, ms);
}
```
