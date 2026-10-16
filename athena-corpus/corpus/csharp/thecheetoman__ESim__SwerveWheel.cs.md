# Assets/Scripts/Robot/SwerveWheel.cs

- source repo: thecheetoman/ESim
- repo url: https://github.com/thecheetoman/ESim
- license: MIT
- created_at: 2026-09-16T23:28:41Z
- file path: Assets/Scripts/Robot/SwerveWheel.cs
- commit: 59cde034d0041d0af0a43cdf7e43d979935b7db8

```csharp
using UnityEngine;

namespace RobotFramework.Controllers.Drivetrain
{
    public class SwerveWheel : MonoBehaviour
    {
        private WheelCollider _wheelCollider;
        public float wheelAngle;

        private void Start()
        {
            _wheelCollider = GetComponent<WheelCollider>();
        }

        private void Update()
        {
            if (wheelAngle < 0)
            {
                wheelAngle = -wheelAngle + 180;
            }

            if (wheelAngle > 360)
            {
                wheelAngle -= 360;
            }

            _wheelCollider.steerAngle = wheelAngle;
            _wheelCollider.brakeTorque = 0.0000000f;
            _wheelCollider.motorTorque = 0.000000000000000000000000000001f;
        }
    }
}```
