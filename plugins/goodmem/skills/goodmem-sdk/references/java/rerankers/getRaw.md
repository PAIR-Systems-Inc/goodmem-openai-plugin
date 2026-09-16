<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# rerankers.getRaw

Get a reranker by ID

Retrieves the details of a specific reranker configuration by its unique identifier. Stored credentials are omitted unless includeCredentials is true and the caller also has READ_RERANKER_CREDENTIALS. Requires READ_RERANKER on the requested reranker. The service distinguishes a missing reranker from an existing reranker the caller cannot read. This is a read-only operation with no side effects and is safe to retry.

Escape hatch. Prefer the typed sibling `get(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
RerankerResponse getRaw(String id, java.util.Map<String, Object> query)
```

[rerankers](../rerankers.md) · [Java](../../java.md)
