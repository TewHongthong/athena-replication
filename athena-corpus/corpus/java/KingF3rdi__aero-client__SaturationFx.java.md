# src/main/java/dev/aero/client/SaturationFx.java

- source repo: KingF3rdi/aero-client
- repo url: https://github.com/KingF3rdi/aero-client
- license: MIT
- created_at: 2026-09-20T13:19:19Z
- file path: src/main/java/dev/aero/client/SaturationFx.java
- commit: d8888aba64351257362cd47f69282311dd942c8f

```java
package dev.aero.client;

import dev.aero.client.mixin.GameRendererAccess;
import net.minecraft.client.MinecraftClient;
import net.minecraft.util.Identifier;

/** Color Saturation: runs one of the bundled post effects (aero:saturation_N, N in steps of 10) over the world. */
public final class SaturationFx {
    private SaturationFx() {}

    public static void tick(MinecraftClient mc) {
        var cfg = AeroClient.CONFIG;
        if (cfg == null || mc.gameRenderer == null) {
            return;
        }
        Identifier want = null;
        if (cfg.colorSaturation && mc.world != null) {
            int pct = Math.max(0, Math.min(200, Math.round(cfg.colorSaturationAmount / 10f) * 10));
            if (pct != 100) {
                want = Identifier.of(AeroClient.MOD_ID, "saturation_" + pct);
            }
        }
        Identifier cur = mc.gameRenderer.getPostProcessorId();
        if (want == null) {
            if (cur != null && AeroClient.MOD_ID.equals(cur.getNamespace())) {
                mc.gameRenderer.clearPostProcessor();
            }
        } else if (!want.equals(cur) && (cur == null || AeroClient.MOD_ID.equals(cur.getNamespace()))) {
            ((GameRendererAccess) mc.gameRenderer).aero$setPostProcessor(want);
        }
    }
}
```
