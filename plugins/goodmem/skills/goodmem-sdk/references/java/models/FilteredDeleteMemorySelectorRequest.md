<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# FilteredDeleteMemorySelectorRequest

Filtered selector scoped to a specific space

- `spaceId` (`SpaceId`): Space ID scope for the filtered delete. Typed wrapper `SpaceId`; build from a raw string with `SpaceId.from(String)`.
- `statusFilter` (`FilteredDeleteMemorySelectorRequestStatusFilter`): Optional processing status filter (PENDING, PROCESSING, COMPLETED, FAILED). Typed enum `FilteredDeleteMemorySelectorRequestStatusFilter`; unknown server values fail Jackson deserialization loudly.
- `filter` (`String`): Optional metadata filter expression

[Java](../../java.md)

Related types — open only those used by your request:

- [FilteredDeleteMemorySelectorRequestStatusFilter](FilteredDeleteMemorySelectorRequestStatusFilter.md)
- [SpaceId](SpaceId.md)
