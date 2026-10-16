# src/SmsBridge/Routing/DefaultSmsProviderRouter.cs

- source repo: teesofttech/SMSBridge
- repo url: https://github.com/teesofttech/SMSBridge
- license: MIT
- created_at: 2026-06-13
- file path: src/SmsBridge/Routing/DefaultSmsProviderRouter.cs
- commit: 1b400e9c1804dc01402d0b9769db5475f76d3785

```csharp
using Microsoft.Extensions.Options;
using SmsBridge.Abstractions;
using SmsBridge.Options;

namespace SmsBridge.Routing;

internal sealed class DefaultSmsProviderRouter : ISmsProviderRouter
{
    private readonly IReadOnlyDictionary<string, ISmsProvider> _providers;
    private readonly SmsBridgeOptions _options;

    public DefaultSmsProviderRouter(
        IEnumerable<ISmsProvider> providers,
        IOptions<SmsBridgeOptions> options)
    {
        _providers = providers.ToDictionary(p => p.Name, StringComparer.OrdinalIgnoreCase);
        _options = options.Value;
    }

    public ISmsProvider Resolve(SmsRoutingContext context)
    {
        var providerName = context.ExplicitProvider ?? _options.DefaultProvider;

        if (string.IsNullOrWhiteSpace(providerName))
            throw new SmsBridgeException(
                "No provider could be resolved. Set 'SmsBridge:DefaultProvider' in configuration or supply a provider name on the message.");

        if (!_providers.TryGetValue(providerName, out var provider))
            throw new SmsBridgeException(
                $"Provider '{providerName}' is not registered. Registered providers: [{string.Join(", ", _providers.Keys)}].");

        return provider;
    }
}
```
