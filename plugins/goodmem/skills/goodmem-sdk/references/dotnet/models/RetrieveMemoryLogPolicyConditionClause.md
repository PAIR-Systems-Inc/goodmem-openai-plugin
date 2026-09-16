<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# RetrieveMemoryLogPolicyConditionClause

One OR clause in a RetrieveMemory log policy condition. All populated dimensions in the clause must match; clauses are ORed together.

`Goodmem.Client.Models.RetrieveMemoryLogPolicyConditionClause`

- `ApiKeyIds` (`IReadOnlyList<string>?`): API key UUID strings used to authenticate RetrieveMemory requests. JSON: `apiKeyIds`.
- `ApiKeyLabelSelectors` (`IReadOnlyDictionary<string, string>?`): Exact API-key label selectors that must all match. JSON: `apiKeyLabelSelectors`.
- `RequestorUserIds` (`IReadOnlyList<string>?`): Authenticated requestor user UUID strings. JSON: `requestorUserIds`.
- `SpaceIds` (`IReadOnlyList<string>?`): Post-permission accessible space UUID strings. JSON: `spaceIds`.
- `SpaceLabelSelectors` (`IReadOnlyDictionary<string, string>?`): Exact space label selectors that must match at least one accessible space. JSON: `spaceLabelSelectors`.

[.NET](../../dotnet.md)
