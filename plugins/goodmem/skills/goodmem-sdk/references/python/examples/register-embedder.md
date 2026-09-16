<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# Register an embedder

Register a known catalog model using an upstream provider key held in an environment
variable. GoodMem's API key authenticates to GoodMem; `OPENAI_API_KEY` authenticates
embedding requests to the provider. Read [create](../embedders/create.md) for
custom models, endpoints, or structured credentials. Attach the returned embedder ID
when creating a space; registration alone does not attach it to existing spaces.

```python
import os
from goodmem import Goodmem

with Goodmem(base_url=os.environ["GOODMEM_BASE_URL"], api_key=os.environ["GOODMEM_API_KEY"]) as client:
    embedder = client.embedders.create(
        display_name="Document embeddings",
        model_identifier="text-embedding-3-small",
        api_key=os.environ["OPENAI_API_KEY"],
    )
    print(embedder.embedder_id)
```

[Python](../../python.md)
