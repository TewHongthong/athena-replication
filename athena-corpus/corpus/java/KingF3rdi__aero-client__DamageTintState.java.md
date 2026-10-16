# src/main/java/dev/aero/client/DamageTintState.java

- source repo: KingF3rdi/aero-client
- repo url: https://github.com/KingF3rdi/aero-client
- license: MIT
- created_at: 2026-09-20T13:19:19Z
- file path: src/main/java/dev/aero/client/DamageTintState.java
- commit: d8888aba64351257362cd47f69282311dd942c8f

```java
package dev.aero.client;

import net.minecraft.client.render.entity.state.LivingEntityRenderState;
import net.minecraft.client.render.entity.state.PlayerEntityRenderState;

/** Shared state for the Damage Tint mixins: the flash moves from the skin to the armor. */
public final class DamageTintState {
    public static final ThreadLocal<Boolean> ARMOR_HURT = ThreadLocal.withInitial(() -> false);

    public static int armorBegin;
    public static int equipHits;
    public static int equipHurtHits;

    private DamageTintState() {}

    public static boolean on(LivingEntityRenderState state) {
        return AeroClient.CONFIG != null && AeroClient.CONFIG.damageTint && state instanceof PlayerEntityRenderState;
    }
}
```
