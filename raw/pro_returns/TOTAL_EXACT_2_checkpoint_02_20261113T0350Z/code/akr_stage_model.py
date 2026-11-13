"""Exact finite AKR stage-one calculation, plus selected stage-two attachments.
All categories are concrete categories of injections; equal functions are equal arrows.
Integral nerve homology is computed by elementary unit cancellations over Z.
A nonunit residual would be reported, never treated as torsion-free.
"""
from collections import defaultdict
from fractions import Fraction
import json, sys
from pathlib import Path

class Cat:
    def __init__(self):
        self.size=[]; self.names=[]; self.hom=defaultdict(set); self.source_rule_failures=[]
    def obj(self,name,n):
        x=len(self.size); self.size.append(n); self.names.append(name)
        self.hom[x,x].add(tuple(range(n))); return x
    def new_target(self,name,maps,universe=None):
        # maps list (old source, tuple of points in a fresh target)
        points=sorted(set(v for _,f in maps for v in f) if universe is None else set(universe),key=repr)
        ix={p:i for i,p in enumerate(points)}
        z=self.obj(name,len(points)); old=z
        for y,f in maps:
            f=tuple(ix[v] for v in f)
            for x in range(old):
                for g in list(self.hom.get((x,y),())):
                    self.hom[x,z].add(tuple(f[t] for t in g))
        return z
    def qfilter(self,name,x,y,f,g,s,n=None):
        fixed={f[a] for a in range(self.size[x]) if f[a]==g[a]}
        edges={f[a]:g[a] for a in range(self.size[x]) if f[a]!=g[a]}
        indeg=set(edges.values()); active=set(edges)|indeg
        paths=[]
        for v in sorted(set(edges)-indeg):
            path=[v]
            while path[-1] in edges: path.append(edges[path[-1]])
            paths.append(path)
        assert set(t for p in paths for t in p)==active, 'directed cycle forbidden'
        needed=max([len(p) for p in paths]+[1])
        n=max(n or 1,needed)
        if n%2==0:n+=1
        k=(s-1)//4; assert s==4*k+1 and k>=n
        coords={v:(j,t) for j,p in enumerate(paths) for t,v in enumerate(p)}
        def beta(i,t,path_n):
            if i<=2*k:
                z=t+i
                return z if z<=2*k else z+2*k-path_n+1
            z=t-i+6*k-path_n+2
            return z if z>2*k else t-i+4*k
        maps=[]
        for i in range(s):
            a=[]
            for v in range(self.size[y]):
                if v in fixed:a.append(('fixed',v))
                elif v in active:
                    j,t=coords[v]; path_n=n if '--literal-common-n' in sys.argv else len(paths[j]); a.append(('path',j,beta(i,t,path_n)))
                else:a.append(('private',v,i))
            assert len(set(a))==len(a)
            maps.append((y,tuple(a)))
        universe=[('fixed',v) for v in fixed]+[('private',v,i) for v in range(self.size[y]) if v not in fixed|active for i in range(s)]+[('path',j,t) for j in range(len(paths)) for t in range(s)]
        z=self.new_target(name,maps,universe)
        alphas=sorted(self.hom[y,z])
        # Equal consecutive maps follow the prescribed quasi-filter identities;
        # verification works on maps before sorting, where cyclic order matters.
        aa=[a for _,a in maps]
        # In the f=coordinate 0, g=coordinate 1 convention the signed
        # neighbour sequence has 2k positive, 2k-1 negative, and two zero terms.
        for i in range(s):
            h,h2=(g,f) if i<2*k else ((g,g) if i==2*k else ((f,g) if i<4*k else (f,f)))
            assert tuple(aa[i][t] for t in h)==tuple(aa[(i+1)%s][t] for t in h2)
        images=[set(a) for a in aa]
        for i in range(s):
            found=False
            for h in (f,g):
                for h2 in (f,g):
                    v1=tuple(aa[i][t] for t in h)
                    v2=tuple(aa[(i+1)%s][t] for t in h2)
                    if v1==v2:
                        found=True
                        valid=(images[i]&images[(i+1)%s]==set(v1))
                        if not valid:
                            failure={'rule':'AKR (11)','target':name,'index':i,'overlap_size':len(images[i]&images[(i+1)%s]),'composite_image_size':len(set(v1))}
                            if '--literal-common-n' in sys.argv:self.source_rule_failures.append(failure)
                            else:raise AssertionError(failure)
            assert found, 'quasi-filter neighbour relation'
            for step in range(1,s-2*n+1):
                assert images[i]&images[(i+step)%s] <= images[i]&images[(i+1)%s], 'AKR (10+)'
                assert images[i]&images[(i-step)%s] <= images[i]&images[(i-1)%s], 'AKR (10-)'
        inverse=[{a[v]:v for v in active} for a in aa]
        for i in range(s):
            for j in range(s):
                differences=set()
                for pt in inverse[i].keys()&inverse[j].keys():
                    v,w=inverse[i][pt],inverse[j][pt]
                    assert coords[v][0]==coords[w][0]
                    differences.add(coords[w][1]-coords[v][1])
                assert len(differences)<=1, 'AKR (9)'
        return z,n
    def sum(self,name,x,y):
        return self.new_target(name,[(x,tuple(('L',i) for i in range(self.size[x]))),
                                     (y,tuple(('R',i) for i in range(self.size[y])))])
    def verify(self):
        for (x,y),fs in self.hom.items():
            for f in fs:assert len(f)==self.size[x] and len(set(f))==len(f) and all(0<=i<self.size[y] for i in f)
        for (x,y),fs in list(self.hom.items()):
            for z in range(len(self.size)):
                for g in self.hom.get((y,z),()):
                    for f in fs:assert tuple(g[t] for t in f) in self.hom[x,z]
        # associativity is equality of composed tuples, hence follows pointwise.

