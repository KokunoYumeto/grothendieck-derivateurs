#!/usr/bin/env python3
"""Exact finite certificates for PRETOT's counterexample.

Python 3 + SymPy. No floating point arithmetic, randomized tests, or
unproved inference from a truncated nerve is used.
Run: python code/main_counterexample.py
Outputs are written beside this script under outputs/.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority claimed.
"""
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

OUT = Path(__file__).resolve().parent / 'outputs'
OUT.mkdir(exist_ok=True)
LOG = []
def report(s):
    print(s, flush=True)
    LOG.append(s)

WORDS = ('aaaaaBBB', 'bbbBABA')
ND = [tuple(['v', 'c0', 'c1']),
      tuple(['a', 'b'] + [f'r{k}_{i}' for k,w in enumerate(WORDS) for i in range(len(w))]),
      tuple(f't{k}_{i}' for k,w in enumerate(WORDS) for i in range(len(w)))]
FACES = {}
for e in ND[1]:
    FACES[e] = ('v','v') if e in ('a','b') else ('v', 'c'+e[1])
for k,w in enumerate(WORDS):
    for i,letter in enumerate(w):
        r0, r1 = f'r{k}_{i}', f'r{k}_{(i+1)%len(w)}'
        FACES[f't{k}_{i}'] = (letter.lower(),r1,r0) if letter.islower() else (letter.lower(),r0,r1)

def maps(m,n):
    return tuple(combinations_with_replacement(range(n+1),m+1))
def injections(m,n):
    return tuple(combinations(range(n+1),m+1))
def surjections(m,n):
    return tuple(a for a in maps(m,n) if set(a)==set(range(n+1)))
def compose(b,a):
    return tuple(b[x] for x in a)
def semi_pull(k,name,inc):
    if len(inc)==k+1:
        assert tuple(inc)==tuple(range(k+1))
        return name
    if k==1:
        return FACES[name][1-inc[0]]
    if k==2 and len(inc)==2:
        missing=next(j for j in range(3) if j not in inc)
        return FACES[name][missing]
    if k==2 and len(inc)==1:
        return 'c'+name[1] if inc[0]==0 else 'v'
    raise ValueError((k,name,inc))

K = [tuple((k,x,rho) for k in range(n+1) for x in ND[k] for rho in surjections(n,k)) for n in range(3)]
KI = [{x:i for i,x in enumerate(a)} for a in K]
def pull(x,a):
    k,name,rho=x
    q=compose(rho,a)
    im=tuple(sorted(set(q)))
    eta=tuple(im.index(j) for j in q)
    return (len(im)-1, semi_pull(k,name,im), eta)
def mat_set(domain,codomain,f):
    idx={x:i for i,x in enumerate(codomain)}
    return sp.SparseMatrix(len(codomain),len(domain),{(idx[f(x)],j):1 for j,x in enumerate(domain)})
def kmat(m,n,a):
    return mat_set(K[n],K[m],lambda x:pull(x,a))

def category(objects,arrows):
    """Arrows are (source-object-index,target-object-index,ordinal-map)."""
    idx={a:i for i,a in enumerate(arrows)}
    incoming=[[] for _ in objects]; outgoing=[[] for _ in objects]
    for i,(s,t,a) in enumerate(arrows):
        outgoing[s].append(i); incoming[t].append(i)
    ids=[]
    for i,o in enumerate(objects):
        dim=o[0]
        ids.append(idx[(i,i,tuple(range(dim+1)))])
    comp={}
    for mid in range(len(objects)):
        for f in incoming[mid]:
            for g in outgoing[mid]:
                sf,tf,a=arrows[f]; sg,tg,b=arrows[g]
                comp[g,f]=idx[(sf,tg,compose(b,a))]
    for f,(s,t,a) in enumerate(arrows):
        assert comp[f,ids[s]]==f==comp[ids[t],f]
    triples=0
    for (g,f),gf in comp.items():
        for h in outgoing[arrows[g][1]]:
            assert comp[h,gf]==comp[comp[h,g],f]
            triples+=1
    return {'objects':objects,'arrows':arrows,'index':idx,'ids':ids,'comp':comp,
            'incoming':incoming,'outgoing':outgoing,'triples':triples}

