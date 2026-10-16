# src/application/exam-intelligence/build-topic-exam-profile.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/exam-intelligence/build-topic-exam-profile.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
import {calculateTopicIncidence} from '../../domain/exam-intelligence/topic-incidence.js';
import {buildTopicImpact} from '../../domain/exam-intelligence/topic-impact.js';

export function buildTopicExamProfile({topic,subjectConfig=null,activeExamTags=[],exams=[],examQuestions=[]}={}){
  const incidence=calculateTopicIncidence({topicId:topic?.id,exams,questions:examQuestions,activeExamTags});
  return buildTopicImpact({topic,subjectConfig,activeExamTags,incidence,exams,examQuestions});
}
```
