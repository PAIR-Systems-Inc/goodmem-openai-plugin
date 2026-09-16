<!-- sdk-ref package=goodmem registry=pypi version=0.1.34 -->

# ocr.document

Run OCR on a document or image

Run OCR on a document or image. Accepts either `file_path` (path to a local file, read and base64-encoded automatically) or `content` (base64-encoded bytes). The server auto-detects the document format; set `format` explicitly only if needed.

Args:
    content (str, optional): Base64-encoded document bytes. Mutually exclusive with `file_path`.
    end_page (int, optional): 0-based inclusive end page
    file_path (str, optional): Path to a local file to OCR. Mutually exclusive with `content`.
    format (OcrInputFormat, optional): Input format hint (AUTO, PDF, TIFF, PNG, JPEG, BMP)
    include_markdown (bool, optional): Include markdown rendering in the response
    include_raw_json (bool, optional): Include raw OCR JSON payload in the response
    start_page (int, optional): 0-based inclusive start page

Returns:
    OcrDocumentResponse

```python
ocr.document(*, content: 'str | None' = None, end_page: 'int | None' = None, file_path: 'str | None' = None, format: 'OcrInputFormat | None' = None, include_markdown: 'bool | None' = None, include_raw_json: 'bool | None' = None, start_page: 'int | None' = None) -> 'OcrDocumentResponse'
```

[ocr](../ocr.md) · [Python](../../python.md)

Related types — open only those used by your request:

- [OcrInputFormat](../models/OcrInputFormat.md)
