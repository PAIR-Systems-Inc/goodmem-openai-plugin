<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# users.delete

Delete a human user

Permanently soft-deletes the user and invalidates credentials acting for that subject. The GoodMem instance owner cannot be deleted; transfer ownership first. Repeating an authorized delete succeeds without rewriting audit data.

```java
void delete(String id)
```

```java
void delete(ai.pairsys.goodmem.client.models.UserId id)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
void delete(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[users](../users.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [UserId](../models/UserId.md)
