# src/SmsBridge/Providers/Infobip/InfobipSmsRequestMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/Infobip/InfobipSmsRequestMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;

namespace SmsBridge.Providers.Infobip;

internal static class InfobipSmsRequestMapper
{
    public static object ToRequestBody(SmsMessage message, string defaultFrom) => new
    {
        messages = new[]
        {
            new
            {
                sender = message.From ?? defaultFrom,
                destinations = new[]
                {
                    new { to = message.To.TrimStart('+') }
                },
                content = new
                {
                    text = message.Body
                }
            }
        }
    };
}
```
