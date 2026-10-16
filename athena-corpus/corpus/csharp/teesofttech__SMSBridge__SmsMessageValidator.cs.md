# src/SmsBridge/Validation/SmsMessageValidator.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Validation/SmsMessageValidator.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;

namespace SmsBridge.Validation;

internal static class SmsMessageValidator
{
    public static void Validate(SmsMessage message)
    {
        if (message is null)
            throw new ArgumentNullException(nameof(message));

        var errors = new List<string>();

        if (string.IsNullOrWhiteSpace(message.To))
            errors.Add("'To' is required.");

        if (string.IsNullOrWhiteSpace(message.Body))
            errors.Add("'Body' is required.");

        if (errors.Count > 0)
            throw new SmsBridgeException($"SMS message validation failed: {string.Join(" ", errors)}");
    }
}
```
