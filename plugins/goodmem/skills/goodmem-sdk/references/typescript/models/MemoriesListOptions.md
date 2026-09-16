<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# MemoriesListOptions

- `includeContent` (`boolean`, optional): Whether to include the original content in the response (defaults to false).
- `includeProcessingHistory` (`boolean`, optional): Whether to include background job processing history in the response (defaults to false).
- `statusFilter` (`"PENDING" | "PROCESSING" | "COMPLETED" | "FAILED"`, optional): Filter memories by processing status (PENDING, PROCESSING, COMPLETED, FAILED).
- `filter` (`string`, optional): Optional metadata filter expression for list results
- `maxResults` (`number`, optional): Maximum number of results per page (defaults to 50, clamped to [1, 500]).
- `nextToken` (`string`, optional): Opaque pagination token for the next page. URL-safe Base64 without padding; do not parse or construct it.
- `sortBy` (`"created_at" | "updated_at" | "content_type" | "processing_status"`, optional): Field to sort by (e.g., 'created_at').
- `sortOrder` (`SortOrder`, optional): Sort direction (ASCENDING or DESCENDING).

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [SortOrder](SortOrder.md)
