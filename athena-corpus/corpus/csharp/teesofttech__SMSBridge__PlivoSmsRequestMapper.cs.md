# src/SmsBridge/Providers/Plivo/PlivoSmsRequestMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/Plivo/PlivoSmsRequestMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;
using SmsBridge.Options;

namespace SmsBridge.Providers.Plivo;

internal static class PlivoSmsRequestMapper
{
    public static IReadOnlyDictionary<string, object> ToRequestBody(
        SmsMessage message,
        PlivoOptions options)
    {
        var body = new Dictionary<string, object>
        {
            ["src"] = message.From ?? options.From,
            ["dst"] = message.To,
            ["text"] = message.Body
        };

        if (!string.IsNullOrWhiteSpace(options.CallbackUrl))
        {
            body["url"] = options.CallbackUrl;
            body["method"] = "POST";
        }

        return body;
    }
}
```
