"""Extract the locally supplied primary PDFs used in the manuscript audit."""
from pathlib import Path
import subprocess, hashlib

root = Path(__file__).resolve().parents[2]
out = root/'research/a_pdf_text'
out.mkdir(parents=True, exist_ok=True)
paths = [
 'grothendieck/DER_II-b/DER_II-b_pages.pdf',
 'grothendieck/DER_XIIc-b/DER_XIIc-b_pages.pdf',
 'grothendieck/DER_XIII-a/DER_XIII-a_pages.pdf',
 'grothendieck/DER_XIII-b/DER_XIII-b_pages.pdf',
 'grothendieck/DER_XVI/DER_XVI_pages.pdf',
 'papers/Rezk_sharp/rezk-sharp-maps.pdf',
 'papers/Maltsiniotis2005_AMBP/AMBP_2005__12_1_1_0.pdf',
 'papers/Cisinski_Ast308/smf_ast_308.pdf',
]
log=[]
for rel in paths:
 p=root/'background'/rel
 target=out/(p.stem+'.txt')
 result=subprocess.run(['pdftotext','-layout',str(p),str(target)],capture_output=True,text=True)
 result.check_returncode()
 log.append(f'{rel}\nSHA256 {hashlib.sha256(p.read_bytes()).hexdigest()}\ntext {target.relative_to(root)} ({target.stat().st_size} bytes)\n{result.stderr.strip()}')
dest=root/'BISITE/code/a_extract_evidence.out.txt'
dest.write_text('\n\n'.join(log)+'\n')
print(f'Extracted {len(paths)} PDFs; log {dest}')
