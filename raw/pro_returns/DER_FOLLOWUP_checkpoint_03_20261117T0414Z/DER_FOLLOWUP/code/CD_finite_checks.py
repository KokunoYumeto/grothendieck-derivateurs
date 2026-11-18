"""Independent checks for DER_FOLLOWUP Parts C and D.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
R0 arrows are represented as actual functions between sets of size 1 and 2.
No code from the supplied drafter's program is imported.
"""
from itertools import product, combinations, combinations_with_replacement
from collections import defaultdict, Counter

# Arrow = source cardinality, target cardinality, tuple of images.
def identity(n): return n,n,tuple(range(n))
def compose(g,f):
    assert f[1]==g[0]
    return f[0],g[1],tuple(g[2][i] for i in f[2])
R=[identity(1),identity(2),(1,2,(0,)),(2,1,(0,0)),(2,2,(0,0))]
RH={(s,t):[a for a in R if a[:2]==(s,t)] for s,t in product((1,2),repeat=2)}
for f,g,h in product(R,repeat=3):
    if f[1]==g[0] and g[1]==h[0]:
        assert compose(h,compose(g,f))==compose(compose(h,g),f)

def paths(N):
    out=[]
    for n in range(N+1):
        for signs in product((1,-1),repeat=n):
            for rest in product((1,2),repeat=n):
                vertices=(1,)+rest
                choices=[RH[(vertices[i],vertices[i+1]) if signs[i]==1 else (vertices[i+1],vertices[i])] for i in range(n)]
                out.extend((signs,vertices,edges) for edges in product(*choices))
    return out

def path_arrow(path,i,j):
    signs,verts,edges=path
    if i==j:return identity(verts[i])
    ans=edges[i]
    for k in range(i+1,j):
        ans=compose(edges[k],ans) if signs[i]==1 else compose(ans,edges[k])
    return ans

def path_hom(c,d):
    signs,vertices,edges=c
    t,v,e=d
    n,m=len(signs),len(t)
    if n==0:
        return [( (0,), (identity(1),) )] if m==0 else []
    result=[]
    for middle in combinations_with_replacement(range(m+1),n-1):
        phi=(0,)+middle+(m,)
        if any(t[j]!=signs[i] for i in range(n) for j in range(phi[i],phi[i+1])):continue
        choices=[(identity(1),)]+[RH[vertices[i],v[phi[i]]] for i in range(1,n+1)]
        for eta in product(*choices):
            ok=True
            for i in range(n):
                q=path_arrow(d,phi[i],phi[i+1])
                if signs[i]==1: ok=compose(q,eta[i])==compose(eta[i+1],edges[i])
                else: ok=compose(q,eta[i+1])==compose(eta[i],edges[i])
                if not ok:break
            if ok:result.append((phi,eta))
    return result

def pc(g,f):
    phi,eta=f;psi,theta=g
    return tuple(psi[i] for i in phi),tuple(compose(theta[j],a) for j,a in zip(phi,eta))

class DSU:
    def __init__(self, xs):self.p={x:x for x in xs}
    def find(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]];x=self.p[x]
        return x
    def join(self,x,y):self.p[self.find(x)]=self.find(y)

def lattice_rank_unit(relations):
    """Unimodular elimination. Exact if every final nonzero relation has a unit pivot."""
    pivots={};deferred=[]
    for row in relations:
        row={k:v for k,v in row.items() if v}
        while row:
            common=next((p for p in pivots if p in row),None)
            if common is None:break
            c=row[common];piv=pivots[common]
            for k,v in piv.items():
                z=row.get(k,0)-c*v
                if z:row[k]=z
                else:row.pop(k,None)
        if not row:continue
        unit=next((k for k,v in row.items() if abs(v)==1),None)
        if unit is None:deferred.append(row);continue
        coeff=row[unit];row={k:v*coeff for k,v in row.items()}
        pivots[unit]=row
    for row in deferred:
        while row:
            p=next((p for p in pivots if p in row),None)
            if p is None:break
            c=row[p]
            for k,v in pivots[p].items():
                z=row.get(k,0)-c*v
                if z:row[k]=z
                else:row.pop(k,None)
        assert not row,('nonunit relation requires Smith form',row)
    return len(pivots)

