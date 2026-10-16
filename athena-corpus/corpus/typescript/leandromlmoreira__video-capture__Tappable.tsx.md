# src/components/ui/Tappable.tsx

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/components/ui/Tappable.tsx
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { ReactNode, useRef, useState } from "react";
import { Animated, Pressable, PressableProps, StyleProp, ViewStyle } from "react-native";
import { motion } from "../../theme/tokens";

export interface Interaction {
  pressed: boolean;
  hovered: boolean;
}

interface TappableProps extends Omit<PressableProps, "style" | "children"> {
  style?: StyleProp<ViewStyle> | ((state: Interaction) => StyleProp<ViewStyle>);
  children: ReactNode | ((state: Interaction) => ReactNode);
  pressScale?: number;
}

const AnimatedPressable = Animated.createAnimatedComponent(Pressable);

export function Tappable({ style, children, pressScale = 0.96, disabled, ...rest }: TappableProps) {
  const scale = useRef(new Animated.Value(1)).current;
  const [hovered, setHovered] = useState(false);
  const [pressed, setPressed] = useState(false);
  const state = { pressed, hovered: hovered && !disabled };

  const animateTo = (value: number, duration: number) =>
    Animated.timing(scale, { toValue: value, duration, easing: motion.out, useNativeDriver: motion.native }).start();

  return (
    <AnimatedPressable
      {...rest}
      disabled={disabled}
      onHoverIn={() => setHovered(true)}
      onHoverOut={() => setHovered(false)}
      onPressIn={(event) => {
        setPressed(true);
        animateTo(pressScale, 120);
        rest.onPressIn?.(event);
      }}
      onPressOut={(event) => {
        setPressed(false);
        animateTo(1, 260);
        rest.onPressOut?.(event);
      }}
      style={[typeof style === "function" ? style(state) : style, { transform: [{ scale }] }]}
    >
      {typeof children === "function" ? children(state) : children}
    </AnimatedPressable>
  );
}
```
