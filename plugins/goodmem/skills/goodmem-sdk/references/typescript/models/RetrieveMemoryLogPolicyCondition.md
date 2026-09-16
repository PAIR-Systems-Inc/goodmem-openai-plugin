<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# RetrieveMemoryLogPolicyCondition

RetrieveMemory log policy condition. Set matchAll=true to match every authenticated RetrieveMemory request and do not provide anyOf clauses. Otherwise, anyOf is required and must contain at least one non-empty scoped clause.

- `matchAll` (`boolean | null`, optional): When true, match every authenticated RetrieveMemory request. Must be omitted or false when anyOf contains clauses. Defaults to false when omitted.
- `anyOf` (`Array<RetrieveMemoryLogPolicyConditionClause> | null`, optional): OR clauses used for scoped matching. Required and non-empty when matchAll is false or omitted. Must be omitted or empty when matchAll is true. Each clause must include at least one match dimension.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RetrieveMemoryLogPolicyConditionClause](RetrieveMemoryLogPolicyConditionClause.md)
