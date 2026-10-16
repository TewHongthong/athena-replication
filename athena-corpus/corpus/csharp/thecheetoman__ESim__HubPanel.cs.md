# Assets/Scripts/Field/HubPanel.cs

- source repo: thecheetoman/ESim
- repo url: https://github.com/thecheetoman/ESim
- license: MIT
- created_at: 2026-09-16T23:28:41Z
- file path: Assets/Scripts/Field/HubPanel.cs
- commit: 59cde034d0041d0af0a43cdf7e43d979935b7db8

```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// relay script cuz fuck you unity
public class HubPanel : MonoBehaviour
{
    public HubSystem hub;

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("GamePiece"))
        {
            hub.playSFX(collision);
        }
    }
}
```
