<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# rerankers.listRaw

List rerankers

Retrieves a list of reranker configurations accessible to the caller, with optional filtering.

IMPORTANT: Pagination is NOT supported - all matching results are returned. Results are ordered by created_at descending. Stored credentials are never included in list responses.

LABEL FILTERS: Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_RERANKER on the GoodMem instance. Each returned reranker must also be visible through READ_RERANKER; unauthorized rerankers are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility.

Escape hatch. Prefer the typed sibling `list(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
java.util.List<RerankerResponse> listRaw(java.util.Map<String, Object> query)
```

[rerankers](../rerankers.md) · [Java](../../java.md)
