"""Retrieve primary sources used in the converse-Miller exploratory attack.

This is ordinary public-URL retrieval. Failed requests and non-PDF responses are
reported and are not worked around. Existing PDFs are retained.
"""
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("A3_Castellana_Flores_published", "https://www.ams.org/journals/tran/2015-367-02/S0002-9947-2014-06132-1/S0002-9947-2014-06132-1.pdf"),
    ("A3_Dwyer_Wilkerson_1990", "https://www.numdam.org/item/AST_1990__191__97_0.pdf"),
    ("A3_Flores_2007", "https://630d8d70-6fa8-4ac2-a19f-246ebe964ec3.filesusr.com/ugd/b82155_12a8f6e62ec34c9fbcd8b8ca25d7547a.pdf"),
    ("A3_Flores_Muro_2018", "https://arxiv.org/pdf/1707.07654"),
]
for stem, url in SOURCES:
    destination = ROOT / "sources" / (stem + ".pdf")
    try:
        if destination.exists():
            data = destination.read_bytes()
            status = "existing"
        else:
            with urllib.request.urlopen(url, timeout=45) as response:
                data = response.read()
            status = "downloaded"
        if not data.startswith(b"%PDF"):
            print(stem, "NON-PDF response; not retained", len(data))
            continue
        destination.write_bytes(data)
        subprocess.run(["pdftotext", "-layout", str(destination), str(destination.with_suffix(".txt"))], check=True)
        print(stem, status, len(data), "bytes; text extracted", url)
    except Exception as exc:
        print(stem, "FAILED", type(exc).__name__, str(exc), url)
