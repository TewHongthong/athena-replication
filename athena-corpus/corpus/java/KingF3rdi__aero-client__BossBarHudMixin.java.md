# src/main/java/dev/aero/client/mixin/BossBarHudMixin.java

- source repo: KingF3rdi/aero-client
- repo url: https://github.com/KingF3rdi/aero-client
- license: MIT
- created_at: 2026-09-20T13:19:19Z
- file path: src/main/java/dev/aero/client/mixin/BossBarHudMixin.java
- commit: d8888aba64351257362cd47f69282311dd942c8f

```java
package dev.aero.client.mixin;

import dev.aero.client.AeroClient;
import net.minecraft.client.gui.hud.BossBarHud;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

@Mixin(value = BossBarHud.class, priority = 2000)
public class BossBarHudMixin {
    @Inject(method = "render", at = @At("HEAD"), cancellable = true, require = 0)
    private void aero$hide(CallbackInfo ci) {
        if (AeroClient.CONFIG != null && (AeroClient.CONFIG.hideBossBar
                || (AeroClient.CONFIG.guiTweaks && !AeroClient.CONFIG.guiBossBar))) {
            ci.cancel();
        }
    }
}
```