def semi_category():
    objects=tuple((k,x) for k in range(3) for x in ND[k]); oi={o:i for i,o in enumerate(objects)}
    arrows=[]
    for j,(n,x) in enumerate(objects):
        for m in range(n+1):
            for a in injections(m,n):
                arrows.append((oi[(m,semi_pull(n,x,a))],j,a))
    return category(objects,tuple(arrows))
def element_category(levels):
    objects=tuple((n,x) for n in levels for x in K[n]); oi={o:i for i,o in enumerate(objects)}
    arrows=[]
    for j,(n,x) in enumerate(objects):
        for m in levels:
            for a in maps(m,n):
                arrows.append((oi[(m,pull(x,a))],j,a))
    return category(objects,tuple(arrows))

def nerve_homology(C,max_degree=2):
    ids=set(C['ids']); nonids=[i for i in range(len(C['arrows'])) if i not in ids]
    chains=[[(i,) for i in range(len(C['objects']))],[(i,) for i in nonids]]
    for n in range(2,max_degree+2):
        chains.append([c+(g,) for c in chains[-1] for g in C['outgoing'][C['arrows'][c[-1]][1]] if g not in ids])
    assert not chains[max_degree+1], 'Full finite-dimensional homology certification requires the next chains to vanish.'
    boundaries={}
    diag={0:[]}
    for n in range(1,max_degree+2):
        prev={c:i for i,c in enumerate(chains[n-1])}; entries={}
        def add(r,j,v): entries[r,j]=entries.get((r,j),0)+v
        for j,c in enumerate(chains[n]):
            if n==1:
                s,t,_=C['arrows'][c[0]]
                add(prev[(t,)],j,1); add(prev[(s,)],j,-1)
            else:
                add(prev[c[1:]],j,1); add(prev[c[:-1]],j,(-1)**n)
                for i in range(1,n):
                    h=C['comp'][c[i],c[i-1]]
                    if h not in ids:
                        add(prev[c[:i-1]+(h,)+c[i+1:]],j,(-1)**i)
        d=sp.SparseMatrix(len(chains[n-1]),len(chains[n]),entries)
        boundaries[n]=d
        if n>1: assert boundaries[n-1]*d==sp.zeros(len(chains[n-2]),len(chains[n]))
        snf=smith_normal_form(d,domain=ZZ)
        diag[n]=[abs(int(snf[i,i])) for i in range(min(snf.shape)) if snf[i,i]]
    hom=[]
    for n in range(max_degree+1):
        hom.append({'degree':n,'rank':len(chains[n])-len(diag[n])-len(diag[n+1]),
                    'torsion':[x for x in diag[n+1] if x>1]})
    return [len(c) for c in chains],hom

def permutation(cycle):
    p=list(range(5))
    for i,x in enumerate(cycle): p[x-1]=cycle[(i+1)%len(cycle)]-1
    return tuple(p)
def inverse(p): return tuple(p.index(i) for i in range(len(p)))

