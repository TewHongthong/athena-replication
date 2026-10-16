# Assets/Scripts/Robot/RigidbodyClothDeformer.cs

- source repo: thecheetoman/ESim
- repo url: https://github.com/thecheetoman/ESim
- license: MIT
- created_at: 2026-09-16T23:28:41Z
- file path: Assets/Scripts/Robot/RigidbodyClothDeformer.cs
- commit: 59cde034d0041d0af0a43cdf7e43d979935b7db8

```csharp
using UnityEngine;
using System.Collections.Generic;

[RequireComponent(typeof(Cloth))]
[RequireComponent(typeof(BoxCollider))] // Enforces the trigger box setup
public class RigidbodyClothDeformer : MonoBehaviour
{
    [Header("Detection Settings")]
    [Tooltip("Layer assigned to your yellow balls to keep entries optimized")]
    public LayerMask ballLayer;

    [Header("Diagnostics")]
    [Tooltip("Logs current counts whenever a ball enters or leaves the zone")]
    public bool logStateChanges = true;

    private const int MaxColliders = 32;

    private Cloth clothComponent;

    // Using Lists as reliable internal trackers
    private readonly List<SphereCollider> activeSpheres = new List<SphereCollider>();
    private readonly List<CapsuleCollider> activeCapsules = new List<CapsuleCollider>();

    // Cached arrays passed directly to Unity's cloth pipeline
    private ClothSphereColliderPair[] spherePairsArray = new ClothSphereColliderPair[0];
    private CapsuleCollider[] capsuleArray = new CapsuleCollider[0];

    void Start()
    {
        clothComponent = GetComponent<Cloth>();

        // Ensure the attached Box Collider is explicitly a trigger zone
        BoxCollider box = GetComponent<BoxCollider>();
        if (box != null)
        {
            box.isTrigger = true;
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        // Explicit layer validation bitmask check
        if (((1 << other.gameObject.layer) & ballLayer) == 0) return;

        bool structuresChanged = false;

        switch (other)
        {
            case SphereCollider sphere:
                if (!activeSpheres.Contains(sphere) && activeSpheres.Count < MaxColliders)
                {
                    activeSpheres.Add(sphere);
                    structuresChanged = true;
                }
                break;

            case CapsuleCollider capsule:
                if (!activeCapsules.Contains(capsule) && activeCapsules.Count < MaxColliders)
                {
                    activeCapsules.Add(capsule);
                    structuresChanged = true;
                }
                break;
        }

        if (structuresChanged)
        {
            RebuildClothArrays();
        }
    }

    private void OnTriggerExit(Collider other)
    {
        // Explicit layer validation bitmask check
        if (((1 << other.gameObject.layer) & ballLayer) == 0) return;

        bool structuresChanged = false;

        switch (other)
        {
            case SphereCollider sphere:
                if (activeSpheres.Remove(sphere))
                {
                    structuresChanged = true;
                }
                break;

            case CapsuleCollider capsule:
                if (activeCapsules.Remove(capsule))
                {
                    structuresChanged = true;
                }
                break;
        }

        if (structuresChanged)
        {
            RebuildClothArrays();
        }
    }

    private void RebuildClothArrays()
    {
        if (clothComponent == null) return;

        // 1. Rebuild and bind Sphere array structures
        spherePairsArray = new ClothSphereColliderPair[activeSpheres.Count];
        for (int i = 0; i < activeSpheres.Count; i++)
        {
            // Instantiates pairs with the second slot cleanly flagged as null
            spherePairsArray[i] = new ClothSphereColliderPair(activeSpheres[i]);
        }
        clothComponent.sphereColliders = spherePairsArray;

        // 2. Rebuild and bind Capsule arrays
        capsuleArray = activeCapsules.ToArray();
        clothComponent.capsuleColliders = capsuleArray;

        if (logStateChanges)
        {
            Debug.Log($"[ClothTriggerDeformer] Arrays Synchronized. Tracked Spheres: {activeSpheres.Count} | Tracked Capsules: {activeCapsules.Count}", this);
        }
    }

    // Optional Clean-up: If an object is destroyed while inside the trigger zone
    private void Update()
    {
        bool cleanupRequired = false;

        for (int i = activeSpheres.Count - 1; i >= 0; i--)
        {
            if (activeSpheres[i] == null)
            {
                activeSpheres.RemoveAt(i);
                cleanupRequired = true;
            }
        }

        for (int i = activeCapsules.Count - 1; i >= 0; i--)
        {
            if (activeCapsules[i] == null)
            {
                activeCapsules.RemoveAt(i);
                cleanupRequired = true;
            }
        }

        if (cleanupRequired)
        {
            RebuildClothArrays();
        }
    }

    void OnDrawGizmos()
    {
        if (!Application.isPlaying) return;

        // Render targets currently reacting to physics
        Gizmos.color = Color.red;
        for (int i = 0; i < activeSpheres.Count; i++)
        {
            if (activeSpheres[i] == null) continue;
            Transform t = activeSpheres[i].transform;
            Gizmos.DrawWireSphere(t.position, activeSpheres[i].radius * Mathf.Max(t.lossyScale.x, t.lossyScale.y, t.lossyScale.z));
        }
    }
}
```
