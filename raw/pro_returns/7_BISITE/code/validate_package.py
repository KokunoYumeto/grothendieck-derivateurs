"""Check the final research package; --checks reruns its finite certificates."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument("--checks",action="store_true")
args=parser.parse_args()
checks=[]
if args.checks:
    programs=("a_finite_audit.py","a_b062_verify.py","a_absolute_relative.py",
              "bc_counterexamples.py","bc_inherited.py","bc_paths.py",
              "dg_finite_checks.py","dg_proper_fibres.py","ef_finite_checks.py")
    for name in programs:
        proc=subprocess.run([sys.executable,str(ROOT/"code"/name)],
             cwd=ROOT.parent,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        target=ROOT/"code"/("recheck_"+Path(name).stem+".out.txt")
        target.write_text(proc.stdout)
        assert proc.returncode==0,(name,proc.stdout[-3000:])
        checks.append({"program":name,"exit_code":proc.returncode,
                       "captured_output":str(target.relative_to(ROOT))})
        print(f"PASS {name}",flush=True)

rows=list(csv.DictReader((ROOT/"BISITE_results.csv").open()))
expected={"id","statement","status","where_proved","depends_on",
          "manuscript_rows_or_pages_settled","notes"}
assert set(rows[0])==expected
assert len(rows)==len({row["id"] for row in rows})
claims={}
citations=set()
for path in (ROOT/"sections").glob("*.tex"):
    text=path.read_text()
    assert text.count(r"\begin{claim}")==text.count(r"\end{claim}"),path
    assert text.count(r"\begin{proof}")==text.count(r"\end{proof}"),path
    for ident,status in re.findall(r"\\begin\{claim\}\{([^}]+)\}\{([^}]+)\}",text):
        assert ident not in claims,ident
        claims[ident]=status
    for match in re.finditer(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}",text):
        citations.update(match.group(1).split(","))
assert claims=={r["id"]:r["status"] for r in rows}
assert all(r["statement"] and r["where_proved"] and r["notes"] for r in rows)
bib=(ROOT/"BISITE_references.bib").read_text()
keys=re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,",bib)
assert len(keys)==len(set(keys))
assert citations<=set(keys),citations-set(keys)
assert len(re.findall(r"\bnote\s*=\s*\{\s*(?:un)?verified\b",bib))==len(keys)
conditional=next(r for r in rows if r["id"]=="C.9")
assert "conditional OpenAI2026Thomason" in conditional["depends_on"]
assert "Suppose" in conditional["statement"]
opens=[r["id"] for r in rows if r["status"]=="Open"]
assert opens==["B.21","C.10","D.12","F.18"],opens
assert all("OpenAI2026" not in r["depends_on"] for r in rows if r["id"]!="C.9")

log=(ROOT/"BISITE_paper.log").read_text()
bad=[line for line in log.splitlines()
     if any(token in line for token in ("Undefined control sequence","undefined citations",
            "There were undefined references","Overfull","Fatal error","LaTeX Error"))]
assert not bad,bad
biblog=(ROOT/"code/build_bibtex.out.txt").read_text()
assert not re.search(r"(Warning--|error message|I couldn't|not found)",biblog)
pdf=ROOT/"BISITE_paper.pdf"
info=subprocess.run(["pdfinfo",str(pdf)],capture_output=True,text=True,check=True).stdout
pagecount=int(re.search(r"Pages:\s+(\d+)",info).group(1))
text=subprocess.run(["pdftotext","-layout",str(pdf),"-"],
                    capture_output=True,text=True,check=True).stdout
for ident,status in claims.items():
    assert re.search(re.escape(ident)+r"\.\s*\["+status+r"\]",text),(ident,status)
# The actual text layer must stay inside the paper, not merely have clean logs.
bbox=subprocess.run(["pdftotext","-bbox",str(pdf),"-"],
                    capture_output=True,text=True,check=True).stdout
# Poppler can emit XML-forbidden C0 characters for legacy mathematical
# font slots; remove only those controls before parsing the coordinates.
invalid_xml_controls=re.findall(r"[\x00-\x08\x0b\x0c\x0e-\x1f]",bbox)
bbox=re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]","",bbox)
tree=ET.fromstring(bbox)
outliers=[]
for pageno,page in enumerate(tree.iter("{http://www.w3.org/1999/xhtml}page"),1):
    width=float(page.attrib["width"]);height=float(page.attrib["height"])
    for word in page.iter("{http://www.w3.org/1999/xhtml}word"):
        a=word.attrib
        if float(a["xMin"])<20 or float(a["xMax"])>width-20 or float(a["yMin"])<20 or float(a["yMax"])>height-20:
            outliers.append({"page":pageno,"word":word.text,"bbox":a})
assert not outliers,outliers[:10]
fonts=subprocess.run(["pdffonts",str(pdf)],capture_output=True,text=True,check=True).stdout
assert "Type 3" not in fonts,fonts
result={
 "statements":len(rows),"statuses":dict(Counter(claims.values())),
 "remaining_open":opens,"bibliography_entries":len(keys),
 "missing_citations":0,"bibliography_warnings":0,"fatal_or_overfull_messages":bad,
 "pdf_pages":pagecount,"pdf_bytes":pdf.stat().st_size,
 "pdf_sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),
 "text_layer_margin_outliers":outliers,"type3_bitmap_fonts":False,
 "bbox_xml_control_characters_removed":len(invalid_xml_controls),
 "finite_certificate_reruns":checks,
 "verification_scope":"Exact finite certificates, registry/citation consistency, clean final build and PDF geometry. Not formal verification of all proofs."}
(ROOT/"code/validate_package.out.json").write_text(json.dumps(result,indent=2)+"\n")
(ROOT/"code/pdfinfo.out.txt").write_text(info)
(ROOT/"code/pdffonts.out.txt").write_text(fonts)
print(json.dumps(result,indent=2))
