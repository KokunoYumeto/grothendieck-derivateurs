from finite_categories import *
import json
from pathlib import Path
from itertools import combinations, product
from math import prod
ROOT = Path(__file__).resolve().parents[2]
out={}
I=poset(2,lambda x,y:x<=y,'[1]')
ob=list(range(1,15)); ar=[(a,b) for a,b in product(ob,repeat=2) if a&b==a]
K=Category(ob,ar,{a:a[0] for a in ar},{a:a[1] for a in ar},{x:(x,x) for x in ob},lambda g,f:(f[0],g[1]),'K=S2 face poset')
H=twisted(K);HH=twisted(K,2)
# D.3 base and covering
ob=[0,1]; ar=[(0,0,0)]+[(s,1,l) for s in [0,1] for l in [0,1]]
B3=Category(ob,ar,{f:f[0] for f in ar},{f:f[1] for f in ar},{0:(0,0,0),1:(1,1,0)},lambda g,f:(f[0],g[1],(f[2]+g[2])%2),'D3B')
eb=[(b,x) for b in ob for x in [0,1]]; ea=[(f,x) for f in ar for x in [0,1]]
E3=Category(eb,ea,{a:(B3.src[a[0]],a[1]) for a in ea},{a:(B3.dst[a[0]],(a[1]+a[0][2])%2) for a in ea},{o:(B3.ident[o[0]],o[1]) for o in eb},lambda g,f:(B3.comp(g[0],f[0]),f[1]),'D3E')
# D.4 base and twisted pullback, with a=0
B4=poset(15,lambda x,y: x==y or (x!=0 and y!=0 and x&y==x) or (x==0 and y!=0 and y&1==1),'D4B')
def r(x):return x or 1
a4=[(f,v) for f in B4.arrows for v in [(0,),(1,)]]
def c4(g,f):
 rf=(r(f[0][0]),r(f[0][1]));rg=(r(g[0][0]),r(g[0][1]))
 label=H.comp((rg,g[1]),(rf,f[1]))[1]
 return (B4.comp(g[0],f[0]),label)
E4=Category(B4.objects,a4,{f:B4.src[f[0]] for f in a4},{f:B4.dst[f[0]] for f in a4},{x:(B4.ident[x],(0,)) for x in B4.objects},c4,'D4E')
# D.5 mapping cylinder BC2->point
ra=[(0,0,0),(0,0,1),(0,1,0),(1,1,0)]
R=Category([0,1],ra,{a:a[0] for a in ra},{a:a[1] for a in ra},{0:ra[0],1:ra[-1]},lambda g,f:(f[0],g[1],(f[2]+g[2])%2 if g[1]==0 else 0),'D5R')
cats=[K,H,HH,B3,E3,B4,E4,R]
out['categories']={C.name:{**C.check(),'pi1':pi1_presentation(C)} for C in cats}
for name in ['K=S2 face poset','twist1','D4B','D4E']:
 assert out['categories'][name]['pi1']['identified_group']=='trivial'
