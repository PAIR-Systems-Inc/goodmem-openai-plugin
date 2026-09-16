# Issue a scoped retrieval key

For an existing space, issue a key for the current human principal with an immutable
ceiling allowing retrieval. Both the principal and issuing key must already have
the required authority; a ceiling does not grant new permissions.
Read [create](../apikeys/create.md), [rules](../models/AccessPolicyRule.md),
[targets](../models/AccessPolicyTarget.md), [operations](../models/Operation.md),
[selectors](../models/Selector.md), and [resource kinds](../models/ResourceKind.md).
Persist `issued.raw_api_key` in your application's secret store before discarding
the response; it is returned only once. This example logs only the key ID.

```python
import os
from goodmem import Goodmem
from goodmem.models import AccessPolicyRule, AccessPolicyTarget, Operation, ResourceKind, Selector

with Goodmem(base_url=os.environ["GOODMEM_BASE_URL"], api_key=os.environ["GOODMEM_API_KEY"]) as client:
    target = AccessPolicyTarget(kind=ResourceKind.SPACE, resource_id=os.environ["GOODMEM_SPACE_ID"])
    issued = client.apikeys.create(authority_mode="SCOPED", ceiling=[
        AccessPolicyRule(operation=Operation.LIST_MEMORY, selector=Selector.EXACT, assigned_resource=target),
        AccessPolicyRule(operation=Operation.READ_MEMORY, selector=Selector.DIRECT_MEMBERS_OF, assigned_resource=target),
    ])
    print(issued.api_key_metadata.api_key_id)
```
