# GoodMem Python SDK Reference

Verified against `goodmem` 0.1.28 (PyPI). Requires Python >= 3.10; depends on
`httpx`, `pydantic`, `python-dateutil`, `typing-extensions`.

```bash
pip install goodmem
```

Package metadata for debugging version mismatches:

```python
import goodmem
goodmem.__version__                  # SDK version, e.g. "0.1.28"
goodmem.__based_on_goodmem_commit__  # server commit the SDK was generated from
```

## Client construction and auth

`Goodmem` (sync) and `AsyncGoodmem` (async) expose every operation as
`client.<namespace>.<method>(...)`. **All API methods take keyword-only
arguments.** The SDK does not read environment variables itself — read them in
your code and pass them in. The conventional variables are `GOODMEM_BASE_URL`
and `GOODMEM_API_KEY`. Never hardcode keys.

```python
import os
from goodmem import Goodmem, AsyncGoodmem

client = Goodmem(
    base_url=os.environ["GOODMEM_BASE_URL"],  # no /v1 suffix
    api_key=os.environ["GOODMEM_API_KEY"],    # gm_..., sent as x-api-key header
)

# Recommended: context manager closes the connection pool
with Goodmem(base_url=os.environ["GOODMEM_BASE_URL"],
             api_key=os.environ["GOODMEM_API_KEY"]) as client:
    ...

async with AsyncGoodmem(base_url=os.environ["GOODMEM_BASE_URL"],
                        api_key=os.environ["GOODMEM_API_KEY"]) as client:
    ...
```

Two mutually exclusive construction modes:

1. **Simple mode** — `Goodmem(base_url, api_key=None, *, timeout=30.0, verify=True)`
   - `timeout` (float | `httpx.Timeout`): default 30.0 s. Raise it for RAG
     retrieval with LLM generation, which can take longer.
   - `verify` (bool | str): `True` uses system CAs, `False` skips TLS
     verification, a path string points at a CA bundle.
2. **Full-control mode** — `Goodmem(http_client=httpx.Client(base_url=...,
   headers={"x-api-key": ...}))` (`httpx.AsyncClient` for `AsyncGoodmem`).
   When `http_client` is given, `base_url`/`api_key`/`timeout`/`verify` must
   not be set — configure them on the httpx client.

`api_key=None` is allowed only for the unauthenticated bootstrap endpoints
(`system.info`, `system.init`); everything else returns 401.

Namespaces: `client.spaces`, `client.memories`, `client.embedders`,
`client.rerankers`, `client.llms`, `client.apikeys`, `client.users`,
`client.system`, `client.ocr`, `client.admin`, `client.ping`.
`AsyncGoodmem` mirrors every method 1:1 — add `await` (and `async for` /
`async with` where noted). Both clients also have `.close()`
(`await client.close()` for async).

## Error handling

All SDK exceptions inherit from `goodmem.errors.GoodMemError`.
`NetworkError` wraps every transport failure (DNS, connect, timeout,
mid-stream disconnect). HTTP errors inherit from `APIError`, which carries
`.status_code` (int), `.body` (str | None), and `.response`
(`httpx.Response | None`).

| Status | Exception |
|--------|-----------|
| 400 | `BadRequestError` |
| 401 | `AuthenticationError` |
| 403 | `PermissionDeniedError` |
| 404 | `NotFoundError` |
| 409 | `ConflictError` (e.g. duplicate resource / client-supplied UUID already in use) |
| 422 | `UnprocessableEntityError` |
| 429 | `RateLimitError` |
| 5xx | `InternalServerError` |

```python
from goodmem.errors import GoodMemError, NotFoundError, ConflictError

try:
    space = client.spaces.get(id=space_id)
except NotFoundError:
    space = None
except GoodMemError as e:   # catches HTTP + network errors in one branch
    raise
```

All exceptions are importable from `goodmem.errors` and also re-exported at
the top level (`from goodmem import NotFoundError`).