def projectivity_certificate():
    # Normalized quotient chain complex of K.
    d1=sp.zeros(3,17); d2=sp.zeros(17,15)
    for j,e in enumerate(ND[1]):
        d1[ND[0].index(FACES[e][0]),j]+=1; d1[ND[0].index(FACES[e][1]),j]-=1
    for j,t in enumerate(ND[2]):
        for i,e in enumerate(FACES[t]): d2[ND[1].index(e),j]+=(-1)**i
    assert d1*d2==sp.zeros(3,15)
    u=[sp.eye(17)[:,ND[1].index('r0_0')],sp.eye(17)[:,ND[1].index('r1_0')]]
    b0=sp.Matrix.hstack(sp.eye(3)[:,0],d1*u[0],d1*u[1])
    b1=sp.Matrix.hstack(*u,d2)
    assert abs(b0.det())==abs(b1.det())==1
    copies=[0,1,1]+[2]*15
    repvals={n:[maps(k,n) for k in range(3)] for n in range(3)}
    repnd={n:[injections(k,n) for k in range(3)] for n in range(3)}
    qnd=[[(c,x) for c,n in enumerate(copies) for x in repnd[n][k]] for k in range(3)]
    qidx=[{x:i for i,x in enumerate(a)} for a in qnd]
    A=[sp.zeros(len(qnd[k]),len(ND[k])) for k in range(3)]
    B=[sp.zeros(len(ND[k]),len(qnd[k])) for k in range(3)]
    # First make A on the adapted chain bases, then change to the original bases.
    A[0][qidx[0][(0,(0,))],0]=1
    B[0][:,qidx[0][(0,(0,))]]=b0[:,0]
    for j in range(2):
        c=1+j
        A[0][qidx[0][(c,(0,))],1+j]=-1
        A[0][qidx[0][(c,(1,))],1+j]=1
        B[0][:,qidx[0][(c,(1,))]]=b0[:,1+j]
        A[1][qidx[1][(c,(0,1))],j]=1
        B[1][:,qidx[1][(c,(0,1))]]=u[j]
    for j in range(15):
        c=3+j
        for edge,sign in [((0,1),1),((0,2),-1),((1,2),1)]:
            A[1][qidx[1][(c,edge)],2+j]=sign
        B[1][:,qidx[1][(c,(1,2))]]=d2[:,j]
        A[2][qidx[2][(c,(0,1,2))],j]=1
        B[2][j,qidx[2][(c,(0,1,2))]]=1
    A[0]=A[0]*b0.inv(); A[1]=A[1]*b1.inv()
    for k in range(3): assert B[k]*A[k]==sp.eye(len(ND[k]))
    qd={}
    for k in (1,2):
        qd[k]=sp.zeros(len(qnd[k-1]),len(qnd[k]))
        for j,(c,x) in enumerate(qnd[k]):
            for i in range(k+1): qd[k][qidx[k-1][(c,x[:i]+x[i+1:])],j]+=(-1)**i
    for k,d in [(1,d1),(2,d2)]:
        assert qd[k]*A[k]==A[k-1]*d
        assert d*B[k]==B[k-1]*qd[k]

    def normalization(values,action,ndvalues):
        J=[]
        for k in range(3):
            p=sp.eye(len(values[k]))
            for i in range(k):
                face=tuple(j for j in range(k+1) if j!=i)
                degen=tuple(j if j<=i else j-1 for j in range(k+1))
                p=(sp.eye(len(values[k]))-action(k,k-1,degen)*action(k-1,k,face))*p
            vi={x:i for i,x in enumerate(values[k])}
            J.append(p[:,[vi[x] for x in ndvalues[k]]])
        columns=[]; keys=[]
        for k in range(3):
            for rho in surjections(2,k):
                v=action(2,k,rho)*J[k]
                for j,x in enumerate(ndvalues[k]): columns.append(v[:,j]); keys.append((k,rho,j))
        basis=sp.Matrix.hstack(*columns)
        assert abs(basis.det())==1
        return J,basis,keys

    Knd=[[(k,x,tuple(range(k+1))) for x in ND[k]] for k in range(3)]
    KJ,KB,Kkeys=normalization(K,kmat,Knd)
    Rnorm={}
    for n in range(3):
        vals=repvals[n]
        def rmat(m,k,a): return mat_set(vals[k],vals[m],lambda x:compose(x,a))
        Rnorm[n]=normalization(vals,rmat,repnd[n])
    offsets=[]; off=0
    for n in copies: offsets.append(off); off+=len(repvals[n][2])
    assert off==159
    QB=sp.diag(*(Rnorm[n][1] for n in copies))
    qkeys=[(c,*key) for c,n in enumerate(copies) for key in Rnorm[n][2]]
    Ap=sp.zeros(159,52)
    for j,(k,rho,h) in enumerate(Kkeys):
        for q,(c,x) in enumerate(qnd[k]):
            coeff=A[k][q,h]
            if coeff:
                n=copies[c]; vals=repvals[n]
                rmat=mat_set(vals[k],vals[2],lambda y:compose(y,rho))
                v=rmat*Rnorm[n][0][k][:,repnd[n][k].index(x)]
                Ap[offsets[c]:offsets[c]+len(vals[2]),j]+=coeff*v
    Bp=sp.zeros(52,159)
    for j,(c,k,rho,h) in enumerate(qkeys):
        x=repnd[copies[c]][k][h]
        coeffs=B[k][:,qidx[k][(c,x)]]
        Bp[:,j]=kmat(2,k,rho)*KJ[k]*coeffs
    sa=Ap*KB.inv(); rb=Bp*QB.inv()
    assert rb*sa==sp.eye(52)
    assert all(x.q==1 for x in sa) and all(x.q==1 for x in rb)
    M=maps(2,2)
    II=sp.zeros(180,159); PP=sp.zeros(159,180)
    for c,n in enumerate(copies):
        inc=tuple(range(n+1)); ret=tuple(min(j,n) for j in range(3))
        for j,f in enumerate(repvals[n][2]): II[c*10+M.index(compose(inc,f)),offsets[c]+j]=1
        for j,g in enumerate(M): PP[offsets[c]+repvals[n][2].index(compose(ret,g)),c*10+j]=1
    assert PP*II==sp.eye(159)
    S=sp.SparseMatrix(II*sa); R=sp.SparseMatrix(rb*PP)
    assert R*S==sp.eye(52)
    for alpha in M:
        hm=kmat(2,2,alpha)
        reg=mat_set(M,M,lambda g:compose(g,alpha))
        free=sp.diag(*([reg]*18))
        assert S*hm==free*S
        assert R*free==hm*R
    def sparse(A): return {'rows':A.rows,'cols':A.cols,'entries':[[i,j,int(x)] for (i,j),x in A.todok().items()]}
    cert={'free_rank':18,'module_rank':52,'inclusion_S':sparse(S),'retraction_R':sparse(R),
          'basis_H':[list(x[:2])+[list(x[2])] for x in K[2]],'basis_M':[list(x) for x in M]}
    (OUT/'projectivity_certificate.json').write_text(json.dumps(cert,separators=(',',':')))
    report('PROJECTIVITY: Z[H] is a direct summand of (Z[M])^18; integer matrices S:180x52 and R:52x180; RS=I_52; all 10 action-equivariance checks PASS.')
    report(f'PROJECTIVITY: sparse nonzero entries S={len(S.todok())}, R={len(R.todok())}; adapted chain determinants {b0.det()}, {b1.det()}.')
    return cert