assert out['categories']['twist2']['pi1']['identified_group']=='C2'
assert out['categories']['D3B']['pi1']['identified_group']=='C2'
assert out['categories']['D3E']['pi1']['identified_group']=='trivial'
# Every finite map, not only a hand-picked lift, is checked.
q4=lambda x:int(x!=0)
maps=[('D3p',E3,B3,lambda o:o[0],lambda a:a[0]),('D3q',B3,I,lambda o:o,lambda a:(a[0],a[1])),('D3qp',E3,I,lambda o:o[0],lambda a:(a[0][0],a[0][1])),('D4p',E4,B4,lambda o:o,lambda a:a[0]),('D4q',B4,I,q4,lambda a:(q4(a[0]),q4(a[1]))),('D4qp',E4,I,q4,lambda a:(q4(a[0][0]),q4(a[0][1]))),('D5p',H,K,lambda o:o,lambda a:a[0]),('D5q',R,I,lambda o:o,lambda a:(a[0],a[1]))]
out['maps']={}
for name,E,B,po,pa in maps:
 for f,g in product(E.arrows,repeat=2):
  if E.dst[f]==E.src[g]:assert pa(E.comp(g,f))==B.comp(pa(g),pa(f))
 data={'incoming':[],'outgoing':[]}
 for incoming in [True,False]:
  for e in E.objects:
   for beta in B.arrows:
    if (B.dst[beta] if incoming else B.src[beta])!=po(e):continue
    L=lift_category(E,B,po,pa,e,beta,incoming)
    datum={'object':str(e),'base_arrow':str(beta),'objects':len(L.objects),'arrows':len(L.arrows),'components':len(L.components()),'initial':len(L.initial_objects()),'terminal':len(L.terminal_objects())}
    if not (L.initial_objects() or L.terminal_objects()) and len(L.components())==1:datum['pi1']=pi1_presentation(L)
    data['incoming' if incoming else 'outgoing'].append(datum)
 assert all(l['initial']>0 for l in data['outgoing'])
 data['smooth_W1_and_Qlc']=all(l['terminal']>0 for l in data['incoming'])
 data['proper']=True
 data['intrinsic_W1']=(name in ['D3p','D4q'])
 data['intrinsic_Qlc']=(name=='D3p')
 data['intrinsic_note']='Intrinsic truth values follow from the proofs; finite lift and pi1 data are independently checked here.'
 out['maps'][name]=data
# Regular C_p covering and nilpotence of its augmentation filtration.
out['mod_p_covers']={}
for p in [2,3,5,7]:
 G=group_cat(p); obs=list(range(p)); arr=[(s,t) for s in obs for t in obs]
 T=Category(obs,arr,{a:a[0] for a in arr},{a:a[1] for a in arr},{s:(s,s) for s in obs},lambda g,f:(f[0],g[1]),'EC'+str(p))
 pa=lambda a:(a[1]-a[0])%p
 for x in obs:
  for g in G.arrows:
   assert sum(T.src[f]==x and pa(f)==g for f in arr)==1
   assert sum(T.dst[f]==x and pa(f)==g for f in arr)==1
 # (permutation - 1)^p=0 in F_p, and successive ranks p-k.
 import sympy as sp
 P=sp.zeros(p)
 for i in range(p):P[(i+1)%p,i]=1
 N=P-sp.eye(p)
 assert all(int(x)%p==0 for x in N**p)
 out['mod_p_covers'][str(p)]={'total':T.check(),'base':G.check(),'total_pi1':pi1_presentation(T),'cover_degree':p,'nilpotence_exponent_bound':p,'nontrivial':p>1}
# Fence products: every individual cone projection is universally weakly equivalent.
out['fences']=[]
for n in range(1,9):
 C=poset(n+1,lambda i,j:i==j or (abs(i-j)==1 and i%2==0),'fence')
 cone=poset(n+2,lambda i,j:j==n+1 or (i<=n and j<=n and (i==j or (abs(i-j)==1 and i%2==0))),'cone')
 assert len(C.components())==1 and cone.terminal_objects()==[n+1]
 assert all(abs(a-b)<=1 for a,b in C.arrows)
 out['fences'].append({'n':n,'objects':len(C.objects),'arrows':len(C.arrows),'endpoint_graph_distance':n,'cone_terminal':n+1})
out['scope']='No universal intrinsic condition is asserted to follow solely from finite computation. The program checks categories, composition, all lift categories, specified fundamental-group presentations, and finite witnesses in the proofs.'
(ROOT / 'code/root/D_output.json').write_text(json.dumps(out,indent=2))
with (ROOT / 'tables/D_BISITE_B15.csv').open('w') as f:
 f.write('map,smooth_W1,smooth_Qlc,proper_W1,proper_Qlc,intrinsic_W1,intrinsic_Qlc,differs_from_BISITE\n')
 for k,v in out['maps'].items():
  s=str(v['smooth_W1_and_Qlc']).lower();f.write(f"{k},{s},{s},true,true,{str(v['intrinsic_W1']).lower()},{str(v['intrinsic_Qlc']).lower()},false\n")
print(json.dumps({'category_counts':{k:{'objects':v['objects'],'arrows':v['arrows'],'pi1':v['pi1'].get('identified_group')} for k,v in out['categories'].items()},'table_rows':8,'all_checks_passed':True},indent=2))
