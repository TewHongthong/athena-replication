# src/podium/errors.py

- source repo: Nikhils-G/podium
- repo url: https://github.com/Nikhils-G/podium
- license: MIT
- created_at: 2026-09-26T18:48:58Z
- file path: src/podium/errors.py
- commit: 64d18bf7ed5c1eef58d5397ff282807ceb3bf23e

```python
"""Typed errors raised by services; mapped to HTTP responses once, in main.py."""


class PodiumError(Exception):
    status_code = 500
    code = "error"

    def __init__(self, message: str = "Something went wrong.", **details):
        super().__init__(message)
        self.message = message
        self.details = details


class NotFound(PodiumError):
    status_code = 404
    code = "not_found"


class Unauthorized(PodiumError):
    status_code = 401
    code = "unauthorized"


class Forbidden(PodiumError):
    status_code = 403
    code = "forbidden"


class Closed(PodiumError):
    """The action is outside its window (submissions closed, voting not open, ...)."""

    status_code = 403
    code = "closed"


class Conflict(PodiumError):
    status_code = 409
    code = "conflict"


class ValidationFailed(PodiumError):
    status_code = 422
    code = "validation_failed"

    def __init__(self, message: str = "Check the highlighted fields.", errors: dict | None = None):
        super().__init__(message)
        self.errors = errors or {}


class RateLimited(PodiumError):
    status_code = 429
    code = "rate_limited"

    def __init__(self, retry_after: int):
        super().__init__(f"Too many requests. Try again in {retry_after} seconds.")
        self.retry_after = retry_after
```
