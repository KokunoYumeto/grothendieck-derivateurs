"""Exact certificate: an F2 affine equalizer at one target, but none over Q."""
from fractions import Fraction
from itertools import product
E=[(0,1,2),(0,1,3),(0,1,5),(0,2,5),(1,2,4),(1,3,5),(2,3,4)]
D=[[int(e[j]==v)-int(e[0]==v) for e in E] for j in [1,2] for v in range(6)]

def solve(A,b,p=0):
 a=[[x%p if p else Fraction(x) for x in row+[rhs]] for row,rhs in zip(A,b)]
 m=len(a);n=len(A[0]);r=0;piv=[]
 for c in range(n):
  z=next((i for i in range(r,m) if a[i][c]),None)
  if z is None:continue
  a[r],a[z]=a[z],a[r]
  t=pow(a[r][c],-1,p) if p else 1/a[r][c]
  a[r]=[(x*t)%p if p else x*t for x in a[r]]
  for i in range(m):
   if i!=r and a[i][c]:
    t=a[i][c];a[i]=[(x-t*y)%p if p else x-t*y for x,y in zip(a[i],a[r])]
  piv.append(c);r+=1
  if r==m:break
 if any(all(x==0 for x in row[:n]) and row[n]!=0 for row in a):return None
 x=[0]*n
 for i,c in enumerate(piv):x[c]=a[i][n]
 return x

mod=solve(D+[[1]*7],[0]*12+[1],2)
lam=solve([list(col) for col in zip(*D)],[1]*7)
assert mod is not None and lam is not None
assert all(sum(c*t for c,t in zip(row,mod))%2==0 for row in D)
assert sum(mod)%2==1
assert all(sum(lam[i]*D[i][j] for i in range(12))==1 for j in range(7))
print('Triples:',E)
print('F2 coefficient vector:',mod,'augmentation',sum(mod)%2)
print('Integral residual D t:',[sum(c*t for c,t in zip(row,mod)) for row in D])
print('Rational dual lambda with lambda D = augmentation:',[str(x) for x in lam])
print('Verified lambda D =',[str(sum(lam[i]*D[i][j] for i in range(12))) for j in range(7)])

# Category: identities; a_i:p->q; b_j:q->r; c_v:p->r;
# b_j a_i=c_{E[j][i]}. These are all nonidentity arrows.
arrows={}
for x in ['p','q','r']:arrows['id_'+x]=(x,x)
for i in range(3):arrows['a'+str(i)]=('p','q')
for j in range(7):arrows['b'+str(j)]=('q','r')
for v in range(6):arrows['c'+str(v)]=('p','r')
def comp(g,f):
 assert arrows[f][1]==arrows[g][0]
 if f.startswith('id_'):return g
 if g.startswith('id_'):return f
 return 'c'+str(E[int(g[1:])][int(f[1:])])
checks=0
for f,g,h in product(arrows,repeat=3):
 if arrows[f][1]==arrows[g][0] and arrows[g][1]==arrows[h][0]:
  assert comp(h,comp(g,f))==comp(comp(h,g),f)
  checks+=1
print('Finite category arrows:',len(arrows),'associativity triples checked:',checks)
print('Every object has an arrow to r. No rational equalizer of (a0,a1,a2) exists at any target.')
print('This category itself is not exact over F2: distinct b_j:q->r cannot be equalized at r.')
