<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# HnswOptions

Optional request-level overrides for pgvector HNSW search settings. Unset fields inherit server defaults.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `efSearch` (`Integer`): HNSW candidate list size (1..1000).
- `iterativeScan` (`HnswIterativeScan`): HNSW iterative scan mode. Use POST retrieve for this advanced tuning control.
- `maxScanTuples` (`Integer`): Maximum tuples to scan during iterative filtering (1..2147483647).
- `scanMemMultiplier` (`Double`): Multiplier on work_mem for iterative scanning (1.0..1000.0).

[Java](../../java.md)

Related types — open only those used by your request:

- [HnswIterativeScan](HnswIterativeScan.md)
