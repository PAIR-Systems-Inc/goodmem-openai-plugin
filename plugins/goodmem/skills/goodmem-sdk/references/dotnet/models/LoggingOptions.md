<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# LoggingOptions

`Goodmem.Client.Models.LoggingOptions`

- `CallerAttributes` (`IReadOnlyDictionary<string, object>?`): Optional flat scalar attributes attached if this request is persisted by caller opt-in or admin policy logging. Supported value types are string, integer, floating-point, and boolean. At most 32 entries are accepted. JSON: `callerAttributes`.
- `Enabled` (`bool?`): Opts this request in to durable server-side request logging. False or omitted does not opt out of admin policy logging. JSON: `enabled`.

[.NET](../../dotnet.md)
