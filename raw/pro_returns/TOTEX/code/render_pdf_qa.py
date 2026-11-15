"""Render the final paper and inspect text bounds; contact sheets are temporary QA.

Requires Poppler and Pillow.  No source images or external network are used.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority claim.
"""
from pathlib import Path
import json
import hashlib
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'code' / 'outputs'
QA = ROOT / '.build' / 'pdf_qa'
QA.mkdir(parents=True, exist_ok=True)
pdf = ROOT / 'TOTEX_paper.pdf'
subprocess.run(['pdftoppm', '-r', '100', '-png', str(pdf), str(QA / 'page')], check=True)
subprocess.run(['pdftotext', '-bbox', str(pdf), str(QA / 'bounds.html')], check=True)
# Poppler can emit XML-forbidden control characters for TeX math glyphs.
raw = (QA / 'bounds.html').read_text(encoding='utf-8')
clean = ''.join(c for c in raw if c in '\t\n\r' or ord(c) >= 32)
tree = ET.ElementTree(ET.fromstring(clean))
ns = {'h': 'http://www.w3.org/1999/xhtml'}
pages = tree.findall('.//h:page', ns)
bad = []
for page_no, page in enumerate(pages, 1):
    width, height = float(page.attrib['width']), float(page.attrib['height'])
    for word in page.findall('.//h:word', ns):
        a = word.attrib
        if (float(a['xMin']) < -0.1 or float(a['yMin']) < -0.1
                or float(a['xMax']) > width + 0.1 or float(a['yMax']) > height + 0.1):
            bad.append({'page': page_no, 'word': word.text, 'bounds': a})
images = sorted(QA.glob('page-*.png'))
for start in range(0, len(images), 6):
    canvas = Image.new('RGB', (850, 1850), '#ddd')
    draw = ImageDraw.Draw(canvas)
    for k, image_path in enumerate(images[start:start + 6]):
        img = Image.open(image_path).convert('RGB')
        img.thumbnail((410, 585))
        x, y = 10 + (k % 2) * 425, 25 + (k // 2) * 615
        canvas.paste(img, (x, y))
        draw.text((x, y - 17), f'Page {start+k+1}', fill='black')
    canvas.save(QA / f'contact-{start//6+1}.png')
result = {'pages': len(pages), 'rendered_pages': len(images),
          'words_outside_page': bad,
          'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
          'manual_review_record': 'The script checks rendering and text bounds; the accompanying report records the manual visual review of the delivered PDF.',
          'temporary_render_directory': '.build/pdf_qa'}
(OUT / 'pdf_layout_audit.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
assert len(pages) == len(images) and not bad
