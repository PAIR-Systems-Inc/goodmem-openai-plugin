---
name: goodmem-sdk
description: Complete SDK references for building GoodMem into applications. Use when the user wants to write code that integrates GoodMem — creating spaces, ingesting memories, semantic retrieval, RAG pipelines, or managing embedders/rerankers/LLMs — in Python (goodmem), TypeScript (@pairsystems/goodmem), Java (ai.pairsys:goodmem-java), or .NET (PairSystems.Goodmem.Client).
---

# GoodMem SDK

GoodMem is a memory and retrieval (RAG) service. Applications store content as
**memories** inside **spaces**; GoodMem chunks and embeds the content
server-side using a registered **embedder**, then serves semantic retrieval
over it — optionally post-processed by a **reranker** (precision) or an
**LLM** (answer generation/summarization). The REST API lives under
`{base_url}/v1` and authenticates with an `x-api-key` header carrying a key
that starts with `gm_`. Every SDK wraps that API with a typed, namespaced
client: `client.<namespace>.<method>(...)`.

## Install

Always use the latest published version; the reference files carry the exact
version they were generated from.

| Language | Package | Install |
|---|---|---|
| Python (>= 3.10) | `goodmem` (PyPI) | `pip install goodmem` |
| TypeScript / Node | `@pairsystems/goodmem` (npm) | `npm install @pairsystems/goodmem` |
| Java (JDK 21+) | `ai.pairsys:goodmem-java` (Maven Central) | add the Maven/Gradle dependency |
| .NET | `PairSystems.Goodmem.Client` (NuGet) | `dotnet add package PairSystems.Goodmem.Client` |

## Python quick start

Credentials always come from the environment — never hardcode keys:

```python
import os
from goodmem import Goodmem

with Goodmem(
    base_url=os.environ["GOODMEM_BASE_URL"],   # e.g. https://your-instance.cloud.goodmem.ai
    api_key=os.environ["GOODMEM_API_KEY"],     # gm_...
) as client:
    memory = client.memories.create(
        space_id="<space-uuid>",
        original_content="GoodMem stores and retrieves memories.",
    )
    with client.memories.retrieve(
        message="what does GoodMem do?",
        space_ids=["<space-uuid>"],
    ) as stream:
        for event in stream:
            if event.retrieved_item:
                print(event.retrieved_item.chunk.chunk.chunk_text)
```

The same flow translates directly to the other SDKs — same namespaces, same
method names in each language's naming convention.

## Core concepts

- **Spaces need an embedder.** `spaces.create` requires at least one embedder
  configuration (`space_embedders`). Register an embedder first (or reuse an
  existing one from `embedders.list()`); passing a known `model_identifier`
  auto-fills provider type, endpoint URL, and dimensionality.
- **Ingestion is asynchronous.** Creating a memory returns immediately with
  `processing_status` of `PENDING`; chunking and embedding happen in the
  background. Poll `memories.get` until the status is `COMPLETED` (or
  `FAILED`) before retrieving — un-indexed memories are invisible to search.
- **Retrieval is scoped and filterable.** Target one or more spaces via
  `space_ids`, or use `space_keys` for per-space metadata filter expressions
  and per-embedder weights. Optional `reranker_id` re-scores results;
  `llm_id` adds LLM answer generation over the retrieved chunks.
- **Results stream.** Retrieval returns a stream of typed events (retrieved
  chunks, memory definitions, LLM reply text, boundaries, status); pass
  `stream=False` to collect them into a list instead.
- **OCR requires GoodMem Enterprise.** The `ocr` namespace fails on
  non-Enterprise instances; ingest documents as text/PDF memories instead.

## Where to go next

Each reference is generated from the published package and stamped with the
version it documents:

- `references/python.md` — complete Python reference (client construction,
  every namespace, pagination, streaming, errors).
- `references/typescript.md` — complete TypeScript reference.
- `references/java.md` — complete Java reference.
- `references/dotnet.md` — complete .NET reference.
