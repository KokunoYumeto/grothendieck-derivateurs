"""Render every final PDF page and make contact sheets for visual inspection."""
from pathlib import Path
import json
import subprocess
from PIL import Image, ImageOps, ImageDraw

root = Path(__file__).resolve().parents[1]
out = root / "code" / "qa"
out.mkdir(exist_ok=True)
pdf = root / "TOTEX2_paper.pdf"
subprocess.run(["pdftoppm", "-png", "-scale-to", "900", str(pdf), str(out/"page")],
               check=True, stdout=subprocess.DEVNULL)
pages = sorted(out.glob("page-*.png"))
summary = []
for batch in range(0, len(pages), 6):
    sheet = Image.new("RGB", (960, 2080), "#e7e7e7")
    draw = ImageDraw.Draw(sheet)
    for j, p in enumerate(pages[batch:batch+6]):
        im = Image.open(p).convert("RGB")
        preview = ImageOps.contain(im, (454, 650))
        x = 13 + (j % 2) * 480
        y = 22 + (j // 2) * 690
        sheet.paste(preview, (x, y))
        draw.text((x, y + 653), f"Page {batch+j+1}", fill="black")
        # Pixel bounds are a diagnostic, not a substitute for visual review.
        gray = im.convert("L")
        ink = gray.point(lambda z: 255 if z < 150 else 0)
        bbox = ink.getbbox()
        summary.append({"page":batch+j+1,"pixels":im.size,"ink_bbox":bbox})
    name = out / f"contact-{batch//6+1:02}.png"
    sheet.save(name)
(out/"page_diagnostics.json").write_text(json.dumps(summary, indent=2))
text = subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"], text=True)
(out/"paper_text.txt").write_text(text)
result = {"pages_rendered":len(pages),
          "contact_sheets":[p.name for p in sorted(out.glob("contact-*.png"))],
          "text_characters":len(text),
          "replacement_characters":text.count("\ufffd"),
          "visual_review":"pending; contact sheets and selected full pages must be inspected"}
(out/"render_summary.json").write_text(json.dumps(result, indent=2))
print(json.dumps(result, indent=2))
