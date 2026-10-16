# Assets/Scripts/Field/TurretStatus.cs

- source repo: thecheetoman/ESim
- repo url: https://github.com/thecheetoman/ESim
- license: MIT
- created_at: 2026-09-16T23:28:41Z
- file path: Assets/Scripts/Field/TurretStatus.cs
- commit: 59cde034d0041d0af0a43cdf7e43d979935b7db8

```csharp
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class TurretStatus : MonoBehaviour
{
    public TextMeshProUGUI turretStatusText;
    public Turret Rturret;

    // Start is called before the first frame update 
    void Start()
    {
    }

    // Update is called once per frame 
    void Update()
    {
        if (Rturret.mode == Turret.TurretMode.Manual)
        {
            turretStatusText.text = "manual aim";
        }
        else
        {
            turretStatusText.text = "auto aim\n(hub)";
        }
    }
}
```
