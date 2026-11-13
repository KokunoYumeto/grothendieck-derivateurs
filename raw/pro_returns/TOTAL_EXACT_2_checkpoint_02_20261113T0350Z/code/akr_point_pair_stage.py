"""A repaired admissible K2 point-pair attachment with a new cycle generator."""
from akr_stage_model import Cat,run,quotient_H
from pathlib import Path
import json
C=Cat();V=C.obj('V',1);W=C.obj('W',3)
for i in range(3):C.hom[V,W].add((i,))
original={(x,y):sorted(fs) for (x,y),fs in C.hom.items()}
for (x,y),fs in sorted(original.items()):
    for i,f in enumerate(fs):
        for j,g in enumerate(fs):C.qfilter(f'Q_{x}_{y}_{i}_{j}',x,y,f,g,45,3)
for x in (V,W):
    for y in (V,W):C.sum(f'S_{x}_{y}',x,y)
T=C.names.index('Q_0_1_0_1');b=sorted(C.hom[W,T])[0]
f=(b[0],);g=(b[1],)
Z,_=C.qfilter('Q_K2_point_pair',V,T,f,g,153,3)
vals,labs=quotient_H(C)
cycle_rank=len(C.hom[W,Z])-len(C.hom[V,Z])+len(vals[Z])
print(json.dumps({'pair':{'source':'V','target':C.names[T],'f':f,'g':g},'new_target':C.names[Z],'vertices':len(C.hom[V,Z]),'edges':len(C.hom[W,Z]),'graph_components':len(vals[Z]),'graph_cycle_rank':cycle_rank,'protected_copies':len(C.hom[T,Z])}),flush=True)
out=run(C,'K1_plus_point_pair_K2_s153',17)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
