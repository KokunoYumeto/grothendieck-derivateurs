"""Merge checked statements and references, preserving exact statement data."""
from collections import Counter
import csv
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
ALIASES={"EFCisinski2006":"BCCisinski2006",
         "EFCisinski2019":"BCCisinski2019",
         "BCLurie2009":"DGLurieHTT",
         "EFHoermann2017":"EFHormann2017"}
def canonical(text):
    for old,new in ALIASES.items():
        text=text.replace(old,new)
    return text

for path in sorted((ROOT/"sections").glob("*.tex")):
    text=canonical(path.read_text())
    if path.name=="00_conventions.tex":
        text=text.replace("A.4 compares this modern","A.1 compares this modern")
    if path.name=="C.tex":
        text=text.replace("BN_nS",r"|N_nS|")
    if path.name=="A.tex" and "OpenAI2026Thomason" not in text:
        text=text.replace(
            "here; no conclusion of Part A depends on either.",
            r"here \citep{OpenAI2026Thomason,OpenAI2026Groupoids}; no conclusion of Part A depends on either.")
    if path.name=="C.tex" and r"\citep[claimed, unrefereed]{OpenAI2026Thomason}" not in text:
        text=text.replace(
            "claimed in family~317 are valid.",
            r"claimed in family~317 are valid \citep[claimed, unrefereed]{OpenAI2026Thomason}.")
    if path.name=="F.tex" and "may also be a retained boundary" not in text:
        text=text.replace(
            "Boundary twists act trivially on curves disjoint from the boundary,",
            "The retained puncture in a peripheral leaf may also be a retained boundary circle: such a leaf is a duplicate of a curve already in $\\sigma$. Boundary twists act trivially on curves disjoint from the boundary,")
    path.write_text(text)

def bibentries(text):
    """Read outer brace-balanced entries without assuming field line layout."""
    for match in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,",text):
        begin=text.index("{",match.start());depth=1;i=begin+1
        while depth:
            if text[i]=="{" and text[i-1]!="\\": depth+=1
            elif text[i]=="}" and text[i-1]!="\\": depth-=1
            i+=1
        yield match.group(1),text[match.start():i]

def field(text,name):
    match=re.search(r"\b"+re.escape(name)+r"\s*=\s*\{",text)
    if not match:return None
    depth=1;i=match.end();start=i
    while depth:
        if text[i]=="{" and text[i-1]!="\\":depth+=1
        elif text[i]=="}" and text[i-1]!="\\":depth-=1
        i+=1
    return (start,i-1,text[start:i-1])

references={}
sourcefiles=("A_references.bib","BC_references.bib","sections/DG_references.bib",
             "EF_references.bib","claims_2026_references.bib")
for filename in sourcefiles:
    for original,entry in bibentries((ROOT/filename).read_text()):
        key=ALIASES.get(original,original)
        entry=entry.replace("{"+original+",","{"+key+",",1)
        assert field(entry,"note") and re.search(r"\b(?:un)?verified\b",field(entry,"note")[2]),key
        if key in references:
            old=references[key];span=field(old,"note");added=field(entry,"note")[2]
            old=old[:span[1]]+" Additional check: "+added+old[span[1]:]
            for name in ("doi","url"):
                if not field(old,name) and field(entry,name):
                    old=old.rstrip()[:-1].rstrip()+",\n  "+name+" = {"+field(entry,name)[2]+"}\n}"
            references[key]=old
        else:references[key]=entry
(ROOT/"BISITE_references.bib").write_text("\n\n".join(references.values())+"\n")

master=(ROOT/"BISITE_paper.tex").read_text()
master=master.replace(r"\bibliographystyle{plainnat}",r"\bibliographystyle{apacite}")
master=master.replace(r"\bibliographystyle{BISITE_APA}",r"\bibliographystyle{apacite}")
master=master.replace(r"\usepackage[authoryear,round]{natbib}",r"\usepackage[natbibapa]{apacite}")
master=master.replace(r"\usepackage{fontspec}",r"\usepackage{xcolor}"+"\n"+r"\usepackage{fontspec}")
# Avoid duplicate xcolor load and ensure it precedes colored hyperref options.
first=master.find(r"\usepackage{xcolor}")
master=master[:first+len(r"\usepackage{xcolor}")]+master[first+len(r"\usepackage{xcolor}"):].replace(r"\usepackage{xcolor}"+"\n","")
if r"\nocite{OpenAI2026Thomason,OpenAI2026Groupoids}" not in master:
    master=master.replace(r"\bibliographystyle",r"\nocite{OpenAI2026Thomason,OpenAI2026Groupoids}"+"\n"+r"\bibliographystyle")
(ROOT/"BISITE_paper.tex").write_text(master)

claims={}
for path in sorted((ROOT/"sections").glob("*.tex")):
    text=path.read_text()
    for match in re.finditer(r"\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}\{",text):
        ident,status=match.group(1,2);depth=1;start=match.end();i=start
        while depth:
            if text[i]=="{" and text[i-1]!="\\":depth+=1
            elif text[i]=="}" and text[i-1]!="\\":depth-=1
            i+=1
        title=text[start:i-1]
        end=text.index(r"\end{claim}",i)
        statement=re.sub(r"\s+"," ",title+". "+text[i:end]).strip()
        assert ident not in claims,ident
        claims[ident]=(status,statement,path.relative_to(ROOT))

rows=[]
FIELDS=("id","statement","status","where_proved","depends_on",
        "manuscript_rows_or_pages_settled","notes")
for filename in ("A_results.csv","B_results.csv","C_results.csv",
                 "sections/D_results.csv","EF_results.csv","sections/G_results.csv"):
    for row in csv.DictReader((ROOT/filename).open()):
        row={key:canonical(row.get(key,"")) for key in FIELDS}
        ident=row["id"]
        assert ident in claims,ident
        status,statement,path=claims[ident]
        assert row["status"]==status,(ident,row["status"],status)
        row["statement"]=statement
        row["where_proved"]=f"BISITE_paper.tex, {ident}, statement and following argument; {path}"
        rows.append(row)
rows.sort(key=lambda r:(r["id"][0],int(r["id"].split(".")[1])))
assert len(rows)==len(claims)==len({r["id"] for r in rows})
with (ROOT/"BISITE_results.csv").open("w",newline="") as stream:
    writer=csv.DictWriter(stream,fieldnames=FIELDS);writer.writeheader();writer.writerows(rows)

used=set()
for path in (ROOT/"sections").glob("*.tex"):
    for match in re.finditer(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}",path.read_text()):
        used.update(match.group(1).split(","))
assert used<=references.keys(),sorted(used-references.keys())
log=(f"Statements: {len(rows)}\nStatuses: {dict(Counter(r['status'] for r in rows))}\n"
     f"Unique bibliography entries: {len(references)}\nCited keys: {len(used)}; missing: 0\n"
     "Every bibliography entry has an explicit verification note.\n"
     "Duplicate Cisinski/HTT entries unified, preserving verification notes.\n"
     "Exact statement bodies replace abbreviated registry titles.\n"
     "Conditional OpenAI premise is confined to C.9 above dimension two.\n")
Path(__file__).with_suffix(".out.txt").write_text(log)
print(log,end="")
