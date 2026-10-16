# backend/src/main/java/com/sushishop/auth/dto/response/ResendVerificationResponse.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/auth/dto/response/ResendVerificationResponse.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.auth.dto.response;

import io.swagger.v3.oas.annotations.media.Schema;

@Schema(description = "Resend verification cooldown status")
public record ResendVerificationResponse(
        @Schema(description = "Seconds until the next resend is allowed, 0 if allowed now", example = "60")
        int cooldownSeconds
) {
}
```
