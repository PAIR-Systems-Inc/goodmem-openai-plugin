# List spaces

```python
import os
from goodmem import Goodmem

with Goodmem(base_url=os.environ["GOODMEM_BASE_URL"],
             api_key=os.environ["GOODMEM_API_KEY"]) as client:
    for space in client.spaces.list():
        print(space.space_id, space.name)
```
