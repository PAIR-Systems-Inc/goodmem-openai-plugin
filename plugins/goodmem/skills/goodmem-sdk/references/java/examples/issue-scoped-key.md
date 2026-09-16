<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# Issue a scoped retrieval key

For an existing space, issue a key for the current human principal with an immutable
ceiling allowing retrieval. Both the principal and issuing key must already have
the required authority; a ceiling does not grant new permissions.
Read [create](../apikeys/create.md), [request](../models/CreateApiKeyRequest.md),
[rules](../models/AccessPolicyRule.md), [targets](../models/AccessPolicyTarget.md),
[operations](../models/Operation.md), [selectors](../models/Selector.md),
[resource kinds](../models/ResourceKind.md), and [typed IDs](../models/ResourceId.md).
Persist `issued.rawApiKey()` in your application's secret store before discarding
the response; it is returned only once. This example logs only the key ID.

```java
import ai.pairsys.goodmem.client.Goodmem;
import ai.pairsys.goodmem.client.models.*;
import java.util.List;

public class IssueScopedKeyExample {
    public static void main(String[] args) {
        try (Goodmem client = Goodmem.builder()
                .baseUrl(System.getenv("GOODMEM_BASE_URL"))
                .apiKey(System.getenv("GOODMEM_API_KEY"))
                .build()) {
            var target = new AccessPolicyTarget(ResourceKind.SPACE,
                ResourceId.from(System.getenv("GOODMEM_SPACE_ID")));
            var issued = client.apikeys.create(CreateApiKeyRequest.builder()
                .authorityMode(ApiKeyAuthorityMode.SCOPED)
                .ceiling(List.of(
                    new AccessPolicyRule(Operation.LIST_MEMORY, Selector.EXACT, target),
                    new AccessPolicyRule(Operation.READ_MEMORY, Selector.DIRECT_MEMBERS_OF, target)))
                .build());
            System.out.println(issued.apiKeyMetadata().apiKeyId());
        }
    }
}
```

[Java](../../java.md)
