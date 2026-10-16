# backend/src/main/java/com/sushishop/auth/dto/request/ForgotPasswordRequest.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/auth/dto/request/ForgotPasswordRequest.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.auth.dto.request;

import com.sushishop.shared.service.EmailNormalizer;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

@Schema(description = "Forgot password request")
public record ForgotPasswordRequest(
        @NotBlank(message = "Email is required")
        @Email(message = "Invalid email format")
        @Schema(description = "Email", example = "user@example.com")
        String email) {

    public ForgotPasswordRequest {
        email = EmailNormalizer.normalize(email);
    }
}
```
