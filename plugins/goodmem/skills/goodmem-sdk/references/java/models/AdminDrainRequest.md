<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# AdminDrainRequest

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `timeoutSec` (`Integer`): Maximum seconds to wait for the server to quiesce before returning.
- `reason` (`String`): Human-readable reason for initiating drain mode.
- `waitForQuiesce` (`Boolean`): If true, wait for in-flight requests to complete and the server to reach QUIESCED before responding.

[Java](../../java.md)
