<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# CreateRetrieveMemoryLogPolicyRequest

REST request for creating an immutable RetrieveMemory log policy.

- `policyId` (`string | null`, optional): Optional client-provided policy UUID.
- `displayName` (`string`, required): Human-readable policy name.
- `description` (`string | null`, optional): Optional operator description.
- `condition` (`RetrieveMemoryLogPolicyCondition`, required): Policy match condition.
- `activeFrom` (`number | null`, optional): Inclusive activation time in milliseconds since epoch.
- `activeUntil` (`number | null`, optional): Exclusive deactivation time in milliseconds since epoch.
- `labels` (`Record<string, string> | null`, optional): Operator labels for listing and administration.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [RetrieveMemoryLogPolicyCondition](RetrieveMemoryLogPolicyCondition.md)
