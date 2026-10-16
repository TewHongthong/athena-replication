# src/SmsBridge/Providers/Unifonic/UnifonicSmsRequestMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/Unifonic/UnifonicSmsRequestMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;
using SmsBridge.Options;

namespace SmsBridge.Providers.Unifonic;

internal static class UnifonicSmsRequestMapper
{
    public static IReadOnlyDictionary<string, string> ToQueryParameters(
        SmsMessage message,
        UnifonicOptions options)
    {
        var parameters = new Dictionary<string, string>
        {
            ["AppSid"] = options.AppSid,
            ["SenderID"] = message.From ?? options.From,
            ["Body"] = message.Body,
            ["Recipient"] = ToUnifonicRecipient(message.To),
            ["responseType"] = "json"
        };

        AddOptionalMetadata(parameters, message, "CorrelationID", "CorrelationID", "correlationId");
        AddOptionalMetadata(parameters, message, "baseEncode", "baseEncode", "base_encode");
        AddOptionalMetadata(parameters, message, "statusCallback", "statusCallback", "status_callback");
        AddOptionalMetadata(parameters, message, "async", "async");

        return parameters;
    }

    private static void AddOptionalMetadata(
        IDictionary<string, string> parameters,
        SmsMessage message,
        string parameterName,
        params string[] metadataKeys)
    {
        if (message.Metadata is null)
            return;

        foreach (var key in metadataKeys)
        {
            if (message.Metadata.TryGetValue(key, out var value) &&
                !string.IsNullOrWhiteSpace(value))
            {
                parameters[parameterName] = value;
                return;
            }
        }
    }

    private static string ToUnifonicRecipient(string recipient)
    {
        if (recipient.StartsWith("+", StringComparison.Ordinal))
            return recipient[1..];

        if (recipient.StartsWith("00", StringComparison.Ordinal))
            return recipient[2..];

        return recipient;
    }
}
```
