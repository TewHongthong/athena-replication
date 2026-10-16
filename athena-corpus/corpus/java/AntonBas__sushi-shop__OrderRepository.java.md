# backend/src/main/java/com/sushishop/order/OrderRepository.java

- source repo: AntonBas/sushi-shop
- repo url: https://github.com/AntonBas/sushi-shop
- license: MIT
- created_at: 2026-06-10T21:14:11Z
- file path: backend/src/main/java/com/sushishop/order/OrderRepository.java
- commit: ae80c5e6c234302eb7c645bea3a6e23c6b624ee4

```java
package com.sushishop.order;

import jakarta.annotation.Nonnull;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.data.jpa.repository.EntityGraph;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;
import java.util.Optional;

public interface OrderRepository extends JpaRepository<Order, Long>, JpaSpecificationExecutor<Order> {

    @Nonnull
    @EntityGraph(attributePaths = {"user"})
    Page<Order> findAll(@Nonnull Specification<Order> spec, @Nonnull Pageable pageable);

    @EntityGraph(attributePaths = {"user"})
    @Query("SELECT o FROM Order o WHERE o.user.email = :email ORDER BY o.createdAt DESC")
    Page<Order> findByUserEmail(@Param("email") String email, Pageable pageable);

    @Query("SELECT oi FROM OrderItem oi JOIN FETCH oi.product WHERE oi.order.id IN :orderIds")
    List<OrderItem> findItemsByOrderIds(@Param("orderIds") List<Long> orderIds);

    @EntityGraph(attributePaths = {"items", "items.product", "user"})
    @Nonnull
    Optional<Order> findById(@Nonnull Long id);

    @Query("SELECT o.user.email FROM Order o WHERE o.id = :id")
    Optional<String> findOwnerEmailById(@Param("id") Long id);
}```
