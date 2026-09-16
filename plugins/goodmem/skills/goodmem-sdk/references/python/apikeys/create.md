<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# apikeys.create

Create a new API key

Issues a new API key and returns its raw value exactly once. Omitted subject and authority_mode create a self-issued human key that inherits the subject's live authority. A SCOPED key requires a nonempty immutable ceiling, and every ceiling rule must be conservatively covered by both the subject's live authority and the issuing credential's effective authority. A scoped issuer can create only scoped children. SERVICE subjects require SCOPED mode and MANAGE_ACCESS on the service identity.

AUTHORIZATION: Requires CREATE_API_KEY on the proposed credential; subject and ceiling checks are repeated by the final insertion statement.

Args:
    labels (dict[str, str], optional): Key-value pairs of metadata associated with the API key. Used for organization and filtering. At most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].
    expires_at (int, optional): Exclusive expiration timestamp in milliseconds since epoch. It must be later than valid_from, which defaults to issuance time; if omitted, the key does not expire.
    api_key_id (str, optional): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use.
    subject_principal_id (str, optional): Principal authenticated by this key. Omit to use the authenticated principal.
    authority_mode (ApiKeyAuthorityMode, optional, default='INHERIT_SUBJECT'): Authority mode. Omit to create a self-issued human key that inherits live authority. A scoped issuing credential may create only SCOPED children.
    ceiling (list[AccessPolicyRule], optional): Immutable authorization ceiling. Required and nonempty for SCOPED; omitted for INHERIT_SUBJECT, with at most 1,000 rules. Every rule must be covered by both the subject's live authority and the issuing credential's effective authority.
    valid_from (int, optional): Inclusive activation time in epoch milliseconds. Omit to activate at issuance time.

Returns:
    CreateApiKeyResponse

```python
apikeys.create(*, labels: 'dict[str, str] | None' = None, expires_at: 'int | None' = None, api_key_id: 'str | None' = None, subject_principal_id: 'str | None' = None, authority_mode: 'ApiKeyAuthorityMode | None' = None, ceiling: 'list[AccessPolicyRule] | None' = None, valid_from: 'int | None' = None) -> 'CreateApiKeyResponse'
```

[apikeys](../apikeys.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [AccessPolicyRule](../models/AccessPolicyRule.md)
- [ApiKeyAuthorityMode](../models/ApiKeyAuthorityMode.md)
