# scripts/generate_key.py

- source repo: Ayush1860/SecureRag
- repo url: https://github.com/Ayush1860/SecureRag
- license: MIT
- created_at: 2026-09-02T18:22:54Z
- file path: scripts/generate_key.py
- commit: a65d2f6f70fdc5dcb477d48353de0374853125e7

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from securerag.security.encryption import VectorStoreEncryptor

print(VectorStoreEncryptor().export_key_b64())
```
