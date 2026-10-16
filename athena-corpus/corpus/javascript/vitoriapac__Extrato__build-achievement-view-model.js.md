# src/application/achievements/build-achievement-view-model.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/achievements/build-achievement-view-model.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
export function buildAchievementViewModel(achievements = []) {
  const rows = (Array.isArray(achievements) ? achievements : []).map(item => ({ ...item, unlocked: Boolean(item?.unlocked) }));
  const unlocked = rows.filter(item => item.unlocked);
  const locked = rows.filter(item => !item.unlocked);
  return {
    total: rows.length,
    unlockedCount: unlocked.length,
    remainingCount: locked.length,
    unlocked,
    locked
  };
}
```
