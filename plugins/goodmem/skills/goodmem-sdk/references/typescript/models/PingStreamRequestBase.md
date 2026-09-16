<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# PingStreamRequestBase

- `targetId` (`string`, required): Target resource ID (UUID)
- `targetTypeHint` (`PingTargetType | null`, optional): Optional hint for the target resource type
- `count` (`number | null`, optional): Number of probes to run (0 uses server default)
- `intervalMs` (`number | null`, optional): Delay between probes in milliseconds (0 uses server default)
- `timeoutMs` (`number | null`, optional): Per-probe timeout in milliseconds (0 uses server default)
- `payloadType` (`PingPayloadType | null`, optional): Desired payload type (defaults to provider-specific value)
- `payload` (`string | null`, optional): Explicit UTF-8 payload to send with each probe (mutually exclusive with payloadSizeBytes)
- `payloadSizeBytes` (`number | null`, optional): Synthetic payload size in bytes (mutually exclusive with payload)
- `maxInFlight` (`number | null`, optional): Maximum concurrent probes (defaults to 1)
- `jitter` (`boolean | null`, optional): Add jitter to probe scheduling
- `labels` (`Record<string, string> | null`, optional): Optional labels to attach to the ping session

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [PingPayloadType](PingPayloadType.md)
- [PingTargetType](PingTargetType.md)
