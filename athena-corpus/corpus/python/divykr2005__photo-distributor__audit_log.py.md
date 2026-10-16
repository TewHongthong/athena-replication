# backend/models/audit_log.py

- source repo: divykr2005/photo-distributor
- repo url: https://github.com/divykr2005/photo-distributor
- license: MIT
- created_at: 2026-08-08T13:49:07Z
- file path: backend/models/audit_log.py
- commit: 56aac18393056585a8161c0b55610faf2900274e

```python
import uuid
from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from database.session import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    guest_id = Column(UUID(as_uuid=True), index=True, nullable=True)
    event_id = Column(UUID(as_uuid=True), index=True, nullable=True)
    action = Column(String(255), nullable=False)
    timestamp = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
```