def quotient_H(C):
    vals=[]; labels=[]
    for x in range(len(C.size)):
        pts=sorted(f[0] for f in C.hom.get((0,x),()))
        parent={p:p for p in pts}
        def root(p):
            while parent[p]!=p:parent[p]=parent[parent[p]];p=parent[p]
            return p
        for f in C.hom.get((1,x),()):
            for i,j in ([(0,1),(0,2)] if '--triple' in sys.argv else [(0,1)]):
                a,b=root(f[i]),root(f[j]);parent[a]=b
        labs={p:root(p) for p in pts}
        vals.append(sorted(set(labs.values())));labels.append(labs)
    return vals,labels

def nerve(C):
    vals,labs=quotient_H(C)
    vertices=[(x,h) for x,vs in enumerate(vals) for h in vs]
    vi={v:i for i,v in enumerate(vertices)}
    arrows=[]; ai={}; outgoing=defaultdict(list)
    for (x,y),fs in C.hom.items():
        if x==y:continue
        for f in sorted(fs):
            for h in vals[x]:
                target=labs[y][f[h]]
                a=(x,y,f,h); idx=len(arrows);arrows.append(a);ai[a]=idx
                outgoing[vi[x,h]].append(idx)
    chains=[[(i,) for i in range(len(vertices))],[(i,) for i in range(len(arrows))]]
    while chains[-1]:
        nxt=[]
        for c in chains[-1]:
            x,y,f,h=arrows[c[-1]]
            t=vi[y,labs[y][f[h]]]
            for j in outgoing[t]:nxt.append(c+(j,))
        if not nxt:break
        chains.append(nxt)
    indices=[{c:i for i,c in enumerate(cs)} for cs in chains]
    boundaries=[{} for _ in chains]
    for j,(x,y,f,h) in enumerate(arrows):
        boundaries[1][j]={vi[y,labs[y][f[h]]]:1,vi[x,h]:-1}
    for d in range(2,len(chains)):
        for j,c in enumerate(chains[d]):
            bd=defaultdict(int)
            bd[indices[d-1][c[1:]]]+=1
            bd[indices[d-1][c[:-1]]]+=(-1)**d
            for i in range(1,d):
                x,y,f,h=arrows[c[i-1]]; yy,z,g,hh=arrows[c[i]]
                assert y==yy
                comp=ai[x,z,tuple(g[t] for t in f),h]
                face=c[:i-1]+(comp,)+c[i+1:]
                bd[indices[d-1][face]]+=(-1)**i
            boundaries[d][j]={r:v for r,v in bd.items() if v}
    for d in range(2,len(chains)):
        for bd in boundaries[d].values():
            twice=defaultdict(int)
            for r,v in bd.items():
                for rr,w in boundaries[d-1][r].items():twice[rr]+=v*w
            assert not any(twice.values())
    support=[[v[0] for v in vertices]]+[[arrows[c[-1]][1] for c in cs] for cs in chains[1:]]
    return [len(cs) for cs in chains],boundaries,support

