"""Finite checks for Part F. Python 3; requires sympy.

Every finite category is explicit, and associativity is checked exhaustively.
Composition comp(g,f) means g after f. The interval pushout is computed from
the actual ordinary coend formula, independently of its homotopy reduction.
"""
from itertools import product
import json
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


class Category:
    def __init__(self, objects, arrows, identities, composition):
        self.objects = list(objects)
        self.arrows = dict(arrows)
        self.identities = dict(identities)
        self.composition = dict(composition)

    def hom(self, a, b):
        return [f for f, (s,t) in self.arrows.items() if (s,t)==(a,b)]

    def comp(self, g, f):
        return self.composition[g,f]

    def check(self):
        for a in self.objects:
            assert self.arrows[self.identities[a]] == (a,a)
        for f,(a,b) in self.arrows.items():
            assert self.comp(self.identities[b],f)==f
            assert self.comp(f,self.identities[a])==f
        pairs=triples=0
        for f,(a,b) in self.arrows.items():
            for g,(bb,c) in self.arrows.items():
                if b!=bb: continue
                pairs+=1
                assert self.arrows[self.comp(g,f)]==(a,c)
                for h,(cc,d) in self.arrows.items():
                    if cc!=c: continue
                    triples+=1
                    assert self.comp(h,self.comp(g,f))==self.comp(self.comp(h,g),f)
        return {'objects':len(self.objects),'arrows':len(self.arrows),
                'composable_pairs':pairs,'associativity_triples':triples}


def thin(objects, le):
    arrows={(a,b):(a,b) for a in objects for b in objects if le(a,b)}
    return Category(objects,arrows,{a:(a,a) for a in objects},
       {(g,f):(arrows[f][0],arrows[g][1]) for f in arrows for g in arrows
        if arrows[f][1]==arrows[g][0]})


def make_c035():
    objects=['a','t','s']
    arr={f'id_{a}':(a,a) for a in objects}
    arr.update(alpha=('a','t'),beta=('a','t'),gamma=('t','s'),delta=('a','s'))
    ids={a:f'id_{a}' for a in objects}
    comp={}
    for f,(a,b) in arr.items():
        comp[ids[b],f]=f; comp[f,ids[a]]=f
    comp['gamma','alpha']='delta';comp['gamma','beta']='delta'
    return Category(objects,arr,ids,comp)


def make_sphere_and_cone(with_cone=True):
    objects=['x','z','a','b']+(['s'] if with_cone else [])
    arr={f'id_{a}':(a,a) for a in objects}
    arr.update(alpha=('x','z'),beta=('x','z'),r=('z','a'),v=('z','b'),
               ra=('x','a'),va=('x','b'))
    if with_cone:
        for a in objects[:-1]: arr['to_s_'+a]=(a,'s')
    ids={a:f'id_{a}' for a in objects};comp={}
    for f,(a,b) in arr.items():
        comp[ids[b],f]=f;comp[f,ids[a]]=f
    for f in ['alpha','beta']:
        comp['r',f]='ra';comp['v',f]='va'
    if with_cone:
        for f,(a,b) in arr.items():
            if b!='s': comp['to_s_'+b,f]='to_s_'+a
    return Category(objects,arr,ids,comp)


def make_h_not_df():
    objects=['0','1','t','s']
    arr={f'id_{a}':(a,a) for a in objects}
    arr.update(a=('0','1'),beta=('1','t'),gamma=('1','t'),c=('0','t'))
    for a in objects[:-1]:arr['to_s_'+a]=(a,'s')
    ids={a:f'id_{a}' for a in objects};comp={}
    for f,(a,b) in arr.items():comp[ids[b],f]=f;comp[f,ids[a]]=f
    comp['beta','a']='c';comp['gamma','a']='c'
    for f,(a,b) in arr.items():
        if b!='s':comp['to_s_'+b,f]='to_s_'+a
    return Category(objects,arr,ids,comp)


def functor_check(C,D,obj,arr):
    for f,(a,b) in C.arrows.items(): assert D.arrows[arr[f]]==(obj[a],obj[b])
    for a in C.objects: assert arr[C.identities[a]]==D.identities[obj[a]]
    for (g,f),h in C.composition.items(): assert D.comp(arr[g],arr[f])==arr[h]
    return True


def natural_check(C,D,Fobj,Farr,Gobj,Garr,eta):
    for a in C.objects: assert D.arrows[eta[a]]==(Fobj[a],Gobj[a])
    for f,(a,b) in C.arrows.items():
        assert D.comp(Garr[f],eta[a])==D.comp(eta[b],Farr[f])
    return True


