# Register an embedder

Register a known catalog model using an upstream provider key from the environment.
Read [create](../embedders/create.md), the
[known-model request](../models/EmbeddersCreateKnownWithoutCredentialsRequest.md), and
[provider key options](../models/ProviderApiKeyOptions.md) when adapting this.
The SDK fills provider settings from its model catalog. Attach the returned embedder ID
when creating a space; registration alone does not attach it to existing spaces.

```ts
import { Goodmem } from "@pairsystems/goodmem";

const client = new Goodmem({
  baseUrl: process.env.GOODMEM_BASE_URL!,
  apiKey: process.env.GOODMEM_API_KEY!,
});
const embedder = await client.embedders.create({
  displayName: "Document embeddings",
  modelIdentifier: "text-embedding-3-small",
}, { apiKey: process.env.OPENAI_API_KEY! });
console.log(embedder.embedderId);
```
