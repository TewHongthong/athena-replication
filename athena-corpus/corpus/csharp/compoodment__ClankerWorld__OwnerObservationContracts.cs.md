# src/ClankerWorld.Viewer/Observation/OwnerObservationContracts.cs

- source repo: compoodment/ClankerWorld
- repo url: https://github.com/compoodment/ClankerWorld
- license: MIT
- created_at: 2026-09-18T08:13:45Z
- file path: src/ClankerWorld.Viewer/Observation/OwnerObservationContracts.cs
- commit: 58d48ddaa57f24bceedae8ac01aff6e7f396920f

```csharp
namespace ClankerWorld.Viewer.Observation;

/// <summary>
/// Authenticated reconnect response. The full capability handshake is coupled
/// to the signed observation so a public discovery handshake cannot be
/// mistaken for authority to inspect the world.
/// </summary>
public sealed record ViewerOwnerReconnect(ViewerHandshake Handshake, ViewerReconnectBaseline Baseline);
```
