from itertools import combinations
from fractions import Fraction

def rank(rows,p=0):
 a=[[x%p if p else Fraction(x) for x in row] for row in rows]
 m=len(a);n=len(a[0]) if m else 0;r=0
 for c in range(n):
  pivot=next((i for i in range(r,m) if a[i][c]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r]
  t=pow(a[r][c],-1,p) if p else 1/a[r][c]
  a[r]=[(x*t)%p if p else x*t for x in a[r]]
  for i in range(m):
   if i==r:continue
   t=a[i][c]
   if t:a[i]=[(x-t*y)%p if p else x-t*y for x,y in zip(a[i],a[r])]
  r+=1
  if r==m:break
 return r

def affine(edges,n,p):
 rows=[]
 for j in [1,2]:
  for v in range(n):rows.append([(int(e[j]==v)-int(e[0]==v)) for e in edges])
 return rank(rows+[ [1]*len(edges)],p)>rank(rows,p)

for n in range(3,7):
 es=list(combinations(range(n),3)); print('n',n,'full affine Q,2,3,5',*[affine(es,n,p) for p in [0,2,3,5]],flush=True)
 if n<=5:
  for r in range(1,len(es)+1):
   for sub in combinations(es,r):
    if affine(sub,n,0):continue
    for p in [2,3,5,7]:
     if affine(sub,n,p):
      print('EXCEPTIONAL',n,p,sub,flush=True);raise SystemExit
print('No exceptional prime among all n<=5 supports.')
