<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# Register an embedder

Register a known catalog model using an upstream provider key from the environment.
Read [create](../embedders/create.md) and the
[request fields](../models/EmbedderCreationRequest.md) when adapting this.
The convenience overload fills provider settings from its model catalog.
Attach the returned embedder ID when creating a space; registration alone does not
attach it to existing spaces.

```java
import ai.pairsys.goodmem.client.Goodmem;
import ai.pairsys.goodmem.client.models.EmbedderCreationRequest;

public class RegisterEmbedderExample {
    public static void main(String[] args) {
        try (Goodmem client = Goodmem.builder()
                .baseUrl(System.getenv("GOODMEM_BASE_URL"))
                .apiKey(System.getenv("GOODMEM_API_KEY"))
                .build()) {
            var embedder = client.embedders.create(EmbedderCreationRequest.builder()
                .displayName("Document embeddings")
                .modelIdentifier("text-embedding-3-small")
                .build(), System.getenv("OPENAI_API_KEY"));
            System.out.println(embedder.embedderId());
        }
    }
}
```

[Java](../../java.md)
