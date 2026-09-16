<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# PingStreamRequest

Request payload for a streaming ping session

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `targetId` (`TargetId`): Target resource ID (UUID). Typed wrapper `TargetId`; build from a raw string with `TargetId.from(String)`.
- `targetTypeHint` (`PingTargetType`): Optional hint for the target resource type
- `count` (`Integer`): Number of probes to run (0 uses server default)
- `intervalMs` (`Integer`): Delay between probes in milliseconds (0 uses server default)
- `timeoutMs` (`Integer`): Per-probe timeout in milliseconds (0 uses server default)
- `payloadType` (`PingPayloadType`): Desired payload type (defaults to provider-specific value)
- `payload` (`String`): Explicit UTF-8 payload to send with each probe (mutually exclusive with payloadSizeBytes)
- `payloadSizeBytes` (`Integer`): Synthetic payload size in bytes (mutually exclusive with payload)
- `maxInFlight` (`Integer`): Maximum concurrent probes (defaults to 1)
- `jitter` (`Boolean`): Add jitter to probe scheduling
- `labels` (`java.util.Map<String, String>`): Optional labels to attach to the ping session

[Java](../../java.md)

Related types — open only those used by your request:

- [PingPayloadType](PingPayloadType.md)
- [PingTargetType](PingTargetType.md)
- [TargetId](TargetId.md)
