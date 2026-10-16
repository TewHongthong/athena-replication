# src/ClankerWorld.Viewer/Observation/LiveWorldRuntimeService.cs

- source repo: compoodment/ClankerWorld
- repo url: https://github.com/compoodment/ClankerWorld
- license: MIT
- created_at: 2026-09-18T08:13:45Z
- file path: src/ClankerWorld.Viewer/Observation/LiveWorldRuntimeService.cs
- commit: 58d48ddaa57f24bceedae8ac01aff6e7f396920f

```csharp
using ClankerWorld.Simulation.Harness;
using ClankerWorld.Simulation.Kernel;

namespace ClankerWorld.Viewer.Observation;

/// <summary>
/// Runs the small live-fixture clock only when the host explicitly enables it.
/// Test hosts remain clock-independent and exercise the same runtime manually.
/// </summary>
public sealed class LiveWorldRuntimeService(LiveSeededWorldRuntime runtime) : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        using var timer = new PeriodicTimer(
            TimeSpan.FromSeconds(1d / KernelClock.ScheduledTicksPerSecond));

        while (await timer.WaitForNextTickAsync(stoppingToken))
        {
            runtime.TryAdvanceOneAction();
        }
    }
}
```
