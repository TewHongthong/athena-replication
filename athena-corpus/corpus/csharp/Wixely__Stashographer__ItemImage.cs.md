# src/Stashographer/Data/Entities/ItemImage.cs

- source repo: Wixely/Stashographer
- repo url: https://github.com/Wixely/Stashographer
- license: MIT
- created_at: 2026-08-18T03:19:36Z
- file path: src/Stashographer/Data/Entities/ItemImage.cs
- commit: e6568f9ca670f00ead30fe18c88491466eba11d1

```csharp
namespace Stashographer.Data.Entities;

/// <summary>How an image contributes to an item's catalogue record.</summary>
public enum ItemImageRole
{
    Front,
    Back,
    Detail,
    Label,
    Receipt,
    Other
}

/// <summary>
/// An ordered item/image association. The same image may belong to several items, while an
/// item can have front, back, detail, receipt, and other views without affecting quantity.
/// </summary>
public sealed class ItemImage
{
    public int ItemId { get; set; }
    public int ImageId { get; set; }
    public ItemImageRole Role { get; set; }
    public bool IsPrimary { get; set; }
    public int SortOrder { get; set; }
    public DateTimeOffset CreatedAt { get; set; }
    public Image Image { get; set; } = new();
}

public enum ImageDerivationKind
{
    Crop
}

/// <summary>Provenance for a generated image, including its retained source region.</summary>
public sealed record ImageDerivation(
    int ParentImageId,
    int ChildImageId,
    ImageDerivationKind Kind,
    decimal? CropX,
    decimal? CropY,
    decimal? CropWidth,
    decimal? CropHeight,
    DateTimeOffset CreatedAt);
```
