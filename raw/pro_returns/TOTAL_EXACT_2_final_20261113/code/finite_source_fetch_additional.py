"""Read public source files and retain HTTP failures, without authentication."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen
urls={
'Isbell1968':'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/344EA0110F34F24298FD42E14305F634/S0008439500056836a.pdf/a-note-on-exact-colimits.pdf',
'GoerssJardine2009':'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Goerss-Jardine2.pdf',
'LaanStrongFlat':'https://kodu.ut.ee/~vlaan/condo.pdf',
'Husainov2002Russian':'https://husainov51.narod.ru/files/rep2rus.pdf',
'Isbell1974attempt':'https://www.jstor.org/stable/pdf/1970960.pdf',
'Oberst1968attempt':'https://link.springer.com/content/pdf/10.1007/BF01111023.pdf',
'AdamekReiterman1975attempt':'https://www.ams.org/tran/1975-211-00/S0002-9947-1975-0376799-X/S0002-9947-1975-0376799-X.pdf',
}
outdir=Path(__file__).resolve().parents[1]/'sources'
def fetch(item):
 name,url=item
 try:
  with urlopen(url,timeout=30) as f:
   data=f.read();status=f.status;content_type=f.headers.get('content-type')
  saved=data.startswith(b'%PDF')
  if saved: (outdir/(name+'.pdf')).write_bytes(data)
  return name,status,content_type,len(data),'PDF saved' if saved else 'non-PDF response'
 except Exception as e: return name,type(e).__name__,str(e)
with ThreadPoolExecutor(max_workers=4) as pool:
 for result in pool.map(fetch,urls.items()): print(result,flush=True)
