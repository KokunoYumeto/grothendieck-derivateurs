#!/usr/bin/env python3
"""Exact finite checks for TOTASPH Parts A and G.

Requires Python 3 and SymPy.  No network access or random input is used.
The output includes integral Smith invariant factors, not just rational Betti
numbers.  The finite simplex category is specified by its face operators and
is also exported with every arrow and every defined composite.
"""
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import json

from sympy import Matrix, zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form


@dataclass
class Cat:
    objects: list
    arrows: list  # dictionaries: name, source, target, identity
    composites: dict  # (g,f) maps to g after f

    def validate(self):
        ids = {a['source']:i for i,a in enumerate(self.arrows) if a['identity']}
        assert set(ids) == set(self.objects)
        expected = {(g,f) for f,a in enumerate(self.arrows)
                    for g,b in enumerate(self.arrows) if a['target']==b['source']}
        assert expected == set(self.composites)
        for (g,f),h in self.composites.items():
            assert self.arrows[h]['source']==self.arrows[f]['source']
            assert self.arrows[h]['target']==self.arrows[g]['target']
        for i,a in enumerate(self.arrows):
            assert self.composites[i,ids[a['source']]]==i
            assert self.composites[ids[a['target']],i]==i
        triples=0
        for (g,f),gf in self.composites.items():
            for h,c in enumerate(self.arrows):
                if c['source']==self.arrows[g]['target']:
                    triples+=1
                    assert self.composites[h,gf] == self.composites[self.composites[h,g],f]
        return {'objects':len(self.objects),'arrows_including_identities':len(self.arrows),
                'composable_pairs':len(expected),'associativity_triples_checked':triples}


def named_category(objects, nonids, nontrivial_composites):
    arrows=[{'name':'id_'+o,'source':o,'target':o,'identity':True} for o in objects]
    arrows += [{'name':n,'source':s,'target':t,'identity':False} for n,s,t in nonids]
    idx={a['name']:i for i,a in enumerate(arrows)}
    table={}
    for f,a in enumerate(arrows):
        for g,b in enumerate(arrows):
            if a['target']!=b['source']:
                continue
            if a['identity']: h=g
            elif b['identity']: h=f
            else: h=idx[nontrivial_composites[b['name'],a['name']]]
            table[g,f]=h
    return Cat(objects,arrows,table)


def normalized_chains(cat):
    levels=[[(o,) for o in cat.objects]]
    nonids=[i for i,a in enumerate(cat.arrows) if not a['identity']]
    levels.append([(i,) for i in nonids])
    while levels[-1]:
        nxt=[s+(i,) for s in levels[-1] for i in nonids
             if cat.arrows[s[-1]]['target']==cat.arrows[i]['source']]
        if not nxt:
            break
        assert len(levels)<6, 'These examples must have bounded nerve dimension.'
        levels.append(nxt)
    return levels


def integral_homology(cat):
    chains=normalized_chains(cat)
    boundary=[zeros(0,len(chains[0]))]
    for n in range(1,len(chains)):
        row={s:i for i,s in enumerate(chains[n-1])}
        mat=zeros(len(row),len(chains[n]))
        for j,s in enumerate(chains[n]):
            if n==1:
                a=cat.arrows[s[0]]
                faces=[((a['target'],),1),((a['source'],),-1)]
            else:
                faces=[(s[1:],1),(s[:-1],(-1)**n)]
                for k in range(1,n):
                    composite=cat.composites[s[k],s[k-1]]
                    if not cat.arrows[composite]['identity']:
                        faces.append((s[:k-1]+(composite,)+s[k+1:],(-1)**k))
            for f,sign in faces:
                mat[row[f],j]+=sign
        assert boundary[-1]*mat==zeros(boundary[-1].rows,mat.cols)
        boundary.append(mat)
    boundary.append(zeros(len(chains[-1]),0))
    inv=[]
    ranks=[]
    for mat in boundary:
        smith=smith_normal_form(mat,domain=ZZ)
        diag=[abs(int(smith[i,i])) for i in range(min(smith.shape)) if smith[i,i]]
        inv.append(diag)
        ranks.append(len(diag))
    homology=[{'degree':n,'free_rank':len(chains[n])-ranks[n]-ranks[n+1],
               'torsion_invariant_factors':[d for d in inv[n+1] if d>1]}
              for n in range(len(chains))]
    return {'nondegenerate_simplex_counts':[len(x) for x in chains],
            'boundary_ranks':ranks[1:-1],
            'nonzero_smith_factors':[{str(d):v.count(d) for d in sorted(set(v))} for v in inv[1:-1]],
            'integral_homology':homology,'boundary_squared_zero':True}


