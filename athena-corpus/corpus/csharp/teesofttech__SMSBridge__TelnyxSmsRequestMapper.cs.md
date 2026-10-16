# src/SmsBridge/Providers/Telnyx/TelnyxSmsRequestMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/Telnyx/TelnyxSmsRequestMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;

namespace SmsBridge.Providers.Telnyx;

internal static class TelnyxSmsRequestMapper
{
    public static object ToRequestBody(SmsMessage message, string defaultFrom) => new
    {
        from = message.From ?? defaultFrom,
        to = message.To,
        text = message.Body
    };
}
```
