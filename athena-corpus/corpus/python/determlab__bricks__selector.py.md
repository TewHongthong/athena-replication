# src/bricks/core/selector.py

- source repo: determlab/bricks
- repo url: https://github.com/determlab/bricks
- license: MIT
- created_at: 2026-06-11T00:07:52Z
- file path: src/bricks/core/selector.py
- commit: 6d401933bb7ae3024637171f649f7066edf256b2

```python
"""Brick selection strategies for narrowing a registry to task-relevant bricks.

Stage 1 of the two-stage architecture: selects a small pool of bricks
from a large registry before YAML composition.

Future strategies (not yet implemented):
- KeywordSelector: match task words against brick tags/descriptions
- SemanticSelector: embed task + brick descriptions, vector similarity top-k
- CategorySelector: parse task for category hints ("calculate" → math bricks)
- LLMPreFilterSelector: one cheap LLM call to pick categories, then filter
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from bricks.core.registry import BrickRegistry


class BrickSelector(ABC):
    """Protocol for selecting relevant bricks from a registry for a given task.

    Stage 1 of the two-stage architecture. Narrows a large registry
    down to a small pool of bricks relevant to the task at hand.

    Concrete implementations:
    - AllBricksSelector: returns everything (default, for small registries)
    """

    @abstractmethod
    def select(self, task: str, registry: BrickRegistry) -> BrickRegistry:
        """Select relevant bricks for a task.

        Args:
            task: Natural language task description.
            registry: Full brick registry to select from.

        Returns:
            A new BrickRegistry containing only the selected bricks.
        """
        ...


class AllBricksSelector(BrickSelector):
    """Returns all bricks from the registry.

    For small registries where filtering is unnecessary.
    This is the default selector.
    """

    def select(self, task: str, registry: BrickRegistry) -> BrickRegistry:
        """Return all bricks — no filtering.

        Args:
            task: Natural language task description (unused).
            registry: Full brick registry.

        Returns:
            The same registry, unmodified.
        """
        return registry
```
