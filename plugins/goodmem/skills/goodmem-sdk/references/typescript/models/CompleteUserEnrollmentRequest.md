<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# CompleteUserEnrollmentRequest

Exchanges one enrollment credential for the target human's initial API key. Omit both apiKeyId and rawApiKey for server-generated key material, or supply both for exact-retry-safe client-generated completion; supplying only one is invalid.

- `enrollmentToken` (`string`, required): Required one-time enrollment credential. Never log or persist it.
- `apiKeyId` (`string | null`, optional): Optional client-generated API-key UUID retained for exact retries. Must be supplied together with rawApiKey, or both fields must be omitted.
- `rawApiKey` (`string | null`, optional): Optional canonical client-generated API key. Must be supplied together with apiKeyId, never logged, and retained for exact retries; omit both fields for server generation.

[TypeScript](../../typescript.md)
