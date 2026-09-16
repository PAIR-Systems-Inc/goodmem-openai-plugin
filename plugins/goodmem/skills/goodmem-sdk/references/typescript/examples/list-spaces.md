<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# List spaces

```ts
import { Goodmem } from "@pairsystems/goodmem";

const baseUrl = process.env.GOODMEM_BASE_URL;
if (!baseUrl) throw new Error("GOODMEM_BASE_URL is required");
const client = new Goodmem({ baseUrl, apiKey: process.env.GOODMEM_API_KEY });
for await (const space of await client.spaces.list()) {
  console.log(space.spaceId, space.name);
}
```

[TypeScript](../../typescript.md)
