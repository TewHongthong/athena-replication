# src/application/analytics/weekly-close-snapshot.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/analytics/weekly-close-snapshot.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
export const WEEKLY_CLOSE_SNAPSHOT_VERSION=1;
export function createWeeklyCloseSnapshot(model,{savedAt,id}={}){if(!model?.period||model.weeklyClose?.state==='insufficient')return null;return{id,period:{...model.period},activeExamTags:Array.isArray(model.activeExamTags)?[...model.activeExamTags]:null,savedAt,version:WEEKLY_CLOSE_SNAPSHOT_VERSION,algorithmVersion:model.weeklyClose.algorithmVersion,weeklyClose:structuredClone(model.weeklyClose),gapMap:structuredClone(model.gapMap),decisionHistory:structuredClone(model.decisionHistory)}}
export function upsertWeeklyCloseSnapshot(list,snapshot){if(!snapshot)return false;const scope=tags=>Array.isArray(tags)?JSON.stringify([...new Set(tags)].sort()):null;const index=list.findIndex(item=>item.period?.start===snapshot.period.start&&item.period?.end===snapshot.period.end&&scope(item.activeExamTags)===scope(snapshot.activeExamTags));if(index>=0)list[index]=snapshot;else list.push(snapshot);return true}
```
