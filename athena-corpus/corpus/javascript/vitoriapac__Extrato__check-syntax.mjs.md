# scripts/check-syntax.mjs

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: scripts/check-syntax.mjs
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
import {readFileSync,readdirSync} from 'node:fs';
import {join,extname} from 'node:path';
import {transformSync} from 'esbuild';

const roots=['scripts','src','tests'];
const ignored=new Set(['node_modules','test-results','playwright-report']);
const files=[];
function collect(directory){
  for(const entry of readdirSync(directory,{withFileTypes:true})){
    if(ignored.has(entry.name))continue;
    const path=join(directory,entry.name);
    if(entry.isDirectory())collect(path);
    else if(['.js','.mjs'].includes(extname(entry.name))&&!entry.name.endsWith('.bundle.js'))files.push(path);
  }
}
roots.forEach(collect);
for(const file of files){
  try{transformSync(readFileSync(file,'utf8'),{loader:'js',sourcefile:file,logLevel:'silent'});}
  catch(error){console.error(error.message);process.exit(1);}
}
console.log(`Sintaxe válida em ${files.length} arquivos JavaScript.`);
```
