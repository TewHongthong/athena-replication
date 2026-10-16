# src/hooks/useRecordings.ts

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/hooks/useRecordings.ts
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { useCallback, useEffect, useState } from "react";
import { NewRecording, Recording } from "../domain/recording";
import { addRecording, listRecordings, removeRecording } from "../storage/recordingStore";

export function useRecordings() {
  const [recordings, setRecordings] = useState<Recording[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    listRecordings()
      .then(setRecordings)
      .catch(() => setRecordings([]))
      .finally(() => setLoading(false));
  }, []);

  const add = useCallback(async (input: NewRecording) => {
    const recording = await addRecording(input);
    setRecordings((current) => [recording, ...current]);
    return recording;
  }, []);

  const remove = useCallback(async (recording: Recording) => {
    await removeRecording(recording);
    setRecordings((current) => current.filter((item) => item.id !== recording.id));
  }, []);

  return { recordings, loading, add, remove };
}
```
