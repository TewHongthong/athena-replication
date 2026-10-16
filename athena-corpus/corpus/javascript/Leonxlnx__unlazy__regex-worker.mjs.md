# scripts/lib/regex-worker.mjs

- source repo: Leonxlnx/unlazy
- repo url: https://github.com/Leonxlnx/unlazy
- license: MIT
- created_at: 2026-08-09
- file path: scripts/lib/regex-worker.mjs
- commit: 16671491f6679ad9378f52604d3bc2415b4120c7

```javascript
import { parentPort } from "node:worker_threads";

parentPort.once("message", ({ source, flags, output }) => {
  try {
    parentPort.postMessage({ matched: new RegExp(source, flags).test(output) });
  } catch (error) {
    parentPort.postMessage({ error: error.message });
  }
});
```
