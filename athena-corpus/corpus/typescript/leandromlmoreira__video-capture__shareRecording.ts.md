# src/actions/shareRecording.ts

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/actions/shareRecording.ts
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import * as Sharing from "expo-sharing";
import { Recording } from "../domain/recording";

export type ShareOutcome = "shared" | "downloaded" | "unavailable";

export const shareIntent: { label: string; icon: "share" | "download" } = {
  label: "Compartilhar",
  icon: "share",
};

export async function shareRecording(recording: Recording): Promise<ShareOutcome> {
  if (!(await Sharing.isAvailableAsync())) return "unavailable";
  await Sharing.shareAsync(recording.uri, {
    mimeType: recording.mimeType,
    dialogTitle: `Tomada ${recording.take}`,
  });
  return "shared";
}
```
