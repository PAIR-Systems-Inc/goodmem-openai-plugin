<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# rerankers.list

List rerankers

Retrieves a list of reranker configurations accessible to the caller, with optional filtering.

IMPORTANT: Pagination is NOT supported - all matching results are returned. Results are ordered by created_at descending. Stored credentials are never included in list responses.

LABEL FILTERS: Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

AUTHORIZATION: Requires LIST_RERANKER on the GoodMem instance. Each returned reranker must also be visible through READ_RERANKER; unauthorized rerankers are filtered in PostgreSQL. The ownerId parameter filters that already-authorized result set and does not grant additional visibility.

```java
java.util.List<RerankerResponse> list()
```

No-filter convenience. Equivalent to passing `null` or a default RerankerListOptions.

```java
java.util.List<RerankerResponse> list(RerankerListOptions options)
```

Typed-options overload. See `RerankerListOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[rerankers](../rerankers.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [RerankerListOptions](../models/RerankerListOptions.md)
