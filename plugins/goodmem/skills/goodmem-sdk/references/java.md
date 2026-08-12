# GoodMem Java SDK Reference

Official Java SDK: `ai.pairsys:goodmem-java` (Maven Central). OpenAI-style surface: every
operation is `client.<namespace>.<method>(...)` on a `Goodmem` (sync) or `AsyncGoodmem`
(async) instance. All facts below verified against version **0.1.7**.

## Dependency

Requires **JDK 21+**. Brings in OkHttp 4.12 and Jackson 2.18 (databind, jdk8, jsr310) transitively.

```xml
<!-- pom.xml -->
<dependency>
    <groupId>ai.pairsys</groupId>
    <artifactId>goodmem-java</artifactId>
    <version>0.1.7</version>
</dependency>
```

```kotlin
// build.gradle.kts
dependencies {
    implementation("ai.pairsys:goodmem-java:0.1.7")
}
```

## Client construction and auth

Read credentials from environment variables — never hardcode keys:

- `GOODMEM_BASE_URL` — server URL, e.g. `http://localhost:8080` (no `/v1` suffix; the SDK adds it)
- `GOODMEM_API_KEY` — API key starting with `gm_`, sent as the `x-api-key` header

```java
import ai.pairsys.goodmem.client.Goodmem;

try (Goodmem client = Goodmem.builder()
        .baseUrl(System.getenv("GOODMEM_BASE_URL"))
        .apiKey(System.getenv("GOODMEM_API_KEY"))
        .timeout(java.time.Duration.ofSeconds(60))   // optional; default 30s
        .build()) {
    // use client
}
```

Builder contract (`Goodmem.builder()` / `AsyncGoodmem.builder()` — identical):

| Method | Notes |
|---|---|
| `baseUrl(String)` | Required. Empty/invalid URL throws `IllegalArgumentException` at `build()`. |
| `apiKey(String)` | Optional only for the bootstrap endpoints `system.info()` / `system.init()`; every other call returns 401 → `AuthenticationException` without it. |
| `timeout(Duration)` | Connect/read/write timeout for the SDK-built OkHttp client (default 30s). Increase for RAG retrieval with LLM generation. **Incompatible with `httpClient(...)`** — combining them throws at `build()`. |
| `httpClient(OkHttpClient)` | BYO mode: pass a pre-configured `OkHttpClient` (interceptors, proxy, custom TLS, pool tuning). You own its lifecycle; `close()` is a no-op in this mode. Configure timeouts on your own client. |

`Goodmem` implements `AutoCloseable` — prefer try-with-resources. The SDK-built client
disables redirect following (a redirect would carry `x-api-key` across hosts); BYO clients
control their own redirect policy.

Namespaces on the client: `admin`, `apikeys`, `embedders`, `llms`, `memories`, `ocr`,
`ping`, `rerankers`, `spaces`, `system`, `users` (public final fields).

## SDK conventions

**Models are Java records** with Jackson annotations; camelCase wire names. Null fields are
omitted from payloads (`@JsonInclude(NON_NULL)`).

**Request builders.** Every request record exposes a nested `Builder`
(`XxxRequest.builder()....build()`) so you set only the fields you need instead of the long
positional constructor. `Map<String,String>` fields named `labels` get a singular
`label(key, value)` append setter.

**Typed IDs.** Resource ids are typed handles — `SpaceId`, `MemoryId`, `EmbedderId`,
`LlmId`, `RerankerId`, `ApiKeyId`, `UserId`, `ChunkId`, `ResultSetId` — each a record
wrapping the id string: `SpaceId.from(String)`, `SpaceId.from(UUID)`, `.asUuid()`,
`.toString()` returns the bare id, and JSON serializes as the bare string. Every
`get`/`delete`/`update` method accepts `String`, `java.util.UUID`, or the typed handle.

**oneOf models** expose static factories per variant so sibling fields can't be mis-set:
`ChunkingConfiguration.recursive(...)`, `RetrievedItem.memory(...)` /
`RetrievedItem.chunk(...)`. Constructing with zero or multiple variants throws
`IllegalArgumentException`.

**Typed list/get options.** List and get methods take a typed options record
(`SpaceListOptions`, `MemoryListOptions`, `MemoryGetOptions`, `EmbedderListOptions`,
`LLMListOptions`, `RerankerListOptions`, `MemoryPageListOptions`, `MemoryPageImageOptions`,
`UsersGetOptions`). A raw `Map<String,Object>` escape hatch exists as `listRaw(...)` /
`getRaw(...)`. Passing no options or `null` means no filter.