def undercategory_connected(cat,subobjects,obj):
    nodes=[i for i,a in enumerate(cat.arrows)
           if a['source']==obj and a['target'] in subobjects]
    pairs=[]
    for f in nodes:
        for h,a in enumerate(cat.arrows):
            if a['source']==cat.arrows[f]['target'] and a['target'] in subobjects:
                g=cat.composites[h,f]
                assert g in nodes
                if not a['identity']: pairs.append((f,g))
    seen=set()
    if nodes:
        seen={nodes[0]}
        changed=True
        while changed:
            old=set(seen)
            for a,b in pairs:
                if a in seen or b in seen: seen.update((a,b))
            changed=old!=seen
    return {'objects':len(nodes),'nonidentity_arrows':len(pairs),
            'nonempty_connected':bool(nodes) and seen==set(nodes)}


def presentation_delta_set():
    # Capital letters denote inverses when traversing a polygon boundary.
    words=['aaaaaBBB','bbbBABA']
    cells={'v':{'dim':0},'c0':{'dim':0},'c1':{'dim':0},
           'a':{'dim':1,'vertices':['v','v']},
           'b':{'dim':1,'vertices':['v','v']}}
    for disk,word in enumerate(words):
        n=len(word)
        for i in range(n):
            cells[f'r{disk}_{i}']={'dim':1,'vertices':[f'c{disk}','v']}
        for i,letter in enumerate(word):
            ri=f'r{disk}_{i}'; rj=f'r{disk}_{(i+1)%n}'
            # Face 0 is the base loop.  Ordering the last two vertices according
            # to the sign ensures that all face identifications are increasing.
            faces=[letter.lower(),rj,ri] if letter.islower() else [letter.lower(),ri,rj]
            cells[f't{disk}_{i}']={'dim':2,'vertices':[f'c{disk}','v','v'],'faces':faces}
    return cells,words


def simplex_category(cells):
    def face(name,subset):
        c=cells[name]; d=c['dim']
        if len(subset)==d+1: return name
        if len(subset)==1: return c['vertices'][subset[0]]
        assert d==2 and len(subset)==2
        omitted=next(i for i in range(3) if i not in subset)
        return c['faces'][omitted]
    arrows=[]; tags=[]
    for target,c in cells.items():
        for k in range(c['dim']+1):
            for subset in combinations(range(c['dim']+1),k+1):
                source=face(target,subset)
                arrows.append({'name':target+':'+''.join(map(str,subset)),
                               'source':source,'target':target,
                               'identity':source==target and k==c['dim']})
                tags.append((target,subset))
    idx={tag:i for i,tag in enumerate(tags)}
    table={}
    for f,a in enumerate(arrows):
        for g,b in enumerate(arrows):
            if a['target']==b['source']:
                target,outer=tags[g]; _,inner=tags[f]
                h=idx[target,tuple(outer[i] for i in inner)]
                assert arrows[h]['source']==a['source']
                table[g,f]=h
    return Cat(list(cells),arrows,table)


def add_final_points(cat,points):
    objects=cat.objects+list(points)
    arrows=[dict(a) for a in cat.arrows]
    for p in points:
        arrows.append({'name':'id_'+p,'source':p,'target':p,'identity':True})
        for o in cat.objects:
            arrows.append({'name':o+'->'+p,'source':o,'target':p,'identity':False})
    direct={(a['source'],a['target']):i for i,a in enumerate(arrows) if a['target'] in points}
    table=dict(cat.composites)
    for f,a in enumerate(arrows):
        for g,b in enumerate(arrows):
            if a['target']!=b['source'] or (g,f) in table: continue
            if a['identity']: h=g
            elif b['identity']: h=f
            else: h=direct[a['source'],b['target']]
            table[g,f]=h
    return Cat(objects,arrows,table)


