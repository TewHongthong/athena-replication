# Assets/Scripts/Field/HubCounter.cs

- source repo: thecheetoman/ESim
- repo url: https://github.com/thecheetoman/ESim
- license: MIT
- created_at: 2026-09-16T23:28:41Z
- file path: Assets/Scripts/Field/HubCounter.cs
- commit: 59cde034d0041d0af0a43cdf7e43d979935b7db8

```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HubCounter : MonoBehaviour
{
    public HubSystem hub;

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("GamePiece"))
        {
            bool wasLegal = false;
            if (other.TryGetComponent<ShotData>(out ShotData shotData))
            {
                wasLegal = shotData.wasShotFromLegalZone;
            }

            if (hub != null)
            {
                hub.countFuel(wasLegal);
            }
        }
    }
}```
