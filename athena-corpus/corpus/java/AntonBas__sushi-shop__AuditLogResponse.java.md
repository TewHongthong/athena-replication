# backend/src/main/java/com/sushishop/audit/dto/AuditLogResponse.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/audit/dto/AuditLogResponse.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.audit.dto;

import com.sushishop.shared.enums.AuditAction;
import io.swagger.v3.oas.annotations.media.Schema;

import java.time.LocalDateTime;

@Schema(description = "Audit log response")
public record AuditLogResponse(
        @Schema(description = "Log ID")
        Long id,

        @Schema(description = "Action performed")
        AuditAction action,

        @Schema(description = "Entity name")
        String entityName,

        @Schema(description = "Entity ID")
        Long entityId,

        @Schema(description = "Details")
        String details,

        @Schema(description = "Performed by")
        String performedBy,

        @Schema(description = "Performed at")
        LocalDateTime performedAt
) {
}```
