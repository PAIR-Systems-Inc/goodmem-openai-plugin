<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# MemoryGetOptions

Typed query options for `client.memories.get`.

 Every field is optional; null values are omitted from the wire request.
 Construct via the fluent `Builder`:

```java
 MemoryGetOptions opts = MemoryGetOptions.builder()
     .includeContent(true)
     .build();

```

- `includeContent` (`Boolean`): Whether to include the original content in the response (defaults to false).
- `includeProcessingHistory` (`Boolean`): Whether to include background job processing history in the response (defaults to false).

[Java](../../java.md)
