"""Exact finite-category verification and exhaustive small-category search.

All arrows, including identities, are counted.  Nonidentity arrows with each
fixed source/target are consecutive, so all tables are covered but some
isomorphic copies remain.  F_2 ranks use exact integer bit operations.
The exhaustive searches cover every monoid of order <=4 and every connected
category with >=2 objects and at most 6 arrows. They do NOT enumerate all
monoids of order 5 or 6 (external enumeration is explicitly cited in paper).
"""
from itertools import product, combinations
from collections import Counter
import json
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

OUT=Path(__file__).with_suffix('.json')

def rank2(columns):
    pivots={}
    for col in columns:
        while col:
            i=col.bit_length()-1
            if i in pivots: col^=pivots[i]
            else:
                pivots[i]=col
                break
    return len(pivots)

class Category:
    def __init__(self,n,ends,comp,name=''):
        self.n=n; self.ends=tuple(ends); self.comp=dict(comp); self.name=name
        self.m=len(ends); self.nonid=tuple(range(n,self.m))
    def verify(self):
        for x in range(self.n): assert self.ends[x]==(x,x)
        for f,(s,t) in enumerate(self.ends):
            assert self.comp[(s,f)]==f and self.comp[(f,t)]==f
        for (f,g),h in self.comp.items():
            assert self.ends[f][1]==self.ends[g][0]
            assert self.ends[h]==(self.ends[f][0],self.ends[g][1])
        for f,g,h in product(range(self.m),repeat=3):
            if self.ends[f][1]==self.ends[g][0] and self.ends[g][1]==self.ends[h][0]:
                assert self.comp[(self.comp[(f,g)],h)]==self.comp[(f,self.comp[(g,h)])]
        return True
    def simplices(self,d):
        if d==0:return [(i,) for i in range(self.n)]
        ans=[(i,) for i in self.nonid]
        for _ in range(1,d):
            ans=[t+(j,) for t in ans for j in self.nonid if self.ends[t[-1]][1]==self.ends[j][0]]
        return ans
    def boundary(self,d):
        source=self.simplices(d); target=self.simplices(d-1)
        ix={s:i for i,s in enumerate(target)}
        cols=[]
        for s in source:
            if d==1:
                fs=[(self.ends[s[0]][1],),(self.ends[s[0]][0],)]
            else:
                fs=[s[1:]]+[s[:i-1]+(self.comp[(s[i-1],s[i])],)+s[i+1:] for i in range(1,d)]+[s[:-1]]
            col={}
            for i,f in enumerate(fs):
                if d>1 and any(a<self.n for a in f): continue
                j=ix[f]; col[j]=col.get(j,0)+(-1)**i
            cols.append(col)
        return target,source,cols
    def betti2(self,dmax):
        dims=[len(self.simplices(i)) for i in range(dmax+2)]
        ranks=[0]+[rank2(sum(1<<j for j,v in col.items() if v%2) for col in self.boundary(i)[2]) for i in range(1,dmax+2)]
        return [dims[i]-ranks[i]-ranks[i+1] for i in range(dmax+1)]
    def matrix(self,d):
        t,s,cs=self.boundary(d); M=sp.zeros(len(t),len(s))
        for i,c in enumerate(cs):
            for j,v in c.items():M[j,i]=v
        return M
    def data(self):
        return {'name':self.name,'objects':self.n,'arrows':self.m,'endpoints':self.ends,'composition_first_then':[[f,g,h] for (f,g),h in sorted(self.comp.items())]}

def make(n,nonid,mul,name):
    ends=[(i,i) for i in range(n)]+list(nonid)
    comp={}
    for f,(s,t) in enumerate(ends):comp[(s,f)]=f;comp[(f,t)]=f
    for f,g in product(range(n,len(ends)),repeat=2):
        if ends[f][1]==ends[g][0]:comp[(f,g)]=mul(f,g)
    c=Category(n,ends,comp,name);c.verify();return c

def poset(levels,name):
    n=sum(map(len,levels)); level={x:i for i,L in enumerate(levels) for x in L}
    nonid=[(i,j) for i in range(n) for j in range(n) if level[i]<level[j]]
    ix={p:i+n for i,p in enumerate(nonid)}
    return make(n,nonid,lambda f,g:ix[(nonid[f-n][0],nonid[g-n][1])],name)

def rp2_category():
    labels=[(i,j,g) for i in range(3) for j in range(i+1,3) for g in range(2)]
    ix={a:3+k for k,a in enumerate(labels)}
    return make(3,[(i,j) for i,j,g in labels],lambda f,g:ix[(labels[f-3][0],labels[g-3][1],(labels[f-3][2]+labels[g-3][2])%2)],'RP2_three_objects')

