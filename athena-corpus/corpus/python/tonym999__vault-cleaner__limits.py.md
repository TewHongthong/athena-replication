# src/vault_cleaner/server/limits.py

- source repo: tonym999/vault-cleaner
- repo url: https://github.com/tonym999/vault-cleaner
- license: MIT
- created_at: 2026-07-18T09:39:13Z
- file path: src/vault_cleaner/server/limits.py
- commit: 1ab2eaed9c327e98fa8c8b169f9cc9b39a64f372

```python
"""Named request limits shared by the server children of issue #49."""

MIB = 1024 * 1024

MAX_EXPORT_BYTES = 32 * MIB
MAX_TOTAL_EXPORT_BYTES = 96 * MIB
MAX_JSON_BODY_BYTES = 1 * MIB

# Flask's application-wide guard covers the largest legal individual request.
# The narrower JSON and aggregate-export limits are enforced by the children
# that accept those bodies.
MAX_REQUEST_BODY_BYTES = MAX_EXPORT_BYTES
```
