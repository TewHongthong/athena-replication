# src/SmsBridge/Providers/Termii/TermiiSmsRequestMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/Termii/TermiiSmsRequestMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;
using SmsBridge.Options;

namespace SmsBridge.Providers.Termii;

internal static class TermiiSmsRequestMapper
{
    public static object ToRequestBody(SmsMessage message, TermiiOptions options) => new
    {
        to = message.To,
        from = message.From ?? options.From,
        sms = message.Body,
        type = ReadMetadata(message, "type") ?? "plain",
        channel = ReadMetadata(message, "channel") ?? options.Channel,
        api_key = options.ApiKey
    };

    private static string? ReadMetadata(SmsMessage message, string key)
    {
        if (message.Metadata is null)
            return null;

        return message.Metadata.TryGetValue(key, out var value) && !string.IsNullOrWhiteSpace(value)
            ? value
            : null;
    }
}
```
