<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# rerankers.get

Get a reranker by ID

Retrieves the details of a specific reranker configuration by its unique identifier. Stored credentials are omitted unless includeCredentials is true and the caller also has READ_RERANKER_CREDENTIALS. Requires READ_RERANKER on the requested reranker. The service distinguishes a missing reranker from an existing reranker the caller cannot read. This is a read-only operation with no side effects and is safe to retry.

```java
RerankerResponse get(String id)
```

No-filter convenience. Equivalent to passing `null` or a default RerankerGetOptions.

```java
RerankerResponse get(String id, RerankerGetOptions options)
```

Typed-options overload. See `RerankerGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
RerankerResponse get(ai.pairsys.goodmem.client.models.RerankerId id)
```

Domain-ID typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
RerankerResponse get(ai.pairsys.goodmem.client.models.RerankerId id, RerankerGetOptions options)
```

Domain-ID typed overload. See `RerankerGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
RerankerResponse get(java.util.UUID id)
```

UUID-typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
RerankerResponse get(java.util.UUID id, RerankerGetOptions options)
```

UUID-typed overload. See `RerankerGetOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[rerankers](../rerankers.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [RerankerGetOptions](../models/RerankerGetOptions.md)
- [RerankerId](../models/RerankerId.md)