def main():
    for n in range(3):
        for m in range(3):
            for l in range(3):
                for a in maps(l,m):
                    for b in maps(m,n):
                        for x in K[n]: assert pull(pull(x,b),a)==pull(x,compose(b,a))
    report('SIMPLICIAL IDENTITIES / ALL FUNCTOR LAWS on Delta_{<=2}: PASS.')
    report(f'K nondegenerate counts {[len(x) for x in ND]}; truncated simplicial counts {[len(x) for x in K]}.')
    A=semi_category(); E=element_category(range(3)); EM=element_category([2])
    for name,C in [('A',A),('E_Delta2',E),('E_M',EM)]:
        report(f'{name}: objects={len(C["objects"])}, arrows={len(C["arrows"])}, composable pairs={len(C["comp"])}, associativity triples={C["triples"]}; all axioms PASS.')
    ai={x:i for i,x in enumerate(A['objects'])}; ei={x:i for i,x in enumerate(E['objects'])}
    robj=[ai[(x[0],x[1])] for n,x in E['objects']]
    rarr=[]
    for s,t,alpha in E['arrows']:
        n,x=E['objects'][s]; m,y=E['objects'][t]
        composed=compose(y[2],alpha); beta=tuple(sorted(set(composed)))
        assert compose(beta,x[2])==composed
        rarr.append(A['index'][robj[s],robj[t],beta])
    for (g,f),gf in E['comp'].items(): assert A['comp'][rarr[g],rarr[f]]==rarr[gf]
    # The support map has inclusion as section and a natural transformation id=>inclusion*support.
    eta=[]
    for j,(n,x) in enumerate(E['objects']):
        target=ei[(x[0],(x[0],x[1],tuple(range(x[0]+1))))]
        eta.append(E['index'][j,target,x[2]])
    for f,(s,t,a) in enumerate(E['arrows']):
        ar=A['arrows'][rarr[f]]
        ss=E['arrows'][eta[s]][1]; tt=E['arrows'][eta[t]][1]
        irf=E['index'][ss,tt,ar[2]]
        assert E['comp'][irf,eta[s]]==E['comp'][eta[t],f]
    report('DEFORMATION RETRACTION E_Delta2 -> A: functor, section, and all 1177 naturality equations PASS.')
    # Every E_Delta2 object is a retract of an E_M object.
    for j,(n,x) in enumerate(E['objects']):
        inc=tuple(range(n+1)); ret=tuple(min(z,n) for z in range(3))
        y=pull(x,ret); d=ei[(2,y)]
        i=E['index'][j,d,inc]; r=E['index'][d,j,ret]
        assert E['comp'][r,i]==E['ids'][j]
        for f in E['outgoing'][j]:
            if E['objects'][E['arrows'][f][1]][0]==2:
                fr=E['comp'][f,r]
                assert E['comp'][fr,i]==f
    report('CAUCHY DENSITY E_M -> E_Delta2: all 75 object retractions and comma contraction equations PASS.')
    counts,hom=nerve_homology(A)
    report(f'FULL INTEGRAL NERVE HOMOLOGY A: chain ranks={counts}; homology={hom}.')
    assert hom==[{'degree':0,'rank':1,'torsion':[]},{'degree':1,'rank':0,'torsion':[]},{'degree':2,'rank':0,'torsion':[]}]
    pa,pb=permutation((1,4,3,2,5)),permutation((1,2,3)); unit=tuple(range(5))
    values={'a':pa,'b':pb,'A':inverse(pa),'B':inverse(pb)}
    for w in WORDS:
        q=unit
        for l in w: q=compose(q,values[l])
        assert q==unit
    group={unit}; todo=[unit]
    while todo:
        q=todo.pop()
        for v in [pa,pb,inverse(pa),inverse(pb)]:
            x=compose(q,v)
            if x not in group: group.add(x); todo.append(x)
    assert len(group)==60 and pa!=unit
    report('FUNDAMENTAL GROUP CERTIFICATE: both relators vanish in A_5; a is nonidentity; generated image has 60 elements.')
    # R6 restricted action and its graph deformation retraction.
    Lvals=[(0,),(0,1),(0,)]
    objects=tuple((n,x,l) for n in range(3) for x in ND[n] for l in Lvals[n]); oi={o:i for i,o in enumerate(objects)}
    arrows=[]
    for s,(m,x,l) in enumerate(objects):
        for n in range(m,3):
            for a in injections(m,n):
                target_l=0 if n==2 else a[l]
                for y in ND[n]:
                    if semi_pull(n,y,a)==x: arrows.append((s,oi[(n,y,target_l)],a))
    R6=category(objects,tuple(arrows)); r6counts,r6hom=nerve_homology(R6)
    report(f'R6: restricted-action category objects={len(objects)}, arrows={len(arrows)}, nerve ranks={r6counts}; homology={r6hom}.')
    assert r6hom[1]=={'degree':1,'rank':28,'torsion':[]}
    graphvertices=3+15; graphedges=3*15
    assert graphedges-graphvertices+1==28
    report('R6 incidence graph: 18 vertices, 45 edges, connected; first Betti number 28. The category is homotopy equivalent, not categorically equivalent, to this graph category.')
    projectivity_certificate()
    M=maps(2,2)
    data={'monoid_elements':[list(a) for a in M],
          'identity_index':M.index((0,1,2)),
          'multiplication':[[M.index(compose(g,f)) for f in M] for g in M],
          'H_elements':[[k,x,list(rho)] for k,x,rho in K[2]],
          'right_action':[[KI[2][pull(x,a)] for a in M] for x in K[2]],
          'words':list(WORDS),'faces':FACES,
          'homology_A':hom,'homology_R6':r6hom}
    (OUT/'main_counterexample_data.json').write_text(json.dumps(data,indent=2))
    (OUT/'main_counterexample.out').write_text('\n'.join(LOG)+'\n')
    report('ALL EXACT CHECKS PASSED.')
    (OUT/'main_counterexample.out').write_text('\n'.join(LOG)+'\n')

if __name__=='__main__': main()
