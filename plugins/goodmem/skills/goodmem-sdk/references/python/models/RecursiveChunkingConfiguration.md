<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# RecursiveChunkingConfiguration

Recursive hierarchical chunking strategy with configurable separators and overlap

```python
from goodmem.models import RecursiveChunkingConfiguration
```

- `chunk_size` (`int`, required): Maximum size of a chunk (should be ≤ context window) JSON: `chunkSize`.
- `chunk_overlap` (`int`, required): Sliding overlap between chunks JSON: `chunkOverlap`.
- `separators` (`list[str] | None`, optional): Hierarchical separator list (order = preference)
- `keep_strategy` (`SeparatorKeepStrategy | None`, required): How to handle separators after splitting. KEEP_NONE is deprecated and behaves as KEEP_END. JSON: `keepStrategy`.
- `separator_is_regex` (`bool | None`, optional): Whether separators are regex patterns JSON: `separatorIsRegex`.
- `length_measurement` (`LengthMeasurement | None`, required): How to measure chunk length JSON: `lengthMeasurement`.

[Python](../../python.md)

Related types — open only those used by your request:

- [LengthMeasurement](LengthMeasurement.md)
- [SeparatorKeepStrategy](SeparatorKeepStrategy.md)
