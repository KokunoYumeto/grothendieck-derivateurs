"""Verify the dimension-dependent flag prism, in dimensions zero through four.

A source object is a flag of nonempty subsets of {0,...,n}; the target
has the extra vertex n+1. The comparison replaces n with n+1. All steps
project back to exactly the original source flag. Only generating flag
inclusions are checked, and transitivity gives all inclusions.
"""
from itertools import combinations
from pathlib import Path
import json

def flags(vertices):
    faces = [frozenset(s) for size in range(1, len(vertices)+1)
             for s in combinations(vertices,size)]
    result = []
    def extend(chain):
        result.append(frozenset(chain))
        for nxt in faces:
            if chain[-1] < nxt:
                extend(chain+[nxt])
    for face in faces:
        extend([face])
    return result

def valid_flag(c):
    if not c or any(not s for s in c):
        return False
    ss = sorted(c,key=len)
    return all(a < b for a,b in zip(ss,ss[1:]))

reports = []
for n in range(5):
    source = flags(tuple(range(n+1)))
    top = frozenset(range(n+1))
    # A stage is specified by a map on source faces; union stages are
    # represented by taking the union of the two face-image sets.
    face_maps = []
    states = {s:s for c in source for s in c}
    stages = [{s:frozenset([t]) for s,t in states.items()}]
    for size in range(n+1,0,-1):
        nxt = {s:(t|{n+1} if n in s and len(s)==size else t)
               for s,t in states.items()}
        stages.append({s:frozenset([states[s],nxt[s]]) for s in states})
        stages.append({s:frozenset([nxt[s]]) for s in states})
        states = nxt
    for size in range(1,n+2):
        nxt = {s:(t-{n} if n in s and len(s)==size else t)
               for s,t in states.items()}
        stages.append({s:frozenset([states[s],nxt[s]]) for s in states})
        stages.append({s:frozenset([nxt[s]]) for s in states})
        states = nxt
    rows = [{c:frozenset(t for s in c for t in stage[s]) for c in source}
            for stage in stages]
    assert len(rows)-1 == 4*(n+1)
    inclusions = [(c-{s},c) for c in source if len(c)>1 for s in c]
    for row in rows:
        for c,image in row.items():
            assert valid_flag(image)
            assert all(s <= frozenset(range(n+2)) for s in image)
            projection = frozenset(frozenset(n if x==n+1 else x for x in s)
                                  for s in image)
            assert projection == c
            if max(c,key=len) != top:
                # The image lies in the degenerate sides, or in the
                # common face {0,...,n-1} shared by the two end facets.
                assert (any(all(i not in s for s in image) for i in range(n))
                        or image == c)
        assert all(row[c] <= row[d] for c,d in inclusions)
    for k,(row,nxt) in enumerate(zip(rows,rows[1:])):
        assert all((row[c] <= nxt[c] if k%2==0 else nxt[c] <= row[c])
                   for c in source)
    assert all(rows[0][c] == c for c in source)
    assert all(rows[-1][c] == frozenset(
        frozenset(n+1 if x==n else x for x in s) for s in c) for c in source)
    reports.append({'dimension':n, 'source_flags':len(source),
                    'generating_order_relations':len(inclusions),
                    'steps':len(rows)-1, 'verified':True})
report = json.dumps({'certificates':reports},indent=2)+'\n'
print(report,end='')
Path(__file__).with_suffix('.out').write_text(report)
