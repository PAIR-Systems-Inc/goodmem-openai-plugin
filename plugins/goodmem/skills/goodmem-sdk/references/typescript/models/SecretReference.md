<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# SecretReference

- `uri` (`string`, required): URI identifying where the secret can be resolved (e.g., vault://, env://)
- `hints` (`Record<string, string> | null`, optional): Optional metadata to help resolvers decode the secret (e.g., {"encoding":"base64"})

[TypeScript](../../typescript.md)
