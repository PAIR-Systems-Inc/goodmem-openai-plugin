<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# RetrieveMemoryLogPolicyCondition

RetrieveMemory log policy condition. Set matchAll=true to match every authenticated RetrieveMemory request and do not provide anyOf clauses. Otherwise, anyOf is required and must contain at least one non-empty scoped clause.

- `matchAll` (`Boolean`): When true, match every authenticated RetrieveMemory request. Must be omitted or false when anyOf contains clauses. Defaults to false when omitted.
- `anyOf` (`java.util.List<RetrieveMemoryLogPolicyConditionClause>`): OR clauses used for scoped matching. Required and non-empty when matchAll is false or omitted. Must be omitted or empty when matchAll is true. Each clause must include at least one match dimension.

[Java](../../java.md)

Related types — open only those used by your request:

- [RetrieveMemoryLogPolicyConditionClause](RetrieveMemoryLogPolicyConditionClause.md)
