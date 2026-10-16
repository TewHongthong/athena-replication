# src/application/calendar/build-unified-reviews.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/calendar/build-unified-reviews.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
export function buildUnifiedReviews({calendar=[],reviewAgenda=[],subjectIdOf=()=>null,subjectName=()=>'',topicName=()=>''}={}){
  const calendarItems=calendar.map(item=>({
    id:item.id,date:item.date,subjectId:subjectIdOf(item),subject:subjectName(item),
    label:item.reviewType&&item.reviewType!=='—'?item.reviewType:'Revisão',
    status:item.status||'Não iniciado',origem:'Calendário'
  }));
  const agendaItems=reviewAgenda.map(item=>({
    id:item.id,date:item.date,subjectId:subjectIdOf(item),subject:subjectName(item),
    label:`${item.topicId?topicName(item.topicId):(item.topic||'Tópico')} · ${item.tipo||''}`,
    status:item.status||'Não iniciado',origem:'Agenda de Revisões'
  }));
  return [...calendarItems,...agendaItems];
}

export function unifiedReviewLabel(item){
  const subject=String(item?.subject||'').trim(),label=String(item?.label||'').trim();
  if(!subject||!label)return label||'Revisão';
  const escaped=subject.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  return label.replace(new RegExp(`^${escaped}\\s*[·•—-]\\s*`,'i'),'').trim()||'Revisão';
}
```
