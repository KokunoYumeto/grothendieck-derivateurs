"""Check the interruption deliverables and render every PDF page for review.

Run after build_pdf.py and build_results_report.mjs. The contact sheets and
page images are review intermediates under a sibling tmp/ directory. The
machine-readable check record remains in code/package_verification.json.
"""
from pathlib import Path
import csv
import json
import re
import subprocess

import fitz
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "tmp" / "totex2_pdf_qa"
QA.mkdir(parents=True, exist_ok=True)
required = ["TOTEX2_paper.tex", "TOTEX2_paper.pdf", "TOTEX2_results.csv",
            "TOTEX2_references.bib", "TOTEX2_report.md"]
for name in required:
    assert (ROOT / name).is_file(), name

header = ["id", "statement", "status", "where_proved", "depends_on",
          "manuscript_pages_settled", "notes"]
with (ROOT / "TOTEX2_results.csv").open(newline="") as f:
    reader = csv.DictReader(f)
    assert reader.fieldnames == header, reader.fieldnames
    rows = list(reader)
assert all(set(r) == set(header) and all(v is not None for v in r.values()) for r in rows)
assert len({r["id"] for r in rows}) == len(rows)
assert all(r["status"] in {"Known", "Proved", "Refuted", "Open"} for r in rows)
metadata = json.loads((ROOT / "code/results_metadata.json").read_text())
assert metadata["header"] == header
assert rows == [{k: e[k] for k in header} for e in metadata["entries"]]
labels = {}
for line in (ROOT / "TOTEX2_paper.aux").read_text().splitlines():
    m = re.match(r"^\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{([^}]+)\}", line)
    if m and "{theorem." in line:
        labels[m[1]] = m[2]
assert set(labels) == {e["label"] for e in metadata["entries"]}
assert set(labels.values()) == {r["id"] for r in rows}
open_labels = {e["label"] for e in metadata["entries"] if e["status"] == "Open"}
assert {"A:main", "A:membership", "B:triple", "C:all-stage", "C:ramsey-scope"} <= open_labels

report = (ROOT / "TOTEX2_report.md").read_text()
assert report.splitlines()[0] == "INCOMPLETE"
assert report.splitlines()[2].startswith("| Requested item |")
requested = ["A.1", "A.2 over Q", "A.2 over every F_p", "B.1", "B.2",
             "C.1", "C.2", "D.1", "D.2", "D.3"]
requested += [f"Lead {i}" for i in (1,2,3,4,6,7,8)]
requested += [f"Lead 5({i})" for i in ("i", "ii", "iii", "iv")]
requested += [f"Lead 9({i})" for i in "abcd"]
assert all(f"| {item} |" in report for item in requested)

log = (ROOT / "code/outputs/latex_final.out").read_text()
markers = ["undefined references", "undefined citations", "multiply defined",
           "Overfull \\hbox", "Overfull \\vbox", "LaTeX Error:", "! error:"]
assert not [m for m in markers if m.lower() in log.lower()]
doc = fitz.open(ROOT / "TOTEX2_paper.pdf")
out_of_bounds = []
replacement_characters = []
text_counts = []
for page_number, page in enumerate(doc, 1):
    text = page.get_text()
    text_counts.append(len(text))
    if "\ufffd" in text:
        replacement_characters.append(page_number)
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                x0, y0, x1, y1 = span["bbox"]
                if x0 < -0.5 or y0 < -0.5 or x1 > page.rect.width + 0.5 or y1 > page.rect.height + 0.5:
                    out_of_bounds.append([page_number, list(span["bbox"]), span["text"]])
assert not out_of_bounds, out_of_bounds
assert not replacement_characters, replacement_characters
assert min(text_counts) > 300
assert "INCOMPLETE" in doc[0].get_text()
subprocess.run(["pdftoppm", "-r", "110", "-png", str(ROOT / "TOTEX2_paper.pdf"),
                str(QA / "page")], check=True)
pages = sorted(QA.glob("page-*.png"))
assert len(pages) == len(doc)
font = ImageFont.load_default(size=18)
sheets = []
for first in range(0, len(pages), 6):
    sheet = Image.new("RGB", (1230, 1190), "#d5dce3")
    draw = ImageDraw.Draw(sheet)
    for local, filename in enumerate(pages[first:first+6]):
        page_image = Image.open(filename).convert("RGB")
        page_image.thumbnail((390, 552), Image.Resampling.LANCZOS)
        col, row = local % 3, local // 3
        x, y = col * 410 + 10, row * 595 + 30
        sheet.paste(page_image, (x, y))
        draw.text((x, y-23), f"PDF page {first+local+1}", fill="#17242f", font=font)
    name = QA / f"contact-{first//6+1:02d}.png"
    sheet.save(name)
    sheets.append(str(name))
result = {"status": "PASS", "pdf_pages": len(doc), "numbered_statements": len(rows),
          "csv_schema": header, "unique_ids": True, "theorem_coverage": True,
          "report_first_line": "INCOMPLETE", "out_of_bounds_text": out_of_bounds,
          "replacement_characters": replacement_characters,
          "latex_unresolved_references_or_overfull_boxes": False,
          "rendered_pages": len(pages), "contact_sheets": sheets,
          "visual_review": "Contact sheets and selected full pages must also be inspected by the reviewer."}
(ROOT / "code/package_verification.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
