from pathlib import Path
import subprocess

root=Path(__file__).resolve().parents[2]
sources={
 'htt':'papers/Lurie_HTT/HTT.pdf',
 'cisinski_catlr':'papers/Cisinski_CatLR/CatLR.pdf',
 'cisinski_ast308':'papers/Cisinski_Ast308/smf_ast_308.pdf',
 'maltsiniotis2005':'papers/Maltsiniotis2005_AMBP/AMBP_2005__12_1_1_0.pdf',
 'joyal':'papers/Joyal_quasicat/JoyalTheoryOfQuasiCategories.pdf',
 'evrard1975':'papers/Evrard1975/BSMF_1975__103__241_0.pdf',
}
out=root/'research'
out.mkdir(exist_ok=True)
log=[]
for name,source in sources.items():
 target=out/f'bc_{name}.txt'
 p=subprocess.run(['pdftotext','-layout',str(root/'background'/source),str(target)],capture_output=True,text=True)
 log.append(f'{source} -> {target.name}: return code {p.returncode}; {p.stderr.strip()}')
 if p.returncode: raise RuntimeError(p.stderr)
(root/'BISITE/code/bc_extract.out.txt').write_text('\n'.join(log)+'\n')
print('\n'.join(log))
