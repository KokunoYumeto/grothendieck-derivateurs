"""Independent integer-only check of Part A's saved projectivity certificate.
This does not import the certificate-generation program or use its matrices.
"""
from pathlib import Path
import json
import sys
output_dir=Path(__file__).resolve().parent/'outputs'
base=Path(sys.argv[1]) if len(sys.argv)>1 else output_dir
p=json.loads((base/'projectivity_certificate.json').read_text(encoding='utf-8'))
d=json.loads((base/'main_counterexample_data.json').read_text(encoding='utf-8'))
M=d['multiplication']; action=d['right_action']
h=len(action); m=len(M); free=p['free_rank']; dim=m*free
assert p['module_rank']==h and dim==180

def matrix(a):
    v=[[0]*a['cols'] for _ in range(a['rows'])]
    for i,j,c in a['entries']:
        assert type(c) is int
        v[i][j]+=c
    return v
S=matrix(p['inclusion_S']); R=matrix(p['retraction_R'])
assert len(S)==dim and len(S[0])==h and len(R)==h and len(R[0])==dim
for i in range(h):
    for j in range(h):
        assert sum(R[i][k]*S[k][j] for k in range(dim))==int(i==j)
Schecks=Rchecks=0
for a in range(m):
    for j in range(h):
        transformed=[0]*dim
        for c in range(free):
            for g in range(m):
                transformed[c*m+M[g][a]]+=S[c*m+g][j]
        assert transformed==[S[k][action[j][a]] for k in range(dim)]
        Schecks+=dim
    for c in range(free):
        for g in range(m):
            transformed=[0]*h
            for x in range(h): transformed[action[x][a]]+=R[x][c*m+g]
            assert transformed==[R[x][c*m+M[g][a]] for x in range(h)]
            Rchecks+=h
report=json.dumps({'RS_identity_entries_checked':h*h,
    'S_equivariance_integer_entries_checked':Schecks,
    'R_equivariance_integer_entries_checked':Rchecks,
    'coefficient_ring':'Z','free_rank_over_ZM':free,
    'module_rank_over_Z':h,'result':'PASS'},indent=2)
output_dir.mkdir(parents=True,exist_ok=True)
(output_dir/'independent_projectivity_check.out').write_text(report+'\n',encoding='utf-8')
print(report)
