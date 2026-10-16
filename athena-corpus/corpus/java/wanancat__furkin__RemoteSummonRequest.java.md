# src/main/java/com/wanancat/furkin/internal/contract/RemoteSummonRequest.java

- source repo: wanancat/furkin
- repo url: https://github.com/wanancat/furkin
- license: MIT
- created_at: 2026-09-19T18:53:15Z
- file path: src/main/java/com/wanancat/furkin/internal/contract/RemoteSummonRequest.java
- commit: 79335b3b0986a4a59414031b56b53b9a9669ce28

```java
package com.wanancat.furkin.internal.contract;

import com.mojang.datafixers.util.Either;
import net.minecraft.resources.ResourceKey;
import net.minecraft.server.level.ChunkHolder;
import net.minecraft.world.level.ChunkPos;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.chunk.ChunkAccess;

import java.util.List;
import java.util.UUID;
import java.util.concurrent.CompletableFuture;

/** 单个待处理远距召唤请求；可变状态只在服务端线程读写，后台只读构造后不变的快照字段。 */
final class RemoteSummonRequest {

    enum State {
        WAIT_CHUNK,
        WAIT_ENTITY_LOAD,
        TERMINAL
    }

    final long requestId;
    final UUID playerUuid;
    final UUID companionId;
    final UUID canonicalUuid;
    final ResourceKey<Level> targetDimension;
    final ChunkPos center;
    final int radius;
    final long deadlineGameTime;
    final RemoteSummonOrigin origin;
    final RemoteSummonFeedback feedback;

    State state = State.WAIT_CHUNK;
    boolean ticketAdded;
    final List<ChunkPos> ticketChunks = new java.util.ArrayList<>();
    boolean feedbackArmed;
    List<CompletableFuture<Either<ChunkAccess, ChunkHolder.ChunkLoadingFailure>>> loadFutures = List.of();
    RemoteSummonResult terminalResult;

    RemoteSummonRequest(long requestId, UUID playerUuid, UUID companionId,
                        UUID canonicalUuid, ResourceKey<Level> targetDimension,
                        ChunkPos center, int radius, long deadlineGameTime,
                        RemoteSummonOrigin origin, RemoteSummonFeedback feedback) {
        this.requestId = requestId;
        this.playerUuid = playerUuid;
        this.companionId = companionId;
        this.canonicalUuid = canonicalUuid;
        this.targetDimension = targetDimension;
        this.center = center;
        this.radius = radius;
        this.deadlineGameTime = deadlineGameTime;
        this.origin = origin;
        this.feedback = feedback;
    }
}```
