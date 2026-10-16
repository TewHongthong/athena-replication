# src/SmsBridge/Providers/Sinch/SinchSmsRequestMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/Sinch/SinchSmsRequestMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;
using SmsBridge.Options;

namespace SmsBridge.Providers.Sinch;

internal static class SinchSmsRequestMapper
{
    public static IReadOnlyDictionary<string, object> ToRequestBody(
        SmsMessage message,
        SinchOptions options)
    {
        var body = new Dictionary<string, object>
        {
            ["from"] = message.From ?? options.From,
            ["to"] = new[] { message.To },
            ["body"] = message.Body
        };

        if (!string.IsNullOrWhiteSpace(options.CallbackUrl))
        {
            body["delivery_report"] = "per_recipient";
            body["callback_url"] = options.CallbackUrl;
        }

        return body;
    }
}
```
