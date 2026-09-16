<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# PingOnceRequest

Request payload for a single ping probe

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `targetId` (`TargetId`): Target resource ID (UUID). Typed wrapper `TargetId`; build from a raw string with `TargetId.from(String)`.
- `targetTypeHint` (`PingTargetType`): Optional hint for the target resource type
- `payloadType` (`PingPayloadType`): Desired payload type (defaults to provider-specific value)
- `payload` (`String`): Explicit UTF-8 payload to send with the probe (mutually exclusive with payloadSizeBytes)
- `payloadSizeBytes` (`Integer`): Synthetic payload size in bytes (mutually exclusive with payload)
- `timeoutMs` (`Integer`): Per-probe timeout in milliseconds (0 uses server default)

[Java](../../java.md)

Related types — open only those used by your request:

- [PingPayloadType](PingPayloadType.md)
- [PingTargetType](PingTargetType.md)
- [TargetId](TargetId.md)
