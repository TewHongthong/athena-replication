# src/hooks/useSweep.ts

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/hooks/useSweep.ts
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { useEffect, useRef } from "react";
import { Animated, Easing } from "react-native";
import { motion } from "../theme/tokens";

export function useSweep(cycleKey: unknown, running: boolean, restingValue = 0.75, duration = 1000) {
  const progress = useRef(new Animated.Value(restingValue)).current;

  useEffect(() => {
    if (!running) {
      progress.setValue(restingValue);
      return;
    }
    progress.setValue(0);
    const animation = Animated.timing(progress, {
      toValue: 1,
      duration,
      easing: Easing.linear,
      useNativeDriver: motion.native,
    });
    animation.start();
    return () => animation.stop();
  }, [cycleKey, running]);

  return progress;
}
```
