"""Selected AKR attachments: test component injectivity and pair-path bounds.
This does not assert persistence at all stages. Source formulas imported from
supplied independent review implementation, reproduced in this deliverable.
"""
from pathlib import Path
import sys,json,importlib.util
root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('akr_indep',root/'code/topology_akr_reference.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def hquot(C,x):
    par=list(range(C.size[x]))
    def rt(a):
        while par[a]!=a:par[a]=par[par[a]];a=par[a]
        return a
    for f in C.hom.get((1,x),()):
        a,b=rt(f[0]),rt(f[1]);par[a]=b
    return [rt(a) for a in range(C.size[x])]

def induced(f,hx,hy):
    image={}
    for i,r in enumerate(hx):
        t=hy[f[i]]
        assert r not in image or image[r]==t
        image[r]=t
    return tuple(image[r] for r in sorted(image))

def path_bound(f,g):
    assert len(set(f))==len(f) and len(set(g))==len(g)
    ed={a:b for a,b in zip(f,g) if a!=b}; heads=set(ed.values())
    seen=set();mx=1
    for s in ed.keys()-heads:
        at=s;n=1
        while at in ed:
            seen.add(at);at=ed[at];n+=1
        seen.add(at);mx=max(mx,n)
    cyc=set(ed)-seen
    return mx,len(cyc)

out=[]
# Distinct representatives of first-stage quasi-filter types and index pairs.
for qname,inds in [('Q_0_1_0_1',(0,1)),('Q_0_1_0_1',(0,44)),('Q_0_1_0_1',(0,22)),
                   ('Q_0_1_0_2',(0,1)),('Q_0_1_0_2',(0,44)),('Q_0_1_0_2',(0,22))]:
    C=m.Cat();m.stage_K1(C);y=C.name.index(qname);fs=sorted(C.hom[(1,y)])
    f,g=fs[inds[0]],fs[inds[1]]
    z,alph,fail,sg=m.quasi_filter(C,'probe_K2',1,y,f,g,153)
    assert fail==0 and sg==1
    hy,hz=hquot(C,y),hquot(C,z)
    ha=[induced(a,hy,hz) for a in alph]
    hw=hquot(C,1)
    w_actions={induced(w,hw,hz) for w in C.hom[(1,z)]}
    reversed_actions=[w for w in w_actions if w[0]!=w[1] and tuple(reversed(w)) in w_actions]
    nonmono=[i for i,a in enumerate(ha) if len(set(a))!=len(a)]
    assert not nonmono
    bigger=[];cycles=[];maxu=maxh=0
    for i in range(len(alph)):
        for j in range(i+1,len(alph)):
            un,uc=path_bound(alph[i],alph[j]);hn,hc=path_bound(ha[i],ha[j])
            assert uc==0
            if hc:cycles.append((i,j,hc))
            if hn>un:bigger.append((i,j,un,hn))
            maxu=max(maxu,un);maxh=max(maxh,hn)
    record={'first_target':qname,'chosen_sorted_W_maps':inds,'new_points':C.size[z],
            'new_W_maps':len(C.hom[(1,z)]),'old_H_components':len(set(hy)),
            'new_H_components':len(set(hz)),'generator_count':len(alph),
            'noninjective_H_generators':nonmono,'distinct_W_component_actions':len(w_actions),'reversed_W_component_actions':reversed_actions,'tested_generator_pairs':len(alph)*(len(alph)-1)//2,
            'H_pair_cycles':cycles,'H_path_bound_larger_than_underlying':bigger,
            'maximum_underlying_path_vertices':maxu,'maximum_H_path_vertices':maxh}
    print(json.dumps(record),flush=True);out.append(record)
print(json.dumps({'cases':len(out),'scope':'selected K2 targets; every pair of their generating alpha maps; no universal assertion'}))
