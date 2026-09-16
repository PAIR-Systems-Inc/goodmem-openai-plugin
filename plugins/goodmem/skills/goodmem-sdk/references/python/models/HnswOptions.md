<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# HnswOptions

Optional request-level overrides for pgvector HNSW search settings. Unset fields inherit server defaults.

- `ef_search` (`int | None`, optional): HNSW candidate list size (1..1000). JSON: `efSearch`.
- `iterative_scan` (`HnswIterativeScan | None`, optional): HNSW iterative scan mode. Use POST retrieve for this advanced tuning control. JSON: `iterativeScan`.
- `max_scan_tuples` (`int | None`, optional): Maximum tuples to scan during iterative filtering (1..2147483647). JSON: `maxScanTuples`.
- `scan_mem_multiplier` (`float | None`, optional): Multiplier on work_mem for iterative scanning (1.0..1000.0). JSON: `scanMemMultiplier`.

[Python](../../python.md)

Related types — open only those used by your request:

- [HnswIterativeScan](HnswIterativeScan.md)
