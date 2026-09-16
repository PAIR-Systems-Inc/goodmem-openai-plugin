<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# UsersGetOptions

Unified options for `users.get` \u2014 pass exactly one of `id` or
 `email`. Mirrors Python's `client.users.get(id=..., email=...)`
 kwargs form so the surface is symmetric across SDKs. Per the
 options-bag convention used by AWS SDK v2, GCP, and the OpenAI Java
 SDK, this is the single entry-point \u2014 there are no separate
 `get(String)` / `getByEmail(String)` overloads.

- `id` (`String`): user UUID (mutually exclusive with `email`)
- `email` (`String`): user email (mutually exclusive with `id`)
- `includeDeleted` (`Boolean`): whether an authorized read may return a permanent tombstone

[Java](../../java.md)
