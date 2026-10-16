# src/react-native/iso-layout-effect.ts

- source repo: guillermolg00/morphicons
- repo url: https://github.com/guillermolg00/morphicons
- license: MIT
- created_at: 2026-08-01
- file path: src/react-native/iso-layout-effect.ts
- commit: 38d2a7221633a453eeafebd872ee3649b9274b22

```typescript
/* Which React effect the binding runs its pre-paint work in.

   The probe is `window`, deliberately, and NEVER `document`: a real React
   Native runtime has no `document` even on a device, so keying off it demotes
   every layout effect in the binding to a passive one — and the Fabric repair
   in index.tsx must run inside the commit, or the stale `d` React just
   reconciled reaches the screen for a frame before the repair lands.
   `window` is the honest server probe instead: React Native defines it,
   react-native-web's server render does not (and there useLayoutEffect warns
   and does nothing, which is what this shim exists to avoid). */

import { useEffect, useLayoutEffect } from "react";

export const useIsoLayoutEffect =
  typeof window === "undefined" ? useEffect : useLayoutEffect;
```
