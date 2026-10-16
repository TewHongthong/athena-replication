# src/Stashographer/Components/Pages/QueueTabSelection.cs

- source repo: Wixely/Stashographer
- repo url: https://github.com/Wixely/Stashographer
- license: MIT
- created_at: 2026-08-18T03:19:36Z
- file path: src/Stashographer/Components/Pages/QueueTabSelection.cs
- commit: e6568f9ca670f00ead30fe18c88491466eba11d1

```csharp
namespace Stashographer.Components.Pages;

internal static class QueueTabSelection
{
    public static int InitialIndex(string? requestedTab, int intakeOpen, int modifyOpen)
    {
        if (string.Equals(requestedTab, "history", StringComparison.OrdinalIgnoreCase)) return 2;
        return string.Equals(requestedTab, "modify", StringComparison.OrdinalIgnoreCase)
               || (!string.Equals(requestedTab, "intake", StringComparison.OrdinalIgnoreCase)
                   && intakeOpen == 0 && modifyOpen > 0)
            ? 1
            : 0;
    }
}
```
