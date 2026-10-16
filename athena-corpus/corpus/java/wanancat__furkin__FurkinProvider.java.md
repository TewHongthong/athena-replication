# src/main/java/com/wanancat/furkin/internal/capability/FurkinProvider.java

- source repo: wanancat/furkin
- repo url: https://github.com/wanancat/furkin
- license: MIT
- created_at: 2026-09-19T18:53:15Z
- file path: src/main/java/com/wanancat/furkin/internal/capability/FurkinProvider.java
- commit: 79335b3b0986a4a59414031b56b53b9a9669ce28

```java
package com.wanancat.furkin.internal.capability;

import net.minecraft.core.Direction;
import net.minecraft.nbt.CompoundTag;
import net.minecraftforge.common.capabilities.Capability;
import net.minecraftforge.common.capabilities.ICapabilitySerializable;
import net.minecraftforge.common.util.LazyOptional;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

/**
 * {@link FurkinData} 的 provider，挂到实体上暴露能力。
 *
 * <p>每个实体持有一个独立的 {@link FurkinData} 实例，随实体生命周期走。</p>
 */
public final class FurkinProvider implements ICapabilitySerializable<CompoundTag> {

    private final FurkinData data = new FurkinData();
    private final LazyOptional<FurkinData> holder = LazyOptional.of(() -> data);

    @NotNull
    @Override
    public <T> LazyOptional<T> getCapability(@NotNull Capability<T> cap, @Nullable Direction side) {
        if (cap == FurkinCapability.FURKIN_DATA) {
            return holder.cast();
        }
        return LazyOptional.empty();
    }

    @Override
    public CompoundTag serializeNBT() {
        return data.serializeNBT();
    }

    @Override
    public void deserializeNBT(CompoundTag nbt) {
        data.deserializeNBT(nbt);
    }

    /** 使能力失效（实体被移除时调用）。 */
    public void invalidate() {
        holder.invalidate();
    }
}
```
