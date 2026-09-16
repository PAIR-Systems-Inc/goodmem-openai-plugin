<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# apikeys.list

List API keys

Requires LIST_API_KEY on the singleton instance, then retrieves one UUID-ordered page containing only credentials that independently pass READ_API_KEY. Both gates use the authenticated principal's live authority and any scoped-key ceiling. Subject, owner, and lifecycle filters are applied after authorization. FULL includes complete immutable ceilings; BASIC omits them, sets ceiling_omitted=true, and permits larger pages. Raw key values and key hashes are never returned.

Args:
    subject_principal_id (str, optional): Filter by exact subject-principal UUID
    owner_principal_id (str, optional): Filter by exact administrative-owner UUID
    lifecycle_state (Literal['NOT_YET_VALID', 'USABLE', 'EXPIRED', 'REVOKED'], optional): Filter by precise lifecycle state
    view (Literal['FULL', 'BASIC'], optional, default='FULL'): Metadata projection; omission defaults to FULL
    max_results (int, optional): Page size; FULL defaults to 10 and permits at most 20, while BASIC defaults to 50 and permits at most 1,000
    next_token (str, optional): Opaque continuation token returned by the preceding page

Returns:
    Page[ApiKeyResponse]

```python
apikeys.list(*, subject_principal_id: 'str | None' = None, owner_principal_id: 'str | None' = None, lifecycle_state: "Literal['NOT_YET_VALID', 'USABLE', 'EXPIRED', 'REVOKED'] | None" = None, view: "Literal['FULL', 'BASIC'] | None" = None, max_results: 'int | None' = None, next_token: 'str | None' = None) -> 'Page[ApiKeyResponse]'
```

[apikeys](../apikeys.md) · [Python](../../python.md)