def rp2_poset():
    # Antipodal orbits of nonempty faces of the octahedral sphere.
    faces=[]
    for k in range(1,4):
        for coords in combinations(range(3),k):
            for signs in product((0,1),repeat=k):
                f=frozenset(zip(coords,signs)); neg=frozenset((i,1-s) for i,s in f)
                rep=min(tuple(sorted(f)),tuple(sorted(neg)))
                if rep not in faces:faces.append(rep)
    orbit=[{frozenset(f),frozenset((i,1-s) for i,s in f)} for f in faces]
    rel=[(i,j) for i in range(13) for j in range(13) if i!=j and any(a<b for a in orbit[i] for b in orbit[j])]
    ix={a:13+k for k,a in enumerate(rel)}
    c=make(13,rel,lambda f,g:ix[(rel[f-13][0],rel[g-13][1])],'RP2_poset_13')
    return c,faces

def band_monoid(extra=False):
    labels=['1']+[(i,j) for i in range(2) for j in range(2)]+(['q','r'] if extra else [])
    def mul(a,b):
        if a=='1':return b
        if b=='1':return a
        if isinstance(a,tuple):
            return (a[0],b[1] if isinstance(b,tuple) else 0)
        if isinstance(b,tuple):return b
        return a
    ix={a:i for i,a in enumerate(labels)}
    c=make(1,[(0,0)]*(len(labels)-1),lambda f,g:ix[mul(labels[g],labels[f])],'S3_monoid_7' if extra else 'S2_monoid_5')
    return c,labels,mul

def weak_compositions(total,length):
    if length==1:yield (total,);return
    for v in range(total+1):
        for tail in weak_compositions(total-v,length-1):yield (v,)+tail

def connected(n,ends):
    seen={0}
    while True:
        more=seen|{t for s,t in ends if s in seen}|{s for s,t in ends if t in seen}
        if more==seen:return len(seen)==n
        seen=more

