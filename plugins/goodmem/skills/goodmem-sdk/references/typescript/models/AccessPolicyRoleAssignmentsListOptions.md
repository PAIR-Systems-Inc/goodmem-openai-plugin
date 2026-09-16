<!-- sdk-ref package=@pairsystems/goodmem registry=npm version=0.1.6 -->

# AccessPolicyRoleAssignmentsListOptions

- `resourceKind` (`"INSTANCE" | "SPACE"`, required): Required INSTANCE or SPACE kind
- `resourceId` (`string`, optional): Required space UUID; omitted for INSTANCE
- `includeRevoked` (`boolean`, optional): Include revoked history
- `maxResults` (`number`, optional): Page size; 0 or omission uses the default of 50, maximum 1,000
- `nextToken` (`string`, optional): Opaque continuation token

[TypeScript](../../typescript.md)
