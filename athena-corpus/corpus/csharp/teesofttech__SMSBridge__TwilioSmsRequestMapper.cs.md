# src/SmsBridge/Providers/Twilio/TwilioSmsRequestMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/Twilio/TwilioSmsRequestMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;
using SmsBridge.Options;

namespace SmsBridge.Providers.Twilio;

internal static class TwilioSmsRequestMapper
{
    /// <summary>Maps a <see cref="SmsMessage"/> to Twilio REST API form fields.</summary>
    public static IEnumerable<KeyValuePair<string, string>> ToFormFields(
        SmsMessage message,
        TwilioOptions options)
    {
        yield return new KeyValuePair<string, string>("To", message.To);
        yield return new KeyValuePair<string, string>("From", message.From ?? options.From);
        yield return new KeyValuePair<string, string>("Body", message.Body);

        if (!string.IsNullOrWhiteSpace(options.StatusCallbackUrl))
            yield return new KeyValuePair<string, string>("StatusCallback", options.StatusCallbackUrl);
    }
}
```
