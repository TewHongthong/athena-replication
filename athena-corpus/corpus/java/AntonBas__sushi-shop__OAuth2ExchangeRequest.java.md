# backend/src/main/java/com/sushishop/auth/dto/request/OAuth2ExchangeRequest.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/auth/dto/request/OAuth2ExchangeRequest.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.auth.dto.request;

import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.NotBlank;

@Schema(description = "OAuth2 one-time exchange code request")
public record OAuth2ExchangeRequest(
        @NotBlank(message = "Code is required")
        @Schema(description = "One-time code issued after OAuth2 login")
        String code
) {
}
```
