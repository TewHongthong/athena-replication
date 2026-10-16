# src/SmsBridge/Providers/AwsSns/AwsSnsSmsRequestMapper.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Providers/AwsSns/AwsSnsSmsRequestMapper.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using SmsBridge.Abstractions;
using SmsBridge.Options;

namespace SmsBridge.Providers.AwsSns;

internal static class AwsSnsSmsRequestMapper
{
    public static IReadOnlyList<KeyValuePair<string, string>> ToFormFields(
        SmsMessage message,
        AwsSnsOptions options)
    {
        var fields = new List<KeyValuePair<string, string>>
        {
            new("Action", "Publish"),
            new("Version", "2010-03-31"),
            new("PhoneNumber", message.To),
            new("Message", message.Body)
        };

        var senderId = message.From ?? options.SenderId;
        if (!string.IsNullOrWhiteSpace(senderId))
        {
            fields.Add(new("MessageAttributes.entry.1.Name", "AWS.SNS.SMS.SenderID"));
            fields.Add(new("MessageAttributes.entry.1.Value.DataType", "String"));
            fields.Add(new("MessageAttributes.entry.1.Value.StringValue", senderId));
        }

        return fields;
    }
}
```
