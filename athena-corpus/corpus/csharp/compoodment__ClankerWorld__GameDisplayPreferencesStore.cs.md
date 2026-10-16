# src/ClankerWorld.GodotClient/ClientState/GameDisplayPreferencesStore.cs

- source repo: compoodment/ClankerWorld
- repo url: https://github.com/compoodment/ClankerWorld
- license: MIT
- created_at: 2026-09-18T08:13:45Z
- file path: src/ClankerWorld.GodotClient/ClientState/GameDisplayPreferencesStore.cs
- commit: 58d48ddaa57f24bceedae8ac01aff6e7f396920f

```csharp
using System.Text.Json;

namespace ClankerWorld.GodotClient.ClientState;

/// <summary>
/// Installation-local display choices. These do not alter world time or save data.
/// </summary>
public sealed record GameDisplayPreferences(
    bool UseTwelveHourClock = false,
    string DateFormat = "dmy",
    int WindowWidth = 1280,
    int WindowHeight = 720,
    int RenderWidth = 1280,
    int RenderHeight = 720);

public sealed class GameDisplayPreferencesStore(string path)
{
    private readonly string path = Path.GetFullPath(path);

    public GameDisplayPreferences Load()
    {
        try
        {
            return File.Exists(path)
                ? JsonSerializer.Deserialize<GameDisplayPreferences>(File.ReadAllText(path)) ?? new()
                : new();
        }
        catch (Exception exception) when (exception is IOException or UnauthorizedAccessException or JsonException)
        {
            return new();
        }
    }

    public void Save(GameDisplayPreferences preferences)
    {
        ArgumentNullException.ThrowIfNull(preferences);
        var directory = Path.GetDirectoryName(path) ??
            throw new InvalidOperationException("The game settings path has no directory.");
        Directory.CreateDirectory(directory);
        var temporary = path + "." + Guid.NewGuid().ToString("N") + ".tmp";
        try
        {
            File.WriteAllText(temporary, JsonSerializer.Serialize(preferences));
            File.Move(temporary, path, overwrite: true);
        }
        finally
        {
            if (File.Exists(temporary)) File.Delete(temporary);
        }
    }
}
```
