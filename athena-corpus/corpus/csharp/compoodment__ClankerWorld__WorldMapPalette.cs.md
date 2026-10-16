# src/ClankerWorld.GodotClient/UI/WorldMapPalette.cs

- source repo: compoodment/ClankerWorld
- repo url: https://github.com/compoodment/ClankerWorld
- license: MIT
- created_at: 2026-09-18T08:13:45Z
- file path: src/ClankerWorld.GodotClient/UI/WorldMapPalette.cs
- commit: 58d48ddaa57f24bceedae8ac01aff6e7f396920f

```csharp
using Godot;

namespace ClankerWorld.GodotClient.UI;

internal static class WorldMapPalette
{
    public static Color TerrainColor(string terrain) => terrain switch
    {
        "meadow" => new Color("5F8F5B"),
        "water" => new Color("4B7FA7"),
        "mountain" => new Color("756D68"),
        _ => new Color("9B5463"),
    };
}
```
