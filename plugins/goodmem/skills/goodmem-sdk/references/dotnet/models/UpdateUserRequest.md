<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# UpdateUserRequest

Updates explicitly present profile fields. Empty username or displayName clears that optional field; an omitted field remains unchanged.

`Goodmem.Client.Models.UpdateUserRequest`

- `DisplayName` (`string?`): Replacement display name. An empty string clears the display name. JSON: `displayName`.
- `Email` (`string?`): Replacement email. A present empty value is invalid. JSON: `email`.
- `MergeLabels` (`IReadOnlyDictionary<string, string>?`): Labels to upsert; must contain at least one entry and is mutually exclusive with replaceLabels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `mergeLabels`.
- `ReplaceLabels` (`IReadOnlyDictionary<string, string>?`): Complete replacement label map; an empty map clears all labels and is mutually exclusive with mergeLabels. At most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `replaceLabels`.
- `Username` (`string?`): Replacement username. An empty string clears the username. JSON: `username`.

[.NET](../../dotnet.md)
