# src/feedback/haptics.ts

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/feedback/haptics.ts
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import * as Haptics from "expo-haptics";

function safely(task: () => Promise<void>) {
  task().catch(() => {});
}

export const haptics = {
  select: () => safely(() => Haptics.selectionAsync()),
  tap: () => safely(() => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light)),
  count: () => safely(() => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium)),
  roll: () => safely(() => Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy)),
  cut: () => safely(() => Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success)),
  warn: () => safely(() => Haptics.notificationAsync(Haptics.NotificationFeedbackType.Warning)),
};
```
