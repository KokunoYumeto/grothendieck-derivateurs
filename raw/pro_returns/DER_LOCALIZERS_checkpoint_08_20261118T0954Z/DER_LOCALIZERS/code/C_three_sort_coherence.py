#!/usr/bin/env python3
"""Finite formal certificate for the tensor used in C.26.

We set E=Id in the three-sort radical-square-zero category.  This makes
the otherwise infinite-coefficient B-map visible in finite matrices.
It tests the tensor formulas and their coherence over the integers.
It does NOT test E(k)=0, the nonzero bidual quotient, or the counterexample's
infinite-dimensional homology.  Those are proved in the manuscript.
"""
from dataclasses import dataclass
from itertools import product
import json
import sympy as sp

# 0,1,2 denote the free projectives. s is the first simple syzygy;
# u is the unit simple.  E=Id makes P2 have dimensions (1,0,1).
DIMS={'0':(1,1,0),'1':(0,1,1),'2':(1,0,1),'s':(0,1,0),'u':(1,0,0)}
ATOMS=tuple(DIMS)

def dims(obj): return tuple(sum(DIMS[a][d] for a in obj) for d in range(3))
def offsets(obj,d):
    out=[0]
    for a in obj: out.append(out[-1]+DIMS[a][d])
    return out

@dataclass
class Mor:
    src:tuple
    dst:tuple
    m:tuple
    def then(self,g):
        assert self.dst==g.src,(self.dst,g.src)
        return Mor(self.src,g.dst,tuple(g.m[d]*self.m[d] for d in range(3)))
    def eq(self,g):
        return self.src==g.src and self.dst==g.dst and all(a==b for a,b in zip(self.m,g.m))

def zero(x,y): return Mor(tuple(x),tuple(y),tuple(sp.zeros(b,a) for a,b in zip(dims(x),dims(y))))
def ident(x): return Mor(tuple(x),tuple(x),tuple(sp.eye(n) for n in dims(x)))
def plus(f,g):
    assert f.src==g.src and f.dst==g.dst
    return Mor(f.src,f.dst,tuple(a+b for a,b in zip(f.m,g.m)))
def scale(c,f): return Mor(f.src,f.dst,tuple(c*m for m in f.m))
def atomic_map(x,y,entries):
    f=zero((x,),(y,))
    return Mor(f.src,f.dst,tuple(sp.Matrix(DIMS[y][d],DIMS[x][d],entries.get(d,[0]*(DIMS[y][d]*DIMS[x][d]))) for d in range(3)))

GEN={('0','0'):('I0',ident(('0',))),('1','1'):('I1',ident(('1',))),
     ('2','2'):('I2',ident(('2',))),('s','s'):('Is',ident(('s',))),
     ('u','u'):('Iu',ident(('u',)))}
for name,x,y,d in [('A','1','0',1),('C','2','1',2),('B','0','2',0),
                    ('i','s','0',1),('q','1','s',1),('p','0','u',0),('j','u','2',0)]:
    GEN[x,y]=(name,atomic_map(x,y,{d:[1]}))
BYNAME={name:f for name,f in GEN.values()}

def pieces(f):
    for a,x in enumerate(f.src):
        for b,y in enumerate(f.dst):
            mats=[]
            for d in range(3):
                os,ot=offsets(f.src,d),offsets(f.dst,d)
                mats.append(f.m[d][ot[b]:ot[b+1],os[a]:os[a+1]])
            if all(m==sp.zeros(*m.shape) for m in mats): continue
            assert (x,y) in GEN,(x,y,mats)
            name,basis=GEN[x,y]
            coeff=None
            for m,n in zip(mats,basis.m):
                for z,w in zip(m,n):
                    if w: coeff=z/w;break
                if coeff is not None:break
            assert coeff is not None
            assert all(m==coeff*n for m,n in zip(mats,basis.m)),(name,mats)
            yield a,b,name,coeff

def atom_tensor(x,y):
    if x=='u':return (y,)
    if y=='u':return (x,)
    if x==y=='0':return ('0','s')
    if x=='0':return (y,)
    if y=='0':return (x,)
    return ()

def tensor_obj(x,y):
    return tuple(a for u in x for v in y for a in atom_tensor(u,v))

