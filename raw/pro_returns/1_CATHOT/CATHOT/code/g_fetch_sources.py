"""Download exact primary sources consulted for Part G; log failures without substitution."""
from pathlib import Path
import urllib.request, subprocess, hashlib
root=Path(__file__).resolve().parents[1]
sources={
'Miller1984':'https://math.mit.edu/~hrm/papers/miller-sullivan-conjecture.pdf',
'Fiedorowicz1984':'https://www.uio.no/studier/emner/matnat/math/MAT9580/gamle-undervisningsressurser/varen-2018/documents/fiedorowicz-classifying-spaces-of-topological-monoids-and-categories-amer-j-math-1984.pdf',
'Sweeney2025v1':'https://arxiv.org/pdf/2502.05276v1',
'Sweeney2026v2':'https://arxiv.org/pdf/2502.05276',
'MartinianSteinberg2025':'https://arxiv.org/pdf/2511.12657',
'CianciOttina2015':'https://arxiv.org/pdf/1512.06088',
'BenBassat2026':'https://arxiv.org/pdf/2610.38760',
'CarcaciaCampos2026':'https://arxiv.org/pdf/2611.09718',
}
for key,url in sources.items():
 p=root/'research'/f'{key}.pdf'
 try:
  data=p.read_bytes() if p.exists() else urllib.request.urlopen(url,timeout=45).read()
  if not data.startswith(b'%PDF'): raise ValueError('Not PDF bytes')
  p.write_bytes(data)
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
  print(key,url,len(data),hashlib.sha256(data).hexdigest())
 except Exception as e: print(key,url,'FAILED',type(e).__name__,str(e))
