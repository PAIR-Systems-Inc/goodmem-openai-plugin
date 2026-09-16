<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# OcrDocumentFromPathRequest

```ts

export type OcrDocumentFromPathRequest = Prettify<OcrDocumentMetadata & {
    path: string | URL;
}>;
```

Effective request fields (including inherited fields and overrides):

- `endPage` (`number | null | undefined`, optional): 0-based inclusive end page
- `format` (`OcrInputFormat | null | undefined`, optional): Input format hint (AUTO, PDF, TIFF, PNG, JPEG, BMP)
- `includeMarkdown` (`boolean | null | undefined`, optional): Include markdown rendering in the response
- `includeRawJson` (`boolean | null | undefined`, optional): Include raw OCR JSON payload in the response
- `path` (`string | URL`, required):
- `startPage` (`number | null | undefined`, optional): 0-based inclusive start page

Helper definitions for the constraints above (kept here to avoid extra page reads):

```ts
export type Prettify<T> = {
    [K in keyof T]: T[K];
} & {};
```

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [OcrDocumentMetadata](OcrDocumentMetadata.md)
- [OcrInputFormat](OcrInputFormat.md)
