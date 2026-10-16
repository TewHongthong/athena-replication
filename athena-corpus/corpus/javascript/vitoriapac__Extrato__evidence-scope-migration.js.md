# src/application/exams/evidence-scope-migration.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/exams/evidence-scope-migration.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
import {normalizeExamTags} from '../../domain/exams/exam-scope.js';

const topicIdOf=record=>record?.topicId||record?.topicRef||null;

export function buildTopicScopeIndex(subjects=[]){
  const index=new Map();
  for(const subject of subjects||[])for(const topic of subject?.topics||[]){
    if(topic?.id)index.set(topic.id,normalizeExamTags(topic.examTags));
  }
  return index;
}

export function snapshotEvidenceScopes(data={}){
  const topicScopes=buildTopicScopeIndex(data.subjects);
  const collections=['studySessions','questoes','reviewAgenda','calendar','topicHistory'];
  for(const field of collections)for(const record of data[field]||[]){
    if(Array.isArray(record.examScope))record.examScope=normalizeExamTags(record.examScope);
    else {
      const topicId=topicIdOf(record);
      record.examScope=topicId&&topicScopes.has(topicId)?topicScopes.get(topicId):null;
    }
  }
  for(const simulation of data.simulados||[]){
    if(Array.isArray(simulation.examScope))simulation.examScope=normalizeExamTags(simulation.examScope);
    else simulation.examScope=normalizeExamTags(Array.isArray(simulation.examTags)?simulation.examTags:simulation.examTag?[simulation.examTag]:[]);
  }
  return data;
}
```
