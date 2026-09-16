<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# RerankerListOptions

Typed query options for `client.rerankers.list`.

 Every field is optional; null values are omitted from the wire request.
 Construct via the fluent `Builder`:

```java
 RerankerListOptions opts = RerankerListOptions.builder()
     .ownerId(UserId.from("value"))
     .build();

```

- `ownerId` (`UserId`): Filter the already-authorized result set by owner principal UUID. Omitting this parameter does not bypass per-reranker READ_RERANKER filtering.
- `providerType` (`ProviderType`): Filter rerankers by provider type. Allowed values match the ProviderType schema.
- `label` (`java.util.Map<String, String>`): Filter by label key-value pairs. Label filters accept either label.= or label[key]=value (for example, label.environment=production or label[environment]=production).

[Java](../../java.md)

Related types — open only those used by your request:

- [ProviderType](ProviderType.md)
- [UserId](UserId.md)
