# src/main/java/dev/aero/client/mixin/ExperienceBarMixin.java

- source repo: KingF3rdi/aero-client
- repo url: https://github.com/KingF3rdi/aero-client
- license: MIT
- created_at: 2026-09-20T13:19:19Z
- file path: src/main/java/dev/aero/client/mixin/ExperienceBarMixin.java
- commit: d8888aba64351257362cd47f69282311dd942c8f

```java
package dev.aero.client.mixin;

import dev.aero.client.AeroClient;
import net.minecraft.client.gui.DrawContext;
import net.minecraft.client.gui.hud.bar.ExperienceBar;
import net.minecraft.client.render.RenderTickCounter;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * The XP bar graphic itself (as opposed to the level-number text, see InGameHudMixin.aero$xpLevel)
 * lives on this dedicated Bar implementation as of 1.21.11.
 */
@Mixin(ExperienceBar.class)
public class ExperienceBarMixin {
    @Inject(method = "renderBar", at = @At("HEAD"), cancellable = true, require = 0)
    private void aero$hideXpBar(DrawContext context, RenderTickCounter tickCounter, CallbackInfo ci) {
        if (AeroClient.CONFIG != null && AeroClient.CONFIG.guiTweaks && !AeroClient.CONFIG.guiXp) {
            ci.cancel();
        }
    }
}
```
