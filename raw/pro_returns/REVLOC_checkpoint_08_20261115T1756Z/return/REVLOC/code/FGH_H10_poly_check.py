#!/usr/bin/env python3
"""Degree-ten polynomial certificate; no Browder or homotopy assertions."""
import importlib.util
import json
from pathlib import Path

base = Path(__file__).parent
spec = importlib.util.spec_from_file_location("lower", base / "D2_fiber_poly_check.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.LABEL.update({(5,0,0,0):"p",(2,2,0,0):"q",(1,1,1,0):"r",(0,0,2,0):"s"})
m.EXP.update({name:ex for ex,name in m.LABEL.items()})
m.GEN_SQ[3][1] = {(0,0,2,0)}
p,mul,xor = m.pol,m.mul,m.xor
C=m.CLASSES
classes={
    "DA":p("aabb"),
    "FA":mul(C["A4"],C["p3"]),
    "Z2":mul(C["z5"],C["z5"]),
    "D2":p("dd"),
    "Q10":p("q","cx","aj","aax","abe","aabb","bg","bbc"),
    "Pp":p("p","ai","cf","aaf","acc","aaac","aaaaa"),
    "Pr":p("r","al","bh","ed"),
}
expected={
    "DA":(set(),C["W8"],set()),
    "FA":(set(),C["W8"],set()),
    "Z2":(set(),C["W8"],set()),
    "D2":(set(),set(),p("bb")),
    "Q10":(xor(C["Pm9"],C["Pn9"],C["ZA9"]),xor(C["M8"],C["C8"],C["W8"]),C["p3"]),
    "Pp":(set(),C["W8"],C["p3"]),
    "Pr":(set(),set(),set()),
}
report=[]
for name,value in classes.items():
    operations=tuple(m.sq(k,value) for k in (1,2,4))
    assert operations==expected[name],(name,[m.show(v) for v in operations],[m.show(v) for v in expected[name]])
    rd=m.reduced_delta(value)
    if name=="Q10":
        wanted={(l,r) for l in C["z5"] for r in C["z5"]}
    elif name in ("DA","FA"):
        other=p("bb") if name=="DA" else C["p3"]
        wanted={(l,r) for l in C["A4"] for r in other}
        wanted|={(r,l) for l in C["A4"] for r in other}
    else:
        wanted=set()
    assert rd==wanted,(name,m.show_tensor(rd),m.show_tensor(wanted))
    report.append({"class":name,"polynomial":m.show(value),"reduced_coproduct":m.show_tensor(rd),
                   **{f"Sq{k}":m.show(v) for k,v in zip((1,2,4),operations)}})
out={"status":"PASS","scope":"Seven degree-ten polynomial classes; 21 primary operations and all coproducts. No Browder, integral or homotopy assertion.","classes":report}
dest=base/"outputs"/"FGH_H10_poly_check.json"
dest.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","classes":len(classes),"operation_values":21,"output":str(dest)}))
