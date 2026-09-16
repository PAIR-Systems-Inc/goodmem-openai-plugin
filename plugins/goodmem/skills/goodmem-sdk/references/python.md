<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# GoodMem Python SDK

[Published package 0.1.34](https://pypi.org/project/goodmem/0.1.34/); server guidance assumes GoodMem 1.0.320 or later.

Install `pip install goodmem==0.1.34` (Python 3.10+). Import `Goodmem` from
`goodmem`, pass `base_url` and `api_key` from the environment, and use the client
as a context manager. `AsyncGoodmem` uses `await` and async iteration.

Methods use keyword arguments. `Page`/`AsyncPage` iteration follows cursors,
including `apikeys.list`. Retrieval is a context-managed stream; `stream=False`
collects events. Preserve usable passages when a status reports synthesis failure.

Models are exported from `goodmem.models`. Model pages show Python field names;
optional fields can be omitted and `None` is allowed only where listed. Use the
operation signature to distinguish a flattened keyword API from a model argument.

Errors are exported from `goodmem`. `APIError` has `status_code`; subclasses include `AuthenticationError`,
`PermissionDeniedError`, `NotFoundError`, and `RateLimitError`. `NetworkError`
wraps transport failures. Keep provider error bodies and keys out of logs.

## Examples

- [Ingest retrieve](python/examples/ingest-retrieve.md)
- [Issue scoped key](python/examples/issue-scoped-key.md)
- [List spaces](python/examples/list-spaces.md)
- [Register embedder](python/examples/register-embedder.md)

## Namespaces

Open one index, then the needed operation and models. Search for a symbol inside this language directory when search is available; avoid reading whole directories.

- [access_policy](python/access_policy.md)
- [access_policy.grants](python/access_policy.grants.md)
- [access_policy.role_assignments](python/access_policy.role_assignments.md)
- [admin](python/admin.md)
- [admin.background_jobs](python/admin.background_jobs.md)
- [admin.license](python/admin.license.md)
- [admin.retrieve_memory_log_policies](python/admin.retrieve_memory_log_policies.md)
- [apikeys](python/apikeys.md)
- [embedders](python/embedders.md)
- [instance](python/instance.md)
- [llms](python/llms.md)
- [memories](python/memories.md)
- [ocr](python/ocr.md)
- [ping](python/ping.md)
- [rerankers](python/rerankers.md)
- [service_identities](python/service_identities.md)
- [spaces](python/spaces.md)
- [system](python/system.md)
- [user_enrollments](python/user_enrollments.md)
- [users](python/users.md)

[SDK rules](../SKILL.md)
