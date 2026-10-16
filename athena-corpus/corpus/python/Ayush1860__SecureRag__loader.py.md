# securerag/ingestion/loader.py

- source repo: Ayush1860/SecureRag
- repo url: https://github.com/Ayush1860/SecureRag
- license: MIT
- created_at: 2026-09-02T18:22:54Z
- file path: securerag/ingestion/loader.py
- commit: a65d2f6f70fdc5dcb477d48353de0374853125e7

```python
from pathlib import Path


def load_tagged_documents(root: str):
    root_path = Path(root)
    for path in root_path.glob("*/*/*.txt"):
        department = path.parent.parent.name
        clearance = path.parent.name
        yield path.read_text(encoding="utf-8"), {"department": department, "clearance": clearance, "source": path.name}


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 120) -> list[str]:
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks
```
