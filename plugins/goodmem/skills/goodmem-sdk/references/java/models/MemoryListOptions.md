<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# MemoryListOptions

Typed query options for `client.memories.list`.

 Every field is optional; null values are omitted from the wire request.
 Construct via the fluent `Builder`:

```java
 MemoryListOptions opts = MemoryListOptions.builder()
     .includeContent(true)
     .build();

```

- `includeContent` (`Boolean`): Whether to include the original content in the response (defaults to false).
- `includeProcessingHistory` (`Boolean`): Whether to include background job processing history in the response (defaults to false).
- `statusFilter` (`MemoriesListStatusFilter`): Filter memories by processing status (PENDING, PROCESSING, COMPLETED, FAILED).
- `filter` (`String`): Optional metadata filter expression for list results
- `maxResults` (`Integer`): Maximum number of results per page (defaults to 50, clamped to [1, 500]).
- `nextToken` (`String`): Opaque pagination token for the next page. URL-safe Base64 without padding; do not parse or construct it.
- `sortBy` (`MemoriesListSortBy`): Field to sort by (e.g., 'created_at').
- `sortOrder` (`SortOrder`): Sort direction (ASCENDING or DESCENDING).

[Java](../../java.md)

Related types — open only those used by your request:

- [MemoriesListSortBy](MemoriesListSortBy.md)
- [MemoriesListStatusFilter](MemoriesListStatusFilter.md)
- [SortOrder](SortOrder.md)
