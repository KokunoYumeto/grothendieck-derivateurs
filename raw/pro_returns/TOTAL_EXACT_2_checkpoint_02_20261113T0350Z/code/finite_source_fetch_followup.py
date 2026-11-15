"""Fetch the additional opened primary research inputs, recording status.

These PDFs are source inputs, not authored deliverables, and are not
automatically licensed for redistribution in the output package.
"""
from pathlib import Path
from urllib.request import Request,urlopen
import json

targets={
 'HubickaNesetril2019.pdf':'https://arxiv.org/pdf/1606.07979',
 'AdamekReiterman1976.pdf':'https://dml.cz/bitstream/handle/10338.dmlcz/105677/CommentatMathUnivCarol_017-1976-1_8.pdf'
}
folder=Path(__file__).resolve().parent.parent/'sources'
for name,url in targets.items():
    try:
        with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as response:
            data=response.read();mime=response.headers.get('Content-Type','')
            record={'url':url,'status':response.status,'content_type':mime,'bytes':len(data)}
        if data.startswith(b'%PDF'):
            path=folder/name;path.write_bytes(data);record['saved_as']=str(path)
        else:record['saved_as']=None
    except Exception as error:record={'url':url,'error':str(error)}
    print(json.dumps(record),flush=True)
