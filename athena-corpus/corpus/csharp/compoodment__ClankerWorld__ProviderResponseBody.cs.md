# src/ClankerWorld.Simulation/Cognition/ProviderResponseBody.cs

- source repo: compoodment/ClankerWorld
- repo url: https://github.com/compoodment/ClankerWorld
- license: MIT
- created_at: 2026-09-18T08:13:45Z
- file path: src/ClankerWorld.Simulation/Cognition/ProviderResponseBody.cs
- commit: 58d48ddaa57f24bceedae8ac01aff6e7f396920f

```csharp
using System.Text;

namespace ClankerWorld.Simulation.Cognition;

/// <summary>Caps remote response bytes before JSON parsing or full buffering.</summary>
public static class ProviderResponseBody
{
    public const int MaximumBytes = 256 * 1024;

    public static async Task<string> ReadAsync(HttpContent content, CancellationToken cancellationToken = default)
    {
        ArgumentNullException.ThrowIfNull(content);
        cancellationToken.ThrowIfCancellationRequested();
        if (content.Headers.ContentLength > MaximumBytes)
        {
            throw new InvalidDataException("The provider response exceeds the byte limit.");
        }

        using var source = await content.ReadAsStreamAsync(cancellationToken).ConfigureAwait(false);
        using var body = new MemoryStream();
        var buffer = new byte[8192];
        while (true)
        {
            var count = await source.ReadAsync(buffer.AsMemory(0, Math.Min(buffer.Length, MaximumBytes + 1 - checked((int)body.Length))), cancellationToken).ConfigureAwait(false);
            if (count == 0)
            {
                return Encoding.UTF8.GetString(body.GetBuffer(), 0, checked((int)body.Length));
            }
            if (body.Length + count > MaximumBytes)
            {
                throw new InvalidDataException("The provider response exceeds the byte limit.");
            }
            body.Write(buffer, 0, count);
        }
    }
}
```
