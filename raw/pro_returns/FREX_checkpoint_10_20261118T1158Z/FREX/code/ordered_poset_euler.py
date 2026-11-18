#!/usr/bin/env python3
"""Integer certificate for Euler weights on all ordered posets through n=5."""
from itertools import product
from collections import Counter
from pathlib import Path
import json,time
from ordered_poset_signed import posets,extensions,restrict_rows


def weight(rows,perm):
    n=len(rows)
    if not n:return 1
    total=0
    for cuts in product((False,True),repeat=n-1):
        blocks=[];start=0
        for i,cut in enumerate(cuts,1):
            if cut:blocks.append(perm[start:i]);start=i
        blocks.append(perm[start:])
        valid=True
        for block in blocks:
            if any(block[i]>=block[i+1] for i in range(len(block)-1)):
                valid=False;break
            mask=sum(1<<i for i in block)
            if any(rows[i]&mask for i in block):valid=False;break
        if valid:total+=(-1)**(n+len(blocks))
    return total


def main():
    started=time.time();weights={};checks=0;report=[];maxabs=0
    for n in range(6):
        pc=0;ec=0;nonzero=0
        for rows in posets(n):
            pc+=1
            ws={perm:weight(rows,perm) for perm in extensions(rows)}
            assert sum(ws.values())==1,(n,rows,'normalization',ws)
            weights[(n,rows)]=ws;ec+=len(ws);nonzero+=sum(bool(w) for w in ws.values())
            maxabs=max([maxabs]+[abs(w) for w in ws.values()])
            for omit in range(n):
                keep=[i for i in range(n) if i!=omit]
                small=restrict_rows(rows,keep);marginal=Counter()
                for perm,w in ws.items():
                    restricted=tuple(i-(i>omit) for i in perm if i!=omit)
                    marginal[restricted]+=w
                for perm,w in weights[(n-1,small)].items():
                    assert marginal[perm]==w,(n,rows,omit,perm,marginal[perm],w)
                    checks+=1
        line={'n':n,'posets':pc,'extensions':ec,'nonzero_weights':nonzero}
        report.append(line);print(line,flush=True)
    result={'levels':report,'integer_marginal_equations_checked':checks,
            'max_absolute_weight':maxabs,'all_checks_passed':True,
            'elapsed_seconds':time.time()-started}
    print(json.dumps(result,indent=2))
    Path('FREX/verification/ordered_poset_euler_report.json').write_text(json.dumps(result,indent=2))


if __name__=='__main__':main()
