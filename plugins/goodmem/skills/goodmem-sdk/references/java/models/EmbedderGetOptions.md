<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# EmbedderGetOptions

Typed query options for `client.embedders.get`.

 Every field is optional; null values are omitted from the wire request.
 Construct via the fluent `Builder`:

```java
 EmbedderGetOptions opts = EmbedderGetOptions.builder()
     .includeCredentials(true)
     .build();

```

- `includeCredentials` (`Boolean`): Whether to return stored credentials. Also accepts include_credentials. Requires READ_EMBEDDER_CREDENTIALS in addition to READ_EMBEDDER.

[Java](../../java.md)
