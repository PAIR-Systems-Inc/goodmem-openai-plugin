<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# GeminiEndpointConfig

Gemini backend routing. DEVELOPER does not use projectId or location; GOOGLE_CLOUD requires projectId and defaults an omitted location to global.

```python
from goodmem.models import GeminiEndpointConfig
```

- `backend` (`GeminiApiBackend | None`, required): Google API surface. UNSPECIFIED is invalid when this configuration is supplied on a write.
- `project_id` (`str | None`, optional): Google Cloud resource project. Required for GOOGLE_CLOUD and unused for DEVELOPER; this is distinct from the ADC quota project. JSON: `projectId`.
- `location` (`str | None`, optional): Google Cloud location. Valid only for GOOGLE_CLOUD; omission defaults to global.

[Python](../../python.md)

Related types — open only those used by your request:

- [GeminiApiBackend](GeminiApiBackend.md)
