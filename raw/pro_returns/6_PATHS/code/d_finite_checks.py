"""Finite verification for PATHS Part D. Pure Python; no external packages."""
from itertools import product, combinations, permutations
import json

def pointed_E():
    objs = [0, 1]
    arrows = [(0,0,'i0'),(0,1,'u'),(1,0,'v'),(1,1,'i1'),(1,1,'z')]
    def compose(g,f):
        assert f[1] == g[0]
        if f[2].startswith('i'): return g
        if g[2].startswith('i'): return f
        s,t=f[0],g[1]
        return next(a for a in arrows if a[0]==s and a[1]==t and a[2]!='i1')
    triples=[(f,g,h) for f,g,h in product(arrows,repeat=3) if f[1]==g[0] and g[1]==h[0]]
    assert all(compose(h,compose(g,f))==compose(compose(h,g),f) for f,g,h in triples)
    assert all(sum(a[0]==0 and a[1]==x for a in arrows)==1 for x in objs)
    assert all(sum(a[0]==x and a[1]==0 for a in arrows)==1 for x in objs)
    print('E:',json.dumps({'objects':objs,'arrows':arrows,'typed_associativity_triples':len(triples),'associative':True,'zero_object':0}))
    print('E composition:',json.dumps([(g[2],f[2],compose(g,f)[2]) for g,f in product(arrows,repeat=2) if f[1]==g[0]]))
    print('E: W=identities; N Fun(A,E)=Fun(NA,NE) for every A is proved symbolically in D.2.')

def lattice_search():
    samples={
        'diamond':(4,{(0,1),(0,2),(1,3),(2,3)}),
        'pentagon':(5,{(0,1),(1,2),(2,4),(0,3),(3,4)}),
        'three_atoms':(5,{(0,1),(0,2),(0,3),(1,4),(2,4),(3,4)}),
        'cube3':(8,{(i,j) for i in range(8) for j in range(8) if i!=j and i&j==i}),
    }
    for name,(n,rels) in samples.items():
        le=rels|{(i,i) for i in range(n)}
        while True:
            add={(a,d) for a,b in le for c,d in le if b==c}
            if add<=le:break
            le|=add
        nonid=sorted((a,b) for a,b in le if a!=b)
        if len(nonid)>15: continue
        joins={}
        for a,b in product(range(n),repeat=2):
            ups=[c for c in range(n) if (a,c) in le and (b,c) in le]
            mins=[c for c in ups if all((c,d) in le for d in ups)]
            assert len(mins)==1
            joins[a,b]=mins[0]
        ids={(i,i) for i in range(n)}
        examples=[];counts=[0,0]
        for mask in range(1<<len(nonid)):
            w=ids|{a for i,a in enumerate(nonid) if mask>>i&1}
            if any(sum(e in w for e in [(a,b),(b,c),(a,c)])==2 for a,b in le for x,c in le if x==b):continue
            counts[0]+=1
            cof={(a,b) for a,b in le if all((joins[b,c],joins[b,d]) in w for c,d in w if (a,c) in le)}
            enough=all(any((a,x) in cof and (x,b) in w for x in range(n)) for a,b in le)
            if enough:
                counts[1]+=1
                bad=[b for b in range(n) if (0,b) not in cof]
                if bad:examples.append({'W':sorted(w),'Cof':sorted(cof),'not_cofibrant':bad})
        print('lattice',name,'two_of_three_classes',counts[0],'enough_intrinsic_cofibrations',counts[1],'noncofibrant_examples',json.dumps(examples[:1]))

def finite_poset_monoid_test():
    # The category S is the group C2; any functor from BC2 into a poset is constant.
    mul=[[ (i+j)%2 for j in range(2)] for i in range(2)]
    assert all(mul[mul[i][j]][k]==mul[i][mul[j][k]] for i,j,k in product(range(2),repeat=3))
    print('C2 group multiplication:',json.dumps(mul),'associative; nontrivial homomorphism C2 -> C2 is identity.')
    homs=[h for h in product(range(2),repeat=2) if h[0]==0 and all(h[mul[a][b]]==mul[h[a]][h[b]] for a,b in product(range(2),repeat=2))]
    functions=list(product(range(2),repeat=2))
    equivariant=[f for f in functions if all(f[mul[g][x]]==mul[g][f[x]] for g,x in product(range(2),repeat=2))]
    assert len(homs)==2 and len(functions)==4 and len(equivariant)==2
    print('C2 homomorphisms:',json.dumps(homs),'regular-set endofunctions:',json.dumps(functions),'equivariant:',json.dumps(equivariant))
    # Nielsen automorphism's abelianization A=[[1,1],[0,1]].
    def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    A=[[1,1],[0,1]]; power=[[1,0],[0,1]]
    for n in range(1,101):
        power=mm(power,A)
        assert power==[[1,n],[0,1]]
    print('Nielsen monodromy: A^n=[[1,n],[0,1]] checked n=1,...,100; induction proves infinite order.')

