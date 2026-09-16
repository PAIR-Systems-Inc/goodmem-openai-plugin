<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# RerankerGetOptions

Typed query options for `client.rerankers.get`.

 Every field is optional; null values are omitted from the wire request.
 Construct via the fluent `Builder`:

```java
 RerankerGetOptions opts = RerankerGetOptions.builder()
     .includeCredentials(true)
     .build();

```

- `includeCredentials` (`Boolean`): Whether to return stored credentials. Also accepts include_credentials. Requires READ_RERANKER_CREDENTIALS in addition to READ_RERANKER.

[Java](../../java.md)
