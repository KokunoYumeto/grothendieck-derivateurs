"""Retrieve the ordinary public primary URLs used for the smash-route audit.

No credentials or access-control bypass are used. Failures are reported and do
not count as an opened original. Run from the DER_LOCALIZERS directory.
"""
from pathlib import Path
import subprocess
import urllib.request

SOURCES = [
    (
        "A3_CFFS_2015",
        "https://www.epfl.ch/labs/hessbellwald-lab/wp-content/uploads/2018/10/"
        "ChacholskiFarjounFloresScherer_gt-v19-n5-p07-published.pdf",
    ),
    (
        "A3_Bousfield_1994",
        "https://www.ams.org/journals/jams/1994-07-04/"
        "S0894-0347-1994-1257059-7/S0894-0347-1994-1257059-7.pdf",
    ),
]

for stem, url in SOURCES:
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read()
            print(stem, response.status, response.headers.get("Content-Type"),
                  len(data), url, flush=True)
        if not data.startswith(b"%PDF"):
            print(stem, "NOT_A_PDF", flush=True)
            continue
        path = Path("sources") / (stem + ".pdf")
        path.write_bytes(data)
        subprocess.run(["pdftotext", "-layout", str(path),
                        str(path.with_suffix(".txt"))], check=True)
        print(stem, "PDF_AND_TEXT_SAVED", flush=True)
    except Exception as error:
        print(stem, type(error).__name__, str(error), url, flush=True)
