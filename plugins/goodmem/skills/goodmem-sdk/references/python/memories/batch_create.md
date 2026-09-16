<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# memories.batch_create

Create multiple memories in a batch

Create multiple memories in a single batch. Each item in `requests` follows the same per-call shape as `memories.create`: provide exactly one of `original_content` or `original_content_b64`; `original_content_b64` requires `content_type` (auto-inferred to `text/plain` for plain-text `original_content`); `original_content_ref` is a metadata pointer that may accompany the content source. Per-item failures are reported individually and do NOT abort the batch.

Args:
    requests (list[MemoryCreationRequest]): Array of memory creation requests.

Returns:
    BatchMemoryResponse

```python
memories.batch_create(*, requests: 'list[MemoryCreationRequest]') -> 'BatchMemoryResponse'
```

[memories](../memories.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [MemoryCreationRequest](../models/MemoryCreationRequest.md)