**Media types.** `ai.pairsys.goodmem.client.MediaTypes` holds common `contentType`
constants: `TEXT_PLAIN`, `TEXT_MARKDOWN`, `APPLICATION_JSON`, `APPLICATION_PDF`,
`IMAGE_PNG`, `IMAGE_JPEG`, etc.

## Spaces

Container for memories. Methods on `client.spaces`:

| Method | Returns |
|---|---|
| `create(SpaceCreationRequest)` | `Space` — auto-injects `Defaults.DEFAULT_CHUNKING_CONFIG` (recursive, 512-char chunks, 64 overlap, `KEEP_END`, character-measured) when `defaultChunkingConfig` is null |
| `get(id)` | `Space` |
| `list()` / `list(SpaceListOptions)` | `Page<Space>` (auto-paginating) |
| `update(id, UpdateSpaceRequest)` | `Space` |
| `delete(id)` | `void` |

`SpaceCreationRequest` components: `name`, `labels` (`Map<String,String>`),
`spaceEmbedders` (`List<SpaceEmbedderConfig>`), `publicRead` (`Boolean`), `ownerId`,
`defaultChunkingConfig` (`ChunkingConfiguration`), `spaceId` (client-supplied id, optional).
`SpaceEmbedderConfig` is `(EmbedderId embedderId, Double defaultRetrievalWeight)`.

`SpaceListOptions` components: `ownerId`, `nameFilter`, `maxResults`, `nextToken`,
`sortBy` (`SpacesListSortBy`: `CREATED_TIME`, `UPDATED_TIME`, `NAME`), `sortOrder`
(`SortOrder`: `ASCENDING`, `DESCENDING`), `label` map (flattened to `label.<key>=<value>`
on the wire; builder also has `label(k, v)`, `sortAscending()`, `sortDescending()`).

`UpdateSpaceRequest` components: `name`, `publicRead`, and `replaceLabels` XOR
`mergeLabels` (setting both throws `IllegalArgumentException`).

`Space` (response) components: `spaceId`, `name`, `labels`, `spaceEmbedders`
(`List<SpaceEmbedder>`), `createdAt`/`updatedAt` (epoch millis as `Long`), `ownerId`,
`createdById`, `updatedById`, `publicRead`, `defaultChunkingConfig`.

```java
import ai.pairsys.goodmem.client.models.*;

Space space = client.spaces.create(
    SpaceCreationRequest.builder()
        .name("support-kb")
        .label("env", "prod")
        .label("team", "support")
        .spaceEmbedders(java.util.List.of(
            new SpaceEmbedderConfig(embedder.embedderId(), null)))
        .publicRead(false)
        .build());

// Find spaces by label, newest first
Page<Space> page = client.spaces.list(
    SpaceListOptions.builder()
        .label("env", "prod")
        .sortBy(SpacesListSortBy.CREATED_TIME)
        .sortDescending()
        .maxResults(50)
        .build());
for (Space s : page) { /* iterates across ALL pages lazily */ }
```

## Memories

Methods on `client.memories`:

| Method | Returns |
|---|---|
| `create(JsonMemoryCreationRequest)` | `Memory` — fills `contentType="text/plain"` when `originalContent` is set with no content type |
| `create(spaceId, java.nio.file.Path)` | `Memory` — file-upload convenience: reads the file, base64-encodes, infers content type (`spaceId` as `String` or `SpaceId`; file is read fully into memory) |
| `get(id)` / `get(id, MemoryGetOptions)` | `Memory` |
| `list(spaceId)` / `list(spaceId, MemoryListOptions)` | `Page<Memory>` |
| `delete(id)` | `void` |
| `content(id)` | `byte[]` — raw original content |
| `pages(id[, MemoryPageListOptions])` | `Page<MemoryPageImage>` — page images extracted from documents |
| `pagesImage(id, pageIndex[, MemoryPageImageOptions])` | `byte[]` (`pageIndex` as `long` or `String`) |
| `batchCreate(JsonBatchMemoryCreationRequest)` | `BatchMemoryResponse` |
| `batchGet(BatchMemoryRetrievalRequest)` | `BatchMemoryResponse` |
| `batchDelete(BatchMemoryDeletionRequest)` | `BatchMemoryResponse` |
| `retrieve(...)` | `RetrieveMemoryStream` — see Retrieval below |

