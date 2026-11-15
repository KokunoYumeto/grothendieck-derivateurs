"""Render every PDF page and prepare contact sheets for visual inspection.

The PNGs are temporary review images, not mathematical evidence. The output
records the structural PDF checks; visual review is described in the report.
"""
from pathlib import Path
import json
import re
import subprocess
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / "tmp" / "pdf_review"
OUT.mkdir(parents=True, exist_ok=True)
doc = fitz.open(ROOT / "GALOIS_paper.pdf")
rendered = []
counts = []
for i, page in enumerate(doc, 1):
    words = page.get_text("words")
    counts.append(len(words))
    assert len(words) > 20, f"Unexpected near-empty page {i}"
    for w in words:
        assert w[0] >= 0 and w[1] >= 0 and w[2] <= page.rect.width+0.5 and w[3] <= page.rect.height+0.5, (i,w)
    assert "\ufffd" not in page.get_text(), f"Replacement character on page {i}"
    path = OUT / f"page_{i:03d}.png"
    page.get_pixmap(matrix=fitz.Matrix(1.4, 1.4), alpha=False).save(path)
    rendered.append(path)

for start in range(0, len(rendered), 16):
    sheet = Image.new("RGB", (960, 1440), "#e1e4e8")
    d = ImageDraw.Draw(sheet)
    for j, path in enumerate(rendered[start:start+16]):
        im = Image.open(path).convert("RGB")
        im.thumbnail((224, 326))
        x = (j%4)*240 + (240-im.width)//2
        y = (j//4)*360+24
        sheet.paste(im, (x,y))
        d.text(((j%4)*240+9,(j//4)*360+7), f"Page {start+j+1}", fill="black")
    sheet.save(OUT / f"contact_{start//16+1:02d}.png")
log = (ROOT / "GALOIS_paper.log").read_text()
bad = [line for line in log.splitlines()
       if re.search(r"Overfull|Underfull|Warning|undefined|^!", line)]
assert not bad, "Final LuaLaTeX diagnostics are not clean: " + repr(bad)
stats_path = ROOT / "research/release_statistics.json"
stats = json.loads(stats_path.read_text())
stats.update(pdf_pages=len(doc), pdf_bytes=(ROOT/"GALOIS_paper.pdf").stat().st_size,
             final_lualatex_diagnostics="clean: no errors, warnings, overfull or underfull boxes")
stats_path.write_text(json.dumps(stats, indent=2)+"\n")
print(f"PASS: {len(doc)} pages rendered; all page text lies within the media box.")
print(f"PASS: every page contains text; word-count range {min(counts)}--{max(counts)}.")
print("PASS: no replacement characters; final LuaLaTeX log has no errors, warnings, overfull or underfull boxes.")
print(f"Prepared {(len(doc)+15)//16} contact sheets and {len(doc)} full-page renders for visual review.")
print("Review images are temporary; the final PDF is the authoritative rendered artifact.")
independent = OUT / "poppler"
independent.mkdir(exist_ok=True)
for page_number in (1, 31, 37, 54, 64):
    result = subprocess.run(
        ["pdftoppm", "-f", str(page_number), "-l", str(page_number),
         "-singlefile", "-scale-to", "1200", "-png",
         str(ROOT / "GALOIS_paper.pdf"), str(independent / f"page_{page_number:03d}")],
        capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
print("PASS: independent Poppler renders of first-page conventions, long formulas, coefficient table, rational tower, and bibliography.")
