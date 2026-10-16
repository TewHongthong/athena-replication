# src/main/java/com/wanancat/furkin/internal/capability/FurkinCapability.java

- source repo: wanancat/furkin
- repo url: https://github.com/wanancat/furkin
- license: MIT
- created_at: 2026-09-19T18:53:15Z
- file path: src/main/java/com/wanancat/furkin/internal/capability/FurkinCapability.java
- commit: 79335b3b0986a4a59414031b56b53b9a9669ce28

```java
package com.wanancat.furkin.internal.capability;

import com.wanancat.furkin.internal.FurkinMod;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.common.capabilities.Capability;
import net.minecraftforge.common.capabilities.CapabilityManager;
import net.minecraftforge.common.capabilities.CapabilityToken;
import net.minecraftforge.common.capabilities.RegisterCapabilitiesEvent;

/**
 * 绒亲能力注册点。
 *
 * <p>持有 {@link Capability}&lt;{@link FurkinData}&gt; 的静态引用，供全模组取用。
 * 注册走 {@link RegisterCapabilitiesEvent}。</p>
 */
public final class FurkinCapability {

    /** 能力标识（ResourceLocation）。 */
    public static final ResourceLocation ID = new ResourceLocation(FurkinMod.MODID, "furkin_data");

    /** 能力实例。 */
    public static final Capability<FurkinData> FURKIN_DATA = CapabilityManager.get(new CapabilityToken<>() {});

    private FurkinCapability() {
    }

    /** 在 {@link RegisterCapabilitiesEvent} 中调用，注册能力。 */
    public static void register(RegisterCapabilitiesEvent event) {
        event.register(FurkinData.class);
    }
}
```