`JsonMemoryCreationRequest` components: `memoryId` (optional client-supplied id),
`spaceId`, `originalContent` (text), `originalContentB64` (base64 binary),
`originalContentRef`, `contentType`, `metadata` (`Map<String,Object>`), `chunkingConfig`,
`extractPageImages` (`Boolean`), `fileField`. Constructor enforces: exactly one of
`originalContent` / `originalContentB64`, and `originalContentB64` requires `contentType`
(violations throw `IllegalArgumentException`). The builder adds
`originalContentBytes(byte[])` which base64-encodes into `originalContentB64`, plus
`spaceId(String)` / `spaceId(UUID)` overloads.

`MemoryGetOptions`: `includeContent`, `includeProcessingHistory`.
`MemoryListOptions`: `includeContent`, `includeProcessingHistory`, `statusFilter`
(`MemoriesListStatusFilter`: `PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`), `filter`
(server-side filter expression), `maxResults`, `nextToken`, `sortBy` (`MemoriesListSortBy`:
`CREATED_AT`, `UPDATED_AT`, `CONTENT_TYPE`, `PROCESSING_STATUS`), `sortOrder`.

`Memory` (response) components: `memoryId`, `spaceId`, `originalContent` (`byte[]`, only
when requested), `originalContentLength`, `originalContentSha256`, `originalContentRef`,
`contentType`, `processingStatus` and `pageImageStatus` (`MemoryProcessingStatus` enum:
`PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`, `UNSPECIFIED`), `pageImageCount`,
`metadata`, `createdAt`, `updatedAt`, `createdById`, `updatedById`, `chunkingConfig`,
`processingHistory`. Embedding is asynchronous — a new memory starts `PENDING` and
becomes retrievable when `COMPLETED`.

```java
// Text memory with metadata
Memory m = client.memories.create(
    JsonMemoryCreationRequest.builder()
        .spaceId(space.spaceId())
        .originalContent("Customer reported login failures after the 2.3 upgrade.")
        .metadata(java.util.Map.of("source", "ticket-4812"))
        .build());

// Upload a PDF from disk
Memory doc = client.memories.create(space.spaceId(), java.nio.file.Path.of("report.pdf"));

// Batch-create several text memories in one call
BatchMemoryResponse batch = client.memories.batchCreate(
    JsonBatchMemoryCreationRequest.builder()
        .requests(java.util.List.of(
            JsonMemoryCreationRequest.builder()
                .spaceId(space.spaceId()).originalContent("note one").build(),
            JsonMemoryCreationRequest.builder()
                .spaceId(space.spaceId()).originalContent("note two").build()))
        .build());
for (BatchMemoryResult r : batch.results()) {
    if (!Boolean.TRUE.equals(r.success())) {
        System.err.println("item " + r.requestIndex() + " failed: " + r.error());
    }
}
```

Batch shapes: `BatchMemoryRetrievalRequest(memoryIds, includeContent,
includeProcessingHistory)`; `BatchMemoryDeletionRequest(requests)` where each
`BatchDeleteMemorySelectorRequest` is exactly one of `memoryId` or `filterSelector`
(`FilteredDeleteMemorySelectorRequest(spaceId, statusFilter, filter)` — deletes by
predicate). `BatchMemoryResponse` is `(List<BatchMemoryResult> results, Long totalDeleted)`;
each `BatchMemoryResult` has `success`, `memoryId`, `memory`, `error`, `requestIndex`,
`deletedCount`.

## Retrieval (semantic search, streaming)

`client.memories.retrieve(...)` performs streaming semantic search (NDJSON over
`POST /v1/memories:retrieve`) and returns a `RetrieveMemoryStream` — an
`Iterable<RetrieveMemoryEvent>` that is also `AutoCloseable`. **Always consume in
try-with-resources**; the iterator can be drained only once.

Overloads:

```java
RetrieveMemoryStream retrieve(RetrieveMemoryRequest request)
RetrieveMemoryStream retrieve(String message, SpaceId... spaceIds)  // simple form
RetrieveMemoryStream retrieve(String message, String... spaceIds)
```

