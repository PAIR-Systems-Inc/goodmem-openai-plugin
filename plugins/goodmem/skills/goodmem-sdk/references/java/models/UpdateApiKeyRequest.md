<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# UpdateApiKeyRequest

Request parameters for updating an API key.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `status` (`ApiKeyResponseStatus`): New status for the API key. INACTIVE is permanent; revoked keys cannot be reactivated. Typed enum `ApiKeyResponseStatus`; unknown server values fail Jackson deserialization loudly.
- `replaceLabels` (`java.util.Map<String, String>`): Replace all existing labels with this set. Mutually exclusive with mergeLabels. The stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].
- `mergeLabels` (`java.util.Map<String, String>`): Merge these labels with existing ones. Mutually exclusive with replaceLabels. The final stored map may contain at most 20 entries; keys and values contain at most 255 characters; keys use [a-z0-9._-].

[Java](../../java.md)

Related types — open only those used by your request:

- [ApiKeyResponseStatus](ApiKeyResponseStatus.md)
