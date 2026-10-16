# src/hooks/useElapsed.ts

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/hooks/useElapsed.ts
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { useEffect, useState } from "react";

export function useElapsed(running: boolean) {
  const [elapsed, setElapsed] = useState(0);

  useEffect(() => {
    if (!running) return;
    const startedAt = Date.now();
    setElapsed(0);
    const timer = setInterval(() => setElapsed(Date.now() - startedAt), 50);
    return () => clearInterval(timer);
  }, [running]);

  return running ? elapsed : 0;
}
```
