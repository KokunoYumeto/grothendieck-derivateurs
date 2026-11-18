exec(open(__file__.replace('C4_random_search','C4_marginal_search')).read().split('for n in range(3,7):')[0])
import random
rng=random.Random(20261118)
for n in range(6,11):
 es=list(combinations(range(n),3))
 for step in range(30000):
  r=rng.randrange(n,min(3*n,len(es))+1)
  sub=rng.sample(es,r)
  if not affine(sub,n,2):continue
  if not affine(sub,n,0):
   print('EXCEPTIONAL',n,2,sorted(sub),flush=True);raise SystemExit
 print('searched',n,flush=True)
print('No exception found')
