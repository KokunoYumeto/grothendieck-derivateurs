#!/usr/bin/env python3
"""Retrieve two primary papers for a scope check; this is not a proof test."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import subprocess
import urllib.request

root = Path(__file__).resolve().parents[1]
papers = {
    "A3_Hopkins_Ravenel_Wilson_1998_author2007":
        "https://math.jhu.edu/~wsw/papers2/math/32-finite-postnikov-H1R8W-1998.pdf",
    "A3_Hopkins_Ravenel_Wilson_1998_author1997":
        "https://www.sas.rochester.edu/mth/sites/doug-ravenel/mypapers/hrw.pdf",
    "A3_CCS_Postnikov_2007":
        "https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/CCScoversPublished.pdf",
}

def fetch(item):
    stem, url = item
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            data = response.read()
            status = response.status
        if not data.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF")
        dest = root / "sources" / (stem + ".pdf")
        dest.parent.mkdir(exist_ok=True)
        dest.write_bytes(data)
        subprocess.run(["pdftotext", "-layout", str(dest), str(dest.with_suffix(".txt"))], check=True)
        return {"source": url, "http_status": status, "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "local_input": dest.relative_to(root).as_posix(),
                "scope": "retrieved and extracted; mathematical reading recorded separately"}
    except Exception as error:
        return {"source": url, "error": type(error).__name__, "message": str(error)}

with ThreadPoolExecutor(max_workers=2) as pool:
    for result in pool.map(fetch, papers.items()):
        print(json.dumps(result, ensure_ascii=False))
