"""Render every final PDF page for human layout review and inspect page bounds."""
from pathlib import Path
import json
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT.parent / 'qa_cathot'
OUT.mkdir(exist_ok=True)
doc = fitz.open(ROOT / 'CATHOT_paper.pdf')
records = []
page_images = []
for number, page in enumerate(doc, 1):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False)
    path = OUT / f'page_{number:03d}.png'
    pix.save(path)
    page_images.append(path)
    blocks = [b for b in page.get_text('blocks') if len(b) >= 7 and b[6] == 0]
    outside = [list(b[:4]) for b in blocks if b[0] < -0.5 or b[1] < -0.5
               or b[2] > page.rect.width + 0.5 or b[3] > page.rect.height + 0.5]
    records.append({'page': number, 'text_characters': len(page.get_text()),
                    'out_of_page_text_blocks': outside})
    assert not outside, (number, outside)
    assert len(page.get_text()) > 80, f'Unexpected near-empty page {number}'

contacts = []
for start in range(0, len(page_images), 8):
    thumb_w, thumb_h, gap, label_h = 450, 637, 18, 26
    canvas = Image.new('RGB', (2 * thumb_w + 3 * gap,
                              4 * (thumb_h + label_h) + 5 * gap), '#d8dce1')
    draw = ImageDraw.Draw(canvas)
    for offset, path in enumerate(page_images[start:start + 8]):
        im = Image.open(path).convert('RGB')
        im.thumbnail((thumb_w, thumb_h))
        x = gap + (offset % 2) * (thumb_w + gap)
        y = gap + (offset // 2) * (thumb_h + label_h + gap)
        draw.text((x, y), f'Page {start + offset + 1}', fill='black')
        canvas.paste(im, (x, y + label_h))
    path = OUT / f'contact_{start // 8 + 1:02d}.png'
    canvas.save(path)
    contacts.append(str(path))

result = {'pages': len(doc), 'pdf_metadata': doc.metadata,
          'render_directory': str(OUT), 'contact_sheets': contacts,
          'page_checks': records,
          'qualification': 'Page bounds and rendering checks do not verify mathematical proofs; visual review is separate.'}
(ROOT / 'code' / 'render_pdf_qa.json').write_text(json.dumps(result, indent=2) + '\n')
print(f'Rendered {len(doc)} pages and {len(contacts)} contact sheets.')
print('No text block extends outside its PDF page; no near-empty pages.')
print('PDF producer:', doc.metadata.get('producer'))
print('Metadata and per-page checks: code/render_pdf_qa.json')
for path in contacts:
    print(path)
