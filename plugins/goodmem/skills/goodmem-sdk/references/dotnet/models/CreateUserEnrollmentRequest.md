<!-- sdk-ref package=PairSystems.Goodmem.Client registry=nuget version=2.0.2 -->

# CreateUserEnrollmentRequest

Options for issuing a one-time enrollment credential to the user named by the request path.

`Goodmem.Client.Models.CreateUserEnrollmentRequest`

- `EnrollmentId` (`string?`): Optional client-provided enrollment UUID; generated when omitted. JSON: `enrollmentId`.
- `RotateExisting` (`bool?`): Whether an existing live enrollment may be revoked and atomically replaced. JSON: `rotateExisting`.

[.NET](../../dotnet.md)
