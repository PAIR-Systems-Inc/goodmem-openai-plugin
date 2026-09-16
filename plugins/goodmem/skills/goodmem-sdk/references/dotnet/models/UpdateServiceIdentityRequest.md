<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# UpdateServiceIdentityRequest

Updates explicitly present profile fields. Empty description clears it; omitted fields remain unchanged. Ownership is changed only through the transfer endpoint.

`Goodmem.Client.Models.UpdateServiceIdentityRequest`

- `Description` (`string?`): Replacement description. An empty string clears the description. JSON: `description`.
- `DisplayName` (`string?`): Replacement display name. A present blank value is invalid. JSON: `displayName`.
- `MergeLabels` (`IReadOnlyDictionary<string, string>?`): Labels to upsert; must contain at least one entry and is mutually exclusive with replaceLabels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `mergeLabels`.
- `ReplaceLabels` (`IReadOnlyDictionary<string, string>?`): Complete replacement label map; an empty map clears all labels and is mutually exclusive with mergeLabels. At most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `replaceLabels`.

[.NET](../../dotnet.md)