## Pagination

List endpoints that page (`spaces.list`, `memories.list`, `memories.pages`)
return `Page[T]` (`AsyncPage[T]` on the async client) with:

- `.data` — items of the current page (list of pydantic models)
- `.next_token` — opaque token for the next page, or `None`
- iteration — `for item in page` auto-fetches all subsequent pages
- `.iter_pages()` — yields `Page` objects one at a time

Common paging keywords: `page_size` (per-request size; for `memories.list`
the server default is 50, clamped to [1, 500]), `max_items` (cap on total
items across all pages), `next_token` (resume from a saved token).

```python
# Iterate everything (auto-paginates)
for space in client.spaces.list():
    print(space.space_id, space.name)

# First page only, then resume later
page = client.spaces.list(page_size=10)
token = page.next_token
for space in client.spaces.list(next_token=token):
    ...

# Async iteration
async for mem in await client.memories.list(space_id=sid):
    ...
```

`embedders.list`, `rerankers.list`, `llms.list`, and `apikeys.list` return
plain lists (no pagination).

## Spaces

A space is a container of memories bound to one or more embedders.

```python
spaces.create(*, name: str, space_embedders: list[SpaceEmbedderConfig],
              default_chunking_config: ChunkingConfiguration = <recursive 512/64>,
              labels: dict[str, str] | None = None, owner_id: str | None = None,
              public_read: bool | None = None, space_id: str | None = None) -> Space
spaces.get(*, id: str) -> Space
spaces.list(*, label=None, name_filter=None, owner_id=None,
            sort_by=None,        # 'created_time' | 'updated_time' | 'name'
            sort_order=None,     # 'ASCENDING' | 'DESCENDING'
            page_size=None, max_items=None, next_token=None) -> Page[Space]
spaces.update(*, id: str, request: UpdateSpaceRequest | dict) -> Space
spaces.delete(*, id: str) -> None
```

- `space_embedders` requires at least one entry. Each entry is a
  `SpaceEmbedderConfig` (importable from `goodmem.models`) or equivalent dict
  with `embedder_id` (required) and optional `default_retrieval_weight`
  (float).
- `default_chunking_config` defaults to recursive chunking
  (`chunkSize=512`, `chunkOverlap=64`, `keepStrategy="KEEP_END"`,
  `lengthMeasurement="CHARACTER_COUNT"`); the same default is exported as
  `goodmem.DEFAULT_CHUNKING_CONFIG`. Per-memory `chunking_config` overrides it.
- `space_id` enables idempotent creation (409 `ConflictError` if taken).
- `name_filter` on list uses glob patterns.
- `UpdateSpaceRequest` fields: `name`, `public_read`, `replace_labels`,
  `merge_labels`. A plain dict with the same keys also works.

`Space` model fields (snake_case attributes): `space_id`, `name`, `labels`,
`space_embedders`, `owner_id`, `public_read`, `default_chunking_config`,
`created_at`, `updated_at`, `created_by_id`, `updated_by_id`.

```python
embedder = client.embedders.list()[0]
space = client.spaces.create(
    name="project-docs",
    space_embedders=[{"embedder_id": embedder.embedder_id}],
    labels={"env": "prod"},
)
client.spaces.update(id=space.space_id, request={"merge_labels": {"team": "ml"}})
```

## Memories

### Create (single)

```python
memories.create(*, space_id: str,
                original_content: str | None = None,       # plain text
                original_content_b64: str | None = None,   # base64 binary
                file_path: str | None = None,              # SDK uploads a local file
                content_type: str | None = None,
                metadata: dict[str, Any] | None = None,
                chunking_config: ChunkingConfiguration | None = None,
                extract_page_images: bool | None = None,
                memory_id: str | None = None,
                original_content_ref: str | None = None) -> Memory
```

