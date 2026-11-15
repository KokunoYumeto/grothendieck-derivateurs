"""Primary-source access log for the finite-projective-dimension route."""
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
import json

targets = {
    "JohnsonMcCarthy1998.pdf": "https://www.ams.org/journals/tran/1998-350-04/S0002-9947-98-02067-4/S0002-9947-98-02067-4.pdf",
    "GaudensSchwartz2005.pdf": "https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2005.06.008.pdf",
    "Pirashvili1999_simplicial.pdf": "https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/C6CB4933C449C72D31F2948D9550477F/S0305004198003211a.pdf/simplicial_degrees_of_functors.pdf",
}
folder = Path(__file__).resolve().parent.parent / "sources"


def fetch(item):
    name, url = item
    try:
        with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=40) as response:
            data = response.read()
            record = {"url": url, "response_url": response.url, "status": response.status,
                      "content_type": response.headers.get("Content-Type", ""), "bytes": len(data)}
        if data.startswith(b"%PDF"):
            path = folder / name
            path.write_bytes(data)
            record.update(saved_as=str(path), sha256=sha256(data).hexdigest())
        else:
            record["saved_as"] = None
    except Exception as error:
        record = {"url": url, "error": str(error)}
    return record


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as pool:
        for record in pool.map(fetch, targets.items()):
            print(json.dumps(record), flush=True)
