"""Render the explicitly selected manuscript pages for checkpoint inspection.

The PNG files are reproducible inspection aids and are excluded from archives.
An inspection verdict is recorded separately after the images are viewed.
"""
from pathlib import Path
import argparse
import subprocess
from PIL import Image, ImageDraw

parser = argparse.ArgumentParser()
parser.add_argument("checkpoint", type=int)
parser.add_argument("pages", nargs="+", type=int)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
dest = root / "verification" / f"checkpoint_{args.checkpoint:02d}_pages"
dest.mkdir(exist_ok=True)
for page in args.pages:
    prefix = dest / f"page_{page:03d}"
    subprocess.run([
        "pdftoppm", "-f", str(page), "-l", str(page), "-r", "96",
        "-png", "-singlefile", str(root / "FREX_paper.pdf"), str(prefix)
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
for start in range(0, len(args.pages), 4):
    group = args.pages[start:start+4]
    sheet = Image.new("RGB", (1240, 2*900), "#dddddd")
    draw = ImageDraw.Draw(sheet)
    for position, page in enumerate(group):
        im = Image.open(dest / f"page_{page:03d}.png").convert("RGB")
        im.thumbnail((600, 850))
        x, y = 10 + 620*(position % 2), 28 + 900*(position // 2)
        sheet.paste(im, (x, y))
        draw.text((x, y-20), f"FREX page {page}", fill="black")
    sheet.save(dest / f"review_sheet_{start//4+1}.png")
print(f"Rendered {len(args.pages)} pages in {dest}")
