<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# CompleteUserEnrollmentRequest

Exchanges one enrollment credential for the target human's initial API key. Omit both apiKeyId and rawApiKey for server-generated key material, or supply both for exact-retry-safe client-generated completion; supplying only one is invalid.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `enrollmentToken` (`String`): Required one-time enrollment credential. Never log or persist it.
- `apiKeyId` (`ApiKeyId`): Optional client-generated API-key UUID retained for exact retries. Must be supplied together with rawApiKey, or both fields must be omitted. Typed wrapper `ApiKeyId`; build from a raw string with `ApiKeyId.from(String)`.
- `rawApiKey` (`String`): Optional canonical client-generated API key. Must be supplied together with apiKeyId, never logged, and retained for exact retries; omit both fields for server generation.

[Java](../../java.md)

Related types — open only those used by your request:

- [ApiKeyId](ApiKeyId.md)
