# src/components/brand/LeaderLoop.tsx

- source repo: leandromlmoreira/video-capture
- repo url: https://github.com/leandromlmoreira/video-capture
- license: MIT
- created_at: 2026-09-26T07:32:29Z
- file path: src/components/brand/LeaderLoop.tsx
- commit: def6b01cdccbd271a07b0ec29a9e39603f0b9e75

```typescript
import { useEffect, useState } from "react";
import { useReducedMotion } from "../../hooks/useReducedMotion";
import { useSweep } from "../../hooks/useSweep";
import { LeaderDial } from "./LeaderDial";

const sequence = [3, 2, 1, 0];
const holdMs = { lit: 1600, count: 1000 };

export function LeaderLoop({ size }: { size: number }) {
  const reduced = useReducedMotion();
  const [step, setStep] = useState(0);
  const value = sequence[step];
  const lit = value === 0;
  const progress = useSweep(step, !reduced && !lit);

  useEffect(() => {
    if (reduced) return;
    const timer = setTimeout(() => setStep((current) => (current + 1) % sequence.length), lit ? holdMs.lit : holdMs.count);
    return () => clearTimeout(timer);
  }, [step, reduced, lit]);

  return <LeaderDial size={size} digit={reduced ? 1 : value} lit={!reduced && lit} progress={progress} reducedMotion={reduced} />;
}
```
