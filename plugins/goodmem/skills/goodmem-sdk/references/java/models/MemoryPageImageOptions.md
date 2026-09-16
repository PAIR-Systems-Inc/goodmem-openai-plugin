<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# MemoryPageImageOptions

Typed query options for `client.memories.pagesImage`.

 Every field is optional; null values are omitted from the wire request.
 Construct via the fluent `Builder`:

```java
 MemoryPageImageOptions opts = MemoryPageImageOptions.builder()
     .dpi(42)
     .build();

```

- `dpi` (`Integer`): Optional rendition filter. If omitted, the unique page-image rendition for the page is returned; if multiple renditions exist, specify dpi and/or contentType.
- `contentType` (`String`): Optional rendition filter. MIME type of the desired page image, such as image/png.

[Java](../../java.md)
