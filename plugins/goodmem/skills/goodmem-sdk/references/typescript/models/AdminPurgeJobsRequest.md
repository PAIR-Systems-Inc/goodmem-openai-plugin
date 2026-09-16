<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# AdminPurgeJobsRequest

- `olderThan` (`string`, required): ISO-8601 timestamp cutoff; only terminal jobs older than this instant are eligible.
- `statuses` (`Array<PurgeableBackgroundJobStatus>`, optional): Optional terminal background job statuses to target for purging. If omitted, all terminal statuses are eligible. Canonical values are BACKGROUND_JOB_SUCCEEDED, BACKGROUND_JOB_FAILED, and BACKGROUND_JOB_CANCELED. Short aliases SUCCEEDED, FAILED, and CANCELED are also accepted for compatibility.
- `dryRun` (`boolean`, optional): If true, report purge counts without deleting any rows.
- `limit` (`number`, optional): Maximum number of jobs to purge in this request. Must be >= 0; 0 means no limit.

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [PurgeableBackgroundJobStatus](PurgeableBackgroundJobStatus.md)
