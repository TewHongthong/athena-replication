# src/SmsBridge/Providers/AfricasTalking/AfricasTalkingSmsRequestMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/AfricasTalking/AfricasTalkingSmsRequestMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;
using SmsBridge.Options;

namespace SmsBridge.Providers.AfricasTalking;

internal static class AfricasTalkingSmsRequestMapper
{
    public static IReadOnlyDictionary<string, string> ToRequestBody(
        SmsMessage message,
        AfricasTalkingOptions options)
    {
        var body = new Dictionary<string, string>
        {
            ["username"] = options.Username,
            ["to"] = message.To,
            ["message"] = message.Body
        };

        var from = message.From ?? options.From;
        if (!string.IsNullOrWhiteSpace(from))
            body["from"] = from;

        AddOptionalMetadata(body, message, "bulkSMSMode", "bulk_sms_mode", "bulkSMSMode");
        AddOptionalMetadata(body, message, "enqueue", "enqueue");
        AddOptionalMetadata(body, message, "keyword", "keyword");
        AddOptionalMetadata(body, message, "linkId", "linkId", "link_id");
        AddOptionalMetadata(body, message, "retryDurationInHours", "retryDurationInHours", "retry_duration_in_hours");

        return body;
    }

    private static void AddOptionalMetadata(
        IDictionary<string, string> body,
        SmsMessage message,
        string fieldName,
        params string[] metadataKeys)
    {
        if (message.Metadata is null)
            return;

        foreach (var key in metadataKeys)
        {
            if (message.Metadata.TryGetValue(key, out var value) &&
                !string.IsNullOrWhiteSpace(value))
            {
                body[fieldName] = value;
                return;
            }
        }
    }
}
```
