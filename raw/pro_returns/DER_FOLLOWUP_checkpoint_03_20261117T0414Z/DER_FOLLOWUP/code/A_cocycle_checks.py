"""Finite checks for the uniform cocycle-category construction in Part A.
All dimensions and boundaries are computed from the stated definitions.
These checks supplement, and do not replace, the uniform all-action proof.
"""
from itertools import combinations, permutations, product
from collections import defaultdict
import random


def rank_mod(rows, p):
    if not rows:
        return 0
    a = [[v % p for v in row] for row in rows]
    m, n = len(a), len(a[0])
    k = 0
    for j in range(n):
        pivot = next((i for i in range(k, m) if a[i][j]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        z = pow(a[k][j], -1, p)
        a[k] = [(z*v) % p for v in a[k]]
        for i in range(m):
            if i != k and a[i][j]:
                z = a[i][j]
                a[i] = [(x-z*y) % p for x,y in zip(a[i],a[k])]
        k += 1
        if k == m:
            break
    return k


def sign_perm(a):
    return -1 if sum(a[i] > a[j] for i in range(len(a)) for j in range(i+1,len(a))) % 2 else 1


def value(c, vertices, p):
    if len(set(vertices)) != len(vertices):
        return 0
    return sign_perm(vertices) * c.get(tuple(sorted(vertices)), 0) % p


def coboundary(c, vertices, degree, p):
    return {s: sum((-1)**i * c.get(s[:i]+s[i+1:],0) for i in range(len(s))) % p
            for s in combinations(vertices,degree+2)}


def primitive(c, vertices, degree, anchor, p):
    return {s: value(c,(anchor,)+s,p) for s in combinations(vertices,degree)}


def restrict(c, vertices):
    ss=set(vertices)
    return {s:v for s,v in c.items() if set(s) <= ss}


def amalgam(c_x,c_z,x,z,degree,anchor,p):
    x,z=set(x),set(z)
    b_x=primitive(c_x,sorted(x),degree,anchor,p)
    b_z=primitive(c_z,sorted(z),degree,anchor,p)
    assert restrict(b_x,x&z)==restrict(b_z,x&z)
    b={}
    for s in combinations(sorted(x|z),degree):
        if set(s)<=x:
            b[s]=b_x.get(s,0)
        elif set(s)<=z:
            b[s]=b_z.get(s,0)
        else:
            b[s]=0
    return coboundary(b, sorted(x|z),degree-1,p)


def moore_dimension(r,m,p):
    # Coordinates of an r-cochain on the m-simplex.
    cols=list(combinations(range(m+1),r+1))
    index={s:i for i,s in enumerate(cols)}
    rows=[]
    for s in combinations(range(m+1),r+2):
        row=[0]*len(cols)
        for i in range(r+2):
            row[index[s[:i]+s[i+1:]]]=(-1)**i
        rows.append(row)
    # Moore condition d_i=0 for i=1,...,m.
    for s,j in index.items():
        if any(i not in s for i in range(1,m+1)):
            row=[0]*len(cols);row[j]=1;rows.append(row)
    return len(cols)-rank_mod(rows,p)


def union_complex(blocks):
    out=set()
    for b in blocks:
        for k in range(1,len(b)+1):
            out.update(combinations(sorted(b),k))
    return out


def betti(complex_,degree,p):
    cells={i:sorted(s for s in complex_ if len(s)==i+1) for i in range(degree+2)}
    def bd_rank(i):
        if i==0:
            return 0
        index={s:j for j,s in enumerate(cells[i-1])}
        rows=[[0]*len(cells[i]) for _ in cells[i-1]]
        for j,s in enumerate(cells[i]):
            for k in range(len(s)):
                rows[index[s[:k]+s[k+1:]]][j]=(-1)**k
        return rank_mod(rows,p)
    return len(cells[degree])-bd_rank(degree)-bd_rank(degree+1)


def encode_flag(perm,top_value):
    faces=[tuple(sorted(perm[:i+1])) for i in range(len(perm))]
    objects=tuple((len(f),top_value if i==len(faces)-1 else 0) for i,f in enumerate(faces))
    arrows=tuple(tuple(faces[i+1].index(v) for v in faces[i]) for i in range(len(faces)-1))
    return (objects,arrows)


def boundary(chain):
    objects,arrows=chain
    n=len(objects)-1
    for i in range(n+1):
        obs=objects[:i]+objects[i+1:]
        if i==0:
            arr=arrows[1:]
        elif i==n:
            arr=arrows[:-1]
        else:
            comp=tuple(arrows[i][v] for v in arrows[i-1])
            arr=arrows[:i-1]+(comp,)+arrows[i+1:]
        yield (-1)**i,(obs,arr)


def last_vertex_value(chain):
    objects,arrows=chain
    vertices=[]
    for i,(size,_) in enumerate(objects):
        v=size-1
        for arrow in arrows[i:]:
            v=arrow[v]
        vertices.append(v)
    if len(set(vertices)) != len(vertices):
        return 0
    return objects[-1][1]


def main():
    print('Moore normalized dimensions, directly from cocycle and face equations:')
    for p in (2,3):
        for r in range(2,7):
            dims=[moore_dimension(r,m,p) for m in range(r+4)]
            assert dims==[int(m==r) for m in range(r+4)]
            print(f'  p={p}, r={r}, m=0..{r+3}: {dims}')
    print('PASS: normalized complex concentrated in degree r with one generator.')
    count=0
    for d,b,c in product(range(3),range(1,4),range(1,4)):
        dd=set(range(d));b0=set(range(d,d+b));b1=set(range(d+b,d+2*b));cc=set(range(d+2*b,d+2*b+c))
        pieces=[dd|b0|b1,dd|b0|cc,dd|b1|cc]
        k=union_complex(pieces)
        for p in (2,3):
            for r in range(2,5):
                assert betti(k,r,p)==0
                count+=1
            assert betti(k,1,p)==(1 if d==0 else 0)
    print(f'PASS: {count} degree-2..4 three-piece cohomology checks; H_1=1 exactly for empty common base.')
    rng=random.Random(20261117)
    trials=0
    for p in (2,3,5):
        for r in range(2,5):
            # Base {0,1}; X subset Xprime, Z meets Xprime exactly in base.
            base={0,1};xp=set(range(0,8));x={0,1,2,4,6};z={0,1,8,9,10}
            for _ in range(30):
                h={s:rng.randrange(p) for s in combinations(sorted(xp|z),r)}
                global_c=coboundary(h,sorted(xp|z),r-1,p)
                cxp=restrict(global_c,xp);cx=restrict(global_c,x);cz=restrict(global_c,z)
                ax=amalgam(cx,cz,x,z,r,0,p)
                axp=amalgam(cxp,cz,xp,z,r,0,p)
                assert restrict(axp,x|z)==ax
                assert restrict(ax,x)==cx and restrict(ax,z)==cz
                assert all(v==0 for v in coboundary(ax,sorted(x|z),r,p).values())
                trials+=1
    print(f'PASS: {trials} anchored amalgam checks, restrictions and naturality, p=2,3,5.')
    for n in range(2,7):
        cycle=defaultdict(int)
        for perm in permutations(range(n+1)):
            s=sign_perm(perm)
            cycle[encode_flag(perm,1)]+=s
            cycle[encode_flag(perm,0)]-=s
        bd=defaultdict(int)
        for c,z in cycle.items():
            for sign,f in boundary(c):
                bd[f]+=sign*z
        assert all(v==0 for v in bd.values())
        eval_=sum(z*last_vertex_value(c) for c,z in cycle.items())%2
        assert eval_==1
        print(f'PASS: xi_{n}: {len(cycle)} signed flags; integer boundary zero; cocycle evaluation mod 2 = {eval_}.')
    # Three-object initial-poset witness T1\Q2.
    objs=range(3)
    le=lambda a,b:a==b or a==0
    assert all(le(0,b) for b in objs)
    assert not any(le(1,b) and le(2,b) for b in objs)
    print('PASS: three-object initial poset has no common successor for its two maximal objects.')
    print('ALL FINITE CHECKS PASSED. The universal action quantifier is proved in A.7, not sampled here.')

if __name__=='__main__':
    main()
