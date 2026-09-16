<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# CreateRetrieveMemoryLogPolicyRequest

REST request for creating an immutable RetrieveMemory log policy.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `policyId` (`PolicyId`): Optional client-provided policy UUID. Typed wrapper `PolicyId`; build from a raw string with `PolicyId.from(String)`.
- `displayName` (`String`): Human-readable policy name.
- `description` (`String`): Optional operator description.
- `condition` (`RetrieveMemoryLogPolicyCondition`): Policy match condition.
- `activeFrom` (`Long`): Inclusive activation time in milliseconds since epoch.
- `activeUntil` (`Long`): Exclusive deactivation time in milliseconds since epoch.
- `labels` (`java.util.Map<String, String>`): Operator labels for listing and administration.

[Java](../../java.md)

Related types — open only those used by your request:

- [PolicyId](PolicyId.md)
- [RetrieveMemoryLogPolicyCondition](RetrieveMemoryLogPolicyCondition.md)
