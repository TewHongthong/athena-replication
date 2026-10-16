# src/ClankerWorld.Viewer/Control/OwnerLifePaceTelemetry.cs

- source repo: compoodment/ClankerWorld
- repo url: https://github.com/compoodment/ClankerWorld
- license: MIT
- created_at: 2026-09-18T08:13:45Z
- file path: src/ClankerWorld.Viewer/Control/OwnerLifePaceTelemetry.cs
- commit: 58d48ddaa57f24bceedae8ac01aff6e7f396920f

```csharp
namespace ClankerWorld.Viewer.Control;

public static partial class OwnerLifePaceTelemetry
{
    [LoggerMessage(EventId = 2211, Level = LogLevel.Information,
        Message = "world_life_pace tick={WorldTick} rate={Rate}")]
    public static partial void Changed(ILogger logger, long worldTick, int rate);
}
```
