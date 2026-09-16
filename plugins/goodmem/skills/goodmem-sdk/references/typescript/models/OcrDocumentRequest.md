<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# OcrDocumentRequest

Request body for OCR document processing.

- `content` (`string | null`, required): Base64-encoded document bytes
- `format` (`OcrInputFormat | null`, optional): Input format hint (AUTO, PDF, TIFF, PNG, JPEG, BMP)
- `includeRawJson` (`boolean | null`, optional): Include raw OCR JSON payload in the response
- `includeMarkdown` (`boolean | null`, optional): Include markdown rendering in the response
- `startPage` (`number | null`, optional): 0-based inclusive start page
- `endPage` (`number | null`, optional): 0-based inclusive end page

[TypeScript](../../typescript.md)

Related types — open only those used by your request:

- [OcrInputFormat](OcrInputFormat.md)
