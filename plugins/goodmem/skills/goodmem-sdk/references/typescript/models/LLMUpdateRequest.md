<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# LLMUpdateRequest

Request body for updating an existing LLM. All fields are optional - only specified fields will be updated. supportedModalities replaces the stored set only when the array contains at least one value; empty or omitted leaves it unchanged and does not count as an update by itself.

```ts

export type LLMUpdateRequest = AtMostOne<LLMUpdateRequestBase, "replaceLabels" | "mergeLabels">;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [AtMostOne](AtMostOne.md)
- [LLMUpdateRequestBase](LLMUpdateRequestBase.md)
