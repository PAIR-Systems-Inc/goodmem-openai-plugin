<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# serviceIdentities.delete

Delete a service identity

Permanently soft-deletes the principal. Its stored credentials remain audit records but can no longer authenticate because their subject is deleted. Repeating an authorized delete succeeds without rewriting audit data.

```java
void delete(String id)
```

```java
void delete(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[serviceIdentities](../serviceIdentities.md) · [Java](../../java.md)
