<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# Ingest and retrieve

Use an existing space with an embedder. Read [create](../memories/create.md),
[get](../memories/get.md), and [retrieve](../memories/retrieve.md) when adapting this.

```python
import os
import time
from goodmem import Goodmem

with Goodmem(
    base_url=os.environ["GOODMEM_BASE_URL"],   # e.g. https://your-instance.cloud.goodmem.ai
    api_key=os.environ["GOODMEM_API_KEY"],     # gm_...
) as client:
    space_id = os.environ["GOODMEM_SPACE_ID"]  # existing space with an embedder
    memory = client.memories.create(
        space_id=space_id,
        original_content="GoodMem stores and retrieves memories.",
    )
    deadline = time.monotonic() + 120
    while memory.processing_status != "COMPLETED":
        if memory.processing_status == "FAILED":
            raise RuntimeError("Memory processing failed; inspect job history in GoodMem.")
        if time.monotonic() >= deadline:
            raise TimeoutError("Memory is still processing; retry retrieval later.")
        time.sleep(0.5)
        memory = client.memories.get(id=memory.memory_id)
    with client.memories.retrieve(
        message="what does GoodMem do?",
        space_ids=[space_id],
    ) as stream:
        for event in stream:
            if event.retrieved_item and event.retrieved_item.chunk:
                print(event.retrieved_item.chunk.chunk.chunk_text)
```

[Python](../../python.md)
