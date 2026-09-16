# Issue a scoped retrieval key

For an existing space, issue a key for the current human principal with an immutable
ceiling allowing retrieval. Both the principal and issuing key must already have
the required authority; a ceiling does not grant new permissions.
Read [create](../apikeys/create.md), [request](../models/CreateApiKeyRequest.md),
[rules](../models/AccessPolicyRule.md), [targets](../models/AccessPolicyTarget.md),
[operations](../models/Operation.md), [selectors](../models/Selector.md), and
[resource kinds](../models/ResourceKind.md).
Persist `issued.rawApiKey` in your application's secret store before discarding the
response; it is returned only once. This example logs only the key ID.

```ts
import { Goodmem } from "@pairsystems/goodmem";

const client = new Goodmem({
  baseUrl: process.env.GOODMEM_BASE_URL!,
  apiKey: process.env.GOODMEM_API_KEY!,
});
const issued = await client.apikeys.create({
  authorityMode: "SCOPED",
  ceiling: [
    { operation: "LIST_MEMORY", selector: "EXACT",
      assignedResource: { kind: "SPACE", resourceId: process.env.GOODMEM_SPACE_ID! } },
    { operation: "READ_MEMORY", selector: "DIRECT_MEMBERS_OF",
      assignedResource: { kind: "SPACE", resourceId: process.env.GOODMEM_SPACE_ID! } },
  ],
});
console.log(issued.apiKeyMetadata?.apiKeyId);
```