def perm_cycle(*cycle):
    p=list(range(5))
    for a,b in zip(cycle,cycle[1:]+cycle[:1]): p[a-1]=b-1
    return tuple(p)


def perm_compose(p,q): return tuple(p[q[i]] for i in range(5))


def perm_inverse(p): return tuple(p.index(i) for i in range(5))


def eval_word(word,a,b):
    p=tuple(range(5))
    values={'a':a,'b':b,'A':perm_inverse(a),'B':perm_inverse(b)}
    for letter in word: p=perm_compose(p,values[letter])
    return p


def serializable_cat(cat):
    return {'objects':cat.objects,'arrows':cat.arrows,
            'composition_convention':'[g,f,h] means g after f equals h',
            'composites':[[g,f,h] for (g,f),h in sorted(cat.composites.items())]}


def main():
    fork=named_category(['z','a','b'],[('r','z','a'),('s','z','b')],{})
    sphere=named_category(['x','z','a','b'],[
        ('alpha','x','z'),('beta','x','z'),('r','z','a'),('s','z','b'),
        ('gamma','x','a'),('delta','x','b')],
        {('r','alpha'):'gamma',('r','beta'):'gamma',
         ('s','alpha'):'delta',('s','beta'):'delta'})
    cells,words=presentation_delta_set()
    acyclic=simplex_category(cells)
    cone=add_final_points(acyclic,['u'])
    suspension=add_final_points(acyclic,['u','t'])
    categories={'fork':fork,'sphere_final_image':sphere,'acyclic_noncontractible':acyclic,
                'one_cone':cone,'two_cones':suspension}
    output={name:{**cat.validate(),**integral_homology(cat)} for name,cat in categories.items()}
    output['fork_inclusion_finality']={o:undercategory_connected(sphere,set(fork.objects),o) for o in sphere.objects}
    assert all(x['nonempty_connected'] for x in output['fork_inclusion_finality'].values())
    assert output['sphere_final_image']['integral_homology']==[
        {'degree':0,'free_rank':1,'torsion_invariant_factors':[]},
        {'degree':1,'free_rank':0,'torsion_invariant_factors':[]},
        {'degree':2,'free_rank':1,'torsion_invariant_factors':[]}]
    for name in ['fork','acyclic_noncontractible','one_cone','two_cones']:
        hs=output[name]['integral_homology']
        assert all(h['free_rank']==(1 if h['degree']==0 else 0) and not h['torsion_invariant_factors'] for h in hs)
    a=perm_cycle(1,4,3,2,5); b=perm_cycle(1,2,3)
    identity=tuple(range(5))
    evaluated=[eval_word(w,a,b) for w in words]
    assert evaluated==[identity,identity] and a!=identity
    cellular=Matrix([[5,-2],[-3,1]])
    assert cellular.det()==-1
    output['nontrivial_fundamental_group_certificate']={
        'presentation_relators':words,'cellular_d2':[[int(x) for x in row] for row in cellular.tolist()],'determinant':int(cellular.det()),
        'permutation_convention':'functions on {1,...,5}; products from right to left',
        'a_images':[i+1 for i in a],'b_images':[i+1 for i in b],
        'relator_images':[[i+1 for i in p] for p in evaluated],
        'a_is_nonidentity':a!=identity}
    output['sieve_checks']={
        'cone_in_two_cones':all(a['source'] in cone.objects for a in suspension.arrows if a['target'] in cone.objects),
        'fork_branches':all(a['source'] in S for S in [{'z','a'},{'z','b'}]
                            for a in fork.arrows if a['target'] in S)}
    assert all(output['sieve_checks'].values())
    outdir=Path(__file__).resolve().parent
    (outdir/'ag_finite_examples.output.json').write_text(json.dumps(output,indent=2)+'\n')
    data={'delta_set_cells':cells,'categories':{n:serializable_cat(c) for n,c in categories.items()}}
    (outdir/'ag_category_data.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__': main()
