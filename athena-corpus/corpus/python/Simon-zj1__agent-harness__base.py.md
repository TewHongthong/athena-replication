# harness/providers/base.py

- source repo: Simon-zj1/agent-harness
- repo url: https://github.com/Simon-zj1/agent-harness
- license: MIT
- created_at: 2026-09-22T17:43:10Z
- file path: harness/providers/base.py
- commit: c58b6f42c63cbc67f14b29049c084196ba5a1910

```python
"""Provider interface: one `chat` method, optional tool calling."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol


@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict[str, Any]
    raw_arguments: str = ""


@dataclass
class ChatResponse:
    text: str = ""
    tool_calls: list[ToolCall] = field(default_factory=list)
    tokens_in: int = 0
    tokens_out: int = 0
    model: str = ""
    finish_reason: str = ""
    raw: dict[str, Any] = field(default_factory=dict)
    cost_usd: float | None = None


class Provider(Protocol):
    name: str

    def chat(
        self,
        messages: list[dict[str, Any]],
        *,
        tools: list[dict[str, Any]] | None = None,
        temperature: float | None = None,
        max_tokens: int | None = None,
    ) -> ChatResponse: ...

    def available(self) -> tuple[bool, str]: ...


def message(role: str, content: str) -> dict[str, Any]:
    return {"role": role, "content": content}
```
