Install `pip install goodmem==@VERSION@` (Python 3.10+). Import `Goodmem` from
`goodmem`, pass `base_url` and `api_key` from the environment, and use the client
as a context manager. `AsyncGoodmem` uses `await` and async iteration.

Methods use keyword arguments. `Page`/`AsyncPage` iteration follows cursors,
including `apikeys.list`. Retrieval is a context-managed stream; `stream=False`
collects events. Preserve usable passages when a status reports synthesis failure.

Model pages give the exact public import and Python field names;
optional fields can be omitted and `None` is allowed only where listed. Use the
operation signature to distinguish a flattened keyword API from a model argument.

Errors are exported from `goodmem`. `APIError` has `status_code`; subclasses include `AuthenticationError`,
`PermissionDeniedError`, `NotFoundError`, and `RateLimitError`. `NetworkError`
wraps transport failures. Keep provider error bodies and keys out of logs.
