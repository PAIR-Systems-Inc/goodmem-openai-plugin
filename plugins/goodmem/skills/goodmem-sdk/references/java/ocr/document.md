<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# ocr.document

```java
OcrDocumentResponse document(OcrDocumentRequest request)
```

Run OCR on a document or image

Runs layout-aware OCR on the provided document bytes and returns per-page results. When a page range is provided, only the inclusive subset is processed. Requires OCR_DOCUMENT permission.

```java
OcrDocumentResponse document(java.nio.file.Path filePath)
```

Convenience overload: reads `filePath` from disk, base64-encodes
 the bytes, and POSTs the OCR request. The server auto-detects the
 document format from the bytes \u2014 pass an explicit format only if
 you have out-of-band knowledge the server can't infer. Mirrors
 Python's `ocr.document(file_path=...)` convenience.

[ocr](../ocr.md) · [Java](../../java.md)

Related types — open only those used by your request:

- [OcrDocumentRequest](../models/OcrDocumentRequest.md)