- Exactly one of `original_content`, `original_content_b64`, `file_path`.
- `content_type` is auto-inferred: `text/plain` for `original_content`, from
  the file extension for `file_path`; required with `original_content_b64`.
- `metadata` is any JSON-serializable dict (nesting allowed) — used later by
  filter expressions.
- `original_content_ref` is a metadata-only pointer to an external location;
  GoodMem does **not** download from it.
- `extract_page_images` hints page-image extraction for eligible document
  types (e.g. PDFs); the images then appear under `memories.pages`.

### Ingestion is asynchronous — poll before retrieving

`create` returns with `processing_status="PENDING"`. Chunking/embedding runs
in the background. Poll until `COMPLETED` (or `FAILED`) before relying on
retrieval:

```python
import time

memory = client.memories.create(space_id=space_id, file_path="./handbook.pdf")

deadline = time.monotonic() + 120
while time.monotonic() < deadline:
    m = client.memories.get(id=memory.memory_id)
    if m.processing_status == "COMPLETED":
        break
    if m.processing_status == "FAILED":
        detail = client.memories.get(id=memory.memory_id,
                                     include_processing_history=True)
        raise RuntimeError(f"ingestion failed: {detail.processing_history}")
    time.sleep(2)
```

### Get / list / content / delete

```python
memories.get(*, id: str, include_content: bool | None = None,
             include_processing_history: bool | None = None) -> Memory
memories.list(*, space_id: str, filter: str | None = None,
              include_content=None, include_processing_history=None,
              sort_by=None,   # 'created_at' | 'updated_at' | 'content_type' | 'processing_status'
              sort_order=None,  # 'ASCENDING' | 'DESCENDING'
              status_filter=None,  # 'PENDING' | 'PROCESSING' | 'COMPLETED' | 'FAILED'
              page_size=None, max_items=None, next_token=None) -> Page[Memory]
memories.content(*, id: str) -> bytes     # raw original content download
memories.delete(*, id: str) -> None
```

`Memory` model fields: `memory_id`, `space_id`, `content_type`,
`processing_status`, `metadata`, `original_content` (bytes, only when
requested), `original_content_length`, `original_content_sha256`,
`original_content_ref`, `chunking_config`, `page_image_status`,
`page_image_count`, `processing_history` (only when requested),
`created_at`, `updated_at`, `created_by_id`, `updated_by_id`.

```python
# All failed ingestions in a space
for m in client.memories.list(space_id=space_id, status_filter="FAILED"):
    print(m.memory_id, m.content_type)

# Metadata-filtered listing (see "Metadata filter expressions" below)
page = client.memories.list(
    space_id=space_id,
    filter="CAST(val('$.category') AS TEXT) = 'runbook'",
    page_size=50,
)
```

### Batch operations

```python
from goodmem import MemoryCreationRequest  # also: from goodmem.api.memories import ...

memories.batch_create(*, requests: list[MemoryCreationRequest]) -> BatchMemoryResponse
memories.batch_get(*, memory_ids: list[str], include_content=None,
                   include_processing_history=None) -> BatchMemoryResponse
memories.batch_delete(*, requests: list[BatchDeleteMemorySelectorRequest]) -> BatchMemoryResponse
```

- `MemoryCreationRequest` fields mirror `memories.create` (text via
  `original_content`, binary via `original_content_b64` + `content_type`,
  plus `metadata`, `chunking_config`, `extract_page_images`, `memory_id`,
  `original_content_ref`). `content_type` is auto-inferred for text.
  There is no `file_path` convenience in batch requests.
- `BatchDeleteMemorySelectorRequest` (import from `goodmem.models` or
  `goodmem.types`) selects either one `memory_id` or a `filter_selector`
  (`FilteredDeleteMemorySelectorRequest`: required `space_id`, plus at least
  one of `status_filter`, `filter`).
