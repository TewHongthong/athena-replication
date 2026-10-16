# src/SmsBridge/Providers/Plivo/PlivoSmsResponseMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/Plivo/PlivoSmsResponseMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using System.Text.Json;
using SmsBridge.Abstractions;

namespace SmsBridge.Providers.Plivo;

internal static class PlivoSmsResponseMapper
{
    public static SmsSendResult FromResponse(string providerName, string json)
    {
        using var doc = JsonDocument.Parse(json);
        var root = doc.RootElement;

        var messageId = root.TryGetProperty("message_uuid", out var uuidEl) &&
                        uuidEl.ValueKind == JsonValueKind.Array &&
                        uuidEl.GetArrayLength() > 0
            ? uuidEl[0].GetString()
            : null;

        return SmsSendResult.Succeeded(providerName, messageId, SmsDeliveryStatus.Queued);
    }

    public static SmsSendResult FromErrorResponse(string providerName, int httpStatusCode, string json)
    {
        string? errorMessage = null;

        try
        {
            using var doc = JsonDocument.Parse(json);
            var root = doc.RootElement;
            errorMessage = root.TryGetProperty("error", out var errEl) ? errEl.GetString() : null;
        }
        catch (JsonException) { /* best-effort */ }

        bool isTransient = httpStatusCode >= 500 || httpStatusCode == 429;
        return SmsSendResult.Failed(
            providerName,
            null,
            errorMessage ?? $"HTTP {httpStatusCode}",
            isTransient,
            mayHaveBeenAccepted: httpStatusCode >= 500);
    }
}
```
