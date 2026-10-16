# src/capture/access.ts

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/capture/access.ts
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
export type AccessStatus = "checking" | "prompt" | "granted" | "denied" | "unavailable" | "not-needed";
export type AccessKey = "camera" | "microphone" | "library";
export type CaptureMode = "setup" | "device" | "demo";

export interface AccessItem {
  key: AccessKey;
  status: AccessStatus;
}

export interface CaptureAccess {
  items: AccessItem[];
  mode: CaptureMode;
  checking: boolean;
  blocked: boolean;
  supportsDemo: boolean;
  request: () => Promise<void>;
  openSettings: () => void;
  enterDemo: () => void;
  backToSetup: () => void;
}
```
