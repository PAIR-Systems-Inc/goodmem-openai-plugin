<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# AdminDrainRequest

- `timeoutSec` (`number | null`, optional): Maximum seconds to wait for the server to quiesce before returning.
- `reason` (`string | null`, optional): Human-readable reason for initiating drain mode.
- `waitForQuiesce` (`boolean | null`, optional): If true, wait for in-flight requests to complete and the server to reach QUIESCED before responding.

[TypeScript](../../typescript.md)