`RetrieveMemoryRequest` components: `message`, `context` (`List<ContextItem>` — each
exactly one of `text` / `binary`), `spaceKeys` (`List<SpaceKey>`), `requestedSize`
(`Integer`, max memories), `outputBudget` (`TokenBudget(Integer tokens)` — LLM
completion-token cap), `fetchMemory` (default true), `fetchMemoryContent` (default false;
requires `fetchMemory`), `hnsw` (`HnswOptions` — advanced index tuning), `postProcessor`
(`PostProcessor`), `logging`. Builder conveniences: `spaceId(String|SpaceId)` single-space,
`spaceIds(...)` varargs/list multi-space, and `postProcessor(ChatPostProcessorConfig)`.

`SpaceKey` is `(SpaceId spaceId, List<EmbedderWeight> embedderWeights, String filter)` —
use `filter` for a per-space metadata filter expression and `embedderWeights`
(`EmbedderWeight(EmbedderId, Double)`) to override retrieval weights.

Each `RetrieveMemoryEvent` has exactly one non-null field:

| Field | Type | Meaning |
|---|---|---|
| `resultSetBoundary` | `ResultSetBoundary` | BEGIN/END marker for a result set (`kind`, `stageName`, `expectedItems`) |
| `retrievedItem` | `RetrievedItem` | one of `memory()` (a `Memory`) or `chunk()` (a `ChunkReference`) |
| `abstractReply` | `AbstractReply` | generated RAG answer: `text`, `relevanceScore`, `resultSetId` |
| `memoryDefinition` | `Memory` | memory record referenced by streamed chunks |
| `status` | `GoodMemStatus` | non-fatal warning (`code`, `message`, `details`); operation continues |

`ChunkReference` carries `chunk` (`MemoryChunkResponse` with `chunkText`, `memoryId`,
`chunkSequenceNumber`, `startOffset`, `endOffset`, ...), `relevanceScore`, `memoryIndex`,
`resultSetId`.

```java
// Plain retrieval
try (RetrieveMemoryStream events =
        client.memories.retrieve("login failures after upgrade", space.spaceId())) {
    for (RetrieveMemoryEvent evt : events) {
        if (evt.retrievedItem() != null && evt.retrievedItem().chunk() != null) {
            System.out.println(evt.retrievedItem().chunk().chunk().chunkText());
        }
    }
}
```

### RAG with the built-in chat post-processor

`ai.pairsys.goodmem.client.ChatPostProcessorConfig` is a validated, typed config for the
built-in RAG pipeline (retrieve → rerank → generate). Fields: `llmId`, `rerankerId`,
`llmTemp` (validated `[0.0, 2.0]`), `genTokenBudget`, `relevanceThreshold`, `maxResults`,
`prompt`, `sysPrompt`, `chronologicalResort`. Setting an LLM-bound field (`llmTemp`,
`genTokenBudget`, `prompt`, `sysPrompt`) without `llmId`, or `relevanceThreshold` without
`rerankerId`, throws `IllegalArgumentException` at build time. Id setters accept `String`,
`UUID`, or the typed handle.

```java
import ai.pairsys.goodmem.client.ChatPostProcessorConfig;

RetrieveMemoryRequest req = RetrieveMemoryRequest.builder()
    .message("Summarize what we know about the 2.3 login regression")
    .spaceId(space.spaceId())
    .requestedSize(10)
    .postProcessor(ChatPostProcessorConfig.builder()
        .llmId(llm.llmId())
        .rerankerId(reranker.rerankerId())
        .relevanceThreshold(0.5)
        .llmTemp(0.2)
        .genTokenBudget(2048L)
        .build())
    .build();

try (RetrieveMemoryStream events = client.memories.retrieve(req)) {
    for (RetrieveMemoryEvent evt : events) {
        if (evt.abstractReply() != null) {
            System.out.println(evt.abstractReply().text());   // generated answer
        }
    }
}
```

For a custom post-processor, use `new PostProcessor(fullyQualifiedFactoryName, configMap)`
directly.

## Embedders

Methods on `client.embedders`:

| Method | Returns |
|---|---|
| `create(EmbedderCreationRequest)` | `EmbedderResponse` |
| `create(EmbedderCreationRequest, String apiKey)` | `EmbedderResponse` — converts the raw provider key into structured credentials |
| `get(id)` | `EmbedderResponse` |
| `list()` / `list(EmbedderListOptions)` | `List<EmbedderResponse>` (plain list, not paged) |
| `update(id, UpdateEmbedderRequest)` | `EmbedderResponse` |
| `delete(id)` | `void` |

