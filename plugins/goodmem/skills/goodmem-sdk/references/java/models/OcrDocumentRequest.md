<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# OcrDocumentRequest

Request body for OCR document processing.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `content` (`String`): Base64-encoded document bytes
- `format` (`OcrInputFormat`): Input format hint (AUTO, PDF, TIFF, PNG, JPEG, BMP)
- `includeRawJson` (`Boolean`): Include raw OCR JSON payload in the response
- `includeMarkdown` (`Boolean`): Include markdown rendering in the response
- `startPage` (`Integer`): 0-based inclusive start page
- `endPage` (`Integer`): 0-based inclusive end page

[Java](../../java.md)

Related types — open only those used by your request:

- [OcrInputFormat](OcrInputFormat.md)
