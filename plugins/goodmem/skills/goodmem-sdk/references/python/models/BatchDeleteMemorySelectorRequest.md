<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# BatchDeleteMemorySelectorRequest

A single delete selector: either memoryId or filterSelector

- `memory_id` (`str | None`, optional): Deletes one specific memory by UUID JSON: `memoryId`.
- `filter_selector` (`FilteredDeleteMemorySelectorRequest | None`, optional): Deletes a filtered set of memories within a specific space JSON: `filterSelector`.

[Python](../../python.md)

Related types — open only those used by your request:

- [FilteredDeleteMemorySelectorRequest](FilteredDeleteMemorySelectorRequest.md)
