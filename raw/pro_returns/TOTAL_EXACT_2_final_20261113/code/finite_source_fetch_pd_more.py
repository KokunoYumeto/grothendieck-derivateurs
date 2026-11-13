"""Archive opened primary sources for the finite-pd follow-up.

The fetch routine records redirects, byte counts and SHA-256 hashes and saves
only responses beginning with the PDF signature.  This is an access log, not
an automated extraction of mathematical claims.
"""
from concurrent.futures import ThreadPoolExecutor
import json

from finite_source_fetch_pd import fetch


TARGETS = {
    "JibladzePirashvili1991.pdf": "https://rmi.tsu.ge/~jib/pubs/jipicat.pdf",
    "Pirashvili2002_polynomial.pdf": "https://numdam.org/item/SB_1999-2000__42__369_0.pdf",
    "Pirashvili1996_kan.pdf": "https://archive.mpim-bonn.mpg.de/id/eprint/4178/1/preprint_1994_143.pdf",
}


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as pool:
        for record in pool.map(fetch, TARGETS.items()):
            print(json.dumps(record), flush=True)
