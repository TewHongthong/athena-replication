# src/main/java/dev/aero/client/mixin/GameRendererAccess.java

- source repo: KingF3rdi/aero-client
- repo url: https://github.com/KingF3rdi/aero-client
- license: MIT
- created_at: 2026-09-20T13:19:19Z
- file path: src/main/java/dev/aero/client/mixin/GameRendererAccess.java
- commit: d8888aba64351257362cd47f69282311dd942c8f

```java
package dev.aero.client.mixin;

import net.minecraft.client.render.GameRenderer;
import net.minecraft.util.Identifier;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.gen.Invoker;

@Mixin(GameRenderer.class)
public interface GameRendererAccess {
    @Invoker("setPostProcessor")
    void aero$setPostProcessor(Identifier id);
}
```
