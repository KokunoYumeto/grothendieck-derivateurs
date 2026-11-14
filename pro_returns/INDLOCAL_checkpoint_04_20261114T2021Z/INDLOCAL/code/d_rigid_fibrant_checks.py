"""Exact finite checks for the countable rigid fibrant-poset construction.

The infinite construction reattaches EVERY generating horn map, even maps
already possessing fillers, at every pass. Its fibrancy and rigidity are
proved symbolically in D.16--D.18; this program certifies finite instances
of the pushout lemma, including all noninjective maps in the stated range.
"""
from itertools import combinations
from pathlib import Path
import json

def flags(vertices):
    faces=[frozenset(x) for k in range(1,len(vertices)+1) for x in combinations(vertices,k)]
    result=[]
    def visit(c):
        result.append(frozenset(c))
        for t in faces:
            if c[-1]<t: visit(c+[t])
    for t in faces: visit([t])
    return result

def make_horn(n,k):
    full=frozenset(range(n+1));missing=full-{k}
    Q=flags(tuple(range(n+1)))
    H=[s for s in Q if full not in s and missing not in s]
    return Q,H

def ideals_from_rel(N,relations):
    ideals=[1<<i for i in range(N)]
    for a,b in relations: ideals[b]|=1<<a
    for k in range(N):
        for b in range(N):
            if (ideals[b]>>k)&1: ideals[b]|=ideals[k]
    return ideals

def verify_poset(ideals):
    N=len(ideals)
    for y in range(N):
        assert (ideals[y]>>y)&1
        for x in range(N):
            if (ideals[y]>>x)&1:
                assert ideals[x]&~ideals[y]==0
                assert x==y or not ((ideals[x]>>y)&1)

def downbeats(ideals):
    out=[]
    for y,I in enumerate(ideals):
        proper=I&~(1<<y)
        for x in range(len(ideals)):
            if (proper>>x)&1 and proper&~ideals[x]==0:
                out.append((y,x));break
    return out

def common_upper(ideals,a,b):
    return any(((I>>a)&1) and ((I>>b)&1) for I in ideals)

def horn_pushout(old,Q,H,mapping):
    N=len(old); Hset=set(H);new=[s for s in Q if s not in Hset]
    idx={s:N+i for i,s in enumerate(new)};res=list(old)
    hidx={s:i for i,s in enumerate(H)}
    for s in new:
        ideal=sum(1<<idx[t] for t in new if t<=s)
        oldpart=frozenset(t for t in s if frozenset([t]) in Hset)
        if oldpart:
            assert oldpart in Hset
            ideal|=old[mapping[hidx[oldpart]]]
        res.append(ideal)
    return res,idx

def all_monotone_maps(H,old):
    N=len(old);q=len(H)
    edges=[(i,j) for i,s in enumerate(H) for j,t in enumerate(H) if s<t]
    # Put high-degree vertices first. Exact backtracking checks each pair
    # as soon as both images have been assigned.
    order=sorted(range(q),key=lambda i:-sum(i in e for e in edges))
    assigned=[None]*q
    def rec(at):
        if at==q:
            yield tuple(assigned);return
        i=order[at]
        for x in range(N):
            ok=True
            for a,b in edges:
                if a==i and assigned[b] is not None and not ((old[assigned[b]]>>x)&1):ok=False;break
                if b==i and assigned[a] is not None and not ((old[x]>>assigned[a])&1):ok=False;break
            if ok:
                assigned[i]=x
                yield from rec(at+1)
                assigned[i]=None
    yield from rec(0)

point=[1]
p4=ideals_from_rel(5,[(0,1),(2,1),(2,3),(4,3)])
reports=[]
for name,old in [('point',point),('P4',p4)]:
    assert not downbeats(old)
    for n in (1,2):
        for k in range(n+1):
            Q,H=make_horn(n,k);count=0;noninjective=0
            for mapping in all_monotone_maps(H,old):
                out,idx=horn_pushout(old,Q,H,mapping)
                verify_poset(out)
                assert out[:len(old)]==old
                assert not downbeats(out)
                for a in range(len(old)):
                    for b in range(len(old)):
                        assert common_upper(out,a,b)==common_upper(old,a,b)
                count+=1;noninjective+=len(set(mapping))<len(mapping)
            reports.append({'source':name,'dimension':n,'horn':k,
                            'all_maps_checked':count,'noninjective_maps':noninjective,
                            'new_objects':len(Q)-len(H),'verified':True})
# Higher-dimensional flags under collapsed attaching maps.
for n in (3,4):
    for k in range(n+1):
        Q,H=make_horn(n,k);out,_=horn_pushout(point,Q,H,(0,)*len(H))
        verify_poset(out);assert not downbeats(out)
        reports.append({'source':'point','dimension':n,'horn':k,
                        'all_maps_checked':1,'noninjective_maps':int(len(H)>1),
                        'new_objects':len(Q)-len(H),'verified':True})

# A complete first horn pass in dimensions 1 and 2 over the point.
first=list(point)
for n in (1,2):
    for k in range(n+1):
        Q,H=make_horn(n,k)
        # All maps to the original point are constant; successive pushouts
        # along these maps equal their simultaneous coproduct attachment.
        first,_=horn_pushout(first,Q,H,(0,)*len(H))
assert not downbeats(first)
# Add one fresh endpoint-0 1-horn at EVERY object of that finite stage.
branched=list(first);witness={}
Q,H=make_horn(1,0)
left_top=frozenset([frozenset([0]),frozenset([0,1])])
for x in range(len(first)):
    branched,idx=horn_pushout(branched,Q,H,(x,))
    witness[x]=idx[left_top]
assert branched[:len(first)]==first
assert not downbeats(branched)
pair_count=0
for z in range(len(first)):
    for x in range(len(first)):
        if x!=z and ((first[z]>>x)&1):
            y=witness[x]
            assert ((branched[y]>>x)&1)
            assert not common_upper(branched,y,z)
            pair_count+=1
# Further arbitrary constant horns do not create a forbidden common upper.
Q,H=make_horn(2,1)
after,_=horn_pushout(branched,Q,H,(0,)*len(H))
for z in range(len(first)):
    for x in range(len(first)):
        if x!=z and ((first[z]>>x)&1):
            assert not common_upper(after,witness[x],z)

result={'exhaustive_horn_pushout_checks':reports,
        'truncated_first_pass_objects':len(first),
        'after_fresh_branch_at_each_object':len(branched),
        'strict_old_pairs_with_verified_branch':pair_count,
        'old_principal_ideals_preserved':True,
        'no_downbeat_points_in_all_checked_pushouts':True,
        'all_common_upper_relations_between_old_objects_preserved':True,
        'note':'The finite code checks local lemmas only. The omega-stage proof establishes the fibrant, rigid infinite example.'}
report=json.dumps(result,indent=2)+'\n'
print(report,end='')
Path(__file__).with_suffix('.out').write_text(report)
