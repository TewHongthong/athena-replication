# src/main/java/com/wanancat/furkin/internal/contract/RemoteSummonFeedback.java

- source repo: wanancat/furkin
- repo url: https://github.com/wanancat/furkin
- license: MIT
- created_at: 2026-09-19T18:53:15Z
- file path: src/main/java/com/wanancat/furkin/internal/contract/RemoteSummonFeedback.java
- commit: 79335b3b0986a4a59414031b56b53b9a9669ce28

```java
package com.wanancat.furkin.internal.contract;

import net.minecraft.server.level.ServerPlayer;

import java.util.UUID;

/**
 * P2 远距召唤的异步终态回调。
 *
 * <p>只在请求已经进入 {@code WAIT_CHUNK} 并异步结束后调用；立即命中的结果由各自入口
 * 直接处理，不会触发本回调。回调在服务端线程执行，入口可据此发送本地化反馈或刷新
 * 绒亲录列表。</p>
 */
@FunctionalInterface
public interface RemoteSummonFeedback {

    RemoteSummonFeedback NONE = (player, companionId, result) -> {
    };

    void onTerminal(ServerPlayer player, UUID companionId, RemoteSummonResult result);
}```
