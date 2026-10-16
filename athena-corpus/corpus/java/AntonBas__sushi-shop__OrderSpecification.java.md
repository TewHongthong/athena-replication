# backend/src/main/java/com/sushishop/order/OrderSpecification.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/order/OrderSpecification.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.order;

import com.sushishop.shared.service.LikePattern;
import org.springframework.data.jpa.domain.Specification;

public class OrderSpecification {
    public static Specification<Order> hasStatus(OrderStatus status) {
        return (root, query, cb) -> status == null ? null : cb.equal(root.get("status"), status);
    }

    public static Specification<Order> hasDeliveryMethod(DeliveryMethod method) {
        return (root, query, cb) -> method == null ? null : cb.equal(root.get("deliveryMethod"), method);
    }

    public static Specification<Order> hasPaymentMethod(PaymentMethod method) {
        return (root, query, cb) -> method == null ? null : cb.equal(root.get("paymentMethod"), method);
    }

    public static Specification<Order> hasSearch(String search) {
        return (root, query, cb) -> {
            if (search == null || search.isBlank()) return null;
            return cb.or(
                    cb.like(cb.lower(root.get("customerName")), LikePattern.containsIgnoreCase(search), LikePattern.ESCAPE),
                    cb.like(root.get("phone"), LikePattern.contains(search), LikePattern.ESCAPE)
            );
        };
    }
}
```
