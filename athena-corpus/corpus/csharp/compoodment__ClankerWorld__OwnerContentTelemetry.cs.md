# src/ClankerWorld.Viewer/Control/OwnerContentTelemetry.cs

- source repo: compoodment/ClankerWorld
- repo url: https://github.com/compoodment/ClankerWorld
- license: MIT
- created_at: 2026-09-18T08:13:45Z
- file path: src/ClankerWorld.Viewer/Control/OwnerContentTelemetry.cs
- commit: 58d48ddaa57f24bceedae8ac01aff6e7f396920f

```csharp
namespace ClankerWorld.Viewer.Control;

public static partial class OwnerContentTelemetry
{
    [LoggerMessage(EventId = 2213, Level = LogLevel.Information,
        Message = "content_rollback tick={WorldTick} package={PackageId} outcome={Outcome}")]
    public static partial void Rollback(ILogger logger, long worldTick, string packageId, string outcome);
}
```
