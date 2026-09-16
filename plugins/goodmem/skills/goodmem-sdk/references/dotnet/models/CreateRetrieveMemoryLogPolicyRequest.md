<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# CreateRetrieveMemoryLogPolicyRequest

REST request for creating an immutable RetrieveMemory log policy.

`Goodmem.Client.Models.CreateRetrieveMemoryLogPolicyRequest`

- `ActiveFrom` (`DateTimeOffset?`): Inclusive activation time in milliseconds since epoch. JSON: `activeFrom`.
- `ActiveUntil` (`DateTimeOffset?`): Exclusive deactivation time in milliseconds since epoch. JSON: `activeUntil`.
- `Condition` (`RetrieveMemoryLogPolicyCondition`, required): Policy match condition. JSON: `condition`.
- `Description` (`string?`): Optional operator description. JSON: `description`.
- `DisplayName` (`string`, required): Human-readable policy name. JSON: `displayName`.
- `Labels` (`IReadOnlyDictionary<string, string>?`): Operator labels for listing and administration. JSON: `labels`.
- `PolicyId` (`string?`): Optional client-provided policy UUID. JSON: `policyId`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [RetrieveMemoryLogPolicyCondition](RetrieveMemoryLogPolicyCondition.md)
