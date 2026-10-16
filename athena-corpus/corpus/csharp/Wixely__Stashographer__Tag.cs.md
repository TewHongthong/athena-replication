# src/Stashographer/Data/Entities/Tag.cs

- source repo: Wixely/Stashographer
- repo url: https://github.com/Wixely/Stashographer
- license: MIT
- created_at: 2026-08-18T03:19:36Z
- file path: src/Stashographer/Data/Entities/Tag.cs
- commit: e6568f9ca670f00ead30fe18c88491466eba11d1

```csharp
namespace Stashographer.Data.Entities;

/// <summary>A reusable, case-insensitively unique label assigned to inventory items.</summary>
public sealed class Tag
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public int ItemCount { get; set; }
    public DateTimeOffset CreatedAt { get; set; }
    public DateTimeOffset UpdatedAt { get; set; }
}
```
