# src/components/brand/Perforations.tsx

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/components/brand/Perforations.tsx
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { StyleSheet, View } from "react-native";

export function Perforations({ width, pitch = 13 }: { width: number; pitch?: number }) {
  const count = Math.max(4, Math.floor(width / pitch));
  return (
    <View style={styles.row} accessibilityElementsHidden importantForAccessibility="no-hide-descendants">
      {Array.from({ length: count }, (_, index) => (
        <View key={index} style={styles.hole} />
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  row: {
    height: 12,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    paddingHorizontal: 5,
  },
  hole: {
    width: 6,
    height: 4.5,
    borderRadius: 1.5,
    backgroundColor: "rgba(236, 230, 217, 0.2)",
  },
});
```
