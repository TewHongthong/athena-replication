# backend/src/main/java/com/sushishop/auth/dto/request/LoginRequest.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/auth/dto/request/LoginRequest.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.auth.dto.request;

import com.sushishop.shared.service.EmailNormalizer;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

@Schema(description = "Login credentials")
public record LoginRequest(
        @Schema(description = "User email", example = "user@example.com")
        @Email(message = "Invalid email format")
        @NotBlank(message = "Email is required")
        @Size(max = 100, message = "Email must be less than 100 characters")
        String email,

        @Schema(description = "User password", example = "password123")
        @NotBlank(message = "Password is required")
        String password
) {

    public LoginRequest {
        email = EmailNormalizer.normalize(email);
    }
}
```
