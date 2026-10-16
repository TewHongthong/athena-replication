# src/ClankerWorld.Viewer/Observation/OwnerWorldRuntimeService.cs

- source repo: compoodment/ClankerWorld
- repo url: https://github.com/compoodment/ClankerWorld
- license: MIT
- created_at: 2026-09-18T08:13:45Z
- file path: src/ClankerWorld.Viewer/Observation/OwnerWorldRuntimeService.cs
- commit: 58d48ddaa57f24bceedae8ac01aff6e7f396920f

```csharp
using ClankerWorld.Simulation.Harness;
using ClankerWorld.Simulation.Kernel;

namespace ClankerWorld.Viewer.Observation;

/// <summary>
/// Drives the cognition-aware fixture only while the host explicitly opts in.
/// Pause state lives in <see cref="OwnerWorldRuntime"/> so the scheduler
/// never creates hidden catch-up mutations.
/// </summary>
public sealed class OwnerWorldRuntimeService(
    OwnerWorldRuntime runtime,
    OwnerWorldStateFile stateFile) : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        using var timer = new PeriodicTimer(
            TimeSpan.FromSeconds(1d / KernelClock.ScheduledTicksPerSecond));

        while (await timer.WaitForNextTickAsync(stoppingToken))
        {
            var result = await runtime.AdvanceOneActionAsync(stoppingToken);
            if (result.Advanced)
            {
                stateFile.Save(runtime);
            }
        }
    }
}
```
