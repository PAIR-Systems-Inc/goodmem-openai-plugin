<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# RetrieveMemoryLogPolicyConditionClause

One OR clause in a RetrieveMemory log policy condition. All populated dimensions in the clause must match; clauses are ORed together.

- `requestorUserIds` (`Array<string> | null`, optional): Authenticated requestor user UUID strings.
- `apiKeyIds` (`Array<string> | null`, optional): API key UUID strings used to authenticate RetrieveMemory requests.
- `spaceIds` (`Array<string> | null`, optional): Post-permission accessible space UUID strings.
- `apiKeyLabelSelectors` (`Record<string, string> | null`, optional): Exact API-key label selectors that must all match.
- `spaceLabelSelectors` (`Record<string, string> | null`, optional): Exact space label selectors that must match at least one accessible space.

[TypeScript](../../typescript.md)
