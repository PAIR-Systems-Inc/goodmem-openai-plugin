<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# SpaceEmbedderConfig

Configuration for associating an embedder with a space.

```python
from goodmem.models import SpaceEmbedderConfig
```

- `embedder_id` (`str`, required): The UUID for the embedder to associate with the space. JSON: `embedderId`.
- `default_retrieval_weight` (`float | None`, optional): Relative weight for this embedder used by default during retrieval. If omitted, defaults to 1.0; values need not sum to 1 and can be overridden per request. JSON: `defaultRetrievalWeight`.

[Python](../../python.md)
