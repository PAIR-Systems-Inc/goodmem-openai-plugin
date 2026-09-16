<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# EmbedderWeight

Per-embedder weight override for retrieval operations.

```python
from goodmem.models import EmbedderWeight
```

- `embedder_id` (`str`, required): The UUID for the embedder. JSON: `embedderId`.
- `weight` (`float`, required): The weight to apply to this embedder's results. Can be positive, negative, or zero.

[Python](../../python.md)
