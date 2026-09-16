<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# GrantAudience

Exactly one principal or the all-authenticated audience.

```python
from goodmem.models import GrantAudience
```

- `principal_id` (`str | None`, optional): Active HUMAN or SERVICE principal UUID. JSON: `principalId`.
- `all_authenticated` (`GrantAudienceAllAuthenticated | None`, optional): Set to true to address every authenticated principal. JSON: `allAuthenticated`.

[Python](../../python.md)

Related types — open only those used by your request:

- [GrantAudienceAllAuthenticated](GrantAudienceAllAuthenticated.md)
