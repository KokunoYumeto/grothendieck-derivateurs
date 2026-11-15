"""Fetch public primary texts; failures are retained in stdout."""
import urllib.request, re
from pathlib import Path
urls = {
'cambridge': 'https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/note-on-exact-colimits/344EA0110F34F24298FD42E14305F634',
'gabriel': 'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Gabriel-Ulmer.pdf',
'ams75': 'https://www.ams.org/journals/tran/1975-211-00/S0002-9947-1975-0376799-X/S0002-9947-1975-0376799-X.pdf'}
outdir = Path(__file__).resolve().parents[1] / 'sources'
outdir.mkdir(exist_ok=True)
for key, url in urls.items():
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = response.read()
            print(key, response.status, response.headers.get('content-type'), len(data))
        if data.startswith(b'%PDF'):
            (outdir / (key + '.pdf')).write_bytes(data)
        else:
            body = data.decode(errors='replace')
            print('\n'.join(re.findall(r'.{0,100}(?:citation_pdf_url|\.pdf).{0,200}', body)))
    except Exception as e:
        print(key, type(e).__name__, str(e))
