<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# llms.delete

Delete an LLM

Permanently deletes an LLM configuration. This operation cannot be undone and removes the LLM record and securely deletes stored credentials.

IMPORTANT: This does NOT invalidate or delete any previously generated content using this LLM - existing generations remain accessible. Requires DELETE_LLM on the requested LLM.

```java
void delete(String id)
```

```java
void delete(ai.pairsys.goodmem.client.models.LlmId id)
```

Domain-ID typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

```java
void delete(java.util.UUID id)
```

UUID-typed overload. Forwards to the String-typed sibling via `toString()` on the promoted argument.

[llms](../llms.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [LlmId](../models/LlmId.md)
