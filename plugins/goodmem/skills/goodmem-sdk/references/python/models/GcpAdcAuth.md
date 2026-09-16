<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# GcpAdcAuth

Configuration for Google Application Default Credentials (ADC).

```python
from goodmem.models import GcpAdcAuth
```

- `scopes` (`list[str] | None`, optional): Additional OAuth scopes. Empty list falls back to the default cloud-platform scope.
- `quota_project_id` (`str | None`, optional): Optional quota project used for billing JSON: `quotaProjectId`.

[Python](../../python.md)
