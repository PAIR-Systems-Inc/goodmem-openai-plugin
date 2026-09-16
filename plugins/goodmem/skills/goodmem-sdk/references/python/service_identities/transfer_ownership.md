<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# service_identities.transfer_ownership

Transfer service-identity ownership

Transfers administrative ownership to another active principal. A service identity cannot own itself. The service identity's subject, immutable creator, credentials, grants, and roles are unchanged.

Args:
    id (str): Service-identity UUID
    request (TransferOwnershipRequest | dict): The request payload. Accepts a TransferOwnershipRequest instance or a plain dict with the same fields.

Returns:
    TransferServiceIdentityOwnershipResponse

```python
service_identities.transfer_ownership(*, id: 'str', request: 'TransferOwnershipRequest | dict') -> 'TransferServiceIdentityOwnershipResponse'
```

[service_identities](../service_identities.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [TransferOwnershipRequest](../models/TransferOwnershipRequest.md)