def tables(n,m):
    # Identity at i is arrow i. Products recorded in traversal order.
    for counts in weak_compositions(m-n,n*n):
        ends=[(i,i) for i in range(n)]
        for i,k in enumerate(counts):ends.extend([(i//n,i%n)]*k)
        if not connected(n,ends):continue
        hom={(i,j):[a for a,p in enumerate(ends) if p==(i,j)] for i in range(n) for j in range(n)}
        comp={}
        for f,(s,t) in enumerate(ends):comp[(s,f)]=f;comp[(f,t)]=f
        cells=[(f,g) for f,g in product(range(n,m),repeat=2) if ends[f][1]==ends[g][0]]
        if any(not hom[(ends[f][0],ends[g][1])] for f,g in cells):continue
        constraints=[(a,b,c) for a,b,c in product(range(n,m),repeat=3) if ends[a][1]==ends[b][0] and ends[b][1]==ends[c][0]]
        def consistent():
            for a,b,c in constraints:
                ab=comp.get((a,b));bc=comp.get((b,c))
                if ab is None or bc is None:continue
                lhs=comp.get((ab,c));rhs=comp.get((a,bc))
                if lhs is not None and rhs is not None and lhs!=rhs:return False
            return True
        # Most constrained products first.
        cells.sort(key=lambda fg:len(hom[(ends[fg[0]][0],ends[fg[1]][1])]))
        def rec(k):
            if k==len(cells):
                yield Category(n,ends,comp)
                return
            f,g=cells[k]
            for h in hom[(ends[f][0],ends[g][1])]:
                comp[(f,g)]=h
                if consistent():yield from rec(k+1)
            del comp[(f,g)]
        yield from rec(0)

def exact_resolution(c,labels,mul):
    # Left projectives RMe; maps use right multiplication. Verify exactness
    # over Z by primitive-image Smith invariants and dimension counting.
    idx={x:i for i,x in enumerate(labels)}
    def ideal(e):return sorted(set(mul(a,e) for a in labels),key=idx.get)
    if len(labels)==7:
        modules=[[ideal((0,0))],[ideal('q')],[ideal((0,0)),labels],[ideal((0,1)),ideal('q')]]
        coef=[None,[[{(1,0):1,(0,0):-1}]],[[{'1':1},{'r':1,'q':-1}]],[[{},{}],[{'1':1},{'1':1}]]]
    else:
        # Left-module version of Fiedorowicz's resolution.
        modules=[[ideal((0,0))],[labels],[ideal((0,0)),ideal((0,1))]]
        coef=[None,[[{(1,0):1,(0,0):-1}]],[[{'1':1},{'1':1}]]]
    bases=[[(j,a) for j,I in enumerate(P) for a in I] for P in modules]
    mats=[sp.ones(1,len(bases[0]))]
    for d in range(1,len(modules)):
        dest={a:i for i,a in enumerate(bases[d-1])};D=sp.zeros(len(dest),len(bases[d]))
        for col,(j,a) in enumerate(bases[d]):
            for i in range(len(modules[d-1])):
                for b,v in coef[d][i][j].items():D[dest[(i,mul(a,b))],col]+=v
        mats.append(D)
    for i in range(1,len(mats)):assert mats[i-1]*mats[i]==sp.zeros(mats[i-1].rows,mats[i].cols)
    ranks=[]; snfs=[]
    for D in mats:
        S=smith_normal_form(D,domain=ZZ)
        ds=[int(S[i,i]) for i in range(min(S.rows,S.cols)) if S[i,i]]
        assert all(abs(x)==1 for x in ds)
        ranks.append(len(ds));snfs.append(ds)
    for d in range(len(bases)-1):assert len(bases[d])-ranks[d]==ranks[d+1]
    assert ranks[-1]==len(bases[-1])
    return {'module_Z_ranks':[len(b) for b in bases],'differential_ranks_including_augmentation':ranks,'nonzero_Smith_diagonals':snfs,'exact':True}

def main():
    result={'examples':[],'exhaustive':[]}
    for n in range(1,4):
        c=poset([list(range(2*i,2*i+2)) for i in range(n+1)],f'S{n}_poset')
        b=c.betti2(n+1);assert b==[1]+[0]*(n-1)+[1,0]
        print(c.name,'objects',c.n,'arrows',c.m,'Betti_F2',b)
        d=c.data();d['Betti_F2']=b;result['examples'].append(d)
    c=rp2_category();b=c.betti2(3);assert b==[1,1,1,0]
    D2=c.matrix(2);S=smith_normal_form(D2,domain=ZZ)
    # H1 torsion is torsion of C1/im d2; d1 has free image.
    diag=[int(S[i,i]) for i in range(min(S.rows,S.cols)) if S[i,i]]
    assert sorted(map(abs,diag))==[1,1,1,2]
    assert c.matrix(2).rank()==4
    print(c.name,'objects',c.n,'arrows',c.m,'Betti_F2',b,'d2_Smith',diag)
    d=c.data();d.update(Betti_F2=b,d2_Smith=diag);result['examples'].append(d)
    c,faces=rp2_poset();b=c.betti2(3);assert b==[1,1,1,0]
    D2=c.matrix(2);S=smith_normal_form(D2,domain=ZZ)
    diag=[int(S[i,i]) for i in range(min(S.rows,S.cols)) if S[i,i]]
    assert [abs(x) for x in diag if abs(x)>1]==[2]
    assert len(c.simplices(2))-D2.rank()==0
    print(c.name,'objects',c.n,'arrows',c.m,'Betti_F2',b,'d2_Smith_nonunits',[x for x in diag if abs(x)>1])
    d=c.data();d.update(Betti_F2=b,face_orbits=faces,d2_Smith=diag);result['examples'].append(d)
    for extra in (False,True):
        c,labels,mul=band_monoid(extra);certificate=exact_resolution(c,labels,mul)
        b=c.betti2(3);assert b==([1,0,0,1] if extra else [1,0,1,0])
        print(c.name,'objects',c.n,'arrows',c.m,'Betti_F2',b,'resolution',certificate)
        d=c.data();d.update(labels=labels,Betti_F2=b,resolution=certificate);result['examples'].append(d)
    for n in range(1,7):
        maxm=4 if n==1 else 6
        for m in range(n,maxm+1):
            count=0;s2=0;s3=0;s3q=0;dist=Counter();cand=[]
            for c in tables(n,m):
                c.verify();count+=1;b=tuple(c.betti2(3));dist[b]+=1
                s2+=(b==(1,0,1,0));s3+=(b==(1,0,0,1))
                if b==(1,0,0,1):
                    r=[0]+[c.matrix(d).rank() for d in range(1,5)]
                    bq=[len(c.simplices(d))-r[d]-r[d+1] for d in range(4)]
                    s3q+=(bq==[1,0,0,1]);cand.append({'category':c.data(),'Betti_Q':bq})
            row={'objects':n,'arrows':m,'tables':count,'S2_candidates_F2':s2,'S3_candidates_F2':s3,'S3_candidates_Q_and_F2':s3q,'rationally_checked_candidates':cand,'Betti_distribution':{str(k):v for k,v in sorted(dist.items())}}
            result['exhaustive'].append(row)
            print('EXHAUSTIVE',json.dumps(row,sort_keys=True),flush=True)
            if m<=4:assert s2==0
            assert s3q==0
    OUT.write_text(json.dumps(result,indent=2))
    print('Wrote',OUT.name)
if __name__=='__main__':main()
