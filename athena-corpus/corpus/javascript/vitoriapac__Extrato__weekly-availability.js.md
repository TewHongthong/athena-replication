# src/application/goals/weekly-availability.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/goals/weekly-availability.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
const clampHours=value=>Math.max(0,Math.min(24,Number(value)||0));

export function buildWeeklyAvailability(hoursByDay={}){
  const days=Array.from({length:7},(_,day)=>({day,hours:clampHours(hoursByDay[String(day)]??hoursByDay[day])}));
  const totalHours=Math.round(days.reduce((sum,item)=>sum+item.hours,0)*100)/100;
  const activeDays=days.filter(item=>item.hours>0).length;
  const averageHours=activeDays?Math.round(totalHours/activeDays*100)/100:0;
  const peakHours=Math.max(0,...days.map(item=>item.hours));
  return {days,totalHours,totalMinutes:Math.round(totalHours*60),activeDays,averageHours,peakHours,state:totalHours?'configured':'empty'};
}

```
