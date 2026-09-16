<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.create

```java
Memory create(JsonMemoryCreationRequest request)
```

Create a new memory

Creates a new memory in a specified space and starts asynchronous processing. The memory begins in PENDING status while a background job performs chunking and embedding generation.

IDEMPOTENCY: If memoryId is omitted, the server generates a new UUID and retries are not idempotent. If the client supplies a stable memoryId, the operation behaves as create-if-absent: the first request creates the memory and subsequent retries return HTTP 409 Conflict (ALREADY_EXISTS) rather than creating duplicates. Returns INVALID_ARGUMENT if space_id, original_content, or content_type is missing or invalid. Returns NOT_FOUND if the specified space does not exist.

AUTHORIZATION: Requires CREATE_MEMORY on the containing space. Side effects include creating the memory record and enqueuing a background processing job.

```java
Memory create(SpaceId spaceId, java.nio.file.Path filePath)
```

Domain-ID typed sibling: same file-upload convenience as the String-typed
 overload, with the leading id parameter promoted to its typed handle so
 the compiler catches cross-resource mixups (e.g. passing a `MemoryId`
 where a `SpaceId` is expected). Forwards through
 `create(String, java.nio.file.Path)`; refer to that method's
 Javadoc for the `@return` / `@throws` contract.

```java
Memory create(String spaceId, java.nio.file.Path filePath)
```

Convenience overload: reads `filePath` from disk, base64-encodes
 the bytes, infers a content type via `java.nio.file.Files.probeContentType`,
 and POSTs a JSON request. For large files consider streaming the bytes
 yourself rather than reading them fully into memory.

[memories](../memories.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [JsonMemoryCreationRequest](../models/JsonMemoryCreationRequest.md)
- [SpaceId](../models/SpaceId.md)
