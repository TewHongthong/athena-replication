# src/utils/debounce.js

- source repo: rolecraft-sh/rolecraft
- repo url: https://github.com/rolecraft-sh/rolecraft
- license: MIT
- created_at: 2026-06-12T15:31:13Z
- file path: src/utils/debounce.js
- commit: b74f936ad1dc051aa5b25ce3154fb532597e802a

```javascript
export const WATCH_DEBOUNCE_MS = 300

export function createDebouncer(waitMs) {
  const timers = new Map()

  function schedule(key, callback) {
    cancel(key)

    const timer = setTimeout(() => {
      timers.delete(key)
      void Promise.resolve()
        .then(callback)
        .catch(() => {})
    }, waitMs)

    timers.set(key, timer)
  }

  function cancel(key) {
    const timer = timers.get(key)
    if (!timer) return false

    clearTimeout(timer)
    timers.delete(key)
    return true
  }

  function cancelAll() {
    for (const timer of timers.values()) {
      clearTimeout(timer)
    }
    timers.clear()
  }

  return { schedule, cancel, cancelAll }
}
```
