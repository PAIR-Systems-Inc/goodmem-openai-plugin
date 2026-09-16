<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# UpdateApiKeyRequest

Request parameters for updating an API key.

`Goodmem.Client.Models.UpdateApiKeyRequest`

- `MergeLabels` (`IReadOnlyDictionary<string, string>?`): Merge these labels with existing ones. Mutually exclusive with replaceLabels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `mergeLabels`.
- `ReplaceLabels` (`IReadOnlyDictionary<string, string>?`): Replace all existing labels with this set. Mutually exclusive with mergeLabels. The stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `replaceLabels`.
- `Status` (`string?`): New status for the API key. INACTIVE is permanent; revoked keys cannot be reactivated. JSON: `status`.

[.NET](../../dotnet.md)
