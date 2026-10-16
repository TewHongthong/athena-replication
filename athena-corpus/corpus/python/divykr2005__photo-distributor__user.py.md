# backend/schemas/user.py

- source repo: divykr2005/photo-distributor
- repo url: https://github.com/divykr2005/photo-distributor
- license: MIT
- created_at: 2026-08-08T13:49:07Z
- file path: backend/schemas/user.py
- commit: 56aac18393056585a8161c0b55610faf2900274e

```python
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    refresh_token: str
```
