<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# PingStreamRequest

Request payload for a streaming ping session

```ts

export type PingStreamRequest = AtMostOne<PingStreamRequestBase, "payload" | "payloadSizeBytes">;
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [AtMostOne](AtMostOne.md)
- [PingStreamRequestBase](PingStreamRequestBase.md)
