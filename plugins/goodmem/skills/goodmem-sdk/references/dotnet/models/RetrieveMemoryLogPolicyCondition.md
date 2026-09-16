<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# RetrieveMemoryLogPolicyCondition

RetrieveMemory log policy condition. Set matchAll=true to match every authenticated RetrieveMemory request and do not provide anyOf clauses. Otherwise, anyOf is required and must contain at least one non-empty scoped clause.

`Goodmem.Client.Models.RetrieveMemoryLogPolicyCondition`

- `AnyOf` (`IReadOnlyList<RetrieveMemoryLogPolicyConditionClause>?`): OR clauses used for scoped matching. Required and non-empty when matchAll is false or omitted. Must be omitted or empty when matchAll is true. Each clause must include at least one match dimension. JSON: `anyOf`.
- `MatchAll` (`bool?`): When true, match every authenticated RetrieveMemory request. Must be omitted or false when anyOf contains clauses. Defaults to false when omitted. JSON: `matchAll`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [RetrieveMemoryLogPolicyConditionClause](RetrieveMemoryLogPolicyConditionClause.md)
