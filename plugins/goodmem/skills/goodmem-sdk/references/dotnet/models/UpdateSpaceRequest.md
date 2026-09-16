<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# UpdateSpaceRequest

Request parameters for updating a space.

`Goodmem.Client.Models.UpdateSpaceRequest`

- `MergeLabels` (`IReadOnlyDictionary<string, string>?`): Labels to merge with existing labels. Mutually exclusive with replaceLabels. JSON: `mergeLabels`.
- `Name` (`string?`): The new name for the space. JSON: `name`.
- `ReplaceLabels` (`IReadOnlyDictionary<string, string>?`): Labels to replace all existing labels. Mutually exclusive with mergeLabels. JSON: `replaceLabels`.

[.NET](../../dotnet.md)
