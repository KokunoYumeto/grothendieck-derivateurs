"""Fetch the primary shape paper used in finite_topos_shape_route.md.

The source is a research input, not an authored deliverable. This script
records the actual public response and a content hash; it grants no
permission to redistribute the downloaded source in the output package.
"""
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
import json

url = "https://arxiv.org/pdf/2608.17525"
target = Path(__file__).resolve().parent.parent / "sources" / "Lehner2026_shape.pdf"
try:
    with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=45) as response:
        data = response.read()
        record = {
            "url": url,
            "response_url": response.url,
            "status": response.status,
            "content_type": response.headers.get("Content-Type", ""),
            "bytes": len(data),
            "sha256": sha256(data).hexdigest(),
        }
    if data.startswith(b"%PDF"):
        target.write_bytes(data)
        record["saved_as"] = str(target)
    else:
        record["saved_as"] = None
except Exception as error:
    record = {"url": url, "error": str(error)}
print(json.dumps(record), flush=True)
