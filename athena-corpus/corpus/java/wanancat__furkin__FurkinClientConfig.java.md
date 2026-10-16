# src/main/java/com/wanancat/furkin/internal/config/FurkinClientConfig.java

- source repo: wanancat/furkin
- repo url: https://github.com/wanancat/furkin
- license: MIT
- created_at: 2026-09-19T18:53:15Z
- file path: src/main/java/com/wanancat/furkin/internal/config/FurkinClientConfig.java
- commit: 79335b3b0986a4a59414031b56b53b9a9669ce28

```java
package com.wanancat.furkin.internal.config;

import net.minecraftforge.common.ForgeConfigSpec;

/**
 * furkin 客户端配置（CLIENT 类型 TOML）。
 *
 * <p><b>设计稿 §5 判据三</b>：客户端项走 {@code CLIENT} TOML，由玩家自己改。
 * 只放 tooltip / 界面偏好，不放任何影响平衡的数值。</p>
 */
public class FurkinClientConfig {

    private static final ForgeConfigSpec.Builder BUILDER = new ForgeConfigSpec.Builder();

    /** 是否在绒亲头顶显示状态图标。设计稿默认开启（唯一视觉辨识）。 */
    public static final ForgeConfigSpec.BooleanValue SHOW_STATUS_ICON = BUILDER
            .comment("Whether to render the status icon above companions.")
            .define("showStatusIcon", true);

    /** 是否显示装备属性加成 tooltip。 */
    public static final ForgeConfigSpec.BooleanValue SHOW_EQUIP_TOOLTIP = BUILDER
            .comment("Whether to show equipment attribute bonus tooltips.")
            .define("showEquipTooltip", true);

    public static final ForgeConfigSpec SPEC = BUILDER.build();
}
```
