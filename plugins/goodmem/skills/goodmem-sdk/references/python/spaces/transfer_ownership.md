<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# spaces.transfer_ownership

Transfer ownership of a space

Transfers an existing space to another active human or service principal. The current space owner, the GoodMem instance owner, or an instance administrator may transfer it; a space-scoped administrator cannot. Only owner and update-audit fields change. Memories, embedder associations, grants, and role assignments remain unchanged. This operation is not idempotent under response semantics: after an unknown outcome, read the space before retrying.

Args:
    id (str): UUID of the existing space to transfer
    request (TransferOwnershipRequest | dict): The request payload. Accepts a TransferOwnershipRequest instance or a plain dict with the same fields.

Returns:
    TransferSpaceOwnershipResponse

```python
spaces.transfer_ownership(*, id: 'str', request: 'TransferOwnershipRequest | dict') -> 'TransferSpaceOwnershipResponse'
```

[spaces](../spaces.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [TransferOwnershipRequest](../models/TransferOwnershipRequest.md)
