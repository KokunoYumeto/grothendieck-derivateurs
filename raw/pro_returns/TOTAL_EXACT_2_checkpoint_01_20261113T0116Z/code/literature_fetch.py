from pathlib import Path
import urllib.request, subprocess, json, concurrent.futures
root=Path(__file__).resolve().parents[1]
dest=root/'work/sources';dest.mkdir(parents=True,exist_ok=True)
sources={
'Isbell1968':'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/344EA0110F34F24298FD42E14305F634/S0008439500056836a.pdf/a-note-on-exact-colimits.pdf',
'GabrielUlmer1971':'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Gabriel-Ulmer.pdf',
'AdamekReiterman1975':'https://www.ams.org/journals/tran/1975-211-00/S0002-9947-1975-0376799-X/S0002-9947-1975-0376799-X.pdf',
'Oberst1968':'https://link.springer.com/content/pdf/10.1007/BF01111023.pdf',
'Isbell1974':'https://www.jstor.org/stable/pdf/1970960.pdf',
'Ershad2016':'https://arxiv.org/pdf/1607.00906',
}
def fetch(item):
    name,url=item
    record={'name':name,'url':url}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        d=urllib.request.urlopen(req,timeout=40).read()
        record.update(bytes=len(d),pdf=d.startswith(b'%PDF'))
        if record['pdf']:
            p=dest/(name+'.pdf');p.write_bytes(d)
            result=subprocess.run(['pdftotext','-layout',str(p),str(dest/(name+'.txt'))],capture_output=True,text=True)
            record.update(pdftotext=result.returncode)
        else: record['head']=d[:100].decode('utf-8',errors='replace')
    except Exception as e:record.update(error=type(e).__name__+': '+str(e))
    return record
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    records=list(pool.map(fetch,sources.items()))
print(json.dumps(records,indent=2))
(root/'code/literature_fetch.out').write_text(json.dumps(records,indent=2)+'\n')
