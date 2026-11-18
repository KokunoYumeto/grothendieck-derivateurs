"""Exact finite certificates for the finite-rank periodic-anchor diagram G34."""
from itertools import product,combinations
from collections import Counter

def labels(m,bound):
    arrows=list(combinations(range(m),2))
    out=[]
    for n in range(1,bound+1):
        out += [s for s in product(arrows,repeat=n) if all(s[i][1]!=s[i+1][0] for i in range(n-1))]
    return out

def fmap(s,e):return tuple((e[a],e[b]) for a,b in s)
def word(s):return [('g',i) for a,b in s for i in range(a,b)]
def image(a,e,d):
    if a[0]=='g':return [('g',i) for i in range(e[a[1]],e[a[1]+1])]
    typ,s=a
    fs=fmap(s,e)
    return word(fs)*d+[(typ,fs)]

count=0
basis=0
for n in range(1,4):
    for size in range(n,n+2):
        js=labels(n,size)
        gens=[('g',i) for i in range(n-1)]+[(p,s) for s in js for p in ['p','q']]
        for m in range(n,5):
            mid_size=max(size,m)
            for e in combinations(range(m),n):
                for k in range(m,6):
                    end_size=max(mid_size,k)+1
                    for f in combinations(range(k),m):
                        comp=tuple(f[i] for i in e)
                        for a in gens:
                            direct=image(a,comp,end_size-size)
                            twice=sum((image(b,f,end_size-mid_size) for b in image(a,e,mid_size-size)),[])
                            assert direct==twice
                            count+=1
                for s in js:
                    fs=fmap(s,e)
                    assert all(fs[i][1]!=fs[i+1][0] for i in range(len(fs)-1))
                    assert len(fs)<=mid_size
                    for typ in ['p','q']:
                        lhs=Counter(image((typ,s),e,mid_size-size))
                        lhs.update(word(fs)*size)
                        rhs=Counter([(typ,fs)]+word(fs)*mid_size)
                        assert lhs==rhs
                        basis+=1

def red(w):
    out=[]
    for a,sgn in w:
        if out and out[-1]==(a,-sgn):out.pop()
        else:out.append((a,sgn))
    return out

nielsen=0
for s in labels(3,3):
    for d in range(5):
        base=word(s)*d
        for typ in ['p','q']:
            anchor=(typ,s)
            forward=[(a,1) for a in base]+[(anchor,1)]
            inverse=[(a,-1) for a in base[::-1]]+[(anchor,1)]
            # Apply inverse substitution to forward; base letters fixed.
            assert red([(a,1) for a in base]+inverse)==[(anchor,1)]
            # Apply forward substitution to inverse.
            assert red([(a,-1) for a in base[::-1]]+forward)==[(anchor,1)]
            nielsen+=2
print('Exact anchor functoriality identities:',count)
print('Natural integral basis identities:',basis)
print('Two-sided free-group Nielsen inverse identities:',nielsen)
print('All normal-form label maps preserve finite reduced-arrow length.')
print('PASS')
