"""Public-source retrieval used in the A.4 source audit; not a theorem test.

The downloaded third-party papers are research inputs excluded from archives.
"""
from pathlib import Path
import urllib.request

root = Path(__file__).resolve().parents[1]
for paper in ("2608.06104", "2608.26876"):
    url = "https://arxiv.org/pdf/" + paper
    try:
        with urllib.request.urlopen(url, timeout=15) as response:
            data = response.read()
            print(url, response.status, response.headers.get("content-type"), len(data))
            if data.startswith(b"%PDF"):
                path = root / "sources" / (paper + ".pdf")
                path.parent.mkdir(exist_ok=True)
                path.write_bytes(data)
                print(path.relative_to(root))
    except Exception as error:
        print(url, type(error).__name__, str(error)[:300])
