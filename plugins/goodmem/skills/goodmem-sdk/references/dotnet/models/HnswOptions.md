<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# HnswOptions

Optional request-level overrides for pgvector HNSW search settings. Unset fields inherit server defaults.

`Goodmem.Client.Models.HnswOptions`

- `EfSearch` (`int?`): HNSW candidate list size (1..1000). JSON: `efSearch`.
- `IterativeScan` (`HnswIterativeScan?`): HNSW iterative scan mode. Use POST retrieve for this advanced tuning control. JSON: `iterativeScan`.
- `MaxScanTuples` (`int?`): Maximum tuples to scan during iterative filtering (1..2147483647). JSON: `maxScanTuples`.
- `ScanMemMultiplier` (`double?`): Multiplier on work_mem for iterative scanning (1.0..1000.0). JSON: `scanMemMultiplier`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [HnswIterativeScan](HnswIterativeScan.md)
