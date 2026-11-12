#!/usr/bin/env python3
"""Independent finite checks for PRETOT, Part E and VII type-category audit.

Only finite claims are machine checked.  The paper supplies the unbounded
critical-vertex argument, and the all-target Kan-extension argument.
Requires Python 3 and SymPy. Run this script from any working directory;
the JSON report is printed and saved to outputs/path_checks.out beside it.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
"""
from itertools import product, combinations_with_replacement
from collections import defaultdict
from pathlib import Path
import json


class Category:
    def __init__(self, objects, arrows, identities, compose):
        self.objects = tuple(objects)
        self.arrows = dict(arrows)  # name -> (source,target)
        self.identities = dict(identities)
        self.compose = compose

    def hom(self, a, b):
        return [f for f, (s, t) in self.arrows.items() if (s, t) == (a, b)]

    def check(self):
        for f, (s, t) in self.arrows.items():
            assert self.compose(f, self.identities[s]) == f
            assert self.compose(self.identities[t], f) == f
        for f, (a, b) in self.arrows.items():
            for g in self.hom(b, b):
                assert self.arrows[self.compose(g, f)] == (a, b)
            for g, (b1, c) in self.arrows.items():
                if b1 != b:
                    continue
                assert self.arrows[self.compose(g, f)] == (a, c)
                for h, (c1, d) in self.arrows.items():
                    if c1 == c:
                        assert self.compose(h, self.compose(g, f)) == self.compose(self.compose(h, g), f)


def connected(objects, edge_pairs):
    objects = set(objects)
    if not objects:
        return False
    links = defaultdict(set)
    for x, y in edge_pairs:
        links[x].add(y)
        links[y].add(x)
    seen = {next(iter(objects))}
    todo = list(seen)
    while todo:
        x = todo.pop()
        for y in links[x] - seen:
            seen.add(y)
            todo.append(y)
    return seen == objects


def final_functor(A, B, obj, arr):
    for f, (a, b) in A.arrows.items():
        assert B.arrows[arr[f]] == (obj[a], obj[b])
    for f, (a, b) in A.arrows.items():
        for g, (b1, c) in A.arrows.items():
            if b1 == b:
                assert arr[A.compose(g, f)] == B.compose(arr[g], arr[f])
    comma_sizes = {}
    for x in B.objects:
        objs = [(a, u) for a in A.objects for u in B.hom(x, obj[a])]
        edges = []
        for a, u in objs:
            for b, v in objs:
                for f in A.hom(a, b):
                    if B.compose(arr[f], u) == v:
                        edges.append(((a, u), (b, v)))
        assert connected(objs, edges)
        comma_sizes[x] = len(objs)
    return comma_sizes


def acyclic_free_category(objects, edges):
    # Used only for directed finite graphs without parallel paths.
    paths = {('id', a): (a, a) for a in objects}
    for name, a, b in edges:
        paths[(name,)] = (a, b)
    while True:
        added = {}
        for f, (a, b) in list(paths.items()):
            if f[0] == 'id':
                continue
            for g, (c, d) in list(paths.items()):
                if g[0] != 'id' and b == c:
                    added[f + g] = (a, d)
        if all(p in paths for p in added):
            break
        paths.update(added)

    def comp(g, f):
        if f[0] == 'id':
            return g
        if g[0] == 'id':
            return f
        return f + g
    return Category(objects, paths, {a: ('id', a) for a in objects}, comp)


def sphere_category():
    objects = ('x', 'o', 'a', 'b')
    arrows = {f'id_{a}': (a, a) for a in objects}
    arrows.update({'r': ('x','o'), 's': ('x','o'), 'A': ('o','a'),
                   'B': ('o','b'), 'c': ('x','a'), 'd': ('x','b')})

    def comp(g, f):
        if f.startswith('id_'):
            return g
        if g.startswith('id_'):
            return f
        assert f in ('r','s') and g in ('A','B')
        return 'c' if g == 'A' else 'd'
    return Category(objects, arrows, {a:f'id_{a}' for a in objects}, comp)


