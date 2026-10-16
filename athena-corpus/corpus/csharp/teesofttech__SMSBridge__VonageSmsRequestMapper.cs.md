# src/SmsBridge/Providers/Vonage/VonageSmsRequestMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/Vonage/VonageSmsRequestMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;
using SmsBridge.Options;

namespace SmsBridge.Providers.Vonage;

internal static class VonageSmsRequestMapper
{
    /// <summary>Builds the form fields for the Vonage SMS API v1.</summary>
    public static IReadOnlyDictionary<string, string> ToFormFields(SmsMessage message, VonageOptions options)
    {
        var fields = new Dictionary<string, string>
        {
            ["from"] = message.From ?? options.From,
            ["to"] = message.To,
            ["text"] = message.Body,
            ["api_key"] = options.ApiKey,
            ["api_secret"] = options.ApiSecret
        };

        if (!IsGsm7(message.Body))
            fields["type"] = "unicode";

        return fields;
    }

    private static bool IsGsm7(string value) =>
        value.All(character =>
            Gsm7BasicCharacters.Contains(character) ||
            Gsm7ExtensionCharacters.Contains(character));

    private const string Gsm7BasicCharacters =
        "@£$¥èéùìòÇ\nØø\rÅåΔ_ΦΓΛΩΠΨΣΘΞ ÆæßÉ !\"#¤%&'()*+,-./0123456789:;<=>?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà";

    private const string Gsm7ExtensionCharacters = "^{}\\[~]|€";
}
```