def pair_spans(x,y):
    ans={};n=0
    for i,u in enumerate(x):
        for j,v in enumerate(y):
            m=len(atom_tensor(u,v));ans[i,j]=(n,n+m);n+=m
    return ans

def put_block(out,f,srcspan,dstspan,c=1):
    sm,tm=srcspan,dstspan
    mats=list(out.m)
    for d in range(3):
        os,ot=offsets(out.src,d),offsets(out.dst,d)
        r0,r1=ot[tm[0]],ot[tm[1]];c0,c1=os[sm[0]],os[sm[1]]
        mats[d][r0:r1,c0:c1]=mats[d][r0:r1,c0:c1]+c*f.m[d]
    return Mor(out.src,out.dst,tuple(mats))

def one_sided(name,z,first=True):
    f=BYNAME[name];x,y=f.src[0],f.dst[0]
    source=atom_tensor(x,z) if first else atom_tensor(z,x)
    target=atom_tensor(y,z) if first else atom_tensor(z,y)
    if name.startswith('I'):return ident(source)
    if z=='u':return f
    out=zero(source,target)
    if z!='0':
        return ident(source) if name=='p' else out
    mm=list(out.m)
    if name in ('A','i'):
        mm[1]=sp.Matrix([0,1] if first else [1,-1])
    elif name=='C':return BYNAME['C']
    elif name=='B':mm[0]=sp.Matrix([[1]])
    elif name=='q':return BYNAME['q']
    elif name=='p':
        mm[0]=sp.Matrix([[1]])
        mm[1]=sp.Matrix([[1,0] if first else [1,1]])
    elif name=='j':return BYNAME['B']
    else:raise AssertionError(name)
    return Mor(source,target,tuple(mm))

def atom_tensor_maps(nf,ng):
    f,g=BYNAME[nf],BYNAME[ng]
    return one_sided(nf,g.src[0],True).then(one_sided(ng,f.dst[0],False))

def tensor(f,g):
    out=zero(tensor_obj(f.src,g.src),tensor_obj(f.dst,g.dst))
    ss,tt=pair_spans(f.src,g.src),pair_spans(f.dst,g.dst)
    for a,b,nf,cf in pieces(f):
        for c,d,ng,cg in pieces(g):
            out=put_block(out,atom_tensor_maps(nf,ng),ss[a,c],tt[b,d],cf*cg)
    return out

def inclusion(obj,i):
    out=zero((obj[i],),obj)
    return put_block(out,ident((obj[i],)),(0,1),(i,i+1))
def projection(obj,i):
    f=inclusion(obj,i)
    return Mor(obj,(obj[i],),tuple(m.T for m in f.m))

def atom_assoc(x,y,z):
    left=tensor_obj(atom_tensor(x,y),(z,))
    right=tensor_obj((x,),atom_tensor(y,z))
    if x==y==z=='0':
        out=zero(left,right);mm=list(out.m)
        mm[0]=sp.Matrix([[1]])
        mm[1]=sp.Matrix([[1,0,0],[0,1,1],[0,1,0]])
        return Mor(left,right,tuple(mm))
    assert left==right,(x,y,z,left,right)
    return ident(left)

def assoc(x,y,z):
    out=zero(tensor_obj(tensor_obj(x,y),z),tensor_obj(x,tensor_obj(y,z)))
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            for k,c in enumerate(z):
                pre=tensor(tensor(projection(x,i),projection(y,j)),projection(z,k))
                post=tensor(inclusion(x,i),tensor(inclusion(y,j),inclusion(z,k)))
                out=plus(out,pre.then(atom_assoc(a,b,c)).then(post))
    return out

def inverse(f):
    return Mor(f.dst,f.src,tuple(m.inv() if m.rows else sp.zeros(0,0) for m in f.m))

def atom_swap(x,y):
    src,dst=atom_tensor(x,y),atom_tensor(y,x)
    if x==y=='0':
        out=ident(src);mm=list(out.m);mm[1]=sp.Matrix([[1,1],[0,-1]])
        return Mor(src,dst,tuple(mm))
    assert src==dst
    return ident(src)

