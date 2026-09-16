<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# RetrieveMemoryLogPolicyConditionClause

One OR clause in a RetrieveMemory log policy condition. All populated dimensions in the clause must match; clauses are ORed together.

```python
from goodmem.models import RetrieveMemoryLogPolicyConditionClause
```

- `requestor_user_ids` (`list[str] | None`, optional): Authenticated requestor user UUID strings. JSON: `requestorUserIds`.
- `api_key_ids` (`list[str] | None`, optional): API key UUID strings used to authenticate RetrieveMemory requests. JSON: `apiKeyIds`.
- `space_ids` (`list[str] | None`, optional): Post-permission accessible space UUID strings. JSON: `spaceIds`.
- `api_key_label_selectors` (`dict[str, str] | None`, optional): Exact API-key label selectors that must all match. JSON: `apiKeyLabelSelectors`.
- `space_label_selectors` (`dict[str, str] | None`, optional): Exact space label selectors that must match at least one accessible space. JSON: `spaceLabelSelectors`.

[Python](../../python.md)
