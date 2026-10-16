# src/ClankerWorld.Simulation/SimulationAssemblyMarker.cs

- source repo: compoodment/ClankerWorld
- repo url: https://github.com/compoodment/ClankerWorld
- license: MIT
- created_at: 2026-09-18T08:13:45Z
- file path: src/ClankerWorld.Simulation/SimulationAssemblyMarker.cs
- commit: 58d48ddaa57f24bceedae8ac01aff6e7f396920f

```csharp
namespace ClankerWorld.Simulation;

/// <summary>
/// Marks the pure authoritative simulation assembly.
/// </summary>
/// <remarks>
/// This is intentionally not world behavior. It gives the foundation test a
/// stable assembly boundary to protect while actual kernel contracts arrive.
/// </remarks>
public sealed class SimulationAssemblyMarker;
```
