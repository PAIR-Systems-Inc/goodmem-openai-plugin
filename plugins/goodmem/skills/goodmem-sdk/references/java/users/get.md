<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# users.get

Unified entry-point \u2014 the SOLE public `get` on this client.
 Mirrors Python's `client.users.get(id=..., email=...)` kwargs
 form and the AWS / GCP / Azure / OpenAI options-bag norm. The mutex
 (exactly one of the option fields must be set) is enforced in
 `UsersGetOptions`'s compact constructor.

```java
UserResponse get(UsersGetOptions opts)
```

[users](../users.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [UsersGetOptions](../models/UsersGetOptions.md)
