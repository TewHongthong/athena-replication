# playwright.config.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: playwright.config.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
import {defineConfig,devices} from '@playwright/test';

export default defineConfig({
  testDir:'./tests/e2e',fullyParallel:false,forbidOnly:!!process.env.CI,timeout:60_000,
  snapshotPathTemplate:'{testDir}/{testFilePath}-snapshots/{arg}{ext}',
  retries:process.env.CI?1:0,workers:process.env.CI?2:3,
  reporter:process.env.CI?'github':'list',
  use:{baseURL:'http://127.0.0.1:4173',screenshot:'only-on-failure',trace:'retain-on-failure',video:'retain-on-failure'},
  webServer:{command:'npm run serve',url:'http://127.0.0.1:4173',reuseExistingServer:!process.env.CI,timeout:30_000},
  projects:[{name:'chromium',use:{...devices['Desktop Chrome']}}]
});
```
