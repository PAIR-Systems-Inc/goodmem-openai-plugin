<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ocr.document

Runs layout-aware OCR on the provided document bytes and returns per-page results. When a page range is provided, only the inclusive subset is processed. Requires OCR_DOCUMENT permission.

```ts
document(request: OcrDocumentRequest, requestOptions?: RequestOptions): Promise<OcrDocumentResponseShape>
```

[ocr](../ocr.md) · [TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [OcrDocumentRequest](../models/OcrDocumentRequest.md)
- [RequestOptions](../models/RequestOptions.md)
