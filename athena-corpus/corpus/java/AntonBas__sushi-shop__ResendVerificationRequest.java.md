# backend/src/main/java/com/sushishop/auth/dto/request/ResendVerificationRequest.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/auth/dto/request/ResendVerificationRequest.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.auth.dto.request;

import com.sushishop.shared.service.EmailNormalizer;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

@Schema(description = "Resend email verification request")
public record ResendVerificationRequest(
        @NotBlank(message = "Email is required")
        @Email(message = "Invalid email format")
        @Schema(description = "Email", example = "user@example.com")
        String email) {

    public ResendVerificationRequest {
        email = EmailNormalizer.normalize(email);
    }
}
```