def homology_units(counts,bd):
    # Cancel a unit incidence x->y, an elementary chain contraction over Z.
    alive=[set(range(n)) for n in counts]
    inv=[defaultdict(set) for _ in counts]
    for d in range(1,len(counts)):
        for x,b in bd[d].items():
            for y in b:inv[d][y].add(x)
    canceled=[0 for _ in counts]
    for d in range(1,len(counts)):
        queue=list(alive[d]); scan=0
        while scan<len(queue):
            x=queue[scan];scan+=1
            if x not in alive[d]:continue
            b=bd[d][x]
            unit=[y for y,v in b.items() if abs(v)==1]
            if not unit:continue
            y=min(unit,key=lambda z:len(inv[d][z]))
            sign=b[y]
            for z in list(inv[d][y]):
                if z==x:continue
                bz=bd[d][z];a=bz[y]*sign
                old=set(bz)
                for r,v in b.items():
                    new=bz.get(r,0)-a*v
                    if new:bz[r]=new
                    else:bz.pop(r,None)
                for r in old-set(bz):inv[d][r].discard(z)
                for r in set(bz)-old:inv[d][r].add(z)
                queue.append(z)
            # Basis transformation in the next degree has zero coefficient on x.
            if d+1<len(counts):
                for z in list(inv[d+1].get(x,())):bd[d+1][z].pop(x,None)
                inv[d+1].pop(x,None)
            for r in b:inv[d][r].discard(x)
            bd[d].pop(x);alive[d].remove(x)
            if d-1>0:
                for r in bd[d-1].get(y,{}):inv[d-1][r].discard(y)
                bd[d-1].pop(y,None)
            alive[d-1].remove(y);canceled[d]+=1
    residual={str(d):{str(x):b for x,b in bd[d].items() if b} for d in range(1,len(counts))}
    if any(residual.values()):
        return {'residual_nonunit_boundaries':residual,'remaining_chain_ranks':[len(s) for s in alive]}
    return {'integral_homology_free_ranks':[len(s) for s in alive], 'unit_cancellations':canceled}

def rank_modp(columns,p=101):
    pivots={}
    for raw in columns.values():
        b={r:v%p for r,v in raw.items() if v%p}
        while b:
            r=min(b)
            if r not in pivots:
                inv=pow(b[r],-1,p)
                pivots[r]={t:(v*inv)%p for t,v in b.items()}
                break
            a=b[r]
            for t,v in pivots[r].items():
                nv=(b.get(t,0)-a*v)%p
                if nv:b[t]=nv
                else:b.pop(t,None)
    return len(pivots)

