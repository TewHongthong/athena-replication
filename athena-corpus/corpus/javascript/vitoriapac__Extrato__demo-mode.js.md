# src/application/demo/demo-mode.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/demo/demo-mode.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
export const APP_MODES=Object.freeze({REAL:'real',DEMO:'demo'});

export function readAppMode(storage){
  try{return storage?.getItem('bb-premium-mode')===APP_MODES.DEMO?APP_MODES.DEMO:APP_MODES.REAL}catch(error){return APP_MODES.REAL}
}
export function enterDemoMode(storage){
  storage?.setItem('bb-premium-mode',APP_MODES.DEMO);
  return APP_MODES.DEMO;
}
export function exitDemoMode(storage,demoKey='bb-premium-study-demo'){
  storage?.removeItem(demoKey);storage?.setItem('bb-premium-mode',APP_MODES.REAL);
  return APP_MODES.REAL;
}
export function resetDemoMode(storage,demoKey='bb-premium-study-demo'){
  storage?.removeItem(demoKey);storage?.setItem('bb-premium-mode',APP_MODES.DEMO);
  return APP_MODES.DEMO;
}
```
