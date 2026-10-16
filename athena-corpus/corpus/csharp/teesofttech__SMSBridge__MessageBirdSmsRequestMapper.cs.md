# src/SmsBridge/Providers/MessageBird/MessageBirdSmsRequestMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/MessageBird/MessageBirdSmsRequestMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;

namespace SmsBridge.Providers.MessageBird;

internal static class MessageBirdSmsRequestMapper
{
    public static IReadOnlyDictionary<string, string> ToFormFields(
        SmsMessage message,
        string defaultFrom) =>
        new Dictionary<string, string>
        {
            ["originator"] = message.From ?? defaultFrom,
            ["recipients"] = message.To.TrimStart('+'),
            ["body"] = message.Body,
            ["datacoding"] = "auto"
        };
}
```
