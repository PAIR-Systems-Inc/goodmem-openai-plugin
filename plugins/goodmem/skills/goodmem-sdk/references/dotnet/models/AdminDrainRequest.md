<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# AdminDrainRequest

`Goodmem.Client.Models.AdminDrainRequest`

- `Reason` (`string?`): Human-readable reason for initiating drain mode. JSON: `reason`.
- `TimeoutSec` (`int?`): Maximum seconds to wait for the server to quiesce before returning. JSON: `timeoutSec`.
- `WaitForQuiesce` (`bool?`): If true, wait for in-flight requests to complete and the server to reach QUIESCED before responding. JSON: `waitForQuiesce`.

[.NET](../../dotnet.md)
