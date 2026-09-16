<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# RetrieveMemoryLogPolicyCondition

RetrieveMemory log policy condition. Set matchAll=true to match every authenticated RetrieveMemory request and do not provide anyOf clauses. Otherwise, anyOf is required and must contain at least one non-empty scoped clause.

- `match_all` (`bool | None`, optional): When true, match every authenticated RetrieveMemory request. Must be omitted or false when any_of contains clauses. Defaults to false when omitted. JSON: `matchAll`.
- `any_of` (`list[RetrieveMemoryLogPolicyConditionClause] | None`, optional): OR clauses used for scoped matching. Required and non-empty when match_all is false or omitted. Must be omitted or empty when match_all is true. Each clause must include at least one match dimension. JSON: `anyOf`.

[Python](../../python.md)

Related types — open only those used by your request:

- [RetrieveMemoryLogPolicyConditionClause](RetrieveMemoryLogPolicyConditionClause.md)
