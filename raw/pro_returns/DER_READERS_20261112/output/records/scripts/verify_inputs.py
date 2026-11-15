#!/usr/bin/env python3
"""Verify and safely extract the three supplied source archives.

The manifest's original-path column is deliberately never copied to outputs.
"""
import argparse,csv,hashlib,io,json,zipfile
from pathlib import Path,PurePosixPath

ARCHIVES={
 'DER_01_french_transcription.zip':'fr',
 'DER_02_english_translation.zip':'en',
 'DER_03_companion_newresults_conventions.zip':'comp',
}

def verify(source,work,record):
    rows=[];archives=[]
    for name,folder in ARCHIVES.items():
        p=source/name
        with zipfile.ZipFile(p) as z:
            entries=list(csv.DictReader(io.StringIO(z.read('MANIFEST.tsv').decode('utf-8-sig')),delimiter='\t'))
            assert entries,('empty manifest',name)
            keys=entries[0].keys()
            pathkey=next(k for k in keys if k.lower() in ('path','zip_path','path_in_zip','archive_path'))
            byteskey=next(k for k in keys if k.lower() in ('bytes','size','size_bytes'))
            hashkey=next(k for k in keys if 'sha256' in k.lower() or 'sha-256' in k.lower())
            for entry in entries:
                member=entry[pathkey];q=PurePosixPath(member)
                assert not q.is_absolute() and '..' not in q.parts and '\\' not in member,('unsafe member',name,member)
                data=z.read(member);actual=hashlib.sha256(data).hexdigest()
                assert len(data)==int(entry[byteskey]),('size mismatch',name,member)
                assert actual.lower()==entry[hashkey].lower(),('hash mismatch',name,member)
                dest=work/folder/Path(*q.parts);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
                rows.append({'archive':name,'path':member,'bytes':len(data),'sha256':actual,'role':entry.get('role',''),'verified':True})
            archives.append({'archive':name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'members_verified':len(entries)})
    record.mkdir(parents=True,exist_ok=True)
    with (record/'MANIFEST_VERIFIED.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['archive','path','bytes','sha256','role','verified'],delimiter='\t');w.writeheader();w.writerows(rows)
    (record/'INPUT_ARCHIVES.json').write_text(json.dumps(archives,indent=2)+'\n')
    print(json.dumps({'archives':len(archives),'verified_members':len(rows)}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('work',type=Path);p.add_argument('record',type=Path);a=p.parse_args();verify(a.source,a.work,a.record)
