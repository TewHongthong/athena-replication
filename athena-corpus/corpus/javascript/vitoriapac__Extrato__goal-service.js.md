# src/application/goals/goal-service.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/goals/goal-service.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
const clamp=(value,min=0,max=Infinity)=>Math.max(min,Math.min(max,Number(value)||0));

export function createGoalService({repository,getDayOfWeek}={}){
  if(!repository||typeof repository.getGoals!=='function')throw new TypeError('Serviço de metas requer repositório.');
  return Object.freeze({
    hoursForDay:day=>clamp(repository.getGoals()?.horasPorDia?.[String(day)]??repository.getGoals()?.horasDiarias,0,24),
    hoursForDate:date=>clamp(repository.getGoals()?.horasPorDia?.[String(getDayOfWeek(date))]??repository.getGoals()?.horasDiarias,0,24),
    updateDailyHours:(day,value,{isToday=false}={})=>{const hours=clamp(value,0,24);repository.updateDailyHours(day,hours);if(isToday)repository.updateGoal('horasDiarias',hours);return hours},
    applyHoursToEveryDay:value=>{const hours=clamp(value,0,24);for(let day=0;day<7;day++)repository.updateDailyHours(day,hours);repository.updateGoal('horasDiarias',hours);return hours},
    clearWeekend:()=>{repository.updateDailyHours(0,0);repository.updateDailyHours(6,0)},
    update:(key,value)=>repository.updateGoal(key,key==='metaAprovacao'?clamp(value,0,100):clamp(value))
  });
}
```