- `BatchMemoryResponse.results` is a list of `BatchMemoryResult` with
  `success` (bool), `memory_id`, `memory`, `error`, `request_index`,
  `deleted_count`; `total_deleted` sums deletions.

```python
result = client.memories.batch_create(requests=[
    MemoryCreationRequest(space_id=space_id, original_content="First note",
                          metadata={"kind": "note"}),
    MemoryCreationRequest(space_id=space_id, original_content="Second note",
                          metadata={"kind": "note"}),
])
for r in result.results:
    if not r.success:
        print("failed:", r.request_index, r.error)

# Delete every FAILED memory in a space
client.memories.batch_delete(requests=[
    {"filter_selector": {"space_id": space_id, "status_filter": "FAILED"}},
])
```

### Page images (documents)

For memories ingested with `extract_page_images=True` (eligible types such as
PDFs):

```python
memories.pages(*, id: str, start_page_index=None, end_page_index=None,
               dpi=None, content_type=None,
               max_results=None, next_token=None) -> Page[MemoryPageImage]
memories.pages_image(*, id: str, page_index: int,
                     dpi=None, content_type=None) -> bytes
```

`MemoryPageImage` fields include `memory_id`, `page_index` (0-based), `dpi`,
`content_type`, `image_content_length`, `image_content_sha256`.

## Retrieval

```python
memories.retrieve(*, message: str,
    space_ids: list[str] | None = None,     # simple scoping by space UUIDs
    space_keys: list[SpaceKey] | None = None,  # per-space filter + embedder weights
    requested_size: int | None = None,      # max memories to retrieve
    fetch_memory: bool | None = None,       # stream memory-definition events
    fetch_memory_content: bool | None = None,  # include raw content (needs fetch_memory)
    context: list[ContextItem] | None = None,  # extra query context (text or binary)
    # post-processing (activated by llm_id and/or reranker_id):
    reranker_id: str | None = None,
    llm_id: str | None = None,
    llm_temp: float | None = None,          # 0.0-2.0, server default 0.3
    gen_token_budget: int | None = None,    # server default 512
    output_budget: TokenBudget | None = None,  # soft completion-token cap, e.g. {"tokens": 800}
    prompt: str | None = None, sys_prompt: str | None = None,
    max_results: int | None = None,         # server default 10 (post-processing only)
    relevance_threshold: float | None = None,  # reranker only
    chronological_resort: bool | None = None,  # server default True (post-processing only)
    post_processor: PostProcessor | None = None,  # raw nested config, advanced
    hnsw: HnswOptions | None = None, logging: LoggingOptions | None = None,
    stream: bool = True,
) -> RetrieveMemoryStream | list[RetrieveMemoryEvent]
```

Scoping: pass `space_ids` (list of UUID strings) for the common case. For
per-space control use `space_keys` — each `SpaceKey` dict/model has
`space_id` (required), optional `filter` (metadata filter expression applied
to that space), and optional `embedder_weights`
(list of `{"embedder_id": ..., "weight": float}`).

### Streaming (default)

The server streams NDJSON events. With `stream=True` (default) the sync
client returns a `RetrieveMemoryStream` context manager:

```python
with client.memories.retrieve(message="how do I rotate keys?",
                              space_ids=[space_id]) as stream:
    for event in stream:
        if event.retrieved_item:                      # a matched chunk
            ref = event.retrieved_item.chunk          # ChunkReference
            print(ref.relevance_score, ref.chunk.chunk_text)
        elif event.abstract_reply:                    # LLM-generated text (llm_id set)
            print(event.abstract_reply.text)
        elif event.status:                            # server-side warnings/errors
            print(event.status.code, event.status.message)
```

