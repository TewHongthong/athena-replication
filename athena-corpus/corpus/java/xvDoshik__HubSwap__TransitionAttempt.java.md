# src/main/java/ru/heldyy/hubswap/gui/TransitionAttempt.java

- source repo: xvDoshik/HubSwap
- repo url: https://github.com/xvDoshik/HubSwap
- license: MIT
- created_at: 2026-08-04T22:22:23Z
- file path: src/main/java/ru/heldyy/hubswap/gui/TransitionAttempt.java
- commit: c6967c6dadcae0fd21acdf29749ea597bf6c7ad9

```java
package ru.heldyy.hubswap.gui;

public class TransitionAttempt {
    private final TransitionMode mode;
    private final int targetNumber;
    private final long startedAt;
    private final int hubDelay;
    private final int clickDelay;
    private final int confirmDelay;

    private boolean finished;

    public TransitionAttempt(TransitionMode mode, int targetNumber, int hubDelay, int clickDelay, int confirmDelay) {
        this.mode = mode;
        this.targetNumber = targetNumber;
        this.startedAt = System.currentTimeMillis();
        this.hubDelay = hubDelay;
        this.clickDelay = clickDelay;
        this.confirmDelay = confirmDelay;
        this.finished = false;
    }

    public TransitionMode getMode() {
        return mode;
    }

    public int getTargetNumber() {
        return targetNumber;
    }

    public long getStartedAt() {
        return startedAt;
    }

    public int getHubDelay() {
        return hubDelay;
    }

    public int getClickDelay() {
        return clickDelay;
    }

    public int getConfirmDelay() {
        return confirmDelay;
    }

    public boolean isFinished() {
        return finished;
    }

    public void finish() {
        this.finished = true;
    }
}```
