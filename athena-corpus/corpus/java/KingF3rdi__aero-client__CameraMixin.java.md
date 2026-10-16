# src/main/java/dev/aero/client/mixin/CameraMixin.java

- source repo: KingF3rdi/aero-client
- repo url: https://github.com/KingF3rdi/aero-client
- license: MIT
- created_at: 2026-09-20T13:19:19Z
- file path: src/main/java/dev/aero/client/mixin/CameraMixin.java
- commit: d8888aba64351257362cd47f69282311dd942c8f

```java
package dev.aero.client.mixin;

import dev.aero.client.AeroClient;
import net.minecraft.block.enums.CameraSubmersionType;
import net.minecraft.client.render.Camera;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

@Mixin(value = Camera.class, priority = 2000)
public class CameraMixin {
    @Inject(method = "getSubmersionType", at = @At("HEAD"), cancellable = true, require = 0)
    private void aero$noFog(CallbackInfoReturnable<CameraSubmersionType> cir) {
        if (AeroClient.CONFIG != null && (AeroClient.CONFIG.noFog || AeroClient.CONFIG.cleanWater)) {
            cir.setReturnValue(CameraSubmersionType.NONE);
        }
    }
}
```