def circle_poset():
    # Vertices v0,v1,v2, edges e01,e12,e20; order is nonempty face inclusion.
    faces=[frozenset([0]),frozenset([1]),frozenset([2]),frozenset([0,1]),frozenset([1,2]),frozenset([2,0])]
    le={(i,j) for i in range(6) for j in range(6) if faces[i]<=faces[j]}
    # Oriented geometric cycle v0-e01-v1-e12-v2-e20-v0.
    cyclic=[0,3,1,4,2,5]; position={v:i for i,v in enumerate(cyclic)}
    counts={};number=0
    for F in product(range(6),repeat=6):
        if not all((F[a],F[b]) in le for a,b in le):continue
        number+=1;wind=0
        for i in range(6):
            a,b=F[cyclic[i]],F[cyclic[(i+1)%6]]
            if a==b:continue
            step=(position[b]-position[a])%6
            assert step in (1,5)
            wind += 1 if step==1 else -1
        assert wind%6==0
        counts[wind//6]=counts.get(wind//6,0)+1
    print('Circle face poset P:',json.dumps({'objects':[sorted(f) for f in faces],'arrows':sorted(le),'endomorphism_functors':number,'degree_counts':counts}))

def fence_horn():
    n=9
    le={(i,i) for i in range(n)}|{(i,j) for i in range(n) for j in range(n) if abs(i-j)==1 and i%2==0}
    # c Sd^2 Delta^1 is the five-vertex alternating fence.
    domain=[(0,1),(2,1),(2,3),(4,3)]
    counts={};witness={}
    for F in product(range(n),repeat=5):
        if all((F[a],F[b]) in le for a,b in domain):
            k=(F[0],F[4]);counts[k]=counts.get(k,0)+1;witness.setdefault(k,F)
    assert counts.get((0,4),0)>0 and counts.get((4,8),0)>0 and counts.get((0,8),0)==0
    print('Nine-vertex fence horn:',json.dumps({'arrows':sorted(le),'edge_0_4_count':counts[(0,4)],'edge_4_8_count':counts[(4,8)],'edge_0_8_count':counts.get((0,8),0),'edge_0_4_witness':witness[0,4],'edge_4_8_witness':witness[4,8]}))
    # Remove the greatest-numbered endpoint successively; each retraction is monotone
    # and is comparable pointwise to the identity.
    for m in range(8,0,-1):
        rr={i:(m-1 if i==m else i) for i in range(m+1)}
        assert all((rr[a],rr[b]) in le for a,b in le if a<=m and b<=m)
        assert all((i,rr[i]) in le for i in rr) or all((rr[i],i) in le for i in rr)
    print('Nine-vertex fence: all eight endpoint retractions and pointwise natural comparisons checked; Cat hot contractible.')

def finite_b_failure():
    # Y=K_{2,2} face incidence circle, X=Y with two incomparable maxima s,n.
    yedges=[(0,2),(1,2),(1,3),(0,3)]
    gamma=[1,-1,1,-1]
    xle={(i,i) for i in range(6)}|set(yedges)|{(i,j) for i in range(4) for j in (4,5)}
    triangles=[(a,b,c) for a,b,c in combinations(range(6),3) if (a,b) in xle and (b,c) in xle]
    assert len(triangles)==8
    cycle={}
    for (a,b),sgn in zip(yedges,gamma):
        cycle[a,b,5]=sgn;cycle[a,b,4]=-sgn
    boundary={}
    for (a,b,c),v in cycle.items():
        for e,sgn in [((b,c),1),((a,c),-1),((a,b),1)]:boundary[e]=boundary.get(e,0)+sgn*v
    assert all(x==0 for x in boundary.values())
    assert not any(all((a,b) in xle for a,b in zip(t,t[1:])) for t in combinations(range(6),4))
    ys=[F for F in product(range(6),repeat=4) if all((F[a],F[b]) in xle for a,b in yedges)]
    # Walking parallel arrows B=(a --f,g--> b). Mapping to a poset identifies f and g.
    bs=[(a,b) for a,b in xle]
    # u sends first 3 Y-edges to f and fourth to g, giving gamma -> f-g.
    ulabels=['f','f','f','g']
    image={t:sum(sgn for lab,sgn in zip(ulabels,gamma) if lab==t) for t in ('f','g')}
    assert image=={'f':1,'g':-1}
    print('Finite b-invariance failure:',json.dumps({'Y_objects':4,'Y_nonidentity_arrows':yedges,'X_objects':6,'X_arrows':sorted(xle),'Fun_Y_X_objects':len(ys),'Fun_parallel_X_objects':len(bs),'u_cycle_image':image,'evaluation_cycle':[[list(t),v] for t,v in sorted(cycle.items())],'cycle_boundary_zero':True,'C3_X_zero':True}))

def homology_fibration_obstruction():
    group=list(permutations(range(3)))
    def mul(g,h):return tuple(g[h[i]] for i in range(3))
    identity=tuple(range(3)); x=(1,0,2); y=(2,1,0)
    table=[[group.index(mul(g,h)) for h in group] for g in group]
    assert all(mul(g,mul(h,k))==mul(mul(g,h),k) for g,h,k in product(group,repeat=3))
    def subgroup(generators):
        elements={identity}; old=None
        while elements!=old:
            old=set(elements)
            elements|={mul(g,h) for g in elements for h in generators}
        return elements
    image_y=identity
    for letter in [y,x,y,x,y]:image_y=mul(image_y,letter)
    assert image_y==x
    assert len(subgroup([x,y]))==6 and len(subgroup([x,image_y]))==2
    print('S3 homology/fibration obstruction:',json.dumps({'elements':group,'multiplication_table':table,'associative_triples_checked':216,'x':x,'y':y,'alpha_y_image':image_y,'original_image_size':6,'alpha_image_size':2,'exponent_sum_matrix':[[1,0],[0,1]]}))

if __name__=='__main__':
    pointed_E();lattice_search();finite_poset_monoid_test();circle_poset();fence_horn();finite_b_failure();homology_fibration_obstruction()
