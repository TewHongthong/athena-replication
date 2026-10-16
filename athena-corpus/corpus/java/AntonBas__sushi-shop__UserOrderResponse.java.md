# backend/src/main/java/com/sushishop/order/dto/response/UserOrderResponse.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/order/dto/response/UserOrderResponse.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.order.dto.response;

import com.sushishop.order.DeliveryMethod;
import com.sushishop.order.OrderStatus;
import com.sushishop.order.PaymentMethod;
import io.swagger.v3.oas.annotations.media.Schema;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;

@Schema(description = "User order response")
public record UserOrderResponse(
        @Schema(description = "Order ID", example = "1")
        Long id,

        @Schema(description = "User email", example = "user@example.com")
        String userEmail,

        @Schema(description = "Order status", example = "NEW")
        OrderStatus status,

        @Schema(description = "Delivery method", example = "DELIVERY")
        DeliveryMethod deliveryMethod,

        @Schema(description = "Payment method", example = "ONLINE")
        PaymentMethod paymentMethod,

        @Schema(description = "Payment status", example = "PAID")
        String paymentStatus,

        @Schema(description = "Total amount", example = "750.00")
        BigDecimal totalAmount,

        @Schema(description = "Order creation time")
        LocalDateTime createdAt,

        @Schema(description = "Order items")
        List<OrderItemResponse> items
) {
}```
