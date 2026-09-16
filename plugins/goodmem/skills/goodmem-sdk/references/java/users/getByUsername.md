<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# users.getByUsername

Get user by username

Returns a user selected by exact username after applying READ_USER authority. includeDeleted permits an authorized caller to inspect a permanent tombstone; it does not grant additional authority. Missing and unauthorized matches both return 404 so this guessable identifier cannot reveal whether a user exists.

```java
UserResponse getByUsername(String username, java.util.Map<String, Object> query)
```

[users](../users.md) · [Java](../../java.md)
