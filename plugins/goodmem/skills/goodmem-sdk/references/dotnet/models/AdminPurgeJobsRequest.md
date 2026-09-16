<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# AdminPurgeJobsRequest

`Goodmem.Client.Models.AdminPurgeJobsRequest`

- `DryRun` (`bool?`): If true, report purge counts without deleting any rows. JSON: `dryRun`.
- `Limit` (`int?`): Maximum number of jobs to purge in this request. Must be >= 0; 0 means no limit. JSON: `limit`.
- `OlderThan` (`string?`): ISO-8601 timestamp cutoff; only terminal jobs older than this instant are eligible. JSON: `olderThan`.
- `Statuses` (`IReadOnlyList<PurgeableBackgroundJobStatus>?`): Optional terminal background job statuses to target for purging. If omitted, all terminal statuses are eligible. Canonical values are BACKGROUND_JOB_SUCCEEDED, BACKGROUND_JOB_FAILED, and BACKGROUND_JOB_CANCELED. Short aliases SUCCEEDED, FAILED, and CANCELED are also accepted for compatibility. JSON: `statuses`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [PurgeableBackgroundJobStatus](PurgeableBackgroundJobStatus.md)
