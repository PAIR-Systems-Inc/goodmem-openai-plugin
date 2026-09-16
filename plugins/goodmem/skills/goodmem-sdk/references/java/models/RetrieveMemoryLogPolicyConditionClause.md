<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# RetrieveMemoryLogPolicyConditionClause

One OR clause in a RetrieveMemory log policy condition. All populated dimensions in the clause must match; clauses are ORed together.

- `requestorUserIds` (`java.util.List<String>`): Authenticated requestor user UUID strings.
- `apiKeyIds` (`java.util.List<ApiKeyId>`): API key UUID strings used to authenticate RetrieveMemory requests. Element type `ApiKeyId`; build each entry from a raw string with `ApiKeyId.from(String)`.
- `spaceIds` (`java.util.List<SpaceId>`): Post-permission accessible space UUID strings. Element type `SpaceId`; build each entry from a raw string with `SpaceId.from(String)`.
- `apiKeyLabelSelectors` (`java.util.Map<String, String>`): Exact API-key label selectors that must all match.
- `spaceLabelSelectors` (`java.util.Map<String, String>`): Exact space label selectors that must match at least one accessible space.

[Java](../../java.md)

Related types — open only those used by your request:

- [ApiKeyId](ApiKeyId.md)
- [SpaceId](SpaceId.md)
