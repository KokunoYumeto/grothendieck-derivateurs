"""Exact finite certificates for Parts A and B; no floating-point inference."""
from collections import Counter
from itertools import combinations, permutations
from math import factorial
import json

def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def canonical_cycle(c):
    i=c.index(min(c))
    return tuple(c[i:]+c[:i])

def face_cycle(c,deleted):
    remaining=sorted(set(c)-{deleted})
    ranks={v:i for i,v in enumerate(remaining)}
    return canonical_cycle([ranks[v] for v in c if v!=deleted])

report={}
fe1=(0,1,0,1)
assert (fe1[0],fe1[1]) == tuple(reversed((fe1[1],fe1[2])))
report['FE1_original']={'class_word':fe1,'alpha1':(0,1),'alpha4':(1,2),'reversal_orbit_size':2}

cyclic=[]
for m in (2,3,5,7):
    word=[(j+i)%m for j in range(m) for i in range(m)]
    assert all(tuple(word[j*m:(j+1)*m])==tuple((j+i)%m for i in range(m)) for j in range(m))
    seen=set();sizes=[]
    for t in permutations(range(m)):
        if t in seen:continue
        orbit={t[j:]+t[:j] for j in range(m)}
        seen.update(orbit);sizes.append(len(orbit))
    assert set(sizes)=={m} and len(seen)==factorial(m)
    cyclic.append({'m':m,'target_points':m*m,'class_orbits':len(sizes),'all_orbit_sizes':m,'augmentation_divisor':m})
report['cyclic_class_certificates']=cyclic

cycle=[1,3,2,4]
cut_rows=[]
for k in range(4):
    reading=cycle[k:]+cycle[:k]
    rank={x:i for i,x in enumerate(reading)}
    chi=lambda i,j:int(rank[j]<rank[i])
    vals={f'{i}{j}':chi(i,j) for i,j in ((1,2),(2,3),(1,3),(2,4),(1,4),(3,4))}
    e1=chi(1,2)+chi(2,3)-chi(1,3)
    e2=chi(1,2)+chi(2,4)-chi(1,4)
    e3=chi(1,2)+chi(2,3)+chi(3,4)-chi(1,4)
    assert (e1,e2,e3)==(1,0,1)
    cut_rows.append({'reading':reading,'chi':vals,'identities':(e1,e2,e3)})
report['linear_cyclic_cuts']=cut_rows

triangles=[(0,1,2),(0,2,1)]
columns=[]
for tail in permutations((1,2,3)):
    c=(0,)+tail
    column=[0,0]
    for i in range(4):column[triangles.index(face_cycle(list(c),i))]+=(-1)**i
    assert column==[0,0]
    columns.append({'cyclic_order':c,'boundary_column':column})
report['linear_cyclic_homology']={'d1':[0],'d2':[1,1],'d3':columns,'H2_rank':1}
report['circle_probability_equations']={'positive_triple':'t+t+(1-t)=1 => t=0','negative_triple':'t+(1-t)+(1-t)=1 => t=1','consistent':False}

cochain=[]
for r in range(2,6):
    vertices=tuple(range(2*r+2))
    primitive={tuple(range(1,r+1)):1}
    def d_value(values,face):
        return sum((-1)**i*values.get(face[:i]+face[i+1:],0) for i in range(len(face)))
    cocycle={s:d_value(primitive,s) for s in combinations(vertices,r+1)}
    assert all(d_value(cocycle,s)==0 for s in combinations(vertices,r+2))
    first=tuple(range(r+1));second=tuple(range(r+1,2*r+2))
    assert (cocycle[first],cocycle[second])==(1,0)
    faces=[[q[:i]+q[i+1:] for i in range(r+1)] for q in (first,second)]
    for p in (2,3,5):
        assert sum((-1)**i*primitive.get(f,0) for i,f in enumerate(faces[0]))%p==1
        assert sum((-1)**i*primitive.get(f,0) for i,f in enumerate(faces[1]))%p==0
    cochain.append({'r':r,'target_points':len(vertices),'face_arrows':2*(r+1),'block_values':[1,0],'d_squared_checks':len(list(combinations(vertices,r+2))),'primes_checked':[2,3,5]})
report['cocycle_face_families']=cochain

def chain_key(subsets,top_label,n):
    objs=tuple((len(s),top_label if len(s)==n+1 else 0) for s in subsets)
    maps=[]
    for s,t in zip(subsets,subsets[1:]):
        ranks={x:i for i,x in enumerate(sorted(t))}
        maps.append(tuple(ranks[x] for x in sorted(s)))
    return objs,tuple(maps)

flags=[]
for n in range(2,7):
    boundary=Counter();evaluation=0;terms=0
    for perm in permutations(range(n+1)):
        sign=parity(perm)
        subsets=[frozenset(perm[:j+1]) for j in range(n+1)]
        maxima=[max(s) for s in subsets]
        if all(maxima[j]<maxima[j+1] for j in range(n)):evaluation+=sign
        for label,coefficient in ((1,sign),(0,-sign)):
            terms+=1
            for j in range(n+1):
                key=chain_key(subsets[:j]+subsets[j+1:],label,n)
                boundary[key]+=coefficient*(-1)**j
    nonzero={k:v for k,v in boundary.items() if v}
    assert not nonzero and evaluation%2==1
    flags.append({'dimension':n,'signed_flag_terms':terms,'nonzero_boundary_coefficients':len(nonzero),'last_vertex_evaluation_mod_2':evaluation%2})
report['DF_integral_flag_cycles']=flags
print(json.dumps(report,indent=2))