def run(C,label,old_objects=None):
    C.verify();counts,bd,support=nerve(C)
    if '--verify-field' in sys.argv:
        field_ranks=[0]+[rank_modp(bd[d]) for d in range(1,len(counts))]+[0]
        field_betti=[counts[d]-field_ranks[d]-field_ranks[d+1] for d in range(len(counts))]
    if old_objects is not None:
        # Quotient chain complex by the old full subcategory.  Old and new
        # simplices can interleave in enumeration; use actual final objects.
        maps=[{j:i for i,j in enumerate(j for j,x in enumerate(ss) if x>=old_objects)} for ss in support]
        relbd=[{} for _ in counts]
        for d in range(1,len(counts)):
            relbd[d]={maps[d][j]:{maps[d-1][i]:a for i,a in b.items() if i in maps[d-1]} for j,b in bd[d].items() if j in maps[d]}
        rel=homology_units([len(m) for m in maps],relbd)
    print(label, 'objects',len(C.size),'arrows',sum(map(len,C.hom.values())),'nerve',counts,flush=True)
    h=homology_units(counts,bd)
    out={'label':label,'construction':('literal_common_n_fails_11' if '--literal-common-n' in sys.argv else 'repaired_actual_path_sizes_verified_9_10_11'),'source_rule_failures':C.source_rule_failures.copy(),'objects':len(C.size),'arrows_including_identities':sum(map(len,C.hom.values())),
         'nondegenerate_nerve_simplex_counts':counts,**h,
         'category_objects':[{'name':C.names[x],'size':C.size[x],'hom_V':len(C.hom.get((0,x),())),
                              'hom_W':len(C.hom.get((1,x),()))} for x in range(len(C.size))]}
    if old_objects is not None:out['relative_to_previous']=rel
    if '--verify-field' in sys.argv:
        out['independent_mod_101_betti']=field_betti
        assert field_betti==out.get('integral_homology_free_ranks')
    print(json.dumps(out,indent=2),flush=True)
    return out

if __name__=='__main__':
    C=Cat();V=C.obj('V',1);W=C.obj('W',3)
    for i in range(3):C.hom[V,W].add((i,))
    results=[run(C,'K0')]
    original={(x,y):sorted(fs) for (x,y),fs in C.hom.items()}
    for (x,y),fs in sorted(original.items()):
        for i,f in enumerate(fs):
            for j,g in enumerate(fs):
                C.qfilter(f'Q_{x}_{y}_{i}_{j}',x,y,f,g,45,3)
    for x in (V,W):
        for y in (V,W):C.sum(f'S_{x}_{y}',x,y)
    results.append(run(C,'K1_all_ordered_pairs_s45'))
    if '--partial-k2' in sys.argv:
        t=C.names.index('Q_0_1_0_1'); fs=sorted(C.hom[W,t]);f,g=fs[:2]
        C.qfilter('Q_K2_selected',W,t,f,g,153,3)
        results.append(run(C,'K1_plus_one_K2_quasifilter_s153',17))
    if '--critical-k3' in sys.argv:
        left=C.names.index('Q_0_1_0_1');right=C.names.index('Q_0_1_1_0')
        t=C.sum('S_K2_two_cycle_targets',left,right)
        results.append(run(C,'K1_plus_K2_sum_of_two_cycle_targets',17))
        lf=next(iter(C.hom[left,t]));rg=next(iter(C.hom[right,t]))
        f=tuple(lf[j] for j in sorted(C.hom[W,left])[0])
        g=tuple(rg[j] for j in sorted(C.hom[W,right])[0])
        old=len(C.size)
        C.qfilter('Q_K3_selected_cross_sum',W,t,f,g,297,3)
        results.append(run(C,'K1_plus_K2_sum_plus_K3_quasifilter_s297',old))
    suffix=('_triple' if '--triple' in sys.argv else '')+('_critical' if '--critical-k3' in sys.argv else '')+('_literal' if '--literal-common-n' in sys.argv else '')
    with Path(__file__).with_name('akr_stages'+suffix+'_output.json').open('w') as f:json.dump(results,f,indent=2)
