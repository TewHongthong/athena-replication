# src/main/java/dev/aero/client/mixin/BeaconBlockEntityRendererMixin.java

- source repo: KingF3rdi/aero-client
- repo url: https://github.com/KingF3rdi/aero-client
- license: MIT
- created_at: 2026-09-20T13:19:19Z
- file path: src/main/java/dev/aero/client/mixin/BeaconBlockEntityRendererMixin.java
- commit: d8888aba64351257362cd47f69282311dd942c8f

```java
package dev.aero.client.mixin;

import dev.aero.client.AeroClient;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

@Mixin(targets = "net.minecraft.client.render.block.entity.BeaconBlockEntityRenderer", priority = 2000)
public class BeaconBlockEntityRendererMixin {
    @Inject(method = "render", at = @At("HEAD"), cancellable = true, require = 0)
    private void aero$noBeacon(CallbackInfo ci) {
        if (AeroClient.CONFIG != null && AeroClient.CONFIG.noBeacons) {
            ci.cancel();
        }
    }

    @Inject(method = {"renderBeam(Lnet/minecraft/client/util/math/MatrixStack;Lnet/minecraft/client/render/VertexConsumerProvider;FFIII)V",
            "renderBeam(Lnet/minecraft/client/util/math/MatrixStack;Lnet/minecraft/client/render/VertexConsumerProvider;FJZIII)V"},
            at = @At("HEAD"), cancellable = true, require = 0)
    private static void aero$noBeaconStatic(CallbackInfo ci) {
        if (AeroClient.CONFIG != null && AeroClient.CONFIG.noBeacons) {
            ci.cancel();
        }
    }
}
```
