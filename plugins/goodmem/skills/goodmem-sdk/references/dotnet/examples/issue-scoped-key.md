<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# Issue a scoped retrieval key

For an existing space, issue a key for the current human principal with an immutable
ceiling allowing retrieval. Both the principal and issuing key must already have
the required authority; a ceiling does not grant new permissions.
Read [create](../ApiKeys/CreateAsync.md), [request](../models/CreateApiKeyRequest.md),
[rules](../models/AccessPolicyRule.md), [targets](../models/AccessPolicyTarget.md),
[operations](../models/Operation.md), [selectors](../models/Selector.md), and
[resource kinds](../models/ResourceKind.md).
Persist `issued.RawApiKey` in your application's secret store before discarding the
response; it is returned only once. This example logs only the key ID.

```csharp
using Goodmem.Client;
using Goodmem.Client.Models;

using var client = new GoodmemClient(new GoodmemClientOptions {
    BaseUrl = Environment.GetEnvironmentVariable("GOODMEM_BASE_URL")!,
    ApiKey = Environment.GetEnvironmentVariable("GOODMEM_API_KEY"),
});
var target = new AccessPolicyTarget {
    Kind = ResourceKind.Space,
    ResourceId = Environment.GetEnvironmentVariable("GOODMEM_SPACE_ID"),
};
var issued = await client.ApiKeys.CreateAsync(new CreateApiKeyRequest {
    AuthorityMode = ApiKeyAuthorityMode.Scoped,
    Ceiling = new[] {
        new AccessPolicyRule { Operation = Operation.ListMemory, Selector = Selector.Exact, AssignedResource = target },
        new AccessPolicyRule { Operation = Operation.ReadMemory, Selector = Selector.DirectMembersOf, AssignedResource = target },
    },
});
Console.WriteLine(issued.ApiKeyMetadata?.ApiKeyId);
```

[.NET](../../dotnet.md)
