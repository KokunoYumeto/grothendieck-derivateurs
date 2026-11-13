"""Retrieve openly linked primary PDFs for the Ramsey/atomic-topos route.

Run from the TOTEX2 directory or any other directory. This writes only to
TOTEX2/work/sources. The URLs were discovered in public primary-source pages.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'work' / 'sources'
DEST.mkdir(parents=True, exist_ok=True)
SOURCES = {
    'HarmanSnowden2024': 'https://arxiv.org/pdf/2204.04526',
    'Masulovic2026': 'https://arxiv.org/pdf/1703.04685',
    'Hubicka2025': 'https://arxiv.org/pdf/2009.00967',
    'HubickaNesetril2019': 'https://arxiv.org/pdf/1606.07979',
    'Caramello2013': 'https://arxiv.org/pdf/1301.0300',
    'NesetrilRodl1979': 'https://dml.cz/bitstream/handle/10338.dmlcz/101598/CzechMathJ_29-1979-2_6.pdf',
    'LaanEtAl2021': 'https://cgasa.sbu.ac.ir/article_101062_d711fecea7c3522ccce3292f904e4a6f.pdf',
}

def fetch(item):
    name, url = item
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(request, timeout=35) as response:
            data = response.read()
            final_url = response.url
        if not data.startswith(b'%PDF'):
            return f'{name}: NOT PDF, {len(data)} bytes, URL {final_url}'
        path = DEST / (name + '.pdf')
        path.write_bytes(data)
        subprocess.run(['pdftotext', '-layout', str(path), str(path.with_suffix('.txt'))], check=True)
        return f'{name}: obtained {len(data)} bytes; extracted text; URL {final_url}'
    except Exception as error:
        return f'{name}: {type(error).__name__}: {error}'

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(fetch, SOURCES.items()):
            print(result, flush=True)