`create` runs registry auto-fill: when `modelIdentifier` matches the bundled model
registry, null fields are filled — `providerType`, `dimensionality`, `maxSequenceLength`,
`supportedModalities`, endpoint URL inference; `distributionType` defaults to `DENSE`.
Fields you set explicitly always win. If the resolved endpoint is a known SaaS host and no
credentials are present, the SDK throws `IllegalArgumentException` synchronously (before
any HTTP call).

`EmbedderCreationRequest` components: `displayName`, `description`, `providerType`
(`ProviderType`: `OPENAI`, `VLLM`, `TEI`, `LLAMA_CPP`, `VOYAGE`, `COHERE`, `JINA`),
`endpointUrl`, `apiPath`, `modelIdentifier`, `dimensionality`, `distributionType`
(`DENSE`/`SPARSE`), `maxSequenceLength`, `supportedModalities` (`Modality`: `TEXT`,
`IMAGE`, `AUDIO`, `VIDEO`), `credentials` (`EndpointAuthentication`), `labels`, `version`,
`monitoringEndpoint`, `ownerId`, `embedderId`.

`EmbedderListOptions`: `ownerId`, `providerType`, `label` map.

```java
// Provider API key from the environment — registry fills the rest
EmbedderResponse embedder = client.embedders.create(
    EmbedderCreationRequest.builder()
        .displayName("openai-large")
        .modelIdentifier("text-embedding-3-large")
        .build(),
    System.getenv("OPENAI_API_KEY"));
```

For self-hosted endpoints (vLLM, TEI, llama.cpp), set `providerType`, `endpointUrl`, and
`modelIdentifier` explicitly; no credentials required for non-SaaS hosts.

## LLMs

Generation-time models used by the chat post-processor. Methods on `client.llms`:

| Method | Returns |
|---|---|
| `create(LLMCreationRequest)` / `create(LLMCreationRequest, String apiKey)` | `CreateLLMResponse` — `(LLMResponse llm, List<GoodMemStatus> statuses)`; registry auto-fill (including `maxContextLength`) + credential check like embedders |
| `get(id)` | `LLMResponse` |
| `list()` / `list(LLMListOptions)` | `List<LLMResponse>` |
| `update(id, LLMUpdateRequest)` | `LLMResponse` |
| `delete(id)` | `void` |

`LLMCreationRequest` components: `displayName`, `description`, `providerType`
(`LLMProviderType`: `OPENAI`, `LITELLM_PROXY`, `OPEN_ROUTER`, `VLLM`, `OLLAMA`,
`LLAMA_CPP`, `CUSTOM_OPENAI_COMPATIBLE`), `endpointUrl`, `apiPath`, `modelIdentifier`,
`supportedModalities`, `credentials`, `labels`, `version`, `monitoringEndpoint`,
`capabilities` (`LLMCapabilities`), `defaultSamplingParams` (`LLMSamplingParams`),
`maxContextLength`, `clientConfig` (`Map<String,Object>`), `ownerId`, `llmId`.

```java
CreateLLMResponse created = client.llms.create(
    LLMCreationRequest.builder()
        .displayName("gpt-4o")
        .modelIdentifier("gpt-4o")
        .build(),
    System.getenv("OPENAI_API_KEY"));
LlmId llmId = created.llm().llmId();
```

## Rerankers

Re-score retrieval hits. Methods on `client.rerankers` mirror embedders:
`create(RerankerCreationRequest[, String apiKey])` → `RerankerResponse`, `get(id)`,
`list([RerankerListOptions])` → `List<RerankerResponse>`,
`update(id, UpdateRerankerRequest)`, `delete(id)`. `RerankerCreationRequest` components:
`displayName`, `description`, `providerType` (`ProviderType`), `endpointUrl`, `apiPath`,
`modelIdentifier`, `supportedModalities`, `credentials`, `labels`, `version`,
`monitoringEndpoint`, `ownerId`, `rerankerId`. Same registry auto-fill and credential
check as embedders.

## API keys

Methods on `client.apikeys`:

| Method | Returns |
|---|---|
| `create(CreateApiKeyRequest)` | `CreateApiKeyResponse` — `(ApiKeyResponse apiKeyMetadata, String rawApiKey)`. `rawApiKey` is shown **only once**; `toString()` redacts it |
| `list()` | `List<ApiKeyResponse>` |
| `update(id, UpdateApiKeyRequest)` | `ApiKeyResponse` |
| `delete(id)` | `void` |

