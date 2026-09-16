<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# PingOnceRequest

Request payload for a single ping probe

`Goodmem.Client.Models.PingOnceRequest`

- `Payload` (`string?`): Explicit UTF-8 payload to send with the probe (mutually exclusive with payloadSizeBytes) JSON: `payload`.
- `PayloadSizeBytes` (`int?`): Synthetic payload size in bytes (mutually exclusive with payload) JSON: `payloadSizeBytes`.
- `PayloadType` (`PingPayloadType?`): Desired payload type (defaults to provider-specific value) JSON: `payloadType`.
- `TargetId` (`string`, required): Target resource ID (UUID) JSON: `targetId`.
- `TargetTypeHint` (`PingTargetType?`): Optional hint for the target resource type JSON: `targetTypeHint`.
- `TimeoutMs` (`int?`): Per-probe timeout in milliseconds (0 uses server default) JSON: `timeoutMs`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [PingPayloadType](PingPayloadType.md)
- [PingTargetType](PingTargetType.md)
