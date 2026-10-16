# src/Stashographer/ImageUrls.cs

- source repo: Wixely/Stashographer
- repo url: https://github.com/Wixely/Stashographer
- license: MIT
- created_at: 2026-08-18T03:19:36Z
- file path: src/Stashographer/ImageUrls.cs
- commit: e6568f9ca670f00ead30fe18c88491466eba11d1

```csharp
namespace Stashographer;

/// <summary>
/// Builds image <c>src</c> values consistently across the app: a stored image is served from
/// <c>/img/{id}</c> (optionally as a thumbnail via <c>?w=</c>), otherwise an optional remote
/// fallback URL (e.g. a lookup provider's cover) is used.
/// </summary>
public static class ImageUrls
{
    public static string? For(int? imageId, string? fallbackUrl = null, int? width = null)
    {
        if (imageId is { } id)
            return width is { } w ? $"/img/{id}?w={w}" : $"/img/{id}";
        return string.IsNullOrWhiteSpace(fallbackUrl) ? null : fallbackUrl;
    }

    public static bool Has(int? imageId, string? fallbackUrl = null) =>
        imageId is not null || !string.IsNullOrWhiteSpace(fallbackUrl);
}
```
