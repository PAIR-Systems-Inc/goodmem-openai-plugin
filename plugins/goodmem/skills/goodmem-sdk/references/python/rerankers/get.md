<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# rerankers.get

Get a reranker by ID

Retrieves the details of a specific reranker configuration by its unique identifier. Stored credentials are omitted unless include_credentials is true and the caller also has READ_RERANKER_CREDENTIALS. Requires READ_RERANKER on the requested reranker. The service distinguishes a missing reranker from an existing reranker the caller cannot read. This is a read-only operation with no side effects and is safe to retry.

Args:
    id (str): The unique identifier of the reranker to retrieve
    include_credentials (bool, optional, default=False): Whether to return stored credentials. Also accepts include_credentials. Requires READ_RERANKER_CREDENTIALS in addition to READ_RERANKER.

Returns:
    RerankerResponse

```python
rerankers.get(*, id: 'str', include_credentials: 'bool | None' = None) -> 'RerankerResponse'
```

[rerankers](../rerankers.md) · [Python](../../python.md)
