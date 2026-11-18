from collections import Counter
import sympy as sp

def reduce_word(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return tuple(out)
def mul(h,g): return reduce_word(h+g)
a=(1,); b=(2,); c=(-2,-1); ab=mul(a,b)
assert mul(ab,c)==()
def boundary_group(f,g):
    d=Counter()
    for w,n in [(g,1),(mul(g,f),-1),(f,1)]:
        if w: d[w]+=n
    return d
boundary=boundary_group(b,a)
boundary.update(boundary_group(c,ab))
expected=Counter({a:1,b:1,c:1})
assert {k:v for k,v in boundary.items() if v}==dict(expected)
cellular=sp.Matrix([[1,0,-1],[0,1,-1]])
assert cellular.rank()==2
assert cellular.nullspace()==[sp.Matrix([1,1,1])]
print('F(a,b) word convention: composition h after g = hg.')
print('Verified (ab)c=1 for c=b^-1 a^-1.')
print('Boundary([b,a]+[c,ab])=[a]+[b]+[c].')
print('Therefore z=sum_x[u_x,gamma_x]-[b,a]-[c,ab] is a cycle.')
print('Cellular d2 =', cellular.tolist())
print('rank(d2)=2; ker(d2)=Z*(1,1,1); gcd maximal minors=1.')
print('Evaluation of omega_theta on z is theta by n_infinity(c,H_infinity)=1.')
