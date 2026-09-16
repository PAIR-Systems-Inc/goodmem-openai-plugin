# Ingest and retrieve

Use an existing space with an embedder. Read [create](../memories/create.md),
[get](../memories/get.md), and [retrieve](../memories/retrieve.md) when adapting this.
The relevant request types are [text memory](../models/MemoryCreateTextRequest.md),
[memory metadata](../models/MemoryCreateMetadata.md), and
[retrieval options](../models/MemoriesRetrieveOptions.md).

```ts
import { Goodmem } from "@pairsystems/goodmem";

const client = new Goodmem({
  baseUrl: process.env.GOODMEM_BASE_URL!,
  apiKey: process.env.GOODMEM_API_KEY!,
});
const spaceId = process.env.GOODMEM_SPACE_ID!;
let memory = await client.memories.create({
  spaceId,
  originalContent: "GoodMem stores and retrieves memories.",
});
const deadline = Date.now() + 120_000;
while (memory.processingStatus !== "COMPLETED") {
  if (memory.processingStatus === "FAILED")
    throw new Error("Memory processing failed; inspect job history in GoodMem.");
  if (Date.now() >= deadline)
    throw new Error("Memory is still processing; retry retrieval later.");
  await new Promise(resolve => setTimeout(resolve, 500));
  memory = await client.memories.get(memory.memoryId);
}
for await (const event of client.memories.retrieve("what does GoodMem do?", { spaceIds: [spaceId] })) {
  if (event.retrievedItem?.chunk)
    console.log(event.retrievedItem.chunk.chunk.chunkText);
}
```
