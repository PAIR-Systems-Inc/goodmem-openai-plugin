# GoodMem Python SDK

Install the supported release with `pip install goodmem==@VERSION@` (Python 3.10+).

```python
import os
from goodmem import Goodmem

with Goodmem(base_url=os.environ["GOODMEM_BASE_URL"],
             api_key=os.environ["GOODMEM_API_KEY"]) as client:
    for space in client.spaces.list():
        print(space.space_id, space.name)
```

`AsyncGoodmem` exposes the same methods with `await` and async iteration.
Use keyword arguments. Paginated methods return `Page` / `AsyncPage`;
iteration follows cursors. In particular, `apikeys.list()` is paginated.
`memories.retrieve()` returns a context-managed stream; `stream=False`
collects events. Handle status warnings separately from retrieved passages.

Use the bounded ingestion example in [the SDK skill](../SKILL.md) before
retrieving newly created content. `spaces.create` accepts `space_embedders`;
there is no `public_read` parameter. Use access policies to grant access.

Errors are exported from `goodmem`: `APIError` has `status_code`, and subclasses
include `AuthenticationError`, `PermissionDeniedError`, `NotFoundError`, and
`RateLimitError`. `NetworkError` wraps transport failures. Avoid logging raw
provider error bodies or API keys.
