<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# CreateApiKeyRequest

Request parameters for creating a new API key.

`Goodmem.Client.Models.CreateApiKeyRequest`

- `ApiKeyId` (`string?`): Optional client-provided UUID for idempotent creation. If not provided, server generates a new UUID. Returns ALREADY_EXISTS if ID is already in use. JSON: `apiKeyId`.
- `AuthorityMode` (`ApiKeyAuthorityMode?`): Authority mode. Omit to create a self-issued human key that inherits live authority. A scoped issuing credential may create only SCOPED children. JSON: `authorityMode`.
- `Ceiling` (`IReadOnlyList<AccessPolicyRule>?`): Immutable authorization ceiling. Required and nonempty for SCOPED; omitted for INHERIT_SUBJECT, with at most 1,000 rules. Every rule must be covered by both the subject's live authority and the issuing credential's effective authority. JSON: `ceiling`.
- `ExpiresAt` (`DateTimeOffset?`): Exclusive expiration timestamp in milliseconds since epoch. It must be later than validFrom, which defaults to issuance time; if omitted, the key does not expire. JSON: `expiresAt`.
- `Labels` (`IReadOnlyDictionary<string, string>?`): Key-value pairs of metadata associated with the API key. Used for organization and filtering. At most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-]. JSON: `labels`.
- `SubjectPrincipalId` (`string?`): Principal authenticated by this key. Omit to use the authenticated principal. JSON: `subjectPrincipalId`.
- `ValidFrom` (`DateTimeOffset?`): Inclusive activation time in epoch milliseconds. Omit to activate at issuance time. JSON: `validFrom`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [AccessPolicyRule](AccessPolicyRule.md)
- [ApiKeyAuthorityMode](ApiKeyAuthorityMode.md)
