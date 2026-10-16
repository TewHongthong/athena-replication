# src/main/java/ru/heldyy/hubswap/gui/TransitionMode.java

- source repo: xvDoshik/HubSwap
- repo url: https://github.com/xvDoshik/HubSwap
- license: MIT
- created_at: 2026-08-04T22:22:23Z
- file path: src/main/java/ru/heldyy/hubswap/gui/TransitionMode.java
- commit: c6967c6dadcae0fd21acdf29749ea597bf6c7ad9

```java
package ru.heldyy.hubswap.gui;

public enum TransitionMode {
    CLASSIC("Classic"),
    LIGHT("Lite"),
    LIGHT120("Lite 1.20"),
    PRIME("Prime");

    private final String displayName;

    TransitionMode(String displayName) {
        this.displayName = displayName;
    }

    public String getDisplayName() {
        return displayName;
    }
}```
