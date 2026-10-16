# src/Stashographer/Data/Entities/CheckoutRecord.cs

- source repo: Wixely/Stashographer
- repo url: https://github.com/Wixely/Stashographer
- license: MIT
- created_at: 2026-08-18T03:19:36Z
- file path: src/Stashographer/Data/Entities/CheckoutRecord.cs
- commit: e6568f9ca670f00ead30fe18c88491466eba11d1

```csharp
namespace Stashographer.Data.Entities;

/// <summary>
/// A lending / whereabouts record. An open record (<see cref="ReturnedAt"/> is null) means
/// the item is currently out; closing it returns the item. History is retained.
/// </summary>
public class CheckoutRecord
{
    public int Id { get; set; }

    public int ItemId { get; set; }

    /// <summary>Item name, populated by the data layer for list views.</summary>
    public string? ItemName { get; set; }

    /// <summary>Who has it (a person's name).</summary>
    public string CheckedOutBy { get; set; } = string.Empty;

    /// <summary>Where it went / any note about its whereabouts.</summary>
    public string? WhereaboutsNote { get; set; }

    public DateTimeOffset CheckedOutAt { get; set; }

    public DateOnly? DueDate { get; set; }

    public DateTimeOffset? ReturnedAt { get; set; }

    public string? Notes { get; set; }
}
```