`CreateApiKeyRequest` components: `labels`, `expiresAt` (`Long` epoch millis; builder also
accepts `java.time.Instant`), `apiKeyId`. `UpdateApiKeyRequest`: `status`, `replaceLabels`
XOR `mergeLabels`. `ApiKeyResponse` exposes `apiKeyId`, `userId`, `keyPrefix`, `status`,
`labels`, `expiresAt`, `lastUsedAt`, audit fields.

```java
CreateApiKeyResponse key = client.apikeys.create(
    CreateApiKeyRequest.builder()
        .label("scope", "ci")
        .expiresAt(java.time.Instant.now().plus(java.time.Duration.ofDays(30)))
        .build());
// Store key.rawApiKey() securely now — it cannot be fetched again.
```

## Users and system

- `client.users.me()` → `UserResponse` (`userId`, `email`, `displayName`, `username`,
  `createdAt`, `updatedAt`)
- `client.users.get(UsersGetOptions)` → `UserResponse` — exactly one of
  `UsersGetOptions.builder().id(...)` or `.email(...)`; setting both/neither throws
  `IllegalArgumentException`
- `client.system.info()` → `SystemInfoResponse` (`version`, `major`, `minor`, `patch`,
  `gitCommit`, `buildTime`, `capabilities` map) — works without an API key; use it as a
  connectivity check
- `client.system.init()` → `SystemInitResponse` — first-boot initialization that creates
  the root user/key; also callable without a key

## OCR (GoodMem Enterprise)

**Requires GoodMem Enterprise** — on non-Enterprise servers OCR calls fail. Layout-aware
text extraction from PDFs and images, separate from memory ingestion:

- `client.ocr.document(OcrDocumentRequest)` → `OcrDocumentResponse`
- `client.ocr.document(java.nio.file.Path)` — reads and base64-encodes the file; server
  auto-detects the format

`OcrDocumentRequest` components: `content` (base64 document bytes), `format`
(`OcrInputFormat`: `AUTO`, `PDF`, `TIFF`, `PNG`, `JPEG`, `BMP`), `includeRawJson`,
`includeMarkdown`, `startPage`, `endPage` (inclusive page range). Response:
`detectedFormat`, `pageCount`, `pages` (`List<OcrPageResult>`), `timings`.

## Ping

Endpoint health probes for registered embedders/LLMs/rerankers:
`client.ping.once(PingOnceRequest)` → `PingResult` (`ok`, `httpStatus`, `rttMs`,
`errorMessage`, `timing`); `client.ping.stream(PingStreamRequest)` → `PingStream`, an
iterable/closeable stream of `PingEvent` — consume in try-with-resources like
`RetrieveMemoryStream`.

## Admin

Server lifecycle operations on `client.admin` (admin permissions required):
`drain(AdminDrainRequest)`, `licenseReload()`, `backgroundJobsPurge(AdminPurgeJobsRequest)`,
and RetrieveMemory log-policy CRUD (`retrieveMemoryLogPoliciesCreate/Get/List/Delete`).

## Pagination

`ai.pairsys.goodmem.client.Page<T>` is returned by `spaces.list`, `memories.list`,
`memories.pages` (embedders/llms/rerankers/apikeys return plain `List`s):

- `items()` → `List<T>` current page only
- `hasMore()` / `nextToken()` — continuation state
- `next()` → `Page<T>` — fetches the next page; throws `NoSuchElementException` when exhausted
- `iterator()` — **lazy cross-page iteration over everything**; usable once
- `iterator(long maxItems)` — capped variant

```java
// Idiomatic: for-each transparently walks every page
for (Memory m : client.memories.list(space.spaceId())) {
    System.out.println(m.memoryId() + " " + m.processingStatus());
}
```

## Async client

`AsyncGoodmem` mirrors `Goodmem` exactly (same builder, namespaces, close semantics);
every method returns `CompletableFuture<T>`. List endpoints return
`CompletableFuture<AsyncPage<T>>` — `AsyncPage` exposes `items()`, `hasMore()`,
`nextToken()` synchronously and `next()` as `CompletableFuture<AsyncPage<T>>`
(intentionally not `Iterable`; chain with `thenCompose`). `memories.retrieve` returns
`CompletableFuture<RetrieveMemoryStream>` — the future completes when stream headers
arrive; consume the stream as usual.

