<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# LLMGetOptions

Typed query options for `client.llms.get`.

 Every field is optional; null values are omitted from the wire request.
 Construct via the fluent `Builder`:

```java
 LLMGetOptions opts = LLMGetOptions.builder()
     .includeCredentials(true)
     .build();

```

- `includeCredentials` (`Boolean`): Whether to return stored credentials. Also accepts include_credentials. Requires READ_LLM_CREDENTIALS in addition to READ_LLM.

[Java](../../java.md)
