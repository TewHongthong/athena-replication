# src/components/studio/CameraRail.tsx

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/components/studio/CameraRail.tsx
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { StyleSheet, View } from "react-native";
import { haptics } from "../../feedback/haptics";
import { IconButton } from "../ui/IconButton";

interface CameraRailProps {
  grid: boolean;
  canFlip: boolean;
  locked: boolean;
  onToggleGrid: () => void;
  onFlip: () => void;
}

export function CameraRail({ grid, canFlip, locked, onToggleGrid, onFlip }: CameraRailProps) {
  return (
    <View style={styles.rail}>
      <IconButton
        icon="grid"
        label="Grade dos terços"
        size={46}
        active={grid}
        onPress={() => {
          haptics.select();
          onToggleGrid();
        }}
      />
      {canFlip ? (
        <IconButton
          icon="flip"
          label="Girar câmera"
          size={46}
          disabled={locked}
          onPress={() => {
            haptics.tap();
            onFlip();
          }}
        />
      ) : null}
    </View>
  );
}

const styles = StyleSheet.create({
  rail: {
    gap: 12,
  },
});
```
