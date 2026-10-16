# src/application/planning/daily-plan-service.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/planning/daily-plan-service.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
export function createDailyPlanService({repository,buildProposal,applyProposal,undoGeneration,clock,idGenerator}={}){
  if(!repository||typeof repository.getDailyPlans!=='function')throw new TypeError('Serviço diário requer repositório.');
  return Object.freeze({calculate:input=>buildProposal({...input,existingPlans:repository.getDailyPlans()}),confirm:(proposal,studyPlan)=>{const operationId=idGenerator('daily-plan-operation'),createdAt=clock.nowISO(),result=applyProposal({dailyPlans:repository.getDailyPlans(),proposal,operationId,now:createdAt,idGenerator});studyPlan.dailyPlanOperations=Array.isArray(studyPlan.dailyPlanOperations)?studyPlan.dailyPlanOperations:[];studyPlan.dailyPlanOperations.push({id:operationId,createdAt,createdItems:result.createdItems,undoneAt:null});return result},undo:(operation,studyPlan)=>{const result=undoGeneration({dailyPlans:repository.getDailyPlans(),operationId:operation.id});operation.undoneAt=result.complete?clock.nowISO():null;operation.protectedItems=result.protectedItems;repository.saveStudyPlan(studyPlan);return result}});
}
```
