<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# CompleteUserEnrollmentRequest

Exchanges one enrollment credential for the target human's initial API key. Omit both apiKeyId and rawApiKey for server-generated key material, or supply both for exact-retry-safe client-generated completion; supplying only one is invalid.

`Goodmem.Client.Models.CompleteUserEnrollmentRequest`

- `ApiKeyId` (`string?`): Optional client-generated API-key UUID retained for exact retries. Must be supplied together with rawApiKey, or both fields must be omitted. JSON: `apiKeyId`.
- `EnrollmentToken` (`string`, required): Required one-time enrollment credential. Never log or persist it. JSON: `enrollmentToken`.
- `RawApiKey` (`string?`): Optional canonical client-generated API key. Must be supplied together with apiKeyId, never logged, and retained for exact retries; omit both fields for server generation. JSON: `rawApiKey`.

[.NET](../../dotnet.md)
