# src/application/planning/replan-service.js

- source repo: vitoriapac/Extrato
- repo url: https://github.com/vitoriapac/Extrato
- license: MIT
- created_at: 2026-08-31T09:50:12Z
- file path: src/application/planning/replan-service.js
- commit: b27c700b6b12123dd68e38a3fab2812776cd6db3

```javascript
export function createReplanService({repository,buildProposal,applyProposal,undoProposal,clock,idGenerator}={}){
  if(!repository||typeof repository.saveAdjustment!=='function')throw new TypeError('Serviço de replanejamento requer repositório.');
  return Object.freeze({
    calculate:input=>buildProposal({...input,plans:input.plans||repository.getDailyPlans()}),
    confirm:proposal=>{
      if(proposal?.state!=='proposal'||!proposal.allocations?.length)return null;
      const operationId=idGenerator('replan-operation'),appliedAt=clock.nowISO();
      const result=applyProposal({dailyPlans:repository.getDailyPlans(),proposal,operationId,now:appliedAt,idGenerator});
      const adjustment={...structuredClone(proposal),id:idGenerator('plan-adjustment'),operationId,confirmedAt:appliedAt,appliedAt,status:'applied',changes:result.changes,undoneAt:null};
      repository.saveAdjustment(adjustment);return {result,adjustment};
    },
    undo:id=>{
      const adjustment=repository.findAdjustment(id);if(!adjustment||adjustment.undoneAt)return null;
      const result=undoProposal({dailyPlans:repository.getDailyPlans(),adjustment});
      repository.saveAdjustment({...adjustment,status:result.complete?'undone':'partially_undone',undoneAt:result.complete?clock.nowISO():null,protectedItems:result.protectedItems});
      return result;
    }
  });
}
```
