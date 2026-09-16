<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# ApiKeyListOptions

Typed query options for `client.apikeys.list`.

 Every field is optional; null values are omitted from the wire request.
 Construct via the fluent `Builder`:

```java
 ApiKeyListOptions opts = ApiKeyListOptions.builder()
     .subjectPrincipalId(SubjectPrincipalId.from("value"))
     .build();

```

- `subjectPrincipalId` (`SubjectPrincipalId`): Filter by exact subject-principal UUID
- `ownerPrincipalId` (`OwnerPrincipalId`): Filter by exact administrative-owner UUID
- `lifecycleState` (`ApiKeyResponseLifecycleState`): Filter by precise lifecycle state
- `view` (`ApikeysListView`): Metadata projection; omission defaults to FULL
- `maxResults` (`Integer`): Page size; FULL defaults to 10 and permits at most 20, while BASIC defaults to 50 and permits at most 1,000
- `nextToken` (`String`): Opaque continuation token returned by the preceding page

[Java](../../java.md)

Related types — open only those used by your request:

- [ApiKeyResponseLifecycleState](ApiKeyResponseLifecycleState.md)
- [ApikeysListView](ApikeysListView.md)
- [OwnerPrincipalId](OwnerPrincipalId.md)
- [SubjectPrincipalId](SubjectPrincipalId.md)