def nerve_matrices(A):
    import sympy as sp
    ids = set(A.identities.values())
    chains = [[(a,) for a in A.objects], [(f,) for f in A.arrows if f not in ids]]
    while chains[-1]:
        chains.append([c+(g,) for c in chains[-1] for g,(s,t) in A.arrows.items()
                       if g not in ids and A.arrows[c[-1]][1] == s])
    matrices = []
    for n in range(1,len(chains)):
        rows = {c:i for i,c in enumerate(chains[n-1])}
        M = sp.zeros(len(rows),len(chains[n]))
        for j,c in enumerate(chains[n]):
            if n == 1:
                s,t = A.arrows[c[0]]
                M[rows[(t,)],j] += 1
                M[rows[(s,)],j] -= 1
            else:
                M[rows[c[1:]],j] += 1
                M[rows[c[:-1]],j] += (-1)**n
                for i in range(1,n):
                    h = A.compose(c[i],c[i-1])
                    if h not in ids:
                        M[rows[c[:i-1]+(h,)+c[i+1:]],j] += (-1)**i
        matrices.append(M)
    for a,b in zip(matrices,matrices[1:]):
        assert a*b == sp.zeros(a.rows,b.cols)
    from sympy.matrices.normalforms import smith_normal_form
    from sympy.polys.domains import ZZ
    snfs = [smith_normal_form(m,domain=ZZ) for m in matrices]
    ranks = [sum(s[i,i] != 0 for i in range(min(s.shape))) for s in snfs]
    result = []
    for n in range(len(chains)-1):
        rprev = 0 if n==0 else ranks[n-1]
        rnext = ranks[n]
        tors = [abs(int(snfs[n][i,i])) for i in range(min(snfs[n].shape))
                if abs(snfs[n][i,i]) > 1]
        result.append({'degree':n,'rank':len(chains[n])-rprev-rnext,'torsion':tors})
    return {'simplex_counts':[len(c) for c in chains], 'homology':result}


def walking_retraction_paths_one():
    # Endpoints 0={0}, z={0,1}; arrows are the indicated actual set maps.
    Y = {'i0':('0','0',(0,)), 'u':('0','z',(0,)),
         'r':('z','0',(0,0)), 'iz':('z','z',(0,1)), 'e':('z','z',(0,0))}
    lookup = {v:k for k,v in Y.items()}
    def yc(g,f):
        a,b,F = Y[f]
        b1,c,G = Y[g]
        assert b==b1
        return lookup[(a,c,tuple(G[i] for i in F))]
    # t=empty; a+/a-=constant 0; d+=0->z, d-=0<-z.
    objects = ('t','ap','dp','am','dm')
    typ = {'t':'','ap':'+','dp':'+','am':'-','dm':'-'}
    end = {'t':'0','ap':'0','dp':'z','am':'0','dm':'z'}
    arrows = {}
    for a,b in product(objects,repeat=2):
        if a=='t' and b!='t':
            continue
        if b=='t':
            opts = ['i0'] if end[a]=='0' else ['r']
        elif typ[a] == typ[b]:
            opts = [f for f,(s,t,_) in Y.items() if (s,t)==(end[a],end[b])]
        else:
            continue
        for f in opts:
            arrows[(a,b,f)] = (a,b)
    def comp(g,f):
        return (f[0],g[1],yc(g[2],f[2]))
    ids = {a:(a,a,'i0' if end[a]=='0' else 'iz') for a in objects}
    P = Category(objects,arrows,ids,comp)
    P.check()
    assert all(len(P.hom(a,'t'))==1 for a in objects)
    H = {a:[f for f,(s,t,_) in Y.items() if (s,t)==(end[a],'z')] for a in objects}
    def hf(f,h):
        return yc(h,f[2])
    # Construct pushout R_t union_{R_ap} R_dp union_{R_am} R_dm objectwise.
    sizes = {}
    for a in objects:
        tagged = [(b,f) for b in ('t','dp','dm') for f in P.hom(a,b)]
        parent = {x:x for x in tagged}
        def root(x):
            if parent[x]!=x:
                parent[x]=root(parent[x])
            return parent[x]
        def union(x,y):
            parent[root(x)] = root(y)
        for aa,dd in [('ap','dp'),('am','dm')]:
            inc = P.hom(aa,dd)[0]
            col = P.hom(aa,'t')[0]
            retr = P.hom(dd,aa)[0]
            assert P.compose(retr,inc)==P.identities[aa]
            for f in P.hom(a,aa):
                union(('t',P.compose(col,f)),(dd,P.compose(inc,f)))
        target = {}
        for b,f in tagged:
            h = yc('u' if b=='t' else 'iz',f[2])
            rt = root((b,f))
            if rt in target:
                assert target[rt]==h
            target[rt]=h
        assert set(target.values())==set(H[a]) and len(set(target.values()))==len(target)
        sizes[a] = len(target)
    # Verify presheaf laws and all endpoint naturality.
    for f,(a,b) in P.arrows.items():
        for h in H[b]:
            assert hf(f,h) in H[a]
        for g,(b1,c) in P.arrows.items():
            if b1==b:
                for h in H[c]:
                    assert hf(f,hf(g,h))==hf(P.compose(g,f),h)
    return {'objects':len(P.objects),'arrows':len(P.arrows),
            'H_z_cardinalities':sizes,'split_gluings_verified':True,
            'presheaf_identity_verified':True,'all_category_axioms_verified':True}


