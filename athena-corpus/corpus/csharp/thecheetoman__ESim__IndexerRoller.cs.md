# Assets/Scripts/Robot/IndexerRoller.cs

- source repo: thecheetoman/ESim
- repo url: https://github.com/thecheetoman/ESim
- license: MIT
- created_at: 2026-09-16T23:28:41Z
- file path: Assets/Scripts/Robot/IndexerRoller.cs
- commit: 59cde034d0041d0af0a43cdf7e43d979935b7db8

```csharp
using UnityEngine;
using Robot.InputHandling;

public class IndexerRoller : MonoBehaviour
{
    [Header("Indexer Settings")]
    [Tooltip("Local-space direction balls should move through this segment (e.g. Vector3.forward). Converted to world space.")]
    public Vector3 moveDirection = Vector3.forward;
    [Tooltip("Base travel speed in m/s along moveDirection, at multiplier = 1.")]
    public float surfaceSpeed = 4f;
    [Tooltip("How hard the ball's velocity is corrected toward the desired speed along moveDirection.")]
    public float correctionForce = 10f;

    private float shootingMult = 1f;
    private bool isEnabled = false;

    private void OnEnable()
    {
        GameManager.OnRobotStateChanged += OnRobotStateChanged;
        isEnabled = GameManager.IsRobotEnabled;
    }

    private void OnDisable()
    {
        GameManager.OnRobotStateChanged -= OnRobotStateChanged;
    }

    private void OnRobotStateChanged(bool enabled)
    {
        isEnabled = enabled;
        if (!isEnabled) shootingMult = 0f;
    }

    private void UpdateShootingMult()
    {
        if (Input.GetKey(KeyCode.U) || (PlayerInputHandler.Instance != null && PlayerInputHandler.Instance.reverseIndexer))
        {
            shootingMult = -7.5f;
        }
        else if (Input.GetKey(KeyCode.Space) || (PlayerInputHandler.Instance != null && PlayerInputHandler.Instance.Shoot))
        {
            shootingMult = 1.2f;
        }
        else
        {
            shootingMult = 1f;
        }
    }

    private void OnTriggerStay(Collider other)
    {
        if (!isEnabled) return;
        if (!other.CompareTag("GamePiece")) return;

        Rigidbody ballRb = other.attachedRigidbody;
        if (ballRb == null) return;

        UpdateShootingMult();

        Vector3 worldMoveDir = transform.TransformDirection(moveDirection).normalized;

        // Only correct the component of velocity ALONG moveDirection -- this is
        // the key fix vs. the original script. Instead of pulling the whole
        // ball toward a fixed point (which can point straight into a wall
        // depending on where the ball currently is), this only ever pushes
        // along one fixed direction, so it can never aim itself into a wall.
        // Sideways/vertical velocity (e.g. from gravity, other balls, or a
        // wall bounce) is left alone.
        Vector3 currentVelAlongDir = Vector3.Project(ballRb.velocity, worldMoveDir);
        Vector3 desiredVel = worldMoveDir * (surfaceSpeed * shootingMult);
        Vector3 correction = desiredVel - currentVelAlongDir;

        ballRb.AddForce(correction * correctionForce, ForceMode.Acceleration);
    }
}```
