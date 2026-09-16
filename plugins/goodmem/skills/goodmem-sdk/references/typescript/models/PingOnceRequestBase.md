<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# PingOnceRequestBase

- `targetId` (`string`, required): Target resource ID (UUID)
- `targetTypeHint` (`PingTargetType | null`, optional): Optional hint for the target resource type
- `payloadType` (`PingPayloadType | null`, optional): Desired payload type (defaults to provider-specific value)
- `payload` (`string | null`, optional): Explicit UTF-8 payload to send with the probe (mutually exclusive with payloadSizeBytes)
- `payloadSizeBytes` (`number | null`, optional): Synthetic payload size in bytes (mutually exclusive with payload)
- `timeoutMs` (`number | null`, optional): Per-probe timeout in milliseconds (0 uses server default)

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [PingPayloadType](PingPayloadType.md)
- [PingTargetType](PingTargetType.md)
