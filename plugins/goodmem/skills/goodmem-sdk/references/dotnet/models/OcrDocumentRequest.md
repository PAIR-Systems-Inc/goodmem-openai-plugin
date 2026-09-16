<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# OcrDocumentRequest

Request body for OCR document processing.

`Goodmem.Client.Models.OcrDocumentRequest`

- `Content` (`string?`): Base64-encoded document bytes JSON: `content`.
- `EndPage` (`int?`): 0-based inclusive end page JSON: `endPage`.
- `Format` (`OcrInputFormat?`): Input format hint (AUTO, PDF, TIFF, PNG, JPEG, BMP) JSON: `format`.
- `IncludeMarkdown` (`bool?`): Include markdown rendering in the response JSON: `includeMarkdown`.
- `IncludeRawJson` (`bool?`): Include raw OCR JSON payload in the response JSON: `includeRawJson`.
- `StartPage` (`int?`): 0-based inclusive start page JSON: `startPage`.

[.NET](../../dotnet.md)

Related types — open only those used by your request:

- [OcrInputFormat](OcrInputFormat.md)
