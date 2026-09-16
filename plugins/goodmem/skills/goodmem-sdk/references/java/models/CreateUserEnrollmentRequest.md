<!-- sdk-ref package=ai.pairsys:goodmem-java registry=maven version=0.2.2 -->

# CreateUserEnrollmentRequest

Options for issuing a one-time enrollment credential to the user named by the request path.

Prefer `builder()` to the canonical record constructor.
 Builder-based call sites remain source-compatible when optional fields are added in later SDK versions.

- `enrollmentId` (`EnrollmentId`): Optional client-provided enrollment UUID; generated when omitted. Typed wrapper `EnrollmentId`; build from a raw string with `EnrollmentId.from(String)`.
- `rotateExisting` (`Boolean`): Whether an existing live enrollment may be revoked and atomically replaced.

[Java](../../java.md)

Related types — open only those used by your request:

- [EnrollmentId](EnrollmentId.md)
