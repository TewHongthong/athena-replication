# src/domain/countdown.ts

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/domain/countdown.ts
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
export const countdownOptions = [0, 3, 5];

export function countdownDigit(elapsedMs: number, seconds: number) {
  if (seconds <= 0) return null;
  const digit = seconds - Math.floor(Math.max(0, elapsedMs) / 1000);
  return digit > 0 ? digit : null;
}

export function nextCountdown(current: number) {
  const index = countdownOptions.indexOf(current);
  return countdownOptions[(index + 1) % countdownOptions.length];
}
```
