#!/usr/bin/env python3
"""Exact finite combinatorics for forgetting one labelled genus-zero mark.

Enumerates every compatible stable split system for n=4,5,6.  These are
the finite posets of boundary strata, NOT the infinite Charney--Lee
categories.  The latter's outgoing lift categories are represented by
the proved finite-object abelian-group presentation H/Delta_s.  No
finite quotient of an infinite cyclic group is substituted for it.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import csv, json

OUT=Path(__file__).resolve().parent

def canon(a,labels):
    a=frozenset(a); b=frozenset(labels)-a
    return min(tuple(sorted(a)),tuple(sorted(b)))

def splits(n):
    labels=frozenset(range(1,n+1))
    return sorted({canon(a,labels) for k in range(2,n-1)
                   for a in combinations(labels,k)})

def compatible(a,b,n):
    labels=set(range(1,n+1)); a=set(a); b=set(b)
    return any(not x for x in (a&b,a-b,b-a,labels-(a|b)))

def systems(n):
    ss=splits(n); ans=[()]
    for k in range(1,n-2):
        ans.extend(s for s in combinations(ss,k)
                   if all(compatible(a,b,n) for a,b in combinations(s,2)))
    return ans

def erase(c,n):
    labels=set(range(1,n)); a=set(c)-{n}; b=labels-a
    return None if min(len(a),len(b))<2 else canon(a,labels)

def subsets(x):
    return (s for k in range(len(x)+1) for s in combinations(x,k))

def outgoing_presentation(sig,eta,n):
    """H has coordinate-sum constraints for retained curves not in eta.

    Since each nonzero column of the twist map has one unit entry and
    every row is hit, all relations are saturated.  Hence ranks here
    are integral ranks and the quotients have no torsion.
    """
    images=tuple(erase(c,n) for c in sig)
    tau=tuple(sorted(set(images)-{None})); eta=set(eta)
    Hrank=len(sig)-len(set(tau)-eta)
    objs=[s for s in subsets(tuple(range(len(sig))))
          if {images[i] for i in s}-{None}==eta]
    hom=[]
    for s in objs:
        for t in objs:
            if set(s)>=set(t):
                rank=Hrank-len(s)
                assert rank>=0
                hom.append((s,t,rank))
    initials=[s for s in objs if all(set(s)>=set(t) for t in objs)
              and Hrank==len(s)]
    if initials:
        kind='contractible'; h=[1,0,0,0]
    else:
        assert len(objs)==1 and Hrank-len(objs[0])==1
        kind='BZ'; h=[1,1,0,0]
    counts=Counter(x for x in images if x is not None)
    assert sum(x is None for x in images)<=1
    assert sum(v-1 for v in counts.values())<=1
    assert not (None in images and any(v==2 for v in counts.values()))
    predicted=(any(v==2 and c not in eta for c,v in counts.items()))
    assert (kind=='BZ')==predicted
    return {'kind':kind,'H_rank':Hrank,'objects':objs,'hom_group_ranks':hom,
            'integral_homology_ranks_0_3':h,'integral_homology_torsion_0_3':[[],[],[],[]],
            'F2_betti_0_3':h,'Q_betti_0_3':h}

def main():
    summary={}; rows=[]; presentations=[]
    strata={n:systems(n) for n in (3,4,5,6)}
    assert [len(strata[n]) for n in (3,4,5,6)]==[1,4,26,236]
    for n,ss in strata.items():
        summary[f'strata_{n}']={'total':len(ss),'by_codimension':dict(sorted(Counter(map(len,ss)).items()))}
        edges=[(i,j) for i,s in enumerate(ss) for j,t in enumerate(ss)
               if set(s)>set(t) and len(s)==len(t)+1]
        (OUT/f'boundary_strata_{n}.json').write_text(json.dumps({'labels':list(range(1,n+1)),
          'objects':ss,'arrows_hasse_exit':edges},indent=2)+'\n')
    for n in (5,6):
        counts=Counter()
        for i,sig in enumerate(strata[n]):
            tau=tuple(sorted({erase(c,n) for c in sig}-{None}))
            for eta in subsets(tau):
                d=outgoing_presentation(sig,eta,n)
                counts[d['kind']]+=1
                rid=f'n{n-1}-s{i}-eta'+'.'.join(str(tau.index(c)) for c in eta)
                rows.append({'case_id':rid,'upstairs_marks':n,'downstairs_marks':n-1,
                   'sigma':repr(sig),'q_sigma':repr(tau),'eta':repr(eta),
                   'lift_type':d['kind'],'H_rank':d['H_rank'],
                   'normalized_objects':len(d['objects']),
                   'H0_Z':'Z','H1_Z':'Z' if d['kind']=='BZ' else '0',
                   'H2_Z':'0','H3_Z':'0','pi1':'Z' if d['kind']=='BZ' else '1'})
                presentations.append({'case_id':rid,**d})
        summary[f'forget_{n}_to_{n-1}']=dict(counts,total=sum(counts.values()))
    with (OUT/'marked_curve_lifts.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    (OUT/'marked_curve_presentations.json').write_text(json.dumps(presentations,indent=2)+'\n')
    (OUT/'marked_curve_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
