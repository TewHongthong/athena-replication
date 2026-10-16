# src/ClankerWorld.Viewer/Control/OwnerCredentialSlotTelemetry.cs

- source repo: compoodment/ClankerWorld
- repo url: https://github.com/compoodment/ClankerWorld
- license: MIT
- created_at: 2026-09-18T08:13:45Z
- file path: src/ClankerWorld.Viewer/Control/OwnerCredentialSlotTelemetry.cs
- commit: 58d48ddaa57f24bceedae8ac01aff6e7f396920f

```csharp
namespace ClankerWorld.Viewer.Control;

public static partial class OwnerCredentialSlotTelemetry
{
    [LoggerMessage(EventId = 2264, Level = LogLevel.Information,
        Message = "provider_credential_slot_delete outcome={Outcome} slot_id={SlotId}")]
    public static partial void Deleted(ILogger logger, string outcome, string slotId);
}
```
