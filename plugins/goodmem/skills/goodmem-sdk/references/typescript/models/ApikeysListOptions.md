<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# ApikeysListOptions

- `subjectPrincipalId` (`string`, optional): Filter by exact subject-principal UUID
- `ownerPrincipalId` (`string`, optional): Filter by exact administrative-owner UUID
- `lifecycleState` (`"NOT_YET_VALID" | "USABLE" | "EXPIRED" | "REVOKED"`, optional): Filter by precise lifecycle state
- `view` (`"FULL" | "BASIC"`, optional): Metadata projection; omission defaults to FULL
- `maxResults` (`number`, optional): Page size; FULL defaults to 10 and permits at most 20, while BASIC defaults to 50 and permits at most 1,000
- `nextToken` (`string`, optional): Opaque continuation token returned by the preceding page

[TypeScript](../../typescript.md)
