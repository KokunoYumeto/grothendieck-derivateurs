#!/usr/bin/env python3
"""Compile the supplied standalone readers and record exact diagnostic counts."""
import argparse, hashlib, json, os, re, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'output'; RECORDS=OUT/'records'

def environment():
    env=os.environ.copy()
    local=ROOT/'work/texmf';fmt=local/'web2c/luahbtex';cache=ROOT/'work/texcache'
    if local.exists() and (fmt/'lualatex.fmt').exists():
        env['TEXMF']='{'+str(local)+',/usr/share/texlive/texmf-dist,/usr/share/texmf}'
        env['TEXFORMATS']=str(fmt)
        env['TEXMFCACHE']=str(cache);env['TEXMFVAR']=str(cache)
    return env

def sanitize(s):
    s=s.replace(str(ROOT),'[workspace]')
    s=re.sub(r'(?:[A-Za-z]:[\\/](?:Users|home)[\\/][^\s\n"<>]+|/(?:Users|home|root|workspace|tmp|opt|usr|var)/[^\s\n"<>]+)','[system path removed]',s)
    s=re.sub(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}','[e-mail address removed]',s)
    return s

def diagnostics(log):
    return dict(errors=re.findall(r'^.*\.(?:tex|sty|cls|def|cfg|fd|lua):\d+: .*|^! .*',log,re.M),
      undefined=re.findall(r'(?:Reference|Citation) `[^\n]*?undefined|There were undefined references',log),
      unsettled=re.findall(r'Label\(s\) may have changed|Rerun to get cross-references right|Rerun to get outlines right',log),
      warnings=re.findall(r'^(?:LaTeX|Package [\w-]+|Class [\w-]+) Warning:.*',log,re.M),
      backend_warnings=re.findall(r'^warning\s+\([^\n]*',log,re.M|re.I),
      missing_glyphs=re.findall(r'^Missing character:.*',log,re.M),
      largest_overfull_hbox_pt=max([float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',log)] or [0.0]),
      largest_overfull_vbox_pt=max([float(x) for x in re.findall(r'Overfull \\vbox \(([0-9.]+)pt too high\)',log)] or [0.0]),
      overfull_hbox=len(re.findall(r'Overfull \\hbox',log)),underfull_hbox=len(re.findall(r'Underfull \\hbox',log)),
      overfull_vbox=len(re.findall(r'Overfull \\vbox',log)),underfull_vbox=len(re.findall(r'Underfull \\vbox',log)))

def refresh_diagnostics():
    """Reparse saved final logs without rebuilding or altering a PDF."""
    for path in (RECORDS/'build').glob('DER_*.json'):
        result=json.loads(path.read_text())
        for old in result.get('passes',[]):
            log=path.with_name(path.stem+f'.pass{old["pass"]}.log')
            if log.exists():old.update(diagnostics(log.read_text()))
        path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')

def compile_one(path,passes=3):
    path=path.resolve();logs=RECORDS/'build';logs.mkdir(parents=True,exist_ok=True)
    rawdir=ROOT/'work/compile';rawdir.mkdir(parents=True,exist_ok=True)
    command=['lualatex','--no-shell-escape','-interaction=nonstopmode','-file-line-error','-halt-on-error',path.name]
    results=[]
    for i in range(1,passes+1):
        raw=rawdir/f'{path.stem}.pass{i}.stdout'
        with raw.open('w') as f:r=subprocess.run(command,cwd=path.parent,env=environment(),stdout=f,stderr=subprocess.STDOUT)
        log=path.with_suffix('.log').read_text(errors='replace') if path.with_suffix('.log').exists() else raw.read_text(errors='replace')
        sanitized=sanitize(log);(logs/f'{path.stem}.pass{i}.log').write_text(sanitized)
        d=diagnostics(sanitized);d['returncode']=r.returncode;d['pass']=i;results.append(d)
        print(json.dumps({'book':path.stem,'pass':i,'returncode':r.returncode,'errors':len(d['errors']),'missing_glyphs':len(d['missing_glyphs']),'warnings':len(d['warnings'])}),flush=True)
        if r.returncode or d['errors']:break
        if i>=2 and not d['unsettled'] and not d['undefined']:break
    page_match=re.search(r'Output written on .*?\((\d+) pages',log,re.S)
    result={'book':path.stem,'source_tex_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'passes':results,'pages':int(page_match.group(1)) if page_match else None,
      'compiled_without_errors':bool(results and results[-1]['returncode']==0 and not results[-1]['errors']),
      'pdf_bytes':path.with_suffix('.pdf').stat().st_size if path.with_suffix('.pdf').exists() else 0,
      'pdf_sha256':hashlib.sha256(path.with_suffix('.pdf').read_bytes()).hexdigest() if path.with_suffix('.pdf').exists() else None}
    (logs/f'{path.stem}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='passes'}),flush=True)
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('files',nargs='*',type=Path);ap.add_argument('--passes',type=int,default=3);ap.add_argument('--refresh-diagnostics',action='store_true');a=ap.parse_args()
    if a.refresh_diagnostics:refresh_diagnostics()
    failed=False
    for p in a.files:
        result=compile_one(p,a.passes);last=result['passes'][-1]
        failed|=not result['compiled_without_errors'] or bool(last['missing_glyphs'] or last['undefined'] or last['unsettled'])
    if failed:raise SystemExit(1)

if __name__=='__main__':main()