def swap(x,y):
    out=zero(tensor_obj(x,y),tensor_obj(y,x))
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            pre=tensor(projection(x,i),projection(y,j))
            post=tensor(inclusion(y,j),inclusion(x,i))
            out=plus(out,pre.then(atom_swap(a,b)).then(post))
    return out

counts={}
def check(key,f,g):
    assert f.eq(g),(key,f.src,f.dst,f.m,g.m)
    counts[key]=counts.get(key,0)+1

def run():
    # All atomic nonzero Hom generators, not merely the projective ones.
    maps=list(BYNAME.items())
    for nf,f in maps:
        for ng,g in maps:
            left=one_sided(nf,g.src[0],True).then(one_sided(ng,f.dst[0],False))
            right=one_sided(ng,f.src[0],False).then(one_sided(nf,g.dst[0],True))
            check('interchange',left,right)
            if f.dst==g.src:
                fg=f.then(g)
                for z in ATOMS:
                    check('composition_first',tensor(f,ident((z,))).then(tensor(g,ident((z,)))),tensor(fg,ident((z,))))
                    check('composition_second',tensor(ident((z,)),f).then(tensor(ident((z,)),g)),tensor(ident((z,)),fg))
        for z in ATOMS:
            check('symmetry_naturality',tensor(f,ident((z,))).then(swap(f.dst,(z,))),swap(f.src,(z,)).then(tensor(ident((z,)),f)))
    for a,b in product(ATOMS,repeat=2):
        check('symmetry_involution',swap((a,),(b,)).then(swap((b,),(a,))),ident(tensor_obj((a,),(b,))))
    # Naturality for every nonidentity generator in each associator slot.
    for nf,f in maps:
        if nf.startswith('I'):continue
        for b,c in product(ATOMS,repeat=2):
            b,c=(b,),(c,)
            check('associator_naturality_first',tensor(tensor(f,ident(b)),ident(c)).then(assoc(f.dst,b,c)),assoc(f.src,b,c).then(tensor(f,ident(tensor_obj(b,c)))))
            check('associator_naturality_middle',tensor(tensor(ident(b),f),ident(c)).then(assoc(b,f.dst,c)),assoc(b,f.src,c).then(tensor(ident(b),tensor(f,ident(c)))))
            check('associator_naturality_last',tensor(ident(tensor_obj(b,c)),f).then(assoc(b,c,f.dst)),assoc(b,c,f.src).then(tensor(ident(b),tensor(ident(c),f))))
    for aa in product(ATOMS,repeat=4):
        a,b,c,d=map(lambda x:(x,),aa)
        left=assoc(tensor_obj(a,b),c,d).then(assoc(a,b,tensor_obj(c,d)))
        right=tensor(assoc(a,b,c),ident(d)).then(assoc(a,tensor_obj(b,c),d)).then(tensor(ident(a),assoc(b,c,d)))
        check('pentagon',left,right)
    for aa in product(ATOMS,repeat=3):
        a,b,c=map(lambda x:(x,),aa)
        left=assoc(a,b,c).then(swap(a,tensor_obj(b,c))).then(assoc(b,c,a))
        right=tensor(swap(a,b),ident(c)).then(assoc(b,a,c)).then(tensor(ident(b),swap(a,c)))
        check('hexagon_first',left,right)
        left=swap(tensor_obj(a,b),c)
        right=assoc(a,b,c).then(tensor(ident(a),swap(b,c))).then(inverse(assoc(a,c,b))).then(tensor(swap(a,c),ident(b))).then(assoc(c,a,b))
        check('hexagon_second',left,right)
    for a,b in product(ATOMS,repeat=2):
        a,b=(a,),(b,)
        check('unit_triangle',assoc(a,('u',),b),ident(tensor_obj(a,b)))
    print(json.dumps({'status':'PASS','arithmetic':'exact integer matrices (therefore also characteristic 2 and every odd characteristic)',
                      'model':'E=Id finite three-sort category; not the infinite-dimensional E=bidual/Id counterexample',
                      'checks':counts,'total':sum(counts.values()),
                      'limitation':'The infinite-dimensional nonzero E(W), its vanishing at k, and all general coefficient-strength identities are proved in the manuscript, not inferred from this finite certificate.'},indent=2))

if __name__=='__main__':run()
