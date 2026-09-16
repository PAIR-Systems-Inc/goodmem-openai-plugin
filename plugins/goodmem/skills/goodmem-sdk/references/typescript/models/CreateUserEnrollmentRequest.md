<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# CreateUserEnrollmentRequest

Options for issuing a one-time enrollment credential to the user named by the request path.

- `enrollmentId` (`string | null`, optional): Optional client-provided enrollment UUID; generated when omitted.
- `rotateExisting` (`boolean | null`, optional): Whether an existing live enrollment may be revoked and atomically replaced.

[TypeScript](../../typescript.md)
