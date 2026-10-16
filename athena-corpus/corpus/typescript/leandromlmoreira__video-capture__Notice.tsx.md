# src/components/ui/Notice.tsx

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/components/ui/Notice.tsx
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { useEffect, useRef } from "react";
import { Animated, StyleSheet, Text } from "react-native";
import { colors, fonts, motion, radii } from "../../theme/tokens";

interface NoticeProps {
  message: string | null;
  tone?: "info" | "error";
}

export function Notice({ message, tone = "info" }: NoticeProps) {
  const reveal = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(reveal, {
      toValue: message ? 1 : 0,
      duration: message ? 260 : 180,
      easing: motion.out,
      useNativeDriver: motion.native,
    }).start();
  }, [message]);

  return (
    <Animated.View
      pointerEvents="none"
      accessibilityLiveRegion="polite"
      style={[
        styles.toast,
        tone === "error" && styles.error,
        {
          opacity: reveal,
          transform: [{ translateY: reveal.interpolate({ inputRange: [0, 1], outputRange: [-8, 0] }) }],
        },
      ]}
    >
      <Text style={styles.text}>{message ?? ""}</Text>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  toast: {
    alignSelf: "center",
    maxWidth: 420,
    paddingHorizontal: 16,
    paddingVertical: 11,
    borderRadius: radii.md,
    backgroundColor: colors.glassStrong,
    borderWidth: 1,
    borderColor: colors.lineStrong,
  },
  error: {
    borderColor: "rgba(255, 59, 46, 0.55)",
  },
  text: {
    fontFamily: fonts.bodyMedium,
    color: colors.bone,
    fontSize: 14,
    textAlign: "center",
  },
});
```
