<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# spaces.update

Update a space

Updates an existing space with new values for the specified fields. Only name and labels can be updated. Fields not included in the request remain unchanged.

IMMUTABLE FIELDS: space_embedders, default_chunking_config, and owner_id cannot be modified after creation.

NAME UNIQUENESS: Name must be unique per owner - returns ALREADY_EXISTS if name conflicts with an existing space. Requires UPDATE_SPACE on the requested space. This operation is idempotent.

Args:
    id (str): The unique identifier of the space to update
    request (UpdateSpaceRequest | dict): The request payload. Accepts a UpdateSpaceRequest instance or a plain dict with the same fields.

Returns:
    Space

```python
spaces.update(*, id: 'str', request: 'UpdateSpaceRequest | dict') -> 'Space'
```

[spaces](../spaces.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [UpdateSpaceRequest](../models/UpdateSpaceRequest.md)
