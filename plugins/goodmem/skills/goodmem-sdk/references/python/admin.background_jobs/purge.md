<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# admin.background_jobs.purge

Purge completed background jobs

Deletes terminal background jobs older than a retention cutoff.

Args:
    older_than (str): ISO-8601 timestamp cutoff; only terminal jobs older than this instant are eligible.
    statuses (list[PurgeableBackgroundJobStatus], optional): Optional terminal background job statuses to target for purging. If omitted, all terminal statuses are eligible. Canonical values are BACKGROUND_JOB_SUCCEEDED, BACKGROUND_JOB_FAILED, and BACKGROUND_JOB_CANCELED. Short aliases SUCCEEDED, FAILED, and CANCELED are also accepted for compatibility.
    dry_run (bool, optional): If true, report purge counts without deleting any rows.
    limit (int, optional): Maximum number of jobs to purge in this request. Must be >= 0; 0 means no limit.

Returns:
    AdminPurgeJobsResponse

```python
admin.background_jobs.purge(*, older_than: 'str', statuses: 'list[PurgeableBackgroundJobStatus] | None' = None, dry_run: 'bool | None' = None, limit: 'int | None' = None) -> 'AdminPurgeJobsResponse'
```

[admin.background_jobs](../admin.background_jobs.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [PurgeableBackgroundJobStatus](../models/PurgeableBackgroundJobStatus.md)
