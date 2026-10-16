# src/application/create-app-context.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/create-app-context.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
const REQUIRED_STORAGE_METHODS=['get','set','remove'];

export function createAppContext({storage,repositories={},clock,idGenerator}={}){
  if(!storage||REQUIRED_STORAGE_METHODS.some(method=>typeof storage[method]!=='function')) throw new TypeError('O contexto requer um provider de armazenamento válido.');
  if(!clock||typeof clock.today!=='function'||typeof clock.nowISO!=='function') throw new TypeError('O contexto requer um relógio válido.');
  if(typeof idGenerator!=='function') throw new TypeError('O contexto requer um gerador de IDs.');
  return Object.freeze({storage,repositories:Object.freeze({...repositories}),clock,idGenerator});
}
```
