<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# MemoryPageListOptions

Typed query options for `client.memories.pages`.

 Every field is optional; null values are omitted from the wire request.
 Construct via the fluent `Builder`:

```java
 MemoryPageListOptions opts = MemoryPageListOptions.builder()
     .startPageIndex(42)
     .build();

```

- `startPageIndex` (`Integer`): Optional lower bound for returned page indices, inclusive.
- `endPageIndex` (`Integer`): Optional upper bound for returned page indices, inclusive.
- `dpi` (`Integer`): Optional rendition filter for page-image DPI.
- `contentType` (`String`): Optional rendition filter for page-image MIME type, such as image/png.
- `maxResults` (`Integer`): Maximum number of results per page.
- `nextToken` (`String`): Opaque pagination token for the next page. Do not parse or construct it.

[Java](../../java.md)
