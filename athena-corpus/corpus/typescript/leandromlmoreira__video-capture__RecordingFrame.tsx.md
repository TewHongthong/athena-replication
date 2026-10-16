# src/components/studio/RecordingFrame.tsx

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/components/studio/RecordingFrame.tsx
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { useEffect, useRef } from "react";
import { Animated, StyleSheet } from "react-native";
import { colors, motion } from "../../theme/tokens";

export function RecordingFrame({ live, radius }: { live: boolean; radius: number }) {
  const presence = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(presence, {
      toValue: live ? 1 : 0,
      duration: live ? 180 : 320,
      easing: motion.out,
      useNativeDriver: motion.native,
    }).start();
  }, [live]);

  return <Animated.View pointerEvents="none" style={[styles.frame, { borderRadius: radius, opacity: presence }]} />;
}

const styles = StyleSheet.create({
  frame: {
    ...StyleSheet.absoluteFill,
    borderWidth: 3,
    borderColor: colors.tally,
  },
});
```
