# portfolio/postprocess_pptx.py

- source repo: sl2ver/wm811k-wafer-defect-classification
- repo url: https://github.com/sl2ver/wm811k-wafer-defect-classification
- license: MIT
- created_at: 2026-09-27T06:25:24Z
- file path: portfolio/postprocess_pptx.py
- commit: 43a5fb115f9c8b0ea8ee79c2e47970b9d0c819ed

```python
"""Turn off mid-word line breaks for Korean text in a .pptx (PowerPoint's default lets a
Korean word break anywhere). Adds latinLnBrk="0" to every <a:pPr> that lacks it and sets run language to ko-KR
(both are needed: PowerPoint ignores the flag on runs tagged en-US).

Usage:  python portfolio/postprocess_pptx.py portfolio/portfolio.pptx
"""
import re
import shutil
import sys
import zipfile
from pathlib import Path

src = Path(sys.argv[1])
tmp = src.with_suffix(".tmp.pptx")
n = 0
with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename.startswith("ppt/slides/slide") and item.filename.endswith(".xml"):
            s = data.decode("utf-8")
            s, k = re.subn(r"<a:pPr(?![^>]*latinLnBrk)", '<a:pPr latinLnBrk="0"', s)
            s = s.replace('lang="en-US"', 'lang="ko-KR"')  # Korean word-wrap needs a Korean run language
            n += k
            data = s.encode("utf-8")
        zout.writestr(item, data)
shutil.move(tmp, src)
print(f"latinLnBrk=0 added to {n} paragraphs, run language set to ko-KR in {src}")
```
