# packages/protocol/src/index.ts

- source repo: Brainferno/brainferno-mcp-bridge
- repo url: https://github.com/Brainferno/brainferno-mcp-bridge
- license: Apache-2.0
- created_at: 2026-08-26
- file path: packages/protocol/src/index.ts
- commit: 95695615162b4db4a3189be9dd0ebf9e7d80c129

```typescript
/**
 * @brainferno/mcp-bridge-protocol — the frozen contract shared by the server and every
 * in-app panel: the five hosts, and the v2 wire frames (zod-validated).
 * See docs/protocol.md. Changes here ripple into every panel.
 */
export * from "./apps.js";
export * from "./protocol.js";
```
