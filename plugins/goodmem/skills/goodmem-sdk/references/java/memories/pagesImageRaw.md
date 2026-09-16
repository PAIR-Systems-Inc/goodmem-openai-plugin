<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.pagesImageRaw

Download memory page image content

Downloads inline bytes for one page image. The page index is required. The optional dpi and content type query parameters act as rendition filters; if omitted, the server returns the unique rendition for that page or rejects ambiguous matches. Requires READ_MEMORY on the containing memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

Escape hatch. Prefer the typed sibling `pagesImage(...)` which accepts an `XxxOptions` record (or no args) instead of a raw `Map<String, Object>`. Use this method only when you need a wire key the typed options class doesn't yet expose.

```java
byte[] pagesImageRaw(String id, String pageIndex, java.util.Map<String, Object> query)
```

[memories](../memories.md) · [Java](../../java.md)