def homology(C):
    nonid=[f for f in C.arrows if f not in C.identities.values()]
    chains=[[(a,) for a in C.objects],[(f,) for f in nonid]]
    while chains[-1]:
        nexts=[]
        for ch in chains[-1]:
            t=C.arrows[ch[-1]][1]
            nexts.extend(ch+(f,) for f in nonid if C.arrows[f][0]==t)
        chains.append(nexts)
    matrices=[Matrix.zeros(0,len(chains[0]))]
    for n in range(1,len(chains)):
        idx={ch:i for i,ch in enumerate(chains[n-1])}
        M=Matrix.zeros(len(chains[n-1]),len(chains[n]))
        for j,ch in enumerate(chains[n]):
            if n==1:
                a,b=C.arrows[ch[0]]; faces=[(b,),(a,)]
            else:
                faces=[ch[1:]]
                for k in range(1,n):
                    faces.append(ch[:k-1]+(C.comp(ch[k],ch[k-1]),)+ch[k+1:])
                faces.append(ch[:-1])
            for k,f in enumerate(faces): M[idx[f],j]+=(-1)**k
        matrices.append(M)
    for n in range(2,len(matrices)):
        assert matrices[n-1]*matrices[n]==Matrix.zeros(matrices[n-1].rows,matrices[n].cols)
    ranks=[m.rank() for m in matrices]
    torsion=[]
    for M in matrices[1:]:
        S=smith_normal_form(M,domain=ZZ)
        diagonal=[abs(int(S[i,i])) for i in range(min(S.rows,S.cols)) if S[i,i]]
        assert all(v==1 for v in diagonal),diagonal
        torsion.append(diagonal)
    betti=[len(chains[n])-ranks[n]-ranks[n+1] for n in range(len(chains)-1)]
    return {'nondegenerate_simplices':[len(x) for x in chains[:-1]],
            'integral_homology_free_ranks':betti,
            'all_nonzero_smith_entries_are_one':True}


def interval_pushout(n,with_cone=True):
    I=list(range(2*n+1))
    def ile(a,b): return a==b or (a%2==0 and abs(a-b)==1)
    P=thin([(r,k) for r in [0,1] for k in I],
           lambda x,y:x[0]<=y[0] and ile(x[1],y[1]))
    U=[x for x in P.objects if x[0]==0 or x[1] in (0,2*n)]
    T=[x for x in P.objects if x not in U]
    D=make_sphere_and_cone(with_cone)
    pobj={u:('z' if u==(0,0) else 'b' if u==(1,0) else 'a') for u in U}
    parr={}
    for f,(u,v) in P.arrows.items():
        if u not in U or v not in U: continue
        a,b=pobj[u],pobj[v]
        parr[f]=D.identities[a] if a==b else 'r' if b=='a' else 'v'
    A=Category(U,{f:st for f,st in P.arrows.items() if st[0] in U and st[1] in U},
               {u:P.identities[u] for u in U},
               {(g,f):h for (g,f),h in P.composition.items()
                if P.arrows[f][0] in U and P.arrows[g][1] in U})
    functor_check(A,D,pobj,parr)
    objs=[('D',a) for a in D.objects]+[('T',t) for t in T]
    arrows={('D',f):(('D',a),('D',b)) for f,(a,b) in D.arrows.items()}
    arrows.update({('T',f):(('T',a),('T',b)) for f,(a,b) in P.arrows.items() if a in T and b in T})
    reprs={};lookup={};crossid=0
    for c,t in product(D.objects,T):
        pairs=[(u,b) for u in U if (u,t) in P.arrows for b in D.hom(c,pobj[u])]
        parent={p:p for p in pairs}
        def find(x):
            while parent[x]!=x: x=parent[x]
            return x
        for f,(u,v) in A.arrows.items():
            if (v,t) not in P.arrows: continue
            for b in D.hom(c,pobj[u]):
                x,y=find((u,b)),find((v,D.comp(parr[f],b)))
                if x!=y: parent[x]=y
        components={}
        for pair in pairs: components.setdefault(find(pair),[]).append(pair)
        for component in components.values():
            key=('cross',crossid);crossid+=1
            arrows[key]=(('D',c),('T',t));reprs[key]=component[0]
            for pair in component: lookup[c,t,pair]=key
    ids={('D',a):('D',D.identities[a]) for a in D.objects}
    ids.update({('T',t):('T',P.identities[t]) for t in T})
    comp={}
    for f,(a,b) in arrows.items():
        for g,(bb,c) in arrows.items():
            if b!=bb: continue
            if f[0]=='D' and g[0]=='D': h=('D',D.comp(g[1],f[1]))
            elif f[0]=='T' and g[0]=='T': h=('T',P.comp(g[1],f[1]))
            elif f[0]=='D' and g[0]=='cross':
                u,z=reprs[g];h=lookup[a[1],c[1],(u,D.comp(z,f[1]))]
            elif f[0]=='cross' and g[0]=='T':
                u,z=reprs[f];h=lookup[a[1],c[1],(u,z)]
            else: raise AssertionError((f,g))
            comp[g,f]=h
    Q=Category(objs,arrows,ids,comp)
    # Relative deformation onto D plus the first upper sink.
    Robj={a:('D','a') if a[0]=='T' and a[1]!=(1,1) else a for a in objs}
    Rarr={}
    for f,(a,b) in arrows.items():
        if a==Robj[a] and b==Robj[b]:Rarr[f]=f
        else:
            hom=Q.hom(Robj[a],Robj[b]);assert len(hom)==1,(f,hom)
            Rarr[f]=hom[0]
    functor_check(Q,Q,Robj,Rarr)
    identobj={a:a for a in objs};identarr={f:f for f in arrows}
    eta={a:Q.identities[a] if Robj[a]==a else Q.hom(Robj[a],a)[0] for a in objs}
    natural_check(Q,Q,Robj,Rarr,identobj,identarr,eta)
    return {'n':n,'base_has_added_cone':with_cone,'source':{**A.check(),**homology(A)},
            'target':{**P.check(),**homology(P)},
            'base_change_target':{**D.check(),**homology(D)},
            'ordinary_pushout':{**Q.check(),**homology(Q)},
            'relative_deformation_to_expected_cone_union_verified':True}


