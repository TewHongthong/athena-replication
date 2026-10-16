# src/IBinaryUnpackable.cs

- source repo: TrentBest/TheSingularityWorkshop.FSM_Serialization
- repo url: https://github.com/TrentBest/TheSingularityWorkshop.FSM_Serialization
- license: MIT
- created_at: 2026-09-26T23:07:23Z
- file path: src/IBinaryUnpackable.cs
- commit: b6ba826742ca6f4507323a478deeaa0b5d915aa9

```csharp
namespace TheSingularityWorkshop.FSM_Serialization;

/// <summary>
/// Defines a type that can reconstruct its state from an <see cref="IBinaryStream"/>.
/// </summary>
public interface IBinaryUnpackable
{
    /// <summary>Reads the type's binary representation from the supplied stream.</summary>
    /// <param name="stream">The source binary stream.</param>
    void Unpack(IBinaryStream stream);
}
```
