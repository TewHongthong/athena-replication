# src/Stashographer/Data/Entities/ItemKind.cs

- source repo: Wixely/Stashographer
- repo url: https://github.com/Wixely/Stashographer
- license: MIT
- created_at: 2026-08-18T03:19:36Z
- file path: src/Stashographer/Data/Entities/ItemKind.cs
- commit: e6568f9ca670f00ead30fe18c88491466eba11d1

```csharp
namespace Stashographer.Data.Entities;

/// <summary>
/// A configurable category of thing (Grocery, Book, Tool, Electronics, …). Kinds are
/// user-extensible and carry a suggested set of attribute field names so the item editor
/// can prompt for the metadata that matters for that kind.
/// </summary>
public class ItemKind
{
    public int Id { get; set; }

    public required string Name { get; set; }

    /// <summary>Icon key resolved via <c>IconCatalog</c> (e.g. "Kitchen", "MenuBook").</summary>
    public string? Icon { get; set; }

    /// <summary>
    /// Suggested custom-attribute field names for this kind (e.g. Book → Author, Publisher).
    /// Stored as a JSON array. Purely advisory — items may carry any attributes.
    /// </summary>
    public List<string> SuggestedAttributes { get; set; } = new();

    /// <summary>Built-in kinds are seeded and cannot be deleted from the UI.</summary>
    public bool IsSystem { get; set; }
}
```
