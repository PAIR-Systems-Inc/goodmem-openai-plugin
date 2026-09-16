<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# AdminPurgeJobsRequest

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `olderThan` (`String`): ISO-8601 timestamp cutoff; only terminal jobs older than this instant are eligible.
- `statuses` (`java.util.List<PurgeableBackgroundJobStatus>`): Optional terminal background job statuses to target for purging. If omitted, all terminal statuses are eligible. Canonical values are BACKGROUND_JOB_SUCCEEDED, BACKGROUND_JOB_FAILED, and BACKGROUND_JOB_CANCELED. Short aliases SUCCEEDED, FAILED, and CANCELED are also accepted for compatibility.
- `dryRun` (`Boolean`): If true, report purge counts without deleting any rows.
- `limit` (`Integer`): Maximum number of jobs to purge in this request. Must be >= 0; 0 means no limit.

[Java](../../java.md)

Related types — open only those used by your request:

- [PurgeableBackgroundJobStatus](PurgeableBackgroundJobStatus.md)
