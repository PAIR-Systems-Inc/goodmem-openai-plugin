<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# Ocr.DocumentFromFileAsync

Run OCR over a local file. Any Content on is replaced by the file's base64-encoded bytes; other fields (page range, markdown, …) are preserved. The caller's request is never mutated.

```csharp
Task<OcrDocumentResponse> DocumentFromFileAsync(string filePath, OcrDocumentRequest? request = null, CancellationToken ct = default)
```

[Ocr](../Ocr.md) · [.NET](../../dotnet.md)

Related types — open only those used by your request:

- [OcrDocumentRequest](../models/OcrDocumentRequest.md)
