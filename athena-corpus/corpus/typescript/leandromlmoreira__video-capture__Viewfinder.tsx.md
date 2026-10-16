# src/capture/Viewfinder.tsx

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/capture/Viewfinder.tsx
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { CameraView } from "expo-camera";
import { useImperativeHandle, useRef } from "react";
import { StyleSheet } from "react-native";
import { ViewfinderProps } from "./viewfinder.types";

export function Viewfinder({ ref, facing, onReady, onFailure }: ViewfinderProps) {
  const cameraRef = useRef<CameraView>(null);

  useImperativeHandle(ref, () => ({
    start: async (limitSeconds) => {
      const video = await cameraRef.current?.recordAsync(
        limitSeconds > 0 ? { maxDuration: limitSeconds } : undefined,
      );
      return video?.uri ? { uri: video.uri, mimeType: "video/mp4" } : null;
    },
    stop: () => cameraRef.current?.stopRecording(),
  }));

  return (
    <CameraView
      ref={cameraRef}
      style={StyleSheet.absoluteFill}
      facing={facing}
      mode="video"
      onCameraReady={onReady}
      onMountError={(event) => onFailure(event.message)}
    />
  );
}
```
