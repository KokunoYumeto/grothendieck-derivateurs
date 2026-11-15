"""Retrieve primary literature for the source audit; no authentication or mirror bypass."""
from pathlib import Path
import urllib.request, json
ROOT=Path(__file__).resolve().parent
URLS={
 "IsbellMitchell1976.pdf":"https://www.ams.org/journals/tran/1976-220-00/S0002-9947-1976-0404377-3/S0002-9947-1976-0404377-3.pdf",
 "AdamekReiterman1976.pdf":"https://dml.cz/bitstream/handle/10338.dmlcz/105677/CommentatMathUnivCarol_017-1976-1_8.pdf",
}
out=[]
for name,url in URLS.items():
 try:
  with urllib.request.urlopen(url,timeout=30) as r: data=r.read()
  if not data.startswith(b"%PDF"): raise ValueError("response is not a PDF")
  (ROOT/name).write_bytes(data)
  out.append({"file":name,"url":url,"bytes":len(data),"status":"downloaded"})
 except Exception as e:
  out.append({"file":name,"url":url,"status":"unavailable","reason":str(e)})
print(json.dumps(out,indent=2))
(ROOT/"source_fetch.out").write_text(json.dumps(out,indent=2)+"\n")
