# backend/src/main/java/com/sushishop/order/dto/response/OrderStatusUpdateResponse.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/order/dto/response/OrderStatusUpdateResponse.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.order.dto.response;

import io.swagger.v3.oas.annotations.media.Schema;

@Schema(description = "Order status update sent via WebSocket")
public record OrderStatusUpdateResponse(
        @Schema(description = "Order ID", example = "1")
        Long orderId,

        @Schema(description = "New order status", example = "COOKING")
        String status,

        @Schema(description = "Payment status", example = "PAID")
        String paymentStatus
) {
}```