Each `RetrieveMemoryEvent` populates one of: `retrieved_item`
(`RetrievedItem` with optional `memory` and `chunk`), `abstract_reply`
(`AbstractReply`: `text`, `relevance_score`), `memory_definition` (`Memory`;
only when `fetch_memory=True`), `result_set_boundary` (`ResultSetBoundary`:
`kind` `"BEGIN"`/`"END"`, `stage_name`), or `status` (`GoodMemStatus`:
`code`, `message`, `details`). Check which field is non-None.
`ChunkReference` carries `relevance_score`, `memory_index`, and `chunk`
(`MemoryChunkResponse` with `chunk_text`, `memory_id`,
`chunk_sequence_number`, `start_offset`, `end_offset`).

With `stream=False`, the call collects everything and returns
`list[RetrieveMemoryEvent]`:

```python
events = client.memories.retrieve(message="query", space_ids=[space_id],
                                  stream=False)
chunks = [e.retrieved_item.chunk for e in events if e.retrieved_item]
```

Async: `retrieve` is a coroutine; await it to get the stream, then use
`async with` / `async for`:

```python
stream = await client.memories.retrieve(message="query", space_ids=[space_id])
async with stream as s:
    async for event in s:
        ...
```

### RAG (reranker + LLM post-processing)

```python
with client.memories.retrieve(
    message="Summarize our incident response policy",
    space_ids=[space_id],
    reranker_id=reranker_id,     # optional: re-score before the LLM
    llm_id=llm_id,               # enables answer generation
    llm_temp=0.2,
    max_results=8,
    fetch_memory=False,          # skip memory-definition events
) as stream:
    answer = "".join(e.abstract_reply.text for e in stream if e.abstract_reply)
```

`llm_id`/`reranker_id` assemble the nested `PostProcessor` structure
automatically; `llm_temp`, `gen_token_budget`, `prompt`, `sys_prompt`,
`max_results`, `relevance_threshold`, `chronological_resort` only take effect
when at least one of them is set.

### Metadata filter expressions

The same filter language is accepted by `SpaceKey.filter` (retrieval),
`memories.list(filter=...)`, and filtered batch delete. Filters compile to
SQL predicates over each memory's metadata JSON:

- `val('<jsonpath>')` extracts a value (PostgreSQL JSONPath, e.g. `$.field`,
  `$.arr[0]`, `$.a.b`); `exists('<jsonpath>')` tests presence.
- Compare with `=`, `!=`, `<`, `<=`, `>`, `>=`, `LIKE`, `ILIKE`, `IN`,
  `CONTAINS`, `OVERLAPS`; combine with `AND` / `OR` / `NOT`.
- `CAST(... AS TEXT/INTEGER/DATE/...)` gives typed comparisons; string
  literals use single quotes (`'O''Brien'` to escape).

```python
with client.memories.retrieve(
    message="deployment steps",
    space_keys=[{
        "space_id": space_id,
        "filter": "CAST(val('$.category') AS TEXT) = 'runbook' "
                  "AND 'prod' IN val('$.tags')",
    }],
) as stream:
    ...
```

## Embedders, rerankers, LLMs

These register model endpoints that GoodMem calls server-side. All three
namespaces share the shape: `create`, `get(id=...)`,
`list(label=None, owner_id=None, provider_type=None) -> list`,
`update(id=..., request=<model or dict>)`, `delete(id=...)`.

**Model registry auto-inference:** for known `model_identifier`s the SDK/server
fill in `provider_type`, `endpoint_url`, `dimensionality`,
`max_sequence_length`, and `supported_modalities`. Registered identifiers (as
of 0.1.28) include OpenAI `text-embedding-3-small/-large`, Cohere
`embed-v4.0` and `embed-*-v3.0`, Jina `jina-embeddings-v2/v3/v4` and
`jina-clip-v1/v2`, Voyage `voyage-3*/4*` families (embedders); `gpt-5*`,
`gpt-4.1*`, `gpt-4o*`, `o1/o3/o4-mini` (LLMs); Cohere `rerank-v3.5/v4.0*`,
Jina `jina-reranker-*`, Voyage `rerank-*` (rerankers).

