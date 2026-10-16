# scripts/refresh_token.py

- source repo: vikasiec/AI-Trading-App
- repo url: https://github.com/vikasiec/AI-Trading-App
- license: MIT
- created_at: 2026-09-25T18:06:05Z
- file path: scripts/refresh_token.py
- commit: beb8d00e020adcbdf2afc156bd87592daa40d881

```python
#!/usr/bin/env python3
"""Single-owner INDstocks token refresh.

Schedule this via cron on ONE machine/process only, before market open:

    # IST servers
    0 9 * * 1-5 /usr/bin/python3 /path/to/scripts/refresh_token.py

    # UTC servers
    30 3 * * 1-5 /usr/bin/python3 /path/to/scripts/refresh_token.py

Do NOT also call this from the main trading loop or the Telegram bot --
they should only read the cached token via jev_indstocks_trader.auth.get_cached_token().
Running this from more than one place will invalidate the token the
other processes are using.
"""
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from dotenv import load_dotenv  # noqa: E402

from jev_indstocks_trader.auth import INDstocksAuth  # noqa: E402
from jev_indstocks_trader.config import load_config  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

if __name__ == "__main__":
    load_dotenv()
    cfg = load_config()
    auth = INDstocksAuth(cfg.indstocks)
    auth.refresh_session()
    print("Token refreshed successfully.")
```