```java
import ai.pairsys.goodmem.client.AsyncGoodmem;

try (AsyncGoodmem client = AsyncGoodmem.builder()
        .baseUrl(System.getenv("GOODMEM_BASE_URL"))
        .apiKey(System.getenv("GOODMEM_API_KEY"))
        .build()) {

    client.memories.retrieve(RetrieveMemoryRequest.builder()
            .message("deployment checklist")
            .spaceId(spaceId)
            .build())
        .thenAccept(events -> {
            try (events) {
                for (RetrieveMemoryEvent e : events) {
                    if (e.abstractReply() != null) System.out.println(e.abstractReply().text());
                }
            }
        })
        .join();
}
```

Async errors complete the future exceptionally with the same typed exceptions, wrapped in
`CompletionException` — unwrap with `ex.getCause()`. Client-side validation errors (null
required args, credential check) throw synchronously before the call is scheduled.

## Error handling

All exceptions are unchecked, rooted at `ai.pairsys.goodmem.client.errors.GoodmemException`:

| Exception | Trigger |
|---|---|
| `GoodmemException` | base; also wraps file-I/O failures in conveniences |
| `NetworkException` | transport failure (extends `GoodmemException`) |
| `ApiException` | any HTTP 4xx/5xx — `getStatusCode()`, `getBody()` |
| `BadRequestException` | 400 |
| `AuthenticationException` | 401 — missing/invalid `GOODMEM_API_KEY` |
| `PermissionDeniedException` | 403 |
| `NotFoundException` | 404 |
| `ConflictException` | 409 |
| `UnprocessableEntityException` | 422 |
| `RateLimitException` | 429 — `getRetryAfterSeconds()` (nullable `Long`) |
| `InternalServerException` | 5xx |

`IllegalArgumentException` signals client-side misuse (null required args, invalid oneOf
combinations, out-of-range values like `llmTemp > 2.0`) and is thrown before any request.

```java
import ai.pairsys.goodmem.client.errors.*;

try {
    Memory m = client.memories.get(memoryId);
} catch (NotFoundException e) {
    // handle missing memory
} catch (RateLimitException e) {
    Long retryAfter = e.getRetryAfterSeconds();  // may be null
} catch (ApiException e) {
    System.err.println("HTTP " + e.getStatusCode() + ": " + e.getBody());
}
```

## End-to-end example

```java
import ai.pairsys.goodmem.client.Goodmem;
import ai.pairsys.goodmem.client.RetrieveMemoryStream;
import ai.pairsys.goodmem.client.models.*;

public class GoodMemQuickstart {
    public static void main(String[] args) {
        try (Goodmem client = Goodmem.builder()
                .baseUrl(System.getenv("GOODMEM_BASE_URL"))
                .apiKey(System.getenv("GOODMEM_API_KEY"))
                .build()) {

            EmbedderResponse embedder = client.embedders.create(
                EmbedderCreationRequest.builder()
                    .displayName("default-embedder")
                    .modelIdentifier("text-embedding-3-small")
                    .build(),
                System.getenv("OPENAI_API_KEY"));

            Space space = client.spaces.create(
                SpaceCreationRequest.builder()
                    .name("project-notes")
                    .spaceEmbedders(java.util.List.of(
                        new SpaceEmbedderConfig(embedder.embedderId(), null)))
                    .build());

            client.memories.create(JsonMemoryCreationRequest.builder()
                .spaceId(space.spaceId())
                .originalContent("The staging cluster runs Kubernetes 1.29.")
                .build());

            try (RetrieveMemoryStream events =
                    client.memories.retrieve("which Kubernetes version?", space.spaceId())) {
                for (RetrieveMemoryEvent evt : events) {
                    if (evt.retrievedItem() != null && evt.retrievedItem().chunk() != null) {
                        System.out.println(evt.retrievedItem().chunk().chunk().chunkText());
                    }
                }
            }
        }
    }
}
```

## Framework integrations

Higher-level bindings exist for LangChain4j (`goodmem-langchain4j`) and Spring AI
(`goodmem-spring-ai`); both are community-published under a maintainer's personal Maven
groupId (`io.github.bashareid`, version 0.1.0) and configure the connection from the same
`GOODMEM_BASE_URL` / `GOODMEM_API_KEY` environment variables. For direct application code,
prefer `ai.pairsys:goodmem-java`.
