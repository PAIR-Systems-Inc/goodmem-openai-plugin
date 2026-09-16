<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# OcrDocumentMetadata

```ts

export type OcrDocumentMetadata = Omit<OcrDocumentRequest, "content">;
```

Effective request fields (including inherited fields and overrides):

- `endPage` (`number | null | undefined`, optional): 0-based inclusive end page
- `format` (`OcrInputFormat | null | undefined`, optional): Input format hint (AUTO, PDF, TIFF, PNG, JPEG, BMP)
- `includeMarkdown` (`boolean | null | undefined`, optional): Include markdown rendering in the response
- `includeRawJson` (`boolean | null | undefined`, optional): Include raw OCR JSON payload in the response
- `startPage` (`number | null | undefined`, optional): 0-based inclusive start page

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [OcrDocumentRequest](OcrDocumentRequest.md)
- [OcrInputFormat](OcrInputFormat.md)