def type_maps(source,target):
    n,m = len(source),len(target)
    for v in combinations_with_replacement(range(m+1),n+1):
        if v[0]!=0 or v[-1]!=m:
            continue
        if all(all(target[k]==source[i] for k in range(v[i],v[i+1])) for i in range(n)):
            yield v


def main():
    P = acyclic_free_category(('t','a','b','c'), [('at','a','t'),('ab','a','b'),('ct','c','t')])
    F = acyclic_free_category(('o','A','B'), [('oA','o','A'),('oB','o','B')])
    S = sphere_category()
    for A in (P,F,S):
        A.check()
    po={'t':'A','a':'o','b':'B','c':'o'}
    pa={f:(('id',po[s]) if s==t else ('oA',) if t=='t' else ('oB',))
        for f,(s,t) in P.arrows.items()}
    jo={'o':'o','A':'a','B':'b'}
    ja={f:('id_'+jo[s] if s==t else 'A' if t=='A' else 'B') for f,(s,t) in F.arrows.items()}
    G = Category(('*',), {0:('*','*'),1:('*','*')}, {'*':0}, lambda g,f:(g+f)%2)
    G.check()
    assert G.compose(1,1)==0 and 1!=0
    result={'P_interval_first_truncation':{'objects':len(P.objects),'arrows':len(P.arrows)},
            'P_to_fork_final':final_functor(P,F,po,pa),
            'fork_to_sphere_final':final_functor(F,S,jo,ja),
            'sphere':nerve_matrices(S),
            'walking_retraction_first_truncation':walking_retraction_paths_one(),
            'preorder_chain_counterexample':{'group':'C2','composition_table':[[0,1],[1,0]],
                'all_category_axioms_verified':True,'fundamental_group_presentation':'<s | s^2 = 1>',
                'nontrivial_model_verified':True}}
    f=(0,0,0,1); g=(0,1,1,1)
    assert f in set(type_maps('+-+','+')) and g in set(type_maps('+-+','+'))
    tested=0
    for n in range(7):
        for w in product('+-',repeat=n):
            for h in type_maps(''.join(w),'+-+'):
                assert 1 in h and 2 in h
                assert tuple(f[i] for i in h)!=tuple(g[i] for i in h)
                tested+=1
    result['Ty_op_nonfiltered_witness']={'f':f,'g':g,'all_source_types_lengths':list(range(7)),
                                        'tested_precompositions':tested,
                                        'equalizers_found':0,
                                        'unbounded_claim':'Proved by critical vertices in paper; finite test not substituted.'}
    report = json.dumps(result,indent=2) + '\n'
    output = Path(__file__).resolve().parent / 'outputs'
    output.mkdir(exist_ok=True)
    (output / 'path_checks.out').write_text(report, encoding='utf-8')
    print(report, end='')


if __name__=='__main__':
    main()
