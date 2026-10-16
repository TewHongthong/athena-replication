# src/ClankerWorld.Viewer/Control/ProviderUsageTelemetry.cs

- source repo: compoodment/ClankerWorld
- repo url: https://github.com/compoodment/ClankerWorld
- license: MIT
- created_at: 2026-09-18T08:13:45Z
- file path: src/ClankerWorld.Viewer/Control/ProviderUsageTelemetry.cs
- commit: 58d48ddaa57f24bceedae8ac01aff6e7f396920f

```csharp
namespace ClankerWorld.Viewer.Control;

public static partial class ProviderUsageTelemetry
{
    [LoggerMessage(EventId = 2281, Level = LogLevel.Warning,
        Message = "provider_usage_limit_reached outcome=paused scope=installation tick={WorldTick}")]
    public static partial void LimitReached(ILogger logger, long worldTick);

    [LoggerMessage(EventId = 2282, Level = LogLevel.Information,
        Message = "provider_usage_limit_configured outcome=accepted enabled={Enabled} limit={AttemptLimit} attempts={Attempts}")]
    public static partial void LimitConfigured(ILogger logger, bool enabled, long? attemptLimit, long attempts);
}
```
