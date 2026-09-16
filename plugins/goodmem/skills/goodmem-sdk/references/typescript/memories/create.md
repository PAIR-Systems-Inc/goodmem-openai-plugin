<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# memories.create

Creates a new memory in a specified space and starts asynchronous processing. The memory begins in PENDING status while a background job performs chunking and embedding generation.

IDEMPOTENCY: If memoryId is omitted, the server generates a new UUID and retries are not idempotent. If the client supplies a stable memoryId, the operation behaves as create-if-absent: the first request creates the memory and subsequent retries return HTTP 409 Conflict (ALREADY_EXISTS) rather than creating duplicates. Returns INVALID_ARGUMENT if space_id, original_content, or content_type is missing or invalid. Returns NOT_FOUND if the specified space does not exist.

AUTHORIZATION: Requires CREATE_MEMORY on the containing space. Side effects include creating the memory record and enqueuing a background processing job.

```ts
create(request: MemoryCreateRequest, requestOptions?: RequestOptions): Promise<MemoryResponseShape>
```

[memories](../memories.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [MemoryCreateRequest](../models/MemoryCreateRequest.md)
- [RequestOptions](../models/RequestOptions.md)
