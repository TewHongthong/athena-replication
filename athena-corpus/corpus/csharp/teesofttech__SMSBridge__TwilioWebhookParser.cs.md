# src/SmsBridge/Webhooks/TwilioWebhookParser.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Webhooks/TwilioWebhookParser.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;

namespace SmsBridge.Webhooks;

/// <summary>Parses Twilio delivery status webhook callbacks.</summary>
public sealed class TwilioWebhookParser : ISmsWebhookParser
{
    public SmsProviderType Provider => SmsProviderType.Twilio;

    public SmsWebhookEvent Parse(IDictionary<string, string> payload)
    {
        payload.TryGetValue("MessageSid", out var messageId);
        payload.TryGetValue("To", out var to);
        payload.TryGetValue("MessageStatus", out var status);
        payload.TryGetValue("ErrorCode", out var errorCode);

        return new SmsWebhookEvent
        {
            Provider = Provider,
            MessageId = messageId,
            To = to,
            Status = MapStatus(status),
            ErrorCode = string.IsNullOrWhiteSpace(errorCode) ? null : errorCode,
            IsTransientFailure = IsTransientError(errorCode),
            Timestamp = DateTimeOffset.UtcNow,
            Raw = new Dictionary<string, string>(payload)
        };
    }

    private static SmsDeliveryStatus MapStatus(string? status) => status?.ToLowerInvariant() switch
    {
        "accepted" => SmsDeliveryStatus.Accepted,
        "queued" => SmsDeliveryStatus.Queued,
        "sending" or "sent" => SmsDeliveryStatus.Sent,
        "delivered" => SmsDeliveryStatus.Delivered,
        "undelivered" => SmsDeliveryStatus.Undelivered,
        "failed" => SmsDeliveryStatus.Failed,
        _ => SmsDeliveryStatus.Unknown
    };

    private static bool IsTransientError(string? errorCode) => errorCode switch
    {
        "30001" or "30003" => true,
        _ => false
    };
}
```
