#!/usr/bin/env python3
"""Public primary-source access attempts for the R19 source audit.

No credentials are used. HTTP failures are recorded rather than bypassed.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request, json, hashlib, datetime

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'notes'/'R19_public_sources'
DEST.mkdir(exist_ok=True)
URLS={
 'findings.ts':'https://raw.githubusercontent.com/Commutator-IO/grothendieck-project/main/src/content/findings.ts',
 'tree.json':'https://api.github.com/repos/Commutator-IO/grothendieck-project/git/trees/main?recursive=1',
 'mathlib44731.json':'https://api.github.com/repos/leanprover-community/mathlib4/pulls/44731',
 'LICENSE':'https://raw.githubusercontent.com/Commutator-IO/grothendieck-project/main/LICENSE',
}

def fetch(item):
    name,url=item
    row={'name':name,'url':url}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'DER-FOLLOWUP-source-audit/1.0'})
        with urllib.request.urlopen(req,timeout=20) as resp:
            data=resp.read()
            row.update(status=resp.status,content_type=resp.headers.get('content-type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        (DEST/name).write_bytes(data)
    except Exception as exc:
        row['error']=str(exc)
    return row

with ThreadPoolExecutor(max_workers=4) as pool:
    rows=list(pool.map(fetch,URLS.items()))
out={'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'attempts':rows}
(ROOT/'code'/'outputs'/'F_source_fetch.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
