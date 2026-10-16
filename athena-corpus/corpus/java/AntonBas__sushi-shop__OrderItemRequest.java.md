# backend/src/main/java/com/sushishop/order/dto/request/OrderItemRequest.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/order/dto/request/OrderItemRequest.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.order.dto.request;

import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;

@Schema(description = "Single item in an order")
public record OrderItemRequest(
        @Schema(description = "Product ID", example = "1")
        @NotNull(message = "Product ID is required")
        Long productId,

        @Schema(description = "Quantity must be greater than 0")
        @NotNull(message = "Quantity is required")
        @Positive(message = "Quantity must be greater than 0")
        @Max(value = 99, message = "Quantity must be less than 100")
        Integer quantity
) {
}```
