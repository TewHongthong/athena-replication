# src/application/planning/build-today-view-model.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/planning/build-today-view-model.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
export function buildTodayViewModel({date,availableMinutes=0,plan=null,priorities=[],pastPlans=[]}={}){
  const minutes=value=>Math.max(0,Math.round(Number(value)||0));
  const items=plan?.items||[];
  const plannedMinutes=items.filter(item=>!['skipped','replaced','deferred'].includes(item.status)).reduce((sum,item)=>sum+minutes(item.plannedMinutes),0);
  const executedMinutes=Math.round(items.reduce((sum,item)=>sum+Math.max(0,Number(item.executedSeconds)||0)/60,0));
  const recoveryMinutes=pastPlans.filter(row=>row.date<date).flatMap(row=>row.items||[]).filter(item=>!['completed','skipped','replaced','deferred'].includes(item.status)).reduce((sum,item)=>sum+Math.max(0,minutes(item.plannedMinutes)-Math.round((Number(item.executedSeconds)||0)/60)),0);
  return {date,availableMinutes:minutes(availableMinutes),plannedMinutes,executedMinutes,recoveryMinutes,progress:plannedMinutes?Math.min(100,Math.round(executedMinutes/plannedMinutes*100)):null,
    nextActivity:items.find(item=>!['completed','skipped','replaced','deferred'].includes(item.status))||priorities[0]||null};
}
```
