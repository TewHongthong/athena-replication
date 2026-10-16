# backend/src/main/java/com/sushishop/order/dto/response/OrderItemResponse.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/order/dto/response/OrderItemResponse.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.order.dto.response;

import io.swagger.v3.oas.annotations.media.Schema;

import java.math.BigDecimal;

@Schema(description = "Order item response")
public record OrderItemResponse(
        @Schema(description = "Product ID", example = "1")
        Long productId,

        @Schema(description = "Product name", example = "Maki")
        String productName,

        @Schema(description = "Quantity", example = "2")
        Integer quantity,

        @Schema(description = "Price per item", example = "250.00")
        BigDecimal unitPrice,

        @Schema(description = "Product main image")
        String mainImage
) {
}```
