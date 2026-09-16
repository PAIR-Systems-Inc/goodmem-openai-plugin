<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.pagesImage

Download memory page image content

Downloads inline bytes for one page image. The page index is required. The optional dpi and content type query parameters act as rendition filters; if omitted, the server returns the unique rendition for that page or rejects ambiguous matches. Requires READ_MEMORY on the containing memory; authority may be granted through DIRECT_MEMBERS_OF its containing space.

```java
byte[] pagesImage(String id, String pageIndex)
```

No-filter convenience. Equivalent to passing `null` or a default MemoryPageImageOptions.

```java
byte[] pagesImage(String id, String pageIndex, MemoryPageImageOptions options)
```

Typed-options overload. See `MemoryPageImageOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
byte[] pagesImage(String id, long pageIndex)
```

Numeric-typed path overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
byte[] pagesImage(String id, long pageIndex, MemoryPageImageOptions options)
```

Numeric-typed path overload. See `MemoryPageImageOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
byte[] pagesImage(ai.pairsys.goodmem.client.models.MemoryId id, String pageIndex)
```

Domain-ID typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
byte[] pagesImage(ai.pairsys.goodmem.client.models.MemoryId id, String pageIndex, MemoryPageImageOptions options)
```

Domain-ID typed overload. See `MemoryPageImageOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
byte[] pagesImage(java.util.UUID id, String pageIndex)
```

UUID-typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
byte[] pagesImage(java.util.UUID id, String pageIndex, MemoryPageImageOptions options)
```

UUID-typed overload. See `MemoryPageImageOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

```java
byte[] pagesImage(java.util.UUID id, long pageIndex)
```

UUID+numeric-typed overload, no-filter convenience. Forwards an empty filter map to the `Raw` sibling.

```java
byte[] pagesImage(java.util.UUID id, long pageIndex, MemoryPageImageOptions options)
```

UUID+numeric-typed overload. See `MemoryPageImageOptions` for the available filter fields. Passing `null` is equivalent to an empty filter set.

[memories](../memories.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [MemoryId](../models/MemoryId.md)
- [MemoryPageImageOptions](../models/MemoryPageImageOptions.md)
