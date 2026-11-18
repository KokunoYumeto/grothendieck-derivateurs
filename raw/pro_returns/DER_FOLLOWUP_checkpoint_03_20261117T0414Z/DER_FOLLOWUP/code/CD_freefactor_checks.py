"""Independent exact checks for finite/finitely presented data in Part D.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).
No program from an earlier return is imported.
"""
from itertools import product, combinations
from fractions import Fraction

def reduce_word(w):
    out=[]
    for x in w:
        if out and out[-1] == -x: out.pop()
        else: out.append(x)
    return tuple(out)

def substitute(w, images):
    out=[]
    for x in w:
        v=images[abs(x)]
        out.extend(v if x>0 else tuple(-a for a in reversed(v)))
    return reduce_word(out)

# a=1, c=2, b=3. Nielsen automorphism and its proposed inverse.
g={1:(1,3), 2:(2,3,3), 3:(3,)}
h={1:(1,-3), 2:(2,-3,-3), 3:(3,)}
for x in (1,2,3,-1,-2,-3):
    assert substitute(substitute((x,),g),h)==(x,)
    assert substitute(substitute((x,),h),g)==(x,)
print('C.9: the two substitutions are mutually inverse on every signed basis element.')
words=[()];tested=0
for n in range(1,10):
    words=[w+(x,) for w in words for x in (1,-1,2,-2) if not w or x!=-w[-1]]
    for w in words:
        image=substitute(w,g)
        assert any(abs(x)==3 for x in image)
        tested+=1
print(f'C.9: all {tested} nonempty reduced words of lengths 1..9 have a surviving b letter in their g-image.')
# The integral Mayer--Vietoris map on H1, in rows a,c,b.
mat=((0,0),(0,0),(-1,-2));kernel=(2,-1)
assert all(sum(row[i]*kernel[i] for i in range(2))==0 for row in mat)
assert mat[2][0] == -1
print('C.9: Mayer--Vietoris matrix [[0,0],[0,0],[-1,-2]] has primitive kernel Z.(2,-1); H2=Z.')
# In the group-colimit relations a=ab and c=cb^2, the first kills b.
assert reduce_word((-1,1,3)) == (3,)
assert substitute((2,3,3), {1:(1,),2:(2,),3:()})==(2,)
print('C.9: eliminating b by the first colimit relation makes the second trivial; colimit is F(a,c).')

# Finite checks of absolute and relative private-vertex eliminations.
def subsets(s):
    s=tuple(s)
    for n in range(len(s)+1):
        yield from (frozenset(t) for t in combinations(s,n))

def rank(rows, ncols):
    rows=[[Fraction(a) for a in row] for row in rows]
    r=0
    for c in range(ncols):
        j=next((j for j in range(r,len(rows)) if rows[j][c]),None)
        if j is None:continue
        rows[r],rows[j]=rows[j],rows[r]
        q=rows[r][c];rows[r]=[a/q for a in rows[r]]
        for j in range(r+1,len(rows)):
            q=rows[j][c]
            if q: rows[j]=[a-q*b for a,b in zip(rows[j],rows[r])]
        r+=1
    return r

valid=afamilies=rfamilies=closed_embeddings=0
for n in range(6):
    vertices=frozenset(range(n));vs=list(subsets(vertices))
    triples=list(combinations(range(n),3))
    for bits in product((0,1),repeat=len(triples)):
        edges=[frozenset(e) for e,b in zip(triples,bits) if b]
        delta={u:2*len(u)-3*sum(e<=u for e in edges) for u in vs}
        if any(delta[u]<=0 for u in vs if u):continue
        valid+=1
        def closed(y):return all(delta[u]>delta[y] for u in vs if y<u)
        points=[v for v in vertices if closed(frozenset((v,)))]
        actual=[e for e in edges if closed(e)]
        assert all(e<=set(points) for e in actual)
        relrows=[]
        for e in actual:
            a,b,c=sorted(e);row=[0]*(2*len(points))
            row[points.index(b)]+=1;row[points.index(a)]-=1
            row[len(points)+points.index(c)]+=1;row[len(points)+points.index(a)]-=1
            relrows.append(row)
        assert rank(relrows,2*len(points))==len(actual)
        for family in subsets(range(len(actual))):
            if not family:continue
            deg={v:sum(v in actual[i] for i in family) for v in vertices}
            assert any(d==1 for d in deg.values())
            afamilies+=1
        for y in vs:
            if not closed(y):continue
            closed_embeddings+=1
            new=[e for e in actual if not e<=y]
            for family in subsets(range(len(new))):
                if not family:continue
                deg={v:sum(v in new[i] for i in family) for v in vertices-y}
                assert any(d==1 for d in deg.values())
                rfamilies+=1
print(f'C_delta: {valid} positive ordered hypergraphs through 5 vertices; {closed_embeddings} closed-subobject embeddings.')
print(f'C_delta: {afamilies} nonempty actual-edge families have a private vertex; {rfamilies} relative families have a new private vertex.')
print('C_delta: every tested integral relation matrix has full row rank, independently of the private-vertex check.')
print('All independent Part D checks passed. Bounded enumeration supports, and does not replace, the general proofs.')
