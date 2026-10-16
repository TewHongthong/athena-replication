# src/capture/viewfinder.types.ts

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/capture/viewfinder.types.ts
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { Ref } from "react";
import { Facing } from "../domain/recording";

export interface CaptureResult {
  uri: string;
  mimeType: string;
  blob?: Blob;
}

export interface ViewfinderHandle {
  start: (limitSeconds: number) => Promise<CaptureResult | null>;
  stop: () => void;
}

export interface ViewfinderProps {
  ref: Ref<ViewfinderHandle>;
  facing: Facing;
  demo: boolean;
  onReady: () => void;
  onFailure: (message: string) => void;
}
```
