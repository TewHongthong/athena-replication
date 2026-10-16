# backend/repositories/user_repository.py

- source repo: divykr2005/photo-distributor
- repo url: https://github.com/divykr2005/photo-distributor
- license: MIT
- created_at: 2026-08-08T13:49:07Z
- file path: backend/repositories/user_repository.py
- commit: 56aac18393056585a8161c0b55610faf2900274e

```python
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from core.security import get_password_hash

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user_in: UserCreate) -> User:
        db_user = User(
            name=user_in.name,
            email=user_in.email,
            password_hash=get_password_hash(user_in.password)
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
```