def main():
    X=make_c035();X.check()
    identobj={a:a for a in X.objects};identarr={f:f for f in X.arrows}
    Fobj={'a':'a','t':'s','s':'s'}
    Farr={f:('delta' if a=='a' and b!='a' else X.identities[Fobj[a]])
          for f,(a,b) in X.arrows.items()}
    Robj={a:'a' for a in X.objects};Rarr={f:'id_a' for f in X.arrows}
    functor_check(X,X,Fobj,Farr);functor_check(X,X,Robj,Rarr)
    natural_check(X,X,identobj,identarr,Fobj,Farr,{'a':'id_a','t':'gamma','s':'id_s'})
    natural_check(X,X,Robj,Rarr,Fobj,Farr,{'a':'id_a','t':'delta','s':'delta'})
    print(json.dumps({'C035':{**X.check(),**homology(X),
        'boundary_at_t':{'objects':2,'nonidentity_arrows':0},
        'relative_natural_zigzag_checked':True}},indent=2))
    Y=make_h_not_df()
    Iobj={a:a for a in Y.objects};Iarr={f:f for f in Y.arrows}
    Robj={a:a if a in ['0','1'] else '1' for a in Y.objects}
    Rarr={f:(Y.identities[Robj[a]] if Robj[a]==Robj[b] else 'a')
          for f,(a,b) in Y.arrows.items()}
    Fobj={a:a if a in ['0','1'] else 's' for a in Y.objects}
    Farr={f:(f if a in ['0','1'] and b in ['0','1'] else
              Y.identities['s'] if a in ['t','s'] else 'to_s_'+a)
          for f,(a,b) in Y.arrows.items()}
    functor_check(Y,Y,Robj,Rarr);functor_check(Y,Y,Fobj,Farr)
    natural_check(Y,Y,Iobj,Iarr,Fobj,Farr,
        {'0':'id_0','1':'id_1','t':'to_s_t','s':'id_s'})
    natural_check(Y,Y,Robj,Rarr,Fobj,Farr,
        {'0':'id_0','1':'id_1','t':'to_s_1','s':'to_s_1'})
    # Normalized chains of two simplicial cones on Delta[1]/boundary.
    d1=Matrix([[0,-1,-1],[0,1,0],[0,0,1]])
    d2=Matrix([[1,1],[0,0],[0,0]])
    assert d1*d2==Matrix.zeros(3,2)
    betti=[3-d1.rank(),3-d1.rank()-d2.rank(),2-d2.rank()]
    assert betti==[1,0,1]
    print(json.dumps({'h_not_discretely_flat':{**Y.check(),**homology(Y),
       'relative_natural_zigzag_checked':True,
       'mapping_space_test_double_cone_circle_homology_ranks':betti}},indent=2))
    for n in [2,3]:print(json.dumps({'C048':interval_pushout(n)},indent=2))
    print(json.dumps({'C048_W2_couniversality_test':interval_pushout(2,False)},indent=2))


if __name__=='__main__':main()
