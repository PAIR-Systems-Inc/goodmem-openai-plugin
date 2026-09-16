<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# memories.retrieve

```java
RetrieveMemoryStream retrieve(RetrieveMemoryRequest request)
```

Advanced semantic memory retrieval with JSON

Streams semantic retrieval results with full feature support including context items and embedder weight overrides, per-space filters, and request-level HNSW tuning.

AUTHORIZATION: Every requested space must grant LIST_MEMORY on that exact space and READ_MEMORY through DIRECT_MEMBERS_OF the space before retrieval begins.

```java
RetrieveMemoryStream retrieve(String message, SpaceId[] spaceIds)
```

Convenience overload: retrieves from the listed spaces with no
 per-embedder weight overrides or filter. Mirrors Python's
 `memories.retrieve(message=..., space_ids=[...])`. For
 post-processor tuning (`llmId`, `rerankerId`, \u2026)
 or per-space `ai.pairsys.goodmem.client.models.SpaceKey` weights,
 use `retrieve(RetrieveMemoryRequest)` with a fluent
 `RetrieveMemoryRequest.Builder` instead.

```java
RetrieveMemoryStream retrieve(String message, String[] spaceIds)
```

String-typed sibling of `retrieve(String, SpaceId...)` \u2014 accepts raw
 UUID strings instead of `SpaceId` handles. Each entry is parsed via
 `SpaceId.from`; otherwise identical to the typed sibling.

[memories](../memories.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [RetrieveMemoryRequest](../models/RetrieveMemoryRequest.md)
- [SpaceId](../models/SpaceId.md)
