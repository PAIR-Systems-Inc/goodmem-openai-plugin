<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# HnswOptions

Optional request-level overrides for pgvector HNSW search settings. Unset fields inherit server defaults.

- `efSearch` (`number | null`, optional): HNSW candidate list size (1..1000).
- `iterativeScan` (`HnswIterativeScan | null`, optional): HNSW iterative scan mode. Use POST retrieve for this advanced tuning control.
- `maxScanTuples` (`number | null`, optional): Maximum tuples to scan during iterative filtering (1..2147483647).
- `scanMemMultiplier` (`number | null`, optional): Multiplier on work_mem for iterative scanning (1.0..1000.0).

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [HnswIterativeScan](HnswIterativeScan.md)
