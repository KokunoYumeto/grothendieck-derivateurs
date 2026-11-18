"""Exact finite certificates used in Part A; no inference of contractibility from homology."""
from itertools import combinations
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

OUT = Path(__file__).resolve().parent / 'outputs'
OUT.mkdir(exist_ok=True)

def presentation_faces(words):
    dims = {'v': 0}
    faces = {}
    for a in sorted({c.lower() for w in words for c in w}):
        dims[a] = 1
        faces[a] = ['v', 'v']
    for k, word in enumerate(words):
        c = f'c{k}'
        dims[c] = 0
        for i in range(len(word)):
            r = f'r{k}_{i}'
            dims[r] = 1
            faces[r] = ['v', c]
        for i, letter in enumerate(word):
            t = f't{k}_{i}'
            r0, r1 = f'r{k}_{i}', f'r{k}_{(i+1)%len(word)}'
            dims[t] = 2
            faces[t] = [letter.lower(), r1, r0] if letter.islower() else [letter.lower(), r0, r1]
    def restrict(target, subset):
        current = target
        for i in sorted(set(range(dims[target]+1))-set(subset), reverse=True):
            current = faces[current][i]
        return current
    arrows = []
    for target, d in dims.items():
        for n in range(d+1):
            for subset in combinations(range(d+1), n+1):
                arrows.append((restrict(target, subset), target, subset))
    index = {a: i for i, a in enumerate(arrows)}
    def comp(i, j):
        # First i, then j.
        a,b,s = arrows[i]
        b2,c,t = arrows[j]
        assert b == b2
        return index[(a,c,tuple(t[q] for q in s))]
    return list(dims), arrows, comp

def double_cone(objects, arrows, comp):
    old_n = len(arrows)
    new = list(arrows)
    for vertex in ['u','t']:
        new.append((vertex,vertex,('id',)))
        new.extend((x,vertex,('cone',)) for x in objects)
    index = {(a,b):i for i,(a,b,_) in enumerate(new) if i >= old_n}
    def extended(i,j):
        a,b,_=new[i]
        b2,c,_=new[j]
        assert b==b2
        if i<old_n and j<old_n:
            return comp(i,j)
        return index[(a,c)]
    return objects+['u','t'],new,extended

def verify(name, objects, arrows, compose):
    by_source={x:[] for x in objects}
    for i,(a,b,s) in enumerate(arrows):
        by_source[a].append(i)
    identities={x:next(i for i,(a,b,_) in enumerate(arrows) if a==b==x) for x in objects}
    composition=[]
    triples=0
    for i,(a,b,_) in enumerate(arrows):
        assert compose(identities[a],i)==i==compose(i,identities[b])
        for j in by_source[b]:
            ij=compose(i,j)
            composition.append([i,j,ij])
            assert arrows[ij][:2]==(a,arrows[j][1])
            for k in by_source[arrows[j][1]]:
                assert compose(ij,k)==compose(i,compose(j,k))
                triples+=1
    nonids=[i for i,(a,b,s) in enumerate(arrows) if a!=b]
    chains=[[(x,) for x in objects],[(i,) for i in nonids]]
    while chains[-1]:
        nxt=[c+(i,) for c in chains[-1] for i in by_source[arrows[c[-1]][1]] if i in nonids]
        if not nxt: break
        chains.append(nxt)
    ranks=[]; factors=[]
    for n in range(1,len(chains)):
        row={c:i for i,c in enumerate(chains[n-1])}
        mat=sp.zeros(len(row),len(chains[n]))
        for col,c in enumerate(chains[n]):
            if n==1:
                a,b,_=arrows[c[0]]
                bd=[((b,),1),((a,),-1)]
            else:
                bd=[(c[1:],1),(c[:-1],(-1)**n)]
                for k in range(1,n):
                    cc=c[:k-1]+(compose(c[k-1],c[k]),)+c[k+1:]
                    bd.append((cc,(-1)**k))
            for face,sign in bd:mat[row[face],col]+=sign
        if n>1:assert prev*mat==sp.zeros(prev.rows,mat.cols)
        snf=smith_normal_form(mat,domain=ZZ)
        diag=[abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i]]
        ranks.append(len(diag));factors.append(diag)
        prev=mat
    rr=[0]+ranks+[0]
    betti=[len(chains[i])-rr[i]-rr[i+1] for i in range(len(chains))]
    result={'name':name,'objects':len(objects),'arrows':len(arrows),
            'associativity_triples_checked':triples,'normalized_chain_ranks':[len(c) for c in chains],
            'boundary_ranks':ranks,'nonunit_smith_factors':[[v for v in a if v!=1] for a in factors],
            'homology_betti_numbers':betti}
    (OUT/f'{name}_category.json').write_text(json.dumps({'objects':objects,'arrows':arrows,'composition':composition},indent=2))
    return result

def perm_product(p,q):return tuple(p[q[i]] for i in range(len(p)))
def perm_power(p,n):
    if n<0:
        p=tuple(p.index(i) for i in range(len(p)));n=-n
    ans=tuple(range(len(p)))
    for _ in range(n):ans=perm_product(ans,p)
    return ans

if __name__=='__main__':
    o,a,c=presentation_faces(['aaaaaBBB','bbbBABA'])
    result=[verify('A_acyclic',o,a,c)]
    oo,aa,cc=double_cone(o,a,c)
    result.append(verify('A_double_cone',oo,aa,cc))
    for excluded in ['u','t']:
        piece=set(oo)-{excluded}
        assert all(source in piece for source,target,_ in aa if target in piece)
    p=(3,4,1,2,0);q=(1,2,0,3,4)
    assert perm_power(p,5)==perm_power(q,3)==perm_power(perm_product(p,q),2)==tuple(range(5))
    assert p!=tuple(range(5))
    result.append({'permutation_witness':{'a':p,'b':q,'ab':perm_product(p,q)},'relators_trivial':True,'a_nontrivial':True,'sieve_cover_verified':True})
    o,a,c=presentation_faces(['aa'])
    result.append(verify('A_RP2',o,a,c))
    (OUT/'A_finite_categories.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
