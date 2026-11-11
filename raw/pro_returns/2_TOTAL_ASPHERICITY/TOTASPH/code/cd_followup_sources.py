"""Fetch public primary references for the exactness follow-up investigation."""
from urllib.request import urlopen
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json, shutil, subprocess
root=Path(__file__).resolve().parents[2]
cache=root/'source_followup';cache.mkdir(exist_ok=True)
old=root/'TOTASPH/research/cd_AKR1981.pdf'
if old.exists():shutil.move(str(old),cache/'AKR1981.pdf')
urls={
'AKR1981':'https://dml.cz/bitstream/handle/10338.dmlcz/101753/CzechMathJ_31-1981-3_3.pdf',
'IsbellMitchell1976':'https://www.ams.org/journals/tran/1976-220-00/S0002-9947-1976-0404377-3/S0002-9947-1976-0404377-3.pdf',
'IsbellMitchell1973':'https://www.ams.org/journals/bull/1973-79-05/S0002-9904-1973-13296-3/S0002-9904-1973-13296-3.pdf',
'AdamekReiterman1975':'https://www.ams.org/journals/tran/1975-211-00/S0002-9947-1975-0376799-X/S0002-9947-1975-0376799-X.pdf',
'Isbell1974':'https://www.jstor.org/stable/pdf/1970960.pdf'
}
def get(item):
    name,url=item;p=cache/(name+'.pdf')
    try:
        if not p.exists():
            data=urlopen(url,timeout=25).read()
            if not data.startswith(b'%PDF'):raise ValueError('Response is not a PDF')
            p.write_bytes(data)
        return {'name':name,'url':url,'status':'available','bytes':p.stat().st_size}
    except Exception as e:return {'name':name,'url':url,'status':'unavailable','error':type(e).__name__+': '+str(e)}
with ThreadPoolExecutor(max_workers=4) as pool:
    for result in pool.map(get,urls.items()):print(json.dumps(result))
print('tesseract:',shutil.which('tesseract'))
