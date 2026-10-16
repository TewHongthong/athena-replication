# src/application/exam-intelligence/build-exam-intelligence.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/exam-intelligence/build-exam-intelligence.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
import {calculateTopicIncidence} from '../../domain/exam-intelligence/topic-incidence.js';

export function buildExamIntelligence({topics=[],exams=[],examQuestions=[],activeExamTags=[]}={}){
  return topics.map(topic=>calculateTopicIncidence({topicId:topic.id,exams,questions:examQuestions,activeExamTags}));
}
```
