<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# admin.transfer_instance_ownership

Transfer GoodMem instance ownership

Transfers the singleton GoodMem instance to another active human principal. Only the current instance owner may invoke this operation; ADMIN, MANAGE_ACCESS, and ordinary grants are insufficient. Ownership and the synthetic ROOT assignment move atomically. All ordinary roles, including ADMIN, remain unchanged. No credential is created or returned. After an unknown outcome, read the current owner before retrying.

Args:
    new_owner_id (str): Existing principal UUID that will become the new owner.

Returns:
    TransferInstanceOwnershipResponse

```python
admin.transfer_instance_ownership(*, new_owner_id: 'str') -> 'TransferInstanceOwnershipResponse'
```

[admin](../admin.md) · [Python](../../python.md)
