# GoodMem Java SDK

Use `ai.pairsys:goodmem-java:@VERSION@` with JDK 21+. The synchronous `Goodmem`
and asynchronous `AsyncGoodmem` clients are `AutoCloseable`. Models live in
`ai.pairsys.goodmem.client.models`; options live in `.api`. Synchronous
`Page<T>` iteration follows cursors, including `apikeys.list`. Async methods
return `CompletableFuture<T>`. Retrieval is a closeable `RetrieveMemoryStream`.

This example uses an existing space with an embedder and waits for indexing:

```java
import ai.pairsys.goodmem.client.Goodmem;
import ai.pairsys.goodmem.client.RetrieveMemoryStream;
import ai.pairsys.goodmem.client.models.*;
import java.time.Duration;

public class GoodmemExample {
    public static void main(String[] args) throws Exception {
        try (Goodmem client = Goodmem.builder()
                .baseUrl(System.getenv("GOODMEM_BASE_URL"))
                .apiKey(System.getenv("GOODMEM_API_KEY"))
                .build()) {
            String spaceId = System.getenv("GOODMEM_SPACE_ID");
            Memory memory = client.memories.create(JsonMemoryCreationRequest.builder()
                .spaceId(spaceId)
                .originalContent("GoodMem stores and retrieves memories.")
                .build());
            long deadline = System.nanoTime() + Duration.ofMinutes(2).toNanos();
            while (!"COMPLETED".equals(String.valueOf(memory.processingStatus()))) {
                if ("FAILED".equals(String.valueOf(memory.processingStatus())))
                    throw new IllegalStateException("Memory processing failed; inspect job history in GoodMem.");
                if (System.nanoTime() >= deadline)
                    throw new IllegalStateException("Memory is still processing; retry retrieval later.");
                Thread.sleep(500);
                memory = client.memories.get(memory.memoryId());
            }
            try (RetrieveMemoryStream events = client.memories.retrieve("what does GoodMem do?", spaceId)) {
                for (RetrieveMemoryEvent event : events) {
                    if (event.retrievedItem() != null && event.retrievedItem().chunk() != null)
                        System.out.println(event.retrievedItem().chunk().chunk().chunkText());
                }
            }
        }
    }
}
```

`ApiException` carries the HTTP status; subclasses include `NotFoundException`
and `RateLimitException`. Keep keys in environment/configuration and avoid
logging raw provider errors. Request builders and typed options are described
in the versioned namespace links below; access uses policies, not public-read flags.
