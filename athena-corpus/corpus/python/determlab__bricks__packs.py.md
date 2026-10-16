# src/bricks/packs.py

- source repo: determlab/bricks
- repo url: https://github.com/determlab/bricks
- license: MIT
- created_at: 2026-06-11T00:07:52Z
- file path: src/bricks/packs.py
- commit: 6d401933bb7ae3024637171f649f7066edf256b2

```python
"""Pack discovery — scans ``bricks.packs`` entry points at runtime."""

from __future__ import annotations

import importlib
import importlib.metadata

from bricks.core.registry import BrickRegistry
from bricks.errors import BricksConfigError


def discover_and_load(registry: BrickRegistry) -> int:
    """Discover installed brick packs and load them into *registry*.

    Iterates the ``bricks.packs`` entry point group, imports each pack's
    module, and calls its ``register(registry)`` function.

    Args:
        registry: The registry to populate with discovered bricks.

    Returns:
        Number of packs loaded.

    Raises:
        BricksConfigError: If no packs are installed.
    """
    eps = list(importlib.metadata.entry_points(group="bricks.packs"))
    if not eps:
        raise BricksConfigError("No brick packs installed. Run: pip install bricks-stdlib")
    for ep in eps:
        module = importlib.import_module(ep.value)
        module.register(registry)
    return len(eps)
```