**`api_key` convenience:** on all three `create` methods, `api_key="sk-..."`
(the *provider's* key, read from the environment) expands to the full
`credentials` structure
(`{"kind": "CREDENTIAL_KIND_API_KEY", "api_key": {"inline_secret": ...}}`).
SaaS providers require it; local/proxy endpoints may omit it.

```python
embedders.create(*, display_name: str, model_identifier: str,
                 api_key=None, credentials=None, provider_type=None,
                 endpoint_url=None, api_path=None, dimensionality=None,
                 max_sequence_length=None, supported_modalities=None,
                 distribution_type="DENSE", labels=None, description=None,
                 version=None, monitoring_endpoint=None, owner_id=None,
                 embedder_id=None) -> EmbedderResponse
```

- Embedder/reranker `provider_type` values: `OPENAI`, `VLLM`, `TEI`,
  `LLAMA_CPP`, `VOYAGE`, `COHERE`, `JINA` (use `OPENAI` for any
  OpenAI-compatible endpoint).
- For unregistered models, supply `provider_type`, `endpoint_url`, and (for
  embedders) `dimensionality` + `supported_modalities` explicitly.
- `supported_modalities` values: `TEXT`, `IMAGE`, `AUDIO`, `VIDEO`.

```python
llms.create(*, display_name: str, model_identifier: str, api_key=None,
            credentials=None, provider_type=None, endpoint_url=None,
            api_path=None, max_context_length=None, capabilities=None,
            default_sampling_params=None, client_config=None,
            supported_modalities=None, labels=None, description=None,
            version=None, monitoring_endpoint=None, owner_id=None,
            llm_id=None) -> CreateLLMResponse

rerankers.create(*, display_name: str, model_identifier: str, api_key=None,
                 credentials=None, provider_type=None, endpoint_url=None,
                 api_path=None, supported_modalities=None, labels=None,
                 description=None, version=None, monitoring_endpoint=None,
                 owner_id=None, reranker_id=None) -> RerankerResponse
```

- LLM `provider_type` values: `OPENAI`, `LITELLM_PROXY`, `OPEN_ROUTER`,
  `VLLM`, `OLLAMA`, `LLAMA_CPP`, `CUSTOM_OPENAI_COMPATIBLE`. The
  `endpoint_url` is the OpenAI-compatible base (typically ends with `/v1`);
  `api_path` defaults to `/chat/completions`.

```python
import os

embedder = client.embedders.create(
    display_name="OpenAI small",
    model_identifier="text-embedding-3-small",
    api_key=os.environ["OPENAI_API_KEY"],   # provider key from env
)

# Self-hosted OpenAI-compatible endpoint (no registry entry)
local = client.embedders.create(
    display_name="Local TEI",
    model_identifier="BAAI/bge-base-en-v1.5",
    provider_type="TEI",
    endpoint_url="http://tei.internal:8080",
    dimensionality=768,
    supported_modalities=["TEXT"],
)

# Update via typed request or plain dict
client.embedders.update(id=embedder.embedder_id,
                        request={"display_name": "OpenAI small (prod)"})
```

Update request types (import from `goodmem.models`): `UpdateEmbedderRequest`,
`UpdateRerankerRequest`, `LLMUpdateRequest`, `UpdateSpaceRequest`,
`UpdateApiKeyRequest`. Plain dicts with the same fields are accepted
everywhere a request object is.

## API keys, users, system

```python
apikeys.create(*, labels=None, expires_at=None,     # ms since epoch; None = no expiry
               api_key_id=None) -> CreateApiKeyResponse   # raw key returned once
apikeys.list() -> list[ApiKeyResponse]
apikeys.update(*, id: str, request: UpdateApiKeyRequest | dict) -> ApiKeyResponse
apikeys.delete(*, id: str) -> None

users.me() -> UserResponse
users.get(*, email=None, id=None) -> UserResponse   # exactly one of the two

system.info() -> SystemInfoResponse   # server build metadata; works without a key
system.init() -> SystemInitResponse   # first-run bootstrap (creates root key)
```

Use `client.system.info()` as a cheap connectivity check before doing real
work.

## OCR (GoodMem Enterprise only)

The `ocr` namespace requires a GoodMem Enterprise license; on other instances
it fails while everything else works. Ingest documents as regular memories
instead if OCR is unavailable.

```python
ocr.document(*, file_path=None,       # local file, or:
             content=None,            # base64-encoded bytes
             format=None,             # 'AUTO' | 'PDF' | 'TIFF' | 'PNG' | 'JPEG' | 'BMP'
             start_page=None, end_page=None,   # 0-based inclusive
             include_markdown=None, include_raw_json=None) -> OcrDocumentResponse
```

## End-to-end example

```python
import os, time
from goodmem import Goodmem, MemoryCreationRequest
from goodmem.errors import GoodMemError

BASE_URL = os.environ["GOODMEM_BASE_URL"]
API_KEY = os.environ["GOODMEM_API_KEY"]

with Goodmem(base_url=BASE_URL, api_key=API_KEY, timeout=120.0) as client:
    # 1. Embedder (reuse if present)
    embedders = client.embedders.list()
    embedder = embedders[0] if embedders else client.embedders.create(
        display_name="OpenAI small",
        model_identifier="text-embedding-3-small",
        api_key=os.environ["OPENAI_API_KEY"],
    )

    # 2. Space
    space = client.spaces.create(
        name="support-kb",
        space_embedders=[{"embedder_id": embedder.embedder_id}],
    )

    # 3. Ingest (batch) and poll until indexed
    created = client.memories.batch_create(requests=[
        MemoryCreationRequest(space_id=space.space_id,
                              original_content=text,
                              metadata={"source": "faq", "tags": ["billing"]})
        for text in ["Refunds take 5-7 days.", "Invoices are emailed monthly."]
    ])
    ids = [r.memory_id for r in created.results if r.success]
    deadline = time.monotonic() + 120
    while time.monotonic() < deadline:
        batch = client.memories.batch_get(memory_ids=ids)
        statuses = {r.memory.processing_status for r in batch.results if r.memory}
        if statuses <= {"COMPLETED"}:
            break
        if "FAILED" in statuses:
            raise RuntimeError("ingestion failed")
        time.sleep(2)

    # 4. Retrieve
    try:
        with client.memories.retrieve(
            message="how long do refunds take?",
            space_keys=[{"space_id": space.space_id,
                         "filter": "'billing' IN val('$.tags')"}],
        ) as stream:
            for event in stream:
                if event.retrieved_item:
                    ref = event.retrieved_item.chunk
                    print(f"{ref.relevance_score:.3f}  {ref.chunk.chunk_text}")
    except GoodMemError as e:
        print("retrieval failed:", e)
```

## Commonly-used types

Import from `goodmem.models` (aggregated re-exports also in `goodmem.types`):

- Responses: `EmbedderResponse`, `RerankerResponse`, `LLMResponse`, `Space`,
  `Memory`, `ApiKeyResponse`, `UserResponse`, `BatchMemoryResponse`
- Retrieval: `RetrieveMemoryEvent`, `RetrievedItem`, `ChunkReference`,
  `AbstractReply`, `SpaceKey`, `ContextItem`, `TokenBudget`
- Configuration: `ChunkingConfiguration`, `SpaceEmbedderConfig`,
  `EndpointAuthentication`, `PostProcessor`
- Enums: `SortOrder` (`ASCENDING`/`DESCENDING`), `Modality`, `ProviderType`,
  `LLMProviderType`, `DistributionType`

All models are pydantic; they accept snake_case field names on construction
and serialize to the API's camelCase aliases automatically. Passing plain
dicts instead of model instances works throughout.
