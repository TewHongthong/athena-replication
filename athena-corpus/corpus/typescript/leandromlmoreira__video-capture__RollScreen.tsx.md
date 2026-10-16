# src/screens/RollScreen.tsx

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/screens/RollScreen.tsx
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { StyleSheet, Text, View } from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";
import { RollPanel } from "../components/roll/RollPanel";
import { IconButton } from "../components/ui/IconButton";
import { Recording } from "../domain/recording";
import { colors, fonts } from "../theme/tokens";

interface RollScreenProps {
  recordings: Recording[];
  loading: boolean;
  onBack: () => void;
  onOpen: (recording: Recording) => void;
}

export function RollScreen({ recordings, loading, onBack, onOpen }: RollScreenProps) {
  const insets = useSafeAreaInsets();
  return (
    <View style={[styles.screen, { paddingTop: insets.top + 12, paddingBottom: insets.bottom }]}>
      <View style={styles.bar}>
        <IconButton icon="back" label="Voltar para a câmera" size={44} onPress={onBack} />
        <Text style={styles.crumb}>CÂMERA / ROLO</Text>
      </View>
      <RollPanel recordings={recordings} loading={loading} onOpen={onOpen} onRecord={onBack} />
    </View>
  );
}

const styles = StyleSheet.create({
  screen: {
    ...StyleSheet.absoluteFill,
    backgroundColor: colors.ink,
    paddingHorizontal: 16,
  },
  bar: {
    flexDirection: "row",
    alignItems: "center",
    gap: 14,
    paddingBottom: 20,
  },
  crumb: {
    fontFamily: fonts.monoMedium,
    fontSize: 10.5,
    letterSpacing: 1.4,
    color: colors.faint,
  },
});
```
