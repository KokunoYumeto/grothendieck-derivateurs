#!/usr/bin/env python3
"""Render every page and check the integrated PDF's structural output.

The contact sheets are for human/model visual inspection. Automated bounds and
text checks do not prove that a page is visually satisfactory or that mathematics
is correct. Full-resolution renders are temporary, not distributed source scans.
"""
from pathlib import Path
import csv
import json
import math
import re
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "POLES_paper.pdf"
OUT = ROOT.parent / "tmp" / "poles_pdf_qa"
OUT.mkdir(parents=True, exist_ok=True)


def run(command):
    result = subprocess.run(command, check=True, text=True, capture_output=True)
    return result.stdout


info = run(["pdfinfo", str(PDF)])
fonts = run(["pdffonts", str(PDF)])
font_rows = [line.split() for line in fonts.splitlines()[2:] if line.strip()]
assert font_rows and all(row[-5] == "yes" for row in font_rows), "An unembedded PDF font was found"
text = run(["pdftotext", "-layout", str(PDF), "-"])
page_count = int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))
pages = text.split("\f")[:page_count]
rows = list(csv.DictReader((ROOT / "POLES_results.csv").open()))
locations = {}
missing = []
for row in rows:
    identifier = row["id"]
    matches = [i+1 for i, page in enumerate(pages)
               if re.search(r"(?m)^\s*"+re.escape(identifier)+r"\.\s", page)]
    if not matches:
        missing.append(identifier)
    locations[identifier] = matches
assert not missing, ("Statement headings absent from PDF", missing)
assert "??" not in text, "Possible unresolved reference marker in PDF"

bbox = OUT / "bbox.html"
run(["pdftotext", "-bbox-layout", str(PDF), str(bbox)])
# Poppler can expose a math font's legacy control-code glyph in word text.
# XML 1.0 forbids those characters; coordinates remain well-defined. Sanitize
# only the impossible XML characters, never the numeric bounding boxes.
raw_xml = bbox.read_text()
invalid_controls = re.findall(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", raw_xml)
xml = ET.ElementTree(ET.fromstring(re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", raw_xml)))
ns = {"h": "http://www.w3.org/1999/xhtml"}
outside = []
for number, page in enumerate(xml.findall(".//h:page", ns), 1):
    width, height = float(page.attrib["width"]), float(page.attrib["height"])
    for word in page.findall(".//h:word", ns):
        box = [float(word.attrib[k]) for k in ("xMin", "yMin", "xMax", "yMax")]
        if box[0] < 10 or box[1] < 5 or box[2] > width-10 or box[3] > height-5:
            outside.append({"page": number, "word": word.text, "box": box})
assert not outside, ("Text approaches/crosses page edge", outside)

for old_render in list(OUT.glob("page-*.png")) + list(OUT.glob("contact-*.png")):
    old_render.unlink()
run(["pdftoppm", "-r", "100", "-png", str(PDF), str(OUT / "page")])
rendered = sorted(OUT.glob("page-*.png"))
assert len(rendered) == page_count, (len(rendered), page_count)
thumb_w, thumb_h, label_h = 265, 375, 24
cols, per_sheet = 4, 16
sheets = []
for start in range(0, page_count, per_sheet):
    count = min(per_sheet, page_count-start)
    sheet = Image.new("RGB", (cols*thumb_w, math.ceil(count/cols)*(thumb_h+label_h)), "#dce2e8")
    draw = ImageDraw.Draw(sheet)
    for offset, filename in enumerate(rendered[start:start+per_sheet]):
        im = Image.open(filename).convert("RGB")
        im.thumbnail((thumb_w-8, thumb_h-8))
        x = (offset % cols)*thumb_w + (thumb_w-im.width)//2
        y = (offset // cols)*(thumb_h+label_h)+label_h
        sheet.paste(im, (x,y))
        draw.text(((offset % cols)*thumb_w+10,y-label_h+5), f"Page {start+offset+1}", fill="black")
    filename = OUT / f"contact-{start//per_sheet+1:02d}.png"
    sheet.save(filename)
    sheets.append(str(filename))

summary = {
    "pages": page_count,
    "pdf_bytes": PDF.stat().st_size,
    "all_statement_headings_present": True,
    "all_fonts_embedded": True,
    "statement_pages": locations,
    "unresolved_reference_markers": False,
    "page_edge_text_violations": outside,
    "legacy_math_control_characters_sanitized_for_bbox_xml": len(invalid_controls),
    "all_pages_rendered": len(rendered),
    "contact_sheets": sheets,
    "pdfinfo": info,
    "pdffonts": fonts,
    "visual_inspection_required": True,
}
(ROOT / "verification" / "pdf_qa_summary.json").write_text(json.dumps(summary, indent=2)+"\n")
print(json.dumps({k:v for k,v in summary.items() if k not in {"statement_pages", "pdfinfo", "pdffonts"}}, indent=2))
print(info)
print(fonts)