def run_paths(N=2):
    obs=paths(N);hom={(i,j):path_hom(c,d) for i,c in enumerate(obs) for j,d in enumerate(obs)}
    print(f'R0 paths of length <= {N}: {len(obs)} objects; {sum(map(len,hom.values()))} arrows.')
    hsets={ij:set(hs) for ij,hs in hom.items()}
    identities=[]
    for i,c in enumerate(obs):
        ident=(tuple(range(len(c[1]))),tuple(identity(v) for v in c[1]))
        identities.append(ident);assert ident in hsets[i,i]
    pairs=0
    for i,j,k in product(range(len(obs)),repeat=3):
        for f in hom[i,j]:
            for g in hom[j,k]:
                assert pc(g,f) in hsets[i,k];pairs+=1
    print('All',pairs,'composable path-arrow pairs have valid composite; function composition supplies associativity.')
    u=(1,2,(0,));r=(2,1,(0,0));iz=identity(2);i0=identity(1)
    for pair in (1,2):
        if pair==1:
            p=obs.index(((1,1),(1,1,2),(i0,u)));d=obs.index(((1,),(1,2),(u,)))
            f=((0,1,1),(i0,u,iz));g=((0,0,1),(i0,i0,iz))
        else:
            p=obs.index(((-1,-1),(1,2,2),(r,iz)));d=obs.index(((-1,),(1,2),(r,)))
            f=((0,1,1),(i0,iz,iz));g=((0,0,1),(i0,r,iz))
        assert f in hsets[p,d] and g in hsets[p,d]
        quot={};Nimages=set()
        for x,c in enumerate(obs):
            ds=DSU(hom[p,x])
            for k in hom[d,x]:ds.join(pc(k,f),pc(k,g))
            quot[x]={k:ds.find(k) for k in hom[p,x]}
            if c[0]:
                assert not ({pc(k,f) for k in hom[d,x]}&{pc(k,g) for k in hom[d,x]})
                # All sums with zero composite have zero endpoint sum, directly fiberwise.
                for side in (f,g):
                    by=defaultdict(set)
                    for k in hom[d,x]:by[pc(k,side)].add(k[1][-1])
                    assert all(len(v)==1 for v in by.values())
            else:
                for k in hom[d,x]:
                    assert pc(k,f)==pc(k,g)
                    for gamma in RH[c[1][-1],2]:Nimages.add(compose(gamma,k[1][-1]))
        assert Nimages=={(2,2,(0,0))}
        print('pair',pair,'kernel tensor image exactly Z.e, so Tor1 = Z on id_z modulo e')
        eo=[(x,h,l) for x,c in enumerate(obs) for h in RH[c[1][-1],2] for l in set(quot[x].values())]
        eindex={o:i for i,o in enumerate(eo)};ea=[]
        for i,(x,h,l) in enumerate(eo):
            for y in range(len(obs)):
                for k in hom[x,y]:
                    nl=quot[y][pc(k,l)]
                    for nh in RH[obs[y][1][-1],2]:
                        if compose(nh,k[1][-1])==h:
                            ea.append((i,eindex[y,nh,nl],k))
        eaindex={a:i for i,a in enumerate(ea)};out=defaultdict(list)
        forest=DSU(range(len(eo)));tree=set();degenerate=set()
        for i,(s,t,k) in enumerate(ea):
            out[s].append(i)
            if s==t and k==identities[eo[s][0]]:degenerate.add(i)
            if forest.find(s)!=forest.find(t):tree.add(i);forest.join(s,t)
        generators=set(range(len(ea)))-tree-degenerate
        def rels():
            for i,(s,t,f0) in enumerate(ea):
                if i in degenerate:continue
                for j in out[t]:
                    if j in degenerate:continue
                    _,w,g0=ea[j]
                    ij=eaindex[s,w,pc(g0,f0)]
                    row=Counter()
                    for e,c in ((i,1),(j,1),(ij,-1)):
                        if e in generators:row[e]+=c
                    yield dict(row)
        nrank=lattice_rank_unit(rels());components=len({forest.find(i) for i in range(len(eo))})
        h1=len(generators)-nrank
        assert components==2 and h1==1
        print('  restricted action category:',len(eo),'objects;',len(ea),'arrows;',len(generators),'cycle generators')
        print('  exact integer unit-pivot calculation: H0 = Z^%d; H1 = Z^%d; no torsion'%(components,h1))


def rewrite(w):
    while True:
        for a,b in [('xy','x'),('yy','y'),('yz','z')]:
            p=w.find(a)
            if p>=0:w=w[:p]+b+w[p+2:];break
        else:return w

def interval_checks():
    rules={'xy':'x','yy':'y','yz':'z'}
    overlaps=[]
    for a,b in product(rules,repeat=2):
        if a[-1]==b[0]:
            w=a+b[1:];v1=rules[a]+b[1:];v2=a[:1]+rules[b]
            assert rewrite(v1)==rewrite(v2);overlaps.append(w)
    print('Interval-monoid critical words:',','.join(overlaps),'all confluent; each rule shortens length.')
    # Every injection on [m] extends by the two endpoints and sends an edge to a contiguous product.
    checked=0
    for m in range(5):
        for n in range(m,6):
            for inj in combinations(range(n+1),m+1):
                phi=(-1,)+inj+(n+1,)
                source=['x']+['y']*m+['z']
                target=['x']+['y']*n+['z']
                for i,s in enumerate(source):
                    image=''.join(target[phi[i]+1:phi[i+1]+1])
                    assert rewrite(image)==s;checked+=1
    print('Interval presentation cocone verified on',checked,'edge images through [5].')
    # On tensoring the Squier/Fox presentation chain complex with Z:
    import sympy as sp
    d2=sp.Matrix([[0,0,0],[1,1,1],[0,0,0]])
    d3=sp.Matrix([[1,0,0,1],[-1,0,1,0],[0,0,-1,-1]])
    assert d2*d3==sp.zeros(3,4)
    assert d2.rank()==1 and d3.rank()==2
    minors=[abs(int(d3.extract(rows,cols).det())) for rows in combinations(range(3),2) for cols in combinations(range(4),2)]
    assert 1 in minors
    print('Interval Squier low-degree matrices: rank d2=1, rank d3=2; primitive image = kernel d2; H1=Z^2,H2=0.')

if __name__=='__main__':
    run_paths(2)
    interval_checks()
    print('All independent finite checks passed.')
